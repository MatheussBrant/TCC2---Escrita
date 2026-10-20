---
name: tcc2-resultados
description: Audita execuções e métricas do TCC2 para produzir tabelas e interpretações rastreáveis, com denominadores, estados indeterminados e limitações do desenho.
---

# Interpretar resultados do pipeline

Leia [contexto e casos já identificados](../../../docs/contexto.md) e C07–C13 da
[matriz](../../../docs/compromissos-tcc1.md). Resolva a configuração efetiva conforme
`AGENTS.md`: `--config` explícito, `fontes.local.json` existente ou `fontes.json`.
O experimento fica, por padrão, no clone interno `tcc2-llm-sast-juiceshop/`.
Confira HEAD/refs e alterações locais antes de usar inventários anteriores;
métricas adicionadas por commits posteriores precisam de evidência atualizada.

Em uma feature, use a campanha e o SHA da base registrada em sua entrega ou
explicitamente escolhida para a tarefa. O [índice de bases](../../../features/BASE_COMUM.md)
seleciona o padrão para novas entregas; não substitui a base de uma entrega iniciada.
Registre a adequação do recorte e eventuais divergências.
Mantenha análises, tabelas e scripts na pasta `saida` daquela feature. Não altere
a base nem troque a campanha durante a rodada sem reconciliação coordenada.

Identifique a execução explicitamente solicitada. Se não houver uma, inventarie
candidatas e proponha um recorte fundamentado; não escolha pelo maior sucesso.
Leia primeiro o `modo` do contrato. Em preflight, confira o relatório de preparação
e a ausência de tentativas; sessões e JSONL podem legitimamente não existir.
`status=concluido` do preflight não significa campanha de correções concluída.
Nas execuções de correção, leia sessões, `resultados_consolidados/execucoes.jsonl`,
manifesto de métricas e catálogo. Confira modelo/provedor, commit alvo, regras, comparador,
aplicador, baseline, política funcional e estado de conclusão.

Antes de citar uma métrica, confira o campo `status`, sua política, numerador e
denominador. `valor` vazio/`null`, denominador zero e indeterminação não são 0%.
Um `casos.csv` pode enumerar casos contratados sem nenhuma tentativa realizada.
Os CSVs são em formato longo: linhas repetidas podem representar populações,
definições de F e políticas distintas, não repetições independentes.

Para uma tabela de resultados:

1. Separe real/dry-run, desenho/diagnóstico P1L, pré/pós-aceite, cache/geração,
   PoC/legado/ampliado, piloto/campanha e ambiente/modelo. Replays não são novas
   gerações independentes. Registre casos solicitados, observados e não concluídos.
2. Preserve R, F e M indeterminados. No consolidado ampliado, TRV usa todas as
   tentativas; TRI/TPF/TNINI usam os medidos e TFF o denominador da TPF. Confira
   a implementação na revisão da execução, pois o legado tem outra política.
3. Explicite F principal (`criterio` no consolidado documentado), sensibilidades
   e regra de parada observada. Não reconstrua silenciosamente uma cadeia hipotética.
4. Mostre n/d, proporção, ausências e fonte/hash. Confira algumas linhas no JSONL
   e a reconciliação de tentativas/casos, evitando dupla contagem de CWEs.
5. Preserve custos desconhecidos e distinga soma de durações de tempo de parede.

As estratégias seguem P1→P4 com parada: as taxas de P2–P4 são condicionais aos
casos restantes. P3/P4 podem acrescentar SAST e documentação juntos; não atribua
melhora exclusivamente a RAG. Não proponha testes estatísticos que suponham
independência entre tentativas do mesmo caso ou amostras comparáveis sem justificativa.

RRIS requer patches aplicados conjuntamente e scans globais comparáveis, com
evidência funcional do conjunto para chamá-lo de remediação validada. Não derive
RRIS da soma de R ou aceites isolados. Classifique resultado não medido como tal.

Se precisar recalcular, inspecione `scripts/reports/consolidate_metrics.py --help`
e use o consolidador offline existente em **saída nova neste repositório**, dentro
da pasta exclusiva quando atuar em uma feature, com entradas/catálogo da execução.
Não execute geração LLM, dry-run do pipeline ou
testes do alvo para uma tarefa de leitura de resultados. Um dry-run pode executar
SAST e testes; ele não equivale ao consolidador offline.

Entregue tabelas regeneráveis, proveniência, resposta delimitada às Qs e lacunas.
Não afirme uma taxa final enquanto o estado da campanha e seus denominadores
permanecerem sem verificação.
