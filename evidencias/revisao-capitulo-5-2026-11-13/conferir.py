"""Confere os números revisados por leitura; grava somente o resumo nesta pasta."""
import csv
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
WRITING = HERE.parents[1]
EXP = WRITING.parent / 'tcc2-llm-sast-juiceshop'
hashes = {}


def read(path):
    content = path.read_bytes()
    hashes[str(path.relative_to(EXP))] = hashlib.sha256(content).hexdigest()
    return content.decode()


def rows(path):
    return list(csv.DictReader(read(path).splitlines()))


catalog = json.loads(read(EXP / 'outputs/catalogos/ampliado_v1/catalogo_issues.json'))
excluded = json.loads(read(EXP / 'outputs/catalogos/ampliado_v1/exclusoes.json'))
triage = dict(Counter(c['classificacao_auditoria'] for c in catalog))
assert triage == {'confirmado': 55, 'falso_positivo': 21, 'inconclusivo': 2}
exclusions = Counter('Coding Challenges' if c['arquivo'].startswith('data/static/codefixes/')
                     else 'GitHub' if c['arquivo'].startswith('.github/workflows/')
                     else 'npm' if c['arquivo'] in ('.npmrc', 'frontend/.npmrc')
                     else 'outro' for c in excluded)
assert exclusions == {'Coding Challenges': 31, 'GitHub': 13, 'npm': 2}
assert len(catalog) + len(excluded) == 124
classification_path = EXP / 'config/classificacao_owasp/v1/classificacao-78-casos.csv'
classification = rows(classification_path)
assert classification_path.read_bytes() == (WRITING / 'evidencias/classificacao-owasp-complementar-2026-11-11/classificacao-78-casos.csv').read_bytes()
by_id = {c['caso_id']: c for c in classification}
assert len(by_id) == len(classification) == 78
assert set(by_id) == {c['caso_id'] for c in catalog}
owasp = Counter(c['owasp_2025_analise'] for c in classification)
assert owasp == {'A01': 26, 'A02': 3, 'A04': 5, 'A05': 22, 'A06': 12, 'A07': 7, 'A08': 3}
chapter = (WRITING / 'manuscrito/05-resultados-discussao.md').read_text()
summary = {'data': '2026-11-13', 'experimento_head': subprocess.check_output(
    ['git', '-C', str(EXP), 'rev-parse', 'HEAD'], text=True).strip(),
    'triagem': triage, 'exclusoes': dict(exclusions), 'distribuicao_owasp': dict(owasp), 'modelos': {}}
runs = [
    ('GPT-4.1 mini', 'AMP_REAL_20261106T151004Z_f49ac0d2', 283, 241, 38, 32, 17),
    ('GPT-5.6 Luna', 'AMP_REAL_20261106T125801Z_0eb68fe4', 277, 223, 51, 39, 22),
    ('GPT-6 Luna', 'AMP_REAL_20261106T105533Z_aa697342', 274, 221, 49, 36, 23),
]
for model, run, total, principal, accepted, confirmed, strict in runs:
    attempts = rows(EXP / 'outputs/rris' / (run + '_METRICAS') / 'tentativas.csv')
    assert len(attempts) == total
    main = [r for r in attempts if r['pos_aceite'] == 'false']
    assert len(main) == principal
    assert len({r['caso_id'] for r in main}) == 78
    sensitivity = {}
    accepted_ids = set()
    for definition, expected in [('sem_separacao', strict), ('marcador', strict), ('criterio', accepted)]:
        successes = [r for r in main if r['status_aplicacao'] == 'aplicado'
                     and r['R'] == r['M'] == r['F_' + definition] == '1']
        assert len(successes) == expected
        percentage = f'{expected / principal * 100:.2f}'.replace('.', ',')
        assert f'{expected}/{principal} ({percentage}%)' in chapter
        sensitivity[definition] = {'aceites': expected, 'tentativas': principal, 'percentual': percentage}
        if definition == 'criterio':
            accepted_ids = {r['caso_id'] for r in successes}
    assert len(accepted_ids) == accepted
    confirmed_ids = {c['caso_id'] for c in catalog if c['classificacao_auditoria'] == 'confirmado'}
    assert len(accepted_ids & confirmed_ids) == confirmed
    confirmed_totals = Counter(by_id[c]['owasp_2025_analise'] for c in confirmed_ids)
    confirmed_accepted = Counter(by_id[c]['owasp_2025_analise'] for c in accepted_ids & confirmed_ids)
    confirmed_table = chapter.split('**Tabela 10a —', 1)[1].split('Fonte:', 1)[0]
    model_column = [r[0] for r in runs].index(model) + 2
    for category, denominator in confirmed_totals.items():
        line = next(line for line in confirmed_table.splitlines() if line.startswith(f'| {category} —'))
        assert line.split('|')[model_column].strip() == f'{confirmed_accepted[category]}/{denominator}'
    by_category = Counter(by_id[c]['owasp_2025_analise'] for c in accepted_ids)
    for category, denominator in owasp.items():
        table_row = next(line for line in chapter.splitlines() if line.startswith(f'| {category} |'))
        assert f'{by_category[category]}/{denominator}' in table_row
    summary['modelos'][model] = {'registros': total, 'principal': principal, 'pos_aceite': total - principal,
        'aceites_confirmados': confirmed, 'confirmados': 55, 'sensibilidade_F': sensitivity,
        'aceites_owasp': {c: by_category[c] for c in sorted(owasp)},
        'owasp_confirmados': {c: {'aceites': confirmed_accepted[c], 'casos': confirmed_totals[c]}
                             for c in sorted(confirmed_totals)}}
summary['fontes_sha256'] = hashes
(HERE / 'conferencia.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k != 'fontes_sha256'}, indent=2, ensure_ascii=False))
