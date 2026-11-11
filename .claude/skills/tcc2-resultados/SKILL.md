---
name: tcc2-resultados
description: Audita execuções e métricas do experimento para produzir tabelas e interpretações rastreáveis, com denominadores, estados indeterminados e limitações do desenho.
---

# Interpretar resultados do pipeline

Leia as [notas do capítulo 5](../../../evidencias/capitulo-5-notas.md) e o
[apoio do capítulo 5](../../../evidencias/capitulo-5-apoio/README.md), que registram o
recorte, as fontes e os cálculos já conferidos. Localize o experimento conforme o
`AGENTS.md` e confira o HEAD do clone antes de reutilizar análises anteriores;
métricas acrescentadas por commits posteriores precisam de evidência atualizada.

Identifique a execução pedida. Sem indicação, use o recorte das notas do capítulo 5
ou proponha um recorte fundamentado; não escolha pelo maior sucesso. Leia primeiro
o `modo` do contrato (`contrato_execucao.json`). Em preflight, confira a preparação e
a ausência de tentativas; `status=concluido` de preflight não significa campanha
concluída. Nas campanhas, leia as sessões, `resultados_consolidados/execucoes.jsonl`
e o manifesto das métricas, e confira modelo, provedor, commit alvo, regras,
comparador, baseline, política funcional e estado de conclusão.

No clone, as tentativas ficam em `outputs/campanha_docker/<EXECUCAO>/` e as métricas
consolidadas com a RRIS em `outputs/rris/<EXECUCAO>_METRICAS/`. Antes de citar uma
métrica, confira `status`, política, numerador e denominador: valor vazio, denominador
zero e indeterminação não são 0%. Os CSVs são em formato longo; linhas repetidas
podem ser populações, definições de F ou políticas diferentes.

Para uma tabela de resultados:

1. Separe real e dry-run, desenho e diagnóstico P1L, tentativas antes e depois do
   aceite, piloto e campanha, ambiente e modelo. Replays não são novas gerações.
2. Preserve R, F e M indeterminados. Na campanha ampliada, a TRV divide pelas
   tentativas feitas até o primeiro aceite de cada caso; TRI, TPF e TNINI usam só as
   medidas, e as variantes `_minima` usam todas as tentativas. Confira a política na
   revisão da execução, porque o legado usa outra.
3. Explicite a definição principal de F (`criterio`), as sensibilidades
   (`sem_separacao`, `marcador`) e a regra de parada observada. A cadeia para no
   aceite com todos os testes; não reconstrua uma cadeia hipotética.
4. Mostre numerador, denominador, proporção, ausências e fonte. Confira algumas
   linhas no JSONL e a reconciliação entre tentativas e casos, sem contar CWEs em dobro.
5. Preserve custos desconhecidos e distinga soma de durações de tempo de relógio.

As estratégias seguem P1→P4 com parada: as taxas de P2–P4 são condicionais aos casos
restantes. P1 e P2 recebem só o código; P3 e P4 acrescentam o alerta do Semgrep e o
documento do RAG ao mesmo tempo, então a melhora de P3 não é atribuível só ao RAG.
Não proponha testes estatísticos que suponham independência entre tentativas do
mesmo caso. A RRIS exige patches aplicados juntos e scans comparáveis; sem validação
funcional do conjunto, é redução no Semgrep, não remediação validada.

Para recalcular, use o consolidador offline do experimento
(`scripts/relatorios/consolidar_metricas.py --help`) com **saída nova nesta escrita**,
em `evidencias/<assunto>-AAAA-MM-DD/`. Não execute geração com LLM, dry-run nem testes
do alvo para uma tarefa de leitura de resultados.

Entregue tabelas regeneráveis, proveniência, resposta delimitada às perguntas e
lacunas. Não afirme uma taxa final enquanto o estado da campanha e seus
denominadores não forem verificados.
