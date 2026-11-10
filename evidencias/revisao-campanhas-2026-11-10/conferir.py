"""Revisão documental offline: não executa campanhas, SAST ou testes."""
import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

csv.field_size_limit(sys.maxsize)

HERE = Path(__file__).resolve().parent
EXP = HERE.parents[2] / 'tcc2-llm-sast-juiceshop'
ROOT = EXP / 'outputs/campanha_docker'
shared = None
summary = []
sources = {}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(path):
    sources[str(path.relative_to(EXP))] = sha(path)
    return json.loads(path.read_text())

for path in sorted(ROOT.glob('AMP_REAL_20261106*/contrato_execucao.json')):
    run = path.parent
    contract = read(path)
    session, = read(run / 'resultados_consolidados' / f'{run.name}_sessoes.json')
    reproduction = read(run / 'sast_antes/reproducao.json')
    raw = run / 'resultados_consolidados/execucoes.jsonl'
    sources[str(raw.relative_to(EXP))] = sha(raw)
    rows = [json.loads(line) for line in raw.read_text().splitlines() if line.strip()]
    assert contract['modo'] == 'real' and not session['dry_run']
    assert session['fim'] and not session['erros']
    assert not session['interrompida_por_orcamento'] and not session['interrompida_pelo_usuario']
    assert reproduction['reproduzido'] and not reproduction['ausentes']
    common = {k:v for k,v in contract.items() if k not in ('execucao', 'inferencia')}
    if shared is None:
        shared = common
    assert common == shared, run.name
    assert session['k'] == 4 and contract['estrategias'] == ['P1','P2','P3','P4']
    assert len(rows) == len({r['tentativa_id'] for r in rows})
    assert all(r['contrato_execucao_sha256'] == sha(path) for r in rows)
    assert all(not r['dry_run'] and not r['do_cache'] for r in rows)
    assert all(r['modelo_solicitado'] == contract['inferencia']['modelo'] for r in rows)
    artifacts = 0
    by_case = defaultdict(list)
    for r in rows:
        by_case[r['caso_id']].append(r)
        for name, expected in r['artefatos_sha256'].items():
            assert sha(run / name) == expected, (run.name, name)
            artifacts += 1
    assert set(by_case) == set(contract['casos']) and len(by_case) == 78
    stop = Counter()
    for chain in by_case.values():
        chain.sort(key=lambda r: r['estrategia_prompt'])
        assert [r['estrategia_prompt'].split('_')[0] for r in chain] == ['P1','P2','P3','P4'][:len(chain)]
        assert all(r['classificacao_sem_separacao'] != 'aceita' for r in chain[:-1])
        if chain[-1]['classificacao_sem_separacao'] == 'aceita':
            stop['aceite_sem_separacao'] += 1
        else:
            assert len(chain) == 4
            stop['esgotamento_P4'] += 1
    normalized = HERE.parent / 'capitulo-5-apoio/consolidados' / run.name / 'tentativas.csv'
    with normalized.open() as stream:
        norm = list(csv.DictReader(stream))
    assert {r['tentativa_id'] for r in norm} == {r['tentativa_id'] for r in rows}
    main = [r for r in norm if r['pos_aceite'] == 'false']
    accepted = {r['caso_id'] for r in main if r['status_aplicacao'] == 'aplicado' and r['R'] == r['F_criterio'] == r['M'] == '1'}
    summary.append(dict(execucao=run.name, modelo=contract['inferencia']['modelo'],
        inicio_brasilia=datetime.fromisoformat(session['inicio']).astimezone(ZoneInfo('America/Sao_Paulo')).isoformat(),
        fim_brasilia=datetime.fromisoformat(session['fim']).astimezone(ZoneInfo('America/Sao_Paulo')).isoformat(),
        casos=len(by_case), registros=len(rows), principal=len(main), pos_aceite=len(norm)-len(main),
        casos_aceitos_criterio=len(accepted), encerramento=dict(stop),
        modelos_retornados=dict(Counter(r['modelo'] for r in rows)),
        classificacoes=dict(Counter(r['classificacao_final'] for r in rows)),
        aplicacao=dict(Counter(r['status_aplicacao'] for r in rows)),
        artefatos_sha256_conferidos=artifacts, geracao=contract['inferencia']['geracao'],
        diagnosticos_sast_inicial=len(reproduction.get('diagnosticos', [])),
        alertas_reproduzidos=reproduction.get('catalogo_qtd'),
        casos_pulados=session['casos_pulados_alerta_ausente'],
        eventos_llm=session['eventos_llm'], duracao_s=session['duracao_s']))
assert len(summary) == 3
(HERE / 'conferencia.json').write_text(json.dumps(dict(campanhas=summary, fontes_sha256=sources,
    campos_contrato_compartilhados=list(shared)), ensure_ascii=False, indent=2) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=2))
