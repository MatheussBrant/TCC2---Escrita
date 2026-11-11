"""Regenera a classificação derivada e os agrupamentos, sem executar o pipeline."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
from collections import Counter, defaultdict

PASTA = Path(__file__).resolve().parent
ESCRITA = PASTA.parents[1]
EXPERIMENTO = ESCRITA.parent / 'tcc2-llm-sast-juiceshop'
ALVO = EXPERIMENTO / 'workspace/catalogo-alvo'
SHA_EXPERIMENTO = '062a203516fd7f55ce86d9c19dc0f23f6e92ed61'
CAMPANHAS = {
    'GPT-4.1 mini': ('AMP_REAL_20261106T151004Z_f49ac0d2', 38),
    'GPT-5.6 Luna': ('AMP_REAL_20261106T125801Z_0eb68fe4', 51),
    'GPT-6 Luna': ('AMP_REAL_20261106T105533Z_aa697342', 49),
}


def sha(bruto):
    return hashlib.sha256(bruto).hexdigest()


def gravar_json(nome, valor):
    (PASTA / nome).write_text(json.dumps(valor, ensure_ascii=False, indent=2) + '\n')


def gravar_csv(nome, linhas):
    assert linhas
    with (PASTA / nome).open('w', newline='') as arq:
        w = csv.DictWriter(arq, fieldnames=list(linhas[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(linhas)


def principal():
    head = subprocess.check_output(['git', '-C', str(EXPERIMENTO), 'rev-parse', 'HEAD'], text=True).strip()
    if head != SHA_EXPERIMENTO:
        raise ValueError('A revisão experimental mudou; conferir a base antes de regenerar.')
    fontes = {}

    def ler(caminho):
        bruto = caminho.read_bytes()
        fontes[str(caminho.relative_to(ESCRITA.parent))] = sha(bruto)
        return bruto

    ler(Path(__file__).resolve())
    catalogo = json.loads(ler(EXPERIMENTO / 'outputs/catalogos/ampliado_v1/catalogo_issues.json'))
    assert len(catalogo) == len({x['caso_id'] for x in catalogo}) == 78
    assert Counter(x['classificacao_auditoria'] for x in catalogo) == {
        'confirmado': 55, 'falso_positivo': 21, 'inconclusivo': 2}
    original = {x['caso_id']: x for x in catalogo}
    manifesto_owasp = json.loads(ler(PASTA / 'fontes-owasp/manifesto.json'))
    por_cwe = defaultdict(set)
    paginas = {}
    for cat, meta in manifesto_owasp['categorias'].items():
        bruto = ler(PASTA / 'fontes-owasp' / meta['arquivo'])
        assert sha(bruto) == meta['sha256']
        partes = re.split(r'(?im)^##\s+List of Mapped CWEs\s*$', bruto.decode())
        assert len(partes) == 2
        cwes = set(re.findall(r'\bCWE-\d+\b', partes[1]))
        assert cwes == set(meta['cwes'])
        for cwe in cwes:
            por_cwe[cwe].add(cat)
        paginas[cat] = 'https://top10.owasp.org/2025/' + meta['arquivo'][:-3] + '/'

    decisoes = json.loads(ler(PASTA / 'decisoes-contextuais.json'))
    assert len(decisoes) == 8
    linhas, evidencias = [], []
    for x in catalogo:
        # Consulta o objeto Git fixado, mesmo se uma cópia de trabalho tiver mudado.
        codigo = subprocess.check_output([
            'git', '-C', str(ALVO), 'show', x['commit_alvo'] + ':' + x['arquivo']])
        assert sha(codigo) == x['arquivo_sha256'], x['caso_id']
        trecho = ''.join(codigo.decode().splitlines(keepends=True)[
            x['trecho_linha_inicio'] - 1:x['trecho_linha_fim']])
        assert trecho == x['trecho'], x['caso_id']
        cwes = x['cwe_ids']
        candidatas = sorted(set().union(*(por_cwe[c] for c in cwes)))
        categoria = x['owasp_2025']
        if categoria:
            metodo = 'categoria original preservada'
            justificativa = 'Associação registrada no catálogo das campanhas, sem reclassificação nesta análise.'
            fonte = 'catálogo original; metadados da regra e mapa de conversão do pipeline'
        elif x['caso_id'] in decisoes:
            dec = decisoes[x['caso_id']]
            categoria = dec['categoria']
            metodo = 'associação contextual documentada'
            justificativa = dec['justificativa']
            fonte = paginas[categoria]
            evidencias.append({
                'caso_id': x['caso_id'], 'commit_alvo': x['commit_alvo'],
                'arquivo': x['arquivo'], 'arquivo_sha256': sha(codigo),
                'linha_inicio': x['linha_inicio'], 'linha_fim': x['linha_fim'],
                'trecho': x['trecho'], 'justificativa_arquivada': x['justificativa_auditoria'],
                'decisao': dec, 'fonte_owasp': fonte,
            })
        else:
            assert len(candidatas) == 1, (x['caso_id'], candidatas)
            categoria = candidatas[0]
            metodo = 'correspondência explícita CWE–OWASP'
            justificativa = 'CWE registrado consta da lista oficial da categoria; não equivale à revalidação da ocorrência.'
            fonte = paginas[categoria]
        if x['classificacao_auditoria'] != 'confirmado':
            justificativa += ' Preservar triagem: não contabilizar como vulnerabilidade confirmada.'
        linhas.append({
            'caso_id': x['caso_id'], 'arquivo': x['arquivo'], 'linha_inicio': x['linha_inicio'],
            'check_id': x['check_id'], 'cwe': '; '.join(cwes),
            'owasp_original': json.dumps(x['owasp_original'], ensure_ascii=False),
            'owasp_2025_original': x['owasp_2025'] or '',
            'owasp_por_cwe': '; '.join(candidatas), 'owasp_2025_analise': categoria,
            'metodo': metodo, 'classificacao_auditoria': x['classificacao_auditoria'],
            'fonte': fonte, 'justificativa': justificativa,
        })
    assert all(x['owasp_2025_analise'] for x in linhas)
    complemento = [x for x in linhas if not x['owasp_2025_original']]
    assert len(complemento) == 49
    assert Counter(x['metodo'] for x in complemento) == {
        'correspondência explícita CWE–OWASP': 41, 'associação contextual documentada': 8}
    gravar_csv('classificacao-complementar.csv', complemento)
    gravar_csv('classificacao-78-casos.csv', linhas)
    gravar_json('revisao-contextual.json', evidencias)

    classificacao = {x['caso_id']: x for x in linhas}
    modelos, resultados = {}, []
    for modelo, (execucao, total_esperado) in CAMPANHAS.items():
        pasta_campanha = EXPERIMENTO / 'outputs/campanha_docker' / execucao
        contrato = json.loads(ler(pasta_campanha / 'contrato_execucao.json'))
        assert len(contrato['casos']) == 78
        caminho = EXPERIMENTO / 'outputs/rris' / (execucao + '_METRICAS') / 'casos.csv'
        linhas_casos = list(csv.DictReader(ler(caminho).decode().splitlines()))
        assert len(linhas_casos) == 78
        assert {x['caso_id'] for x in linhas_casos} == set(original)
        assert all(x['iniciado'] == 'true' for x in linhas_casos)
        aceitos = {x['caso_id'] for x in linhas_casos if x['aceito_criterio'] == 'true'}
        assert len(aceitos) == total_esperado
        modelos[modelo] = aceitos
        for x in linhas_casos:
            c = classificacao[x['caso_id']]
            resultados.append({
                'modelo': modelo, 'execucao': execucao, 'caso_id': x['caso_id'],
                'owasp_2025_original': c['owasp_2025_original'],
                'owasp_2025_analise': c['owasp_2025_analise'],
                'classificacao_auditoria': c['classificacao_auditoria'],
                'aceito_criterio': x['aceito_criterio'],
                'definicao_f': 'criterio', 'populacao': '78 casos iniciados por modelo',
            })
    gravar_csv('casos-modelos-classificados.csv', resultados)
    resumo = []
    for cat in sorted({x['owasp_2025_analise'] for x in linhas}):
        grupo = [x for x in linhas if x['owasp_2025_analise'] == cat]
        ids = {x['caso_id'] for x in grupo}
        triagem = Counter(x['classificacao_auditoria'] for x in grupo)
        for modelo, aceitos in modelos.items():
            resumo.append({
                'categoria': cat, 'modelo': modelo, 'definicao_f': 'criterio',
                'casos_aceitos': len(ids & aceitos), 'total_casos': len(ids),
                'classificacao_confirmado': triagem['confirmado'],
                'classificacao_falso_positivo': triagem['falso_positivo'],
                'classificacao_inconclusivo': triagem['inconclusivo'],
            })
    for modelo, (_, total) in CAMPANHAS.items():
        rs = [x for x in resumo if x['modelo'] == modelo]
        assert sum(x['total_casos'] for x in rs) == 78
        assert sum(x['casos_aceitos'] for x in rs) == total
    gravar_csv('aceites-por-owasp-complementar.csv', resumo)
    tabela = ['| Categoria OWASP 2025 | GPT-4.1 mini | GPT-5.6 Luna | GPT-6 Luna |',
              '|---|---|---|---|']
    for cat in sorted({x['categoria'] for x in resumo}):
        rs = [x for x in resumo if x['categoria'] == cat]
        tabela.append('| ' + cat + ' | ' + ' | '.join(
            f"{x['casos_aceitos']}/{x['total_casos']}" for x in rs) + ' |')
    (PASTA / 'tabela-owasp-complementar.md').write_text('\n'.join(tabela) + '\n')
    gravar_json('manifesto-conferencia.json', {
        'consulta': '2026-11-11', 'sha_experimento': head,
        'sha_owasp': manifesto_owasp['commit'], 'fontes_sha256': fontes,
        'casos': 78, 'originais_preservados': 29, 'complementares': 49,
        'correspondencias_explicitas': 41, 'associacoes_contextuais': 8,
        'arquivos_alvo_conferidos_por_caso': 78,
        'distribuicao_78': dict(sorted(Counter(x['owasp_2025_analise'] for x in linhas).items())),
        'distribuicao_complemento': dict(sorted(Counter(x['owasp_2025_analise'] for x in complemento).items())),
        'totais_aceitos': {m: len(ids) for m, ids in modelos.items()},
        'artefatos_sha256': {nome: sha((PASTA / nome).read_bytes()) for nome in (
            'classificacao-complementar.csv', 'classificacao-78-casos.csv',
            'revisao-contextual.json', 'casos-modelos-classificados.csv',
            'aceites-por-owasp-complementar.csv', 'tabela-owasp-complementar.md')},
        'limite': 'Revisão documental com apoio automatizado; não é validação humana independente, novo teste de exploração ou revisão integral dos CWEs originais.',
    })
    print('\n'.join(tabela))
    print('Conferidos: 78 casos; 49 complementares; 234 pares caso/modelo; totais 38, 51 e 49 preservados.')


if __name__ == '__main__':
    principal()
