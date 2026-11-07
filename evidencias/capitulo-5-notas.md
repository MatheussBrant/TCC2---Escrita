# Capítulo 5 — notas de evidência e revisão do primeiro rascunho

**Estado:** primeiro rascunho produzido em 07/11/2026 a pedido do autor.
Conferência documental e cálculos com apoio automatizado; não houve revisão
humana independente, aprovação da orientadora ou auditoria de segurança.

## Entrega e recorte

- Texto: [05-resultados-discussao.md](../manuscrito/05-resultados-discussao.md).
- Plano: [plano-paragrafos-capitulo-5.md](../docs/plano-paragrafos-capitulo-5.md).
- Estilo: [criterios-escrita.md](../docs/criterios-escrita.md) e linguagem do TCC1.
- Continuidade: introdução, metodologia, implementação e notas dos capítulos 3–4.
- Fonte experimental: `../../tcc2-llm-sast-juiceshop`, HEAD
  `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas na consulta.
- Alvo: Juice Shop 20.1.1, commit `f915bddd82790d0f3018902d36ae9b4241a5f51f`.
- Campanhas finais reais de 06/11/2026, 78 casos solicitados e iniciados por modelo.
- Foram utilizadas as skills espelhadas de redação e resultados em `.claude/skills/`.
  Os arquivos históricos de contexto, matriz e features citados nas instruções
  locais permanecem ausentes; os destinos explícitos do pedido foram respeitados.
- Preservados os capítulos 1–4, as referências, o Markdown completo do TCC1 e
  `05-consideracoes-finais.md`. O índice foi atualizado separadamente.
- Não foram executadas novas campanhas, chamadas LLM, Semgrep, testes do alvo,
  simulações ou avaliação conjunta. Não foram lidas credenciais ou `.env`.
- Foi executado somente o consolidador offline existente, em saída nova na escrita,
  seguido de derivações por leitura de arquivos e geração de um gráfico.

## Campanhas e conferências

| Modelo | Execução | Registros totais | Principal | Pós-aceite | Casos aceitos |
|---|---|---:|---:|---:|---:|
| GPT-4.1 mini | `AMP_REAL_20261106T151004Z_f49ac0d2` | 283 | 241 | 42 | 38/78 |
| GPT-5.6 Luna | `AMP_REAL_20261106T125801Z_0eb68fe4` | 277 | 223 | 54 | 51/78 |
| GPT-6 Luna | `AMP_REAL_20261106T105533Z_aa697342` | 274 | 221 | 53 | 49/78 |

Para cada execução, fontes originais:

- `outputs/campanha_docker/<EXEC>/contrato_execucao.json`.
- `outputs/campanha_docker/<EXEC>/resultados_consolidados/execucoes.jsonl`.
- `outputs/campanha_docker/<EXEC>/resultados_consolidados/<EXEC>_sessoes.json`.
- `outputs/rris/<EXEC>_METRICAS/metricas.json`, CSVs e manifesto.
- `outputs/rris/<EXEC>/manifesto.json`, scans e validação funcional.
- `outputs/catalogos/ampliado_v1/catalogo_issues.json` e resumo da triagem de origem.

Condições compartilhadas conferidas por igualdade dos campos dos contratos:
commit alvo, casos, comparador, estratégias, catálogo, perfil SAST, componentes
de prompt, baseline, RAG e validação. Diferenças de geração e tarifas permaneceram
identificadas por modelo. As três sessões têm término registrado e não indicam
interrupção pelo usuário ou pelo orçamento. Não houve reutilização local de
respostas, simulação ou diagnóstico adicional nesses registros.

O consolidador existente foi executado com F=`criterio`, catálogo ampliado,
entrada da campanha e manifesto da RRIS, sem mutar a fonte. Os 15 artefatos de
cada saída nova foram comparados byte a byte aos originais: **45/45 idênticos**.
Também foram conferidos os hashes dos artefatos publicados nos manifestos.
O próprio leitor do consolidador verificou contratos, snapshots, hashes e arquivos
associados segundo sua implementação; isso não equivale a auditoria independente
da adequação dos critérios ou à inspeção manual de todos os patches.

Comando utilizado, a partir da raiz experimental, substituindo `<EXEC>` por cada
identificador da tabela:

```sh
python3 scripts/relatorios/consolidar_metricas.py \
  --execucao <EXEC> \
  --entrada outputs/campanha_docker/<EXEC> \
  --catalogo outputs/catalogos/ampliado_v1/catalogo_issues.json \
  --saida ../TCC2---Escrita/evidencias/capitulo-5-apoio/consolidados/<EXEC> \
  --definicao-f criterio \
  --evidencia-rris outputs/rris/<EXEC>/manifesto.json
```

O destino deve ser novo: o consolidador recusa sobrescrever uma saída existente.
As saídas desta conferência foram preservadas em `capitulo-5-apoio/consolidados/`.

## Cálculos derivados e denominadores

Script: [analisar_dados.py](capitulo-5-apoio/analisar_dados.py).
Dados completos desta análise: [dados-conferidos.json](capitulo-5-apoio/dados-conferidos.json).

1. População principal: linhas reais do desenho com `pos_aceite=false` no CSV
   normalizado pelo consolidador. A soma com pós-aceite reconcilia o JSONL.
2. TRV: tentativas aplicadas com R=F=M=1 / todas as tentativas dessa população.
   Foram recalculados os numeradores e denominadores, sem imputar zero às ausências.
3. TRI, TPF, TNINI e TFF: somente medições disponíveis do critério correspondente.
   TFF usa o mesmo denominador da TPF. Todas as três interpretações de F foram conferidas.
4. Aceite por caso: conjunto distinto de IDs com pelo menos uma tentativa aceita.
   O denominador é o conjunto de 78 casos solicitados, diferente da TRV.
5. Estratégias: primeiros aceites e tentativas alcançadas na cadeia principal.
   Não foram reconstruídas cadeias alternativas nem feitos testes estatísticos.
6. Tipos, regras e OWASP: partições por campo catalogado, sem criar categorias
   ausentes ou duplicar casos por CWEs. A composição dos conjuntos de CWEs é
   preservada como informação auxiliar, não usada para multiplicar ocorrências.
7. Sobreposição: interseções e diferenças dos conjuntos de IDs aceitos na definição
   principal. As oito combinações exclusivas, incluindo nenhum aceite, somam 78.
8. Custo: soma das respostas de toda a campanha, inclusive pós-aceite; separada da
   soma somente da população principal. O custo por caso aceito da Tabela 7 divide
   o total operacional pelos casos aceitos, sem apresentar essa razão como custo
   de um único patch ou custo integral de uso em produção.
9. Tarifas: custo de cada resposta recalculado com tokens ordinários, leitura e
   escrita de cache do provedor e saída, conforme contrato e implementação.
   Foram respeitados os arredondamentos por resposta. Não houve consulta a preços
   atuais ou fatura; são custos calculados segundo a configuração da execução.
10. Tempos: média e mediana de `duracao_llm_s` sobre todas as respostas; duração
    da única sessão convertida de segundos para minutos. A soma de durações
    concorrentes não foi tratada como tempo de parede. A RRIS é uma execução
    separada e não integra a duração das campanhas apresentada.
11. RRIS: (alertas antes − alertas depois) / alertas antes, com confirmação das
    contagens nos scans arquivados. A interpretação permaneceu estática quando
    o conjunto não recebeu aprovação funcional.

Resultados regeneráveis:

- [metricas-conferidas.csv](capitulo-5-apoio/metricas-conferidas.csv): n/d das métricas e definições de F.
- [estrategias.csv](capitulo-5-apoio/estrategias.csv): primeiros aceites e denominadores por etapa.
- [grupos-casos.csv](capitulo-5-apoio/grupos-casos.csv): aceites por tipo, regra, OWASP e rótulo arquivado.
- [casos-modelos.csv](capitulo-5-apoio/casos-modelos.csv): IDs, aceites e primeiro aceite por modelo.
- [tentativas-resumo.csv](capitulo-5-apoio/tentativas-resumo.csv): população, critérios, custos e latências.
- [fontes-sha256.json](capitulo-5-apoio/fontes-sha256.json): hashes das fontes diretamente consultadas;
  os manifestos originais e reconsolidados registram a cadeia mais extensa de fontes.

### Custos por população

| Modelo | Todas as respostas (US$) | Somente população principal (US$) | Diferença: pós-aceite (US$) |
|---|---:|---:|---:|
| GPT-4.1 mini | 0.433169 | 0.371354 | 0.061815 |
| GPT-5.6 Luna | 0.314826 | 0.247220 | 0.067606 |
| GPT-6 Luna | 0.138800 | 0.108694 | 0.030106 |

A tabela de referência do plano usava o custo total operacional. Esse recorte foi
preservado na comparação, com explicitação de que ele abrange mais linhas do
que a TRV. Não se dividiu silenciosamente custo operacional por tentativas da
população principal para calcular custo médio de uma tentativa científica.

## Divergências de interpretação investigadas

- **834 registros versus 685 tentativas principais:** diferença de 149 registros
  pós-aceite, não duplicação acidental nem novas observações independentes para TRV.
- **Parada e classificação:** parada por aceite sem separação; classificação
  principal por critérios. Fonte: `src/pipeline/orquestracao/campanha.py`,
  `_aceita_estrita` e atribuição de `classificacao_final`.
- **78 casos versus 55 rótulos confirmados:** campanhas mantiveram também 21 falsos
  positivos e dois inconclusivos. Recorte descritivo confirmado: 32/55, 39/55,
  36/55 aceitos. Não foi alterado retroativamente o experimento para fingir que
  esses casos não foram processados. Eventual mudança do recorte analítico exige
  revisão explícita das populações e da metodologia.
- **Cache desligado versus tokens de cache:** não houve reutilização local de
  respostas. Campos de leitura/escrita de cache do provedor integram a tarifação
  de algumas respostas e não significam repetição de uma tentativa científica.
- **Sensibilidade funcional:** as definições por marcador e sem separação têm
  valores agregados iguais nestas populações; não se afirmou que sejam definições
  equivalentes em geral. O ganho com F por critérios não valida toda classificação de D.
- **RRIS alta versus aprovação:** 48,72%, 70,51% e 60,26% são reduções estáticas;
  nenhum conjunto foi aprovado funcionalmente. Não foram descritas como remediação
  integrada validada nem obtidas pela soma de aceites individuais.

## Exemplos e alcance da análise qualitativa

Procedimento realizado nesta redação: seleção editorial e leitura de artefatos
com apoio automatizado, buscando contraste entre aceite dependente de D, remoção
acompanhada de regressão e propostas diferentes para o mesmo alerta. Não é revisão
humana, auditoria independente, análise exaustiva ou amostragem representativa.
A pendência de inspeção qualitativa no Capítulo 3 foi preservada; após revisão
dos autores, sua redação pode ser alinhada a este procedimento documental,
sem afirmar que ocorreu uma validação humana anterior.

Script: [conferir_exemplos.py](capitulo-5-apoio/conferir_exemplos.py).
Índice: [exemplos/indice.json](capitulo-5-apoio/exemplos/indice.json).
Foram conferidos existência e SHA-256 de **28 artefatos**, sete em cada tentativa:
prompt, resposta, patch, evidência funcional de SAST, comparação, scan e testes.
Os excertos de código do manuscrito são literais; os patches completos foram
copiados para a pasta de apoio, sem alterar os originais.

| Exemplo | Tentativa | R / F crit. / F estrito / M | Rótulo arquivado |
|---|---|---|---|
| pedidos-mini-p1 | `AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2` | 1 / 1 / 0 / 1 | confirmado |
| captcha-mini-p1 | `AMP869de4721b99fc7c_A05_CODEINJ_P1_AMP_REAL_20261106T151004Z_f49ac0d2` | 1 / 0 / 0 / 1 | falso_positivo |
| captcha-luna6-p1 | `AMP869de4721b99fc7c_A05_CODEINJ_P1_AMP_REAL_20261106T105533Z_aa697342` | 1 / 0 / 0 / 1 | falso_positivo |
| captcha-luna6-p2 | `AMP869de4721b99fc7c_A05_CODEINJ_P2_AMP_REAL_20261106T105533Z_aa697342` | 1 / 1 / 1 / 1 | falso_positivo |

- Pedidos: consulta em `routes/trackOrder.ts`; falha de teste de injeção separada
  em D. O texto não deriva segurança completa ou equivalência semântica de R/F/M.
- CAPTCHA: `routes/captcha.ts`, caso `AMP869de4721b99fc7c`, rótulo arquivado falso
  positivo, expressão original formada por números e operadores internos.
  A proposta mini/P1 avalia da esquerda para a direita, em desacordo com a
  precedência aritmética; falhas arquivadas em 2+3*4 e 2-3*4.
- Para 2+3*4, o valor 20 decorre da leitura da ordem das operações no patch,
  confrontada com o resultado esperado 14 no teste; não é resultado de um teste
  novo executado nesta tarefa. O manuscrito distingue essa leitura dos registros.
- Luna6/P1 também falhou; Luna6/P2 recebeu R=F=M=1 inclusive sem separação.
  Os prompts são de tentativas distintas, sem inferir que P2 aprendeu com os
  erros de P1 ou que o roteiro foi a causa isolada do resultado.
- O fato de o CAPTCHA ter rótulo de falso positivo é relevante para interpretar
  o exemplo: pode demonstrar regressão ou preservação após uma edição, mas não
  prova que uma vulnerabilidade real precisava ser corrigida.

## RRIS e falhas do conjunto

Foram conferidos scans, manifestos e `validacao_funcional.json` de cada modelo.
O relatório distingue as falhas iniciais e os grupos executados depois da primeira
falha. A síntese considerou a união de `testes_falhos_f_criterio` nesses campos,
sem contar falhas classificadas em D como regressões funcionais por inferência.

- GPT-4.1 mini: 38 selecionados, 34 aplicados, quatro conflitos, 78 → 40 alertas.
- GPT-5.6 Luna: 51 selecionados, 43 aplicados, oito conflitos, 78 → 23 alertas.
- GPT-6 Luna: 49 selecionados, 40 aplicados, nove conflitos, 78 → 31 alertas.
- Os três conjuntos falharam em login de usuário recém-criado e no contrato
  adicional de feedback normal. Os Luna também falharam na integridade de
  cenários de último IP. São falhas registradas, não causas atribuídas a patches.
- Oito avisos de cobertura estática limitada constam de cada relatório de RRIS.
- Não houve investigação causal completa nem reexecução para isolar interações.
  O rascunho relata o resultado do conjunto e mantém esse limite.

## Bibliografia verificada para 5.9

Foram conferidos metadados e resumos nas páginas primárias, em 07/11/2026:

1. Khan, Arshiya; Liu, Guannan; Gao, Xing. *Code Vulnerability Repair with Large
   Language Model using Context-Aware Prompt Tuning*. Publicação SPW 2025,
   pp. 283–287, versão arXiv v2 de 11/06/2025.
   [Fonte primária](https://arxiv.org/abs/2409.18395v2).
   Uso limitado ao escopo de Copilot, estouro de buffer e contexto de segurança.
2. Sriram, Vidyut et al. *Improving LLM-Assisted Secure Code Generation through
   Retrieval-Augmented-Generation and Multi-Tool Feedback*. arXiv, 2026, v1.
   [Fonte primária](https://arxiv.org/abs/2601.00509v1).
   Uso limitado à recuperação semântica, refinamento com compilador, CodeQL e KLEE.

Ambos constam das referências herdadas e do capítulo 2. O manuscrito não compara
suas taxas às deste estudo nem reutiliza percentuais bibliográficos sem analisar
compatibilidade. Esta consulta não equivale a revisão integral dos artigos ou
da bibliografia do TCC1. Não foram acrescentados DOI ou referências não verificados.

## Gráfico e arquivos de apoio

- [Figura em PNG](../manuscrito/assets/capitulo-5/aceites-por-estrategia.png).
- [Figura em PDF](../manuscrito/assets/capitulo-5/aceites-por-estrategia.pdf).
- [Figura em SVG](../manuscrito/assets/capitulo-5/aceites-por-estrategia.svg).
- Dados: `estrategias.csv`, com complemento sem aceite = 78 − soma dos aceites.
- Script: [gerar_grafico.py](capitulo-5-apoio/gerar_grafico.py).
- Dependências: [requisitos-graficos.txt](capitulo-5-apoio/requisitos-graficos.txt).
- A ferramenta de gráficos foi instalada em ambiente temporário separado;
  nenhum ambiente do experimento foi modificado.
- As três barras foram conferidas com soma de 78 e contagens coerentes com as
  tabelas. O gráfico foi inspecionado visualmente; não é captura do painel.
- Numeração de tabelas e figura é local ao capítulo; precisa de integração global.

Para reproduzir as derivações, a partir da raiz da escrita:

```sh
python3 evidencias/capitulo-5-apoio/analisar_dados.py
python3 evidencias/capitulo-5-apoio/conferir_exemplos.py
python3 evidencias/capitulo-5-apoio/gerar_grafico.py
```

O último comando requer as dependências de gráficos; os primeiros usam a biblioteca
padrão. Eles leem os consolidados preservados e os artefatos originais e atualizam
somente os arquivos de apoio da escrita. Não executam o pipeline experimental.

## Mapa de evidências por parágrafo

Os caminhos de código abaixo são relativos à raiz do experimento no SHA fixado.

| Plano | Seção | Evidência e alcance |
|---|---|---|
| C5-P01–P02 | Abertura | Capítulos 3–4, plano atual e definição operacional. |
| C5-P03 | 5.1 | Contratos e sessões finais; igualdade dos componentes comuns e encerramento registrado. |
| C5-P04–P05 | 5.1 | Catálogo ampliado, resumo da triagem e `grupos-casos.csv`; 124/46/78, 55/21/2, 29 com OWASP e 49 sem. Autoria humana não inferida. |
| C5-P06 | 5.1 | JSONL, CSV normalizado, política de cadeia do consolidador e `campanha.py`; totais e pós-aceites. |
| C5-P07–P10 | 5.2 | `metricas-conferidas.csv`, populações dos relatórios e normalização; numeradores, denominadores, ausências e sensibilidade. Recorte confirmado em `grupos-casos.csv`. |
| C5-P11–P14 | 5.3 | `estrategias.csv`, `casos-modelos.csv`, contratos e montagem de prompts; sem atribuição causal ao RAG/roteiro. |
| C5-P15–P17 | 5.4 | Aceites por caso, TRV, TAP e critérios; interseções e diferenças de IDs em `dados-conferidos.json`. |
| C5-P18 | 5.4 | JSONL, tokens, tarifas contratuais e `_custo` de `cliente_openai.py`; custos operacionais distintos da população principal. |
| C5-P19 | 5.4 | Latências de respostas, horários e duração da sessão; médias e medianas derivadas, sem somar paralelismo como tempo de parede. |
| C5-P20–P22 | 5.5 | Catálogo, grupos por sigla, regra e OWASP; as partições conservam denominadores sem preencher campos ausentes. |
| C5-P23–P26 | 5.6 | Quatro tentativas, patches, comparações, respostas e testes; 28 hashes conferidos e excertos literais. Leitura com apoio automatizado, sem auditoria humana. |
| C5-P27–P29 | 5.7 | Manifestos e scans da RRIS, falhas iniciais e grupos subsequentes; não foi isolada a origem causal das regressões. |
| C5-P30–P34 | 5.8 | Q1–Q5 da introdução e resultados conferidos de 5.1–5.7. Respostas limitadas aos critérios e ao desenho. |
| C5-P35 | 5.9 | Páginas primárias verificadas de Khan et al. e Sriram et al.; aproximação conceitual, sem equiparar desenhos e taxas. |
| C5-P36–P37 | 5.9 | Exemplos e RRIS; implicações interpretativas explícitas, sem alegar uso em produção ou revisão humana integral. |
| C5-P38–P40 | 5.10 | Limites do método, definições de D, amostra e contratos; replicabilidade possível distinta de replicação independente. |

## Pendências para revisão dos autores

| ID | Local | Pendência específica |
|---|---|---|
| PE5-01 | 5.1–5.2 / recorte | Confirmar a apresentação principal dos 78 casos, que inclui 21 rótulos de falso positivo e dois inconclusivos. O recorte dos 55 confirmados foi mostrado separadamente. Uma eventual restrição analítica exige ajustar definições, tabelas e metodologia explicitamente, preservando o que foi executado. |
| PE5-02 | 5.2 e 5.10 | Identificar responsáveis e procedimento da triagem e revisar a adequação dos critérios de D; a análise automatizada não comprova validação humana dessas classificações. |
| PE5-03 | 5.6 e continuidade com 3.10 | Revisar os exemplos e alinhar a declaração de análise qualitativa ao procedimento documental aqui registrado. A redação do capítulo 3 foi preservada e ainda contém pendência sobre inspeção qualitativa. |
| PE5-04 | Integração | Conferir apresentação e largura das tabelas no template, numeração global de 12 tabelas e da figura e formato das citações. |
| PE5-05 | 5.9 / referencial | Revisar a discussão bibliográfica e sua integração com o capítulo 2; nesta tarefa foram conferidos metadados e resumos de dois estudos, sem revisão bibliográfica integral. |
| PE5-06 | Revisão final | Revisar clareza das respostas Q1–Q5 e das interpretações, incluindo custos calculados versus faturamento e redução estática versus aprovação funcional conjunta. |

A declaração sobre uso de IA e a justificativa específica de escolha dos Luna
permanecem como pendências da metodologia; não foram preenchidas por inferência.
A investigação causal das falhas conjuntas e novas réplicas foram identificadas
como limites, não executadas para completar a redação.

## Conferências finais

- 40 unidades de conteúdo do plano, dez seções, 12 tabelas, um gráfico e dois excertos.
- 45 artefatos reconsolidados idênticos e denominadores recalculados.
- 834 registros reconciliados em 685 tentativas principais e 149 pós-aceites.
- 28 hashes dos exemplos conferidos; nenhum novo teste ou chamada de geração.
- Perguntas e objetivos conferidos com a introdução; sem novos testes estatísticos.
- Markdown completo e manuscritos anteriores preservados, exceto atualização do índice.
- Sem alteração dos resultados experimentais, commit ou push.

## Abertura dos parágrafos

- **C5-P01 / Abertura:** Este capítulo apresenta e discute os resultados das campanhas finais do pipeline no OWASP Juice Shop. A análise considera a geração de propo…
- **C5-P02 / Abertura:** Inicialmente, são caracterizados os casos e as campanhas. Em seguida, são apresentados os resultados gerais, as diferenças entre estratégias…
- **C5-P03 / 5.1 Caracterização das campanhas e dos casos:** Foram consideradas três campanhas reais concluídas em 6 de novembro de 2026, uma por modelo: GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna. Elas c…
- **C5-P04 / 5.1 Caracterização das campanhas e dos casos:** O catálogo reuniu 78 ocorrências elegíveis, obtidas a partir de 124 alertas, com 46 exclusões na preparação. Os casos foram distribuídos em …
- **C5-P05 / 5.1 Caracterização das campanhas e dos casos:** A classificação arquivada da triagem identificou 55 casos como confirmados, 21 como falsos positivos e dois como inconclusivos. Esses rótulo…
- **C5-P06 / 5.1 Caracterização das campanhas e dos casos:** Todos os casos receberam tentativas nas três campanhas. A Tabela 1 distingue os registros produzidos da população principal, delimitada pelo…
- **C5-P07 / 5.2 Resultados gerais do pipeline:** O pipeline produziu pelo menos uma tentativa aceita para parte dos casos em todos os modelos, conforme a Tabela 2. O GPT-5.6 Luna apresentou…
- **C5-P08 / 5.2 Resultados gerais do pipeline:** A avaliação dos critérios isolados mostrou que remover o alerta e preservar o funcionamento foram obstáculos diferentes. A TRI permaneceu pr…
- **C5-P09 / 5.2 Resultados gerais do pipeline:** Parte das propostas não chegou à avaliação completa. No GPT-4.1 mini, 17 tentativas não foram aplicadas; no GPT-5.6 Luna, foram sete; e, no …
- **C5-P10 / 5.2 Resultados gerais do pipeline:** Os resultados foram sensíveis ao tratamento dos testes associados à manutenção das vulnerabilidades. A Tabela 4 mostra que a definição por c…
- **C5-P11 / 5.3 Comparação das estratégias de prompt:** As estratégias foram comparadas dentro de cada modelo, preservando o número de casos que alcançou cada etapa. Como mostra a Tabela 5, P1 rec…
- **C5-P12 / 5.3 Comparação das estratégias de prompt:** As estratégias posteriores contribuíram com casos que não haviam recebido aceite nas etapas anteriores. Além dos aceites de P1, P2–P4 acresc…
- **C5-P13 / 5.3 Comparação das estratégias de prompt:** A interpretação do conteúdo dos prompts exige considerar o que mudou entre as condições. P2 acrescentou o roteiro de resposta, enquanto P3 a…
- **C5-P14 / 5.3 Comparação das estratégias de prompt:** A sequência introduziu uma seleção que limita conclusões sobre a melhor estratégia. Os casos resolvidos inicialmente deixaram de participar …
- **C5-P15 / 5.4 Comparação entre modelos de linguagem:** A comparação entre modelos indicou diferenças no desempenho observado sob as condições compartilhadas. O GPT-5.6 Luna alcançou 51 casos acei…
- **C5-P16 / 5.4 Comparação entre modelos de linguagem:** Os aceites apresentaram sobreposição, mas não foram idênticos. Conforme a Tabela 6, 32 casos foram aceitos pelos três modelos e 58 por pelo …
- **C5-P17 / 5.4 Comparação entre modelos de linguagem:** Os critérios intermediários ajudam a compreender essas diferenças. O GPT-5.6 Luna apresentou a maior proporção de propostas aplicadas, com 2…
- **C5-P18 / 5.4 Comparação entre modelos de linguagem:** O menor custo registrado foi o do GPT-6 Luna, que também apresentou o menor quociente entre custo da campanha e casos aceitos, conforme a Ta…
- **C5-P19 / 5.4 Comparação entre modelos de linguagem:** Os tempos mostraram outra dimensão da comparação. O GPT-4.1 mini apresentou a menor latência média de geração, enquanto a sessão do GPT-6 Lu…
- **C5-P20 / 5.5 Resultados por tipo de vulnerabilidade e categoria:** A distribuição dos aceites variou entre os tipos de alerta catalogados, como mostra a Tabela 9. Os três modelos tiveram oito aceites entre o…
- **C5-P21 / 5.5 Resultados por tipo de vulnerabilidade e categoria:** O agrupamento por regra refinou essa descrição. Na regra relacionada ao uso de HTML tratado como confiável no Angular, os três modelos obtiv…
- **C5-P22 / 5.5 Resultados por tipo de vulnerabilidade e categoria:** A comparação por OWASP foi limitada pela disponibilidade do mapeamento. A Tabela 10 conserva os códigos registrados no catálogo e mantém os …
- **C5-P23 / 5.6 Análise de correções e falhas representativas:** Foram selecionados dois casos para examinar quatro tentativas com resultados contrastantes. A seleção considerou a disponibilidade dos artef…
- **C5-P24 / 5.6 Análise de correções e falhas representativas:** O primeiro caso foi a consulta de acompanhamento de pedidos apresentada no Capítulo 4. Na tentativa P1 do GPT-4.1 mini, o patch substituiu a…
- **C5-P25 / 5.6 Análise de correções e falhas representativas:** No segundo caso, o alerta incidiu sobre eval no cálculo do CAPTCHA. A tentativa P1 do GPT-4.1 mini substituiu a avaliação dinâmica por opera…
- **C5-P26 / 5.6 Análise de correções e falhas representativas:** Para o mesmo alerta do CAPTCHA, a tentativa P1 do GPT-6 Luna também foi rejeitada pelos testes, mas P2 produziu uma proposta que tratou a pr…
- **C5-P27 / 5.7 Redução conjunta de alertas e RRIS:** A avaliação conjunta partiu dos primeiros aceites por caso e tentou integrar os patches em uma cópia limpa do projeto. Parte deles não pôde …
- **C5-P28 / 5.7 Redução conjunta de alertas e RRIS:** Os scans globais registraram 78 alertas antes da aplicação conjunta. Após a integração possível, os totais foram 40, 23 e 31, respectivament…
- **C5-P29 / 5.7 Redução conjunta de alertas e RRIS:** Nenhum dos três conjuntos integrados recebeu aprovação funcional, inclusive na definição por critérios. Entre as falhas documentadas, os trê…
- **C5-P30 / 5.8 Respostas às perguntas de pesquisa:** Em relação à Q1, foi possível produzir tentativas aceitas pelo pipeline segundo a definição operacional adotada: houve pelo menos um aceite …
- **C5-P31 / 5.8 Respostas às perguntas de pesquisa:** Para a Q2, as estratégias contribuíram de forma diferente ao longo da sequência: P1 produziu aceites iniciais e P2–P4 acrescentaram outros c…
- **C5-P32 / 5.8 Respostas às perguntas de pesquisa:** Quanto à Q3, o desempenho variou descritivamente conforme os tipos e as regras, como nos contrastes entre XSS, IDOR e travessia de diretório…
- **C5-P33 / 5.8 Respostas às perguntas de pesquisa:** Para a Q4, foram identificadas limitações práticas na aplicação das edições, na avaliação funcional e na integração das propostas. Referênci…
- **C5-P34 / 5.8 Respostas às perguntas de pesquisa:** Em resposta à Q5, o GPT-5.6 Luna apresentou o maior número de casos aceitos e a maior TRV, enquanto o GPT-6 Luna teve o menor custo registra…
- **C5-P35 / 5.9 Discussão com a literatura e implicações:** Os achados dialogam com a discussão do referencial sobre contexto e validação externa. Khan, Liu e Gao (2025) investigaram reparo de estouro…
- **C5-P36 / 5.9 Discussão com a literatura e implicações:** Neste experimento, a combinação de SAST e testes permitiu distinguir situações que uma única verificação não separaria. O exemplo do CAPTCHA…
- **C5-P37 / 5.9 Discussão com a literatura e implicações:** Como implicação prática, os modelos puderam apoiar a elaboração de propostas, mas os resultados não sustentaram sua adoção automática como v…
- **C5-P38 / 5.10 Ameaças à validade e síntese do capítulo:** A validade das medidas depende do alcance das regras e dos testes e da qualidade das classificações utilizadas. A remoção do alerta não prov…
- **C5-P39 / 5.10 Ameaças à validade e síntese do capítulo:** A generalização foi limitada a uma aplicação deliberadamente vulnerável, uma revisão do alvo e uma campanha final por modelo. O Juice Shop p…
- **C5-P40 / 5.10 Ameaças à validade e síntese do capítulo:** Os resultados indicaram que o pipeline produziu aceites individuais e reduções estáticas conjuntas, com diferenças entre modelos, estratégia…

## Hashes do texto e da referência preservada

SHA-256 do rascunho: `cc8157059fd03847ad1e04f1558c3e097ed440ff4df02c298e1da66038f21f40`.

SHA-256 de 05-consideracoes-finais.md: `111811c5fc9c2ac67a13beaa2d95eeb24e2c7bef39bcc3d3498281d284652a9e`.

