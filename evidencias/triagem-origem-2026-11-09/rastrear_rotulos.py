"""Rastreia rótulos arquivados por leitura; não executa scans, testes ou LLMs."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import yaml

OUT = Path(__file__).resolve().parent
EXP = OUT.parents[2] / 'tcc2-llm-sast-juiceshop'
ROOT = EXP / 'outputs/auditoria_sast/combinado-hZGD7r'
sources = {}

def load(path):
    sources[str(path.relative_to(EXP))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return json.loads(path.read_text()) if path.suffix == '.json' else yaml.safe_load(path.read_text())

summary = load(ROOT / 'triagem-final/resumo.json')
matrix_path = EXP / 'outputs/auditoria_sast/rodada12/matriz_desafios.json'
matrix = load(matrix_path)
assert sources[str(matrix_path.relative_to(EXP))] == summary['matriz_historica_sha256']
review_path = ROOT / 'revisao.json'
reviews = load(review_path)
assert sources[str(review_path.relative_to(EXP))] == summary['revisao_sha256']
final = load(ROOT / 'triagem-final/alertas_classificados.json')
cat = load(EXP / 'outputs/catalogos/ampliado_v1/catalogo_issues.json')
historical = {x['id']: x for x in matrix['alertas']}
configs = [EXP / 'config/auditoria_desafios.yaml'] + [EXP / f'config/auditoria_desafios_rodada{i}.yaml' for i in range(2, 13)]
entries = [(str(p.relative_to(EXP)), i, rule) for p in configs for i, rule in enumerate(load(p).get('triagem', []), 1)]
rows = []
for item in final:
    if item['status'] not in ('confirmado', 'inconclusivo'):
        continue
    explicit = [r for r in reviews if (r['regra'], r['arquivo'], r['inicio'], r['fim']) == (item['regra'], item['arquivo'], item['inicio'], item['fim'])]
    reference_ids = item['referencias_historicas']
    trace_mode = 'referencias_historicas'
    if not reference_ids:
        assert explicit, item
        reference_ids = [x['id'] for x in matrix['alertas'] if (x['regra'], x['arquivo'], x['inicio'], x['fim']) == (item['regra'], item['arquivo'], item['inicio'], item['fim'])]
        trace_mode = 'revisao_explicita_com_historico_por_identidade'
    history = []
    for ident in reference_ids:
        original = historical[ident]
        assert (original['regra'], original['arquivo'], original['inicio'], original['fim']) == (item['regra'], item['arquivo'], item['inicio'], item['fim'])
        candidates = [(p, i, r) for p, i, r in entries if r['regra'] == original['regra'] and r['arquivo'] == original['arquivo'] and r['linha'] == original['inicio'] and ('scan' not in r or r['scan'] == original['scan'])]
        assert candidates, ident
        config_path, index, origin = candidates[0]
        assert origin['status'] == original['triagem']['status'] == item['status']
        history.append({'id_historico': ident, 'scan': original['scan'], 'arquivo_triagem': config_path,
                        'entrada_triagem': index, 'status': origin['status'], 'justificativa_inicial': origin['motivo'],
                        'justificativa_matriz': original['triagem']['motivo']})
    assert history
    match = [c for c in cat if (c['check_id'], c['arquivo'], c['linha_inicio'], c['linha_fim']) == (item['regra'], item['arquivo'], item['inicio'], item['fim'])]
    assert len(match) == 1 and match[0]['classificacao_auditoria'] == item['status']
    rows.append({'caso_id': match[0]['caso_id'], 'numero_scan': item['numero'], 'status': item['status'],
                 'arquivo': item['arquivo'], 'inicio': item['inicio'], 'fim': item['fim'], 'regra': item['regra'],
                 'justificativa_final': item['motivo'], 'desafios': item['desafios'],
                 'modo_rastreio': trace_mode, 'referencias_no_registro': item['referencias_historicas'],
                 'origens': history, 'revisao_explicita': explicit})
assert Counter(r['status'] for r in rows) == {'confirmado': 55, 'inconclusivo': 2}
for rel in ['scripts/auditoria/gerar_matriz_desafios.py','scripts/auditoria/classificar_scan_combinado.py',
            'scripts/auditoria/revisar_associacoes.py','scripts/experimento/gerar_catalogo_ampliado.py',
            'config/revisoes_associacoes_rodada6.yaml','outputs/auditoria_sast/combinado-hZGD7r/RELATORIO.md']:
    p = EXP / rel
    sources[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
(OUT / 'rastreio.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
(OUT / 'fontes-sha256.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2, sort_keys=True)+'\n')
with (OUT / 'rastreio.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['caso_id','numero_scan','status','arquivo','inicio','regra','justificativa_final','fontes_triagem','revisao_explicita'])
    writer.writeheader()
    for row in rows:
        writer.writerow({**{k:row[k] for k in ['caso_id','numero_scan','status','arquivo','inicio','regra','justificativa_final']},
                         'fontes_triagem': ';'.join(sorted({r['arquivo_triagem'] for r in row['origens']})),
                         'revisao_explicita': bool(row['revisao_explicita'])})
print('Origem rastreada: 55 confirmados e 2 inconclusivos; modos:', dict(Counter(r['modo_rastreio'] for r in rows)))
print('Correspondência com catálogo e hashes da matriz e revisão conferidos; nenhum experimento executado.')
