#!/usr/bin/env python3
"""Confere consolidados existentes e deriva tabelas; não executa o experimento."""
from pathlib import Path
from collections import Counter
from itertools import combinations
from statistics import mean, median
import csv
import hashlib
import json
import sys

csv.field_size_limit(sys.maxsize)
HERE = Path(__file__).resolve().parent
EXP = HERE.parents[2] / 'tcc2-llm-sast-juiceshop'
RUNS = {
    'GPT-4.1 mini': 'AMP_REAL_20261106T151004Z_f49ac0d2',
    'GPT-5.6 Luna': 'AMP_REAL_20261106T125801Z_0eb68fe4',
    'GPT-6 Luna': 'AMP_REAL_20261106T105533Z_aa697342',
}
DEFS = ('sem_separacao', 'marcador', 'criterio')
sources = {}


def read(path):
    sources[str(path.relative_to(EXP))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return json.loads(path.read_text())


def export(name, rows):
    with (HERE / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def rate(n, d):
    return {'numerador': n, 'denominador': d, 'percentual': n * 100 / d if d else None}


catalog = read(EXP / 'outputs/catalogos/ampliado_v1/catalogo_issues.json')
by_id = {c['caso_id']: c for c in catalog}
assert len(by_id) == 78
summary = {'catalogo': {}, 'modelos': {}, 'sobreposicao': {}, 'verificacoes': {}}
for key in ('sigla_vuln', 'owasp_2025', 'classificacao_auditoria', 'check_id'):
    summary['catalogo'][key] = dict(Counter(str(c[key]) for c in catalog))
summary['catalogo']['quantidade_cwe_composta'] = dict(Counter('|'.join(c['cwe_ids']) for c in catalog))
slim_rows, group_rows, strategy_rows, metrics_rows, cases_rows = [], [], [], [], []
sets = {}
shared = None

for model, run_id in RUNS.items():
    run = EXP / 'outputs/campanha_docker' / run_id
    original = EXP / 'outputs/rris' / (run_id + '_METRICAS')
    fresh = HERE / 'consolidados' / run_id
    manifest = read(original / 'manifesto.json')
    for name, expected in manifest['artefatos_sha256'].items():
        assert hashlib.sha256((original / name).read_bytes()).hexdigest() == expected, (run_id, name)
    comparisons = {p.name: p.read_bytes() == (original / p.name).read_bytes()
                   for p in fresh.iterdir() if p.is_file()}
    assert all(comparisons.values()), (run_id, comparisons)
    summary['verificacoes'][model] = {'artefatos_identicos_reconsolidacao': comparisons}
    report = read(original / 'metricas.json')
    contract = read(run / 'contrato_execucao.json')
    session = read(run / 'resultados_consolidados' / (run_id + '_sessoes.json'))
    with (fresh / 'tentativas.csv').open() as f:
        all_rows = list(csv.DictReader(f))
    raw_path = run / 'resultados_consolidados/execucoes.jsonl'
    sources[str(raw_path.relative_to(EXP))] = hashlib.sha256(raw_path.read_bytes()).hexdigest()
    raw_rows = [json.loads(line) for line in raw_path.read_text().splitlines() if line.strip()]
    assert len(all_rows) == len(raw_rows)
    assert all(r['condicao'] == 'desenho' and r['dry_run'] == 'false' and r['do_cache'] == 'false' for r in all_rows)
    assert set(contract['casos']) == set(by_id)
    common = {key: contract[key] for key in ('commit_alvo', 'casos', 'comparador', 'estrategias',
              'hashes_catalogo', 'perfil_sha256', 'componentes_prompt_sha256',
              'baseline_testes_sha256', 'rag', 'validacao')}
    if shared is None:
        shared = common
    else:
        assert common == shared, (model, 'Condições compartilhadas divergentes')
    assert len(session) == 1 and session[0].get('fim')
    assert not session[0].get('interrompida_por_orcamento')
    assert not session[0].get('interrompida_pelo_usuario')
    main_rows = [r for r in all_rows if r['pos_aceite'] == 'false']
    assert len({(r['caso_id'], r['estrategia_curta']) for r in main_rows}) == len(main_rows)
    metrics = report['populacoes']['real_desenho']
    assert len(main_rows) == metrics['tentativas']
    accepted = {r['caso_id'] for r in main_rows if r['status_aplicacao'] == 'aplicado'
                and r['R'] == r['F_criterio'] == r['M'] == '1'}
    sets[model] = accepted
    assert len(accepted) == report['metricas_por_caso']['real_desenho']['criterio']['CR']['numerador']
    sensitivity = {}
    for definition in DEFS:
        fm = 'F_' + definition
        recomputed = {
            'TRV': rate(sum(r['status_aplicacao'] == 'aplicado' and r['R'] == r[fm] == r['M'] == '1' for r in main_rows), len(main_rows)),
            'TAP': rate(sum(r['status_aplicacao'] == 'aplicado' for r in main_rows), len(main_rows)),
            'TRI': rate(sum(r['R'] == '1' for r in main_rows), sum(r['R'] in ('0', '1') for r in main_rows)),
            'TPF': rate(sum(r[fm] == '1' for r in main_rows), sum(r[fm] in ('0', '1') for r in main_rows)),
            'TNINI': rate(sum(r['M'] == '1' for r in main_rows), sum(r['M'] in ('0', '1') for r in main_rows)),
            'TFF': rate(sum(r[fm] == '0' for r in main_rows), sum(r[fm] in ('0', '1') for r in main_rows)),
        }
        for name, value in recomputed.items():
            original_metric = metrics['definicoes'][definition]['metricas'][name]
            assert all(value[k] == original_metric[k] for k in ('numerador', 'denominador')), (model, definition, name)
            metrics_rows.append({'modelo': model, 'populacao': 'real_desenho', 'definicao_f': definition, 'metrica': name, **value})
        sensitivity[definition] = recomputed
    status = dict(Counter(r['status_aplicacao'] for r in main_rows))
    for strategy in ('P1', 'P2', 'P3', 'P4'):
        rows = [r for r in main_rows if r['estrategia_curta'] == strategy]
        successes = sum(r['status_aplicacao'] == 'aplicado' and r['R'] == r['F_criterio'] == r['M'] == '1' for r in rows)
        original_group = next(g for g in report['agregacoes']['real_desenho']['estrategia'] if g['grupo'] == strategy)
        assert successes == original_group['definicoes']['criterio']['TRV']['numerador']
        strategy_rows.append({'modelo': model, 'estrategia': strategy, **rate(successes, len(rows)), 'populacao': 'real_desenho', 'definicao_f': 'criterio'})
    for dimension in ('sigla_vuln', 'check_id', 'owasp_2025', 'classificacao_auditoria'):
        groups = sorted({str(c[dimension]) for c in catalog})
        for group in groups:
            members = {c['caso_id'] for c in catalog if str(c[dimension]) == group}
            group_rows.append({'modelo': model, 'dimensao': dimension, 'grupo': group,
                               **rate(len(accepted & members), len(members)), 'definicao_f': 'criterio'})
    for case in report['casos']:
        cases_rows.append({'modelo': model, 'caso_id': case['caso_id'], 'aceito': case['caso_id'] in accepted,
                           'estrategia_primeiro_aceite': case['estrategia_aceite_original'],
                           'sigla_vuln': by_id[case['caso_id']]['sigla_vuln'],
                           'classificacao_arquivada': by_id[case['caso_id']]['classificacao_auditoria']})
    for row in all_rows:
        slim_rows.append({'modelo': model, **{k: row[k] for k in ('tentativa_id', 'caso_id', 'estrategia_curta', 'pos_aceite', 'status_aplicacao', 'R', 'F_sem_separacao', 'F_marcador', 'F_criterio', 'M', 'custo_usd', 'tokens_entrada', 'tokens_saida', 'duracao_llm_s')}})
    costs = report['custos_tempos']
    total_cost = sum(float(r['custo_usd']) for r in all_rows)
    main_cost = sum(float(r['custo_usd']) for r in main_rows)
    tariffs = contract['inferencia']['precos']
    for row in raw_rows:
        tokens_in, tokens_out = row['tokens_entrada'], row['tokens_saida']
        cached, written = row.get('tokens_entrada_cache') or 0, row.get('tokens_escrita_cache') or 0
        in_factor, out_factor = (2, 1.5) if model != 'GPT-4.1 mini' and tokens_in > 272000 else (1, 1)
        recalculated_cost = (((tokens_in-cached-written)*tariffs['entrada'] + cached*tariffs['entrada_cache']
                              + written*tariffs.get('entrada_escrita_cache', 0))*in_factor
                             + tokens_out*tariffs['saida']*out_factor)/1000000
        assert round(recalculated_cost, 6) == row['custo_usd'], (model, row['tentativa_id'], 'custo')
    assert abs(total_cost - costs['custo_usd']['total_conhecido']) < .000002
    latencies = [float(r['duracao_llm_s']) for r in all_rows]
    rr = report['RRIS']
    rr_manifest = read(EXP / 'outputs/rris' / run_id / 'manifesto.json')
    functional = read(EXP / 'outputs/rris' / run_id / 'validacao_funcional.json')
    rr_failures = set(functional['testes_falhos_f_criterio'])
    for group in functional['grupos_apos_a_primeira_falha']:
        rr_failures.update(group['testes_falhos_f_criterio'])
    for side in ('antes', 'depois'):
        scan = read(EXP / 'outputs/rris' / run_id / f'scan_{side}.json')
        assert len(scan['results']) == rr['I_' + side]
    summary['modelos'][model] = {
        'execucao': run_id, 'contrato': contract, 'sessao': session,
        'total_registros': len(all_rows), 'populacao_principal': len(main_rows), 'pos_aceite': len(all_rows)-len(main_rows),
        'casos_aceitos': sorted(accepted), 'metricas': sensitivity, 'status_aplicacao': status,
        'R_M_nao_medidos': metrics['R_M_nao_medidos'],
        'F_nao_medido': metrics['definicoes']['criterio']['F_nao_medido'],
        'incompletas_normalizacao': metrics['definicoes']['criterio']['normalizacao_incompleta'],
        'indeterminadas_sast': metrics['indeterminadas_sast'],
        'custo_total_usd': total_cost, 'custo_populacao_principal_usd': main_cost,
        'custo_total_por_caso_aceito_usd': total_cost/len(accepted),
        'latencia_media_s': mean(latencies), 'latencia_mediana_s': median(latencies),
        'tokens_entrada': sum(int(r['tokens_entrada']) for r in all_rows),
        'tokens_saida': sum(int(r['tokens_saida']) for r in all_rows),
        'tokens_entrada_cache_provedor': sum(r.get('tokens_entrada_cache') or 0 for r in raw_rows),
        'tokens_escrita_cache_provedor': sum(r.get('tokens_escrita_cache') or 0 for r in raw_rows),
        'duracao_campanha_s': costs['duracoes_sessoes'][0]['duracao_s'],
        'latencia_acumulada_s': sum(latencies),
        'rris': {'selecionados': len(accepted), 'aplicados': len(rr['patches_aplicados']),
                 'conflitos': len(rr['conflitos']), 'antes': rr['I_antes'], 'depois': rr['I_depois'],
                 'percentual': (rr['I_antes']-rr['I_depois'])/rr['I_antes']*100,
                 'conjunto_funcionalmente_validado': rr['conjunto_funcionalmente_validado'],
                 'falhas_funcionais_uniao': sorted(rr_failures),
                 'avisos_cobertura_scan': len(rr['cobertura_limitada'])},
    }

for a, b in combinations(RUNS, 2):
    summary['sobreposicao'][a + ' / ' + b] = len(sets[a] & sets[b])
all_sets = list(sets.values())
summary['sobreposicao']['todos'] = len(set.intersection(*all_sets))
summary['sobreposicao']['ao_menos_um'] = len(set.union(*all_sets))
summary['sobreposicao']['nenhum'] = len(set(by_id) - set.union(*all_sets))
summary['sobreposicao']['exclusivos'] = {model: sorted(accepted - set.union(*(s for m,s in sets.items() if m != model))) for model, accepted in sets.items()}
summary['sobreposicao']['combinacoes_exclusivas'] = dict(Counter('|'.join(m for m in RUNS if c in sets[m]) or 'nenhum' for c in by_id))
export('metricas-conferidas.csv', metrics_rows)
export('estrategias.csv', strategy_rows)
export('grupos-casos.csv', group_rows)
export('casos-modelos.csv', cases_rows)
export('tentativas-resumo.csv', slim_rows)
(HERE / 'dados-conferidos.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
(HERE / 'fontes-sha256.json').write_text(json.dumps(sources, ensure_ascii=False, indent=2, sort_keys=True)+'\n')
print('Conferidos os três consolidados e derivados CSVs, sobreposição, custos e tempos.')
print('Todos os artefatos reconsolidados são idênticos aos originais, byte a byte.')
print('Sobreposição:', json.dumps(summary['sobreposicao'], ensure_ascii=False))
for model, data in summary['modelos'].items():
    print(model, 'principal/total/pós', data['populacao_principal'], data['total_registros'], data['pos_aceite'],
          'latência média/mediana', round(data['latencia_media_s'],3), round(data['latencia_mediana_s'],3),
          'custo total/principal', round(data['custo_total_usd'],6), round(data['custo_populacao_principal_usd'],6),
          'status', data['status_aplicacao'])
