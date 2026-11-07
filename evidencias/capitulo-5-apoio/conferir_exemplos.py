#!/usr/bin/env python3
"""Verifica e documenta quatro tentativas de dois casos já executados."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
EXP = HERE.parents[2] / 'tcc2-llm-sast-juiceshop'
DEST = HERE / 'exemplos'
DEST.mkdir(exist_ok=True)
selections = [
    ('pedidos-mini-p1', 'AMP_REAL_20261106T151004Z_f49ac0d2', 'AMP20721d202c8b96d6', 'P1_simples'),
    ('captcha-mini-p1', 'AMP_REAL_20261106T151004Z_f49ac0d2', 'AMP869de4721b99fc7c', 'P1_simples'),
    ('captcha-luna6-p1', 'AMP_REAL_20261106T105533Z_aa697342', 'AMP869de4721b99fc7c', 'P1_simples'),
    ('captcha-luna6-p2', 'AMP_REAL_20261106T105533Z_aa697342', 'AMP869de4721b99fc7c', 'P2_raciocinio_guiado'),
]
catalog = {c['caso_id']: c for c in json.loads((EXP/'outputs/catalogos/ampliado_v1/catalogo_issues.json').read_text())}
summaries = []
for name, execution, case_id, strategy in selections:
    run = EXP / 'outputs/campanha_docker' / execution
    records = [json.loads(line) for line in (run/'resultados_consolidados/execucoes.jsonl').read_text().splitlines() if line.strip()]
    row = next(r for r in records if r['caso_id'] == case_id and r['estrategia_prompt'] == strategy)
    artifacts = {}
    for relative, expected in row['artefatos_sha256'].items():
        path = run / relative
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, path
        artifacts[str(path.relative_to(EXP))] = expected
    patch_path = EXP / row['artefatos']['patch']
    (DEST / (name+'.diff')).write_bytes(patch_path.read_bytes())
    test_path = EXP / row['artefatos']['validacao']
    test = json.loads(test_path.read_text())
    assert bool(row['F_criterio']) == test['F_criterio']
    summary = {
        'nome': name, 'execucao': execution, 'caso_id': case_id, 'tentativa_id': row['tentativa_id'],
        'modelo': row['modelo'], 'estrategia': strategy, 'arquivo': row['arquivo'],
        'classificacao_arquivada': catalog[case_id]['classificacao_auditoria'],
        'justificativa_arquivada': catalog[case_id]['justificativa_auditoria'],
        **{k: row[k] for k in ('R','F_criterio','F_sem_separacao','M','classificacao_final',
                              'testes_falhos_d_criterio','testes_falhos_f_criterio')},
        'selecao_testes': test.get('selecao'), 'etapas': test.get('etapas'), 'sha256': artifacts,
    }
    (DEST / (name+'.json')).write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    summaries.append(summary)
assert summaries[0]['R'] == summaries[0]['F_criterio'] == summaries[0]['M'] == 1
assert summaries[0]['F_sem_separacao'] == 0
assert summaries[1]['R'] == summaries[1]['M'] == 1 and summaries[1]['F_criterio'] == 0
assert summaries[2]['R'] == summaries[2]['M'] == 1 and summaries[2]['F_criterio'] == 0
assert summaries[3]['R'] == summaries[3]['M'] == summaries[3]['F_criterio'] == summaries[3]['F_sem_separacao'] == 1
(DEST/'indice.json').write_text(json.dumps(summaries, ensure_ascii=False, indent=2)+'\n')
print('Conferidas quatro tentativas de dois casos:', sum(len(s['sha256']) for s in summaries), 'hashes de artefatos.')
