# Capítulo 5 — plano por parágrafo

**Título proposto:** Resultados e discussão.

**Estado:** proposta de organização e roteiro para desenvolver com os autores.
Segue as decisões de apresentar resultados, interpretá-los e responder Q1–Q5,
com comparação explícita dos três modelos. Quantidade de parágrafos e títulos
podem ser ajustados na revisão. Este documento não é o capítulo redigido nem
uma aprovação acadêmica ou revisão integral dos resultados.

## Diretrizes de conteúdo

- Capítulo 3 define o método; capítulo 4 explica a implementação; capítulo 5
  apresenta o observado, desenvolve a interpretação e responde às perguntas.
- Preservar Q1–Q4 e responder à Q5 acrescentada sobre eficácia, custo e tempo.
- Apresentar resultados gerais e depois examinar estratégias, modelos e tipos de casos.
- Dar espaço à sensibilidade de F, aos resultados qualitativos e à RRIS conjunta.
- Distinguir caso aceito, tentativa aceita, remoção de alerta e vulnerabilidade
  demonstradamente corrigida. Não tratar os 78 casos como falhas reais comprovadas.
- Usar n/d, população, definição de F e política em tabelas e gráficos de taxas.
- Distinguir análise planejada, cálculo disponível e análise efetivamente realizada.
- Explicar dificuldades à luz dos registros, sem refazer a descrição técnica do capítulo 4.
- Manter a explicação de Docker e replicação breve, conforme preferência do autor.

## Base e limites da consulta

Experimento irmão `../../tcc2-llm-sast-juiceshop`, revisão
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas na consulta.
Campanhas de 06/11/2026 com métricas incluindo RRIS em `outputs/rris/`.
Foram lidos consolidados e código selecionado para planejar; não houve novas
chamadas LLM, campanhas, testes do alvo, análise estatística ou inspeção integral
 dos patches nesta tarefa.

O arquivo [05-consideracoes-finais.md](../manuscrito/05-consideracoes-finais.md)
ainda contém as considerações finais do TCC1 e permanece preservado. A redação
deste novo capítulo e a reorganização da conclusão serão tarefas posteriores.

Planos relacionados: [capítulo 3](plano-paragrafos-capitulo-3.md),
[capítulo 4](plano-paragrafos-capitulo-4.md) e
[diretrizes gerais](diretrizes-escrita.md).

## Linguagem e profundidade adotadas

Seguir os [critérios de escrita](criterios-escrita.md), definidos pelo autor:
linguagem acadêmica, objetiva e explicativa, próxima à do TCC1. Desenvolver uma
ideia central por parágrafo, explicar termos na primeira ocorrência e conectar
cada explicação à finalidade do estudo. As fontes e os detalhes internos deste
plano servem à conferência do redator; não precisam ser transcritos no texto.

Apresentar o resultado e explicar seu significado. Usar tabelas e gráficos
selecionados, comentando apenas os valores que sustentam a interpretação.
Manter os denominadores e as limitações claros, evitando repetir ressalvas
ou aprofundar métodos estatísticos que não façam parte da análise realizada.

## Roteiro dos parágrafos

### Abertura do capítulo

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P01 | Apresentar a finalidade do capítulo: expor os resultados, interpretá-los e responder às perguntas de pesquisa. |
| C5-P02 | Apresentar a ordem da discussão, dos resultados gerais às comparações, aos exemplos e às respostas Q1–Q5. |

**Fontes/condição para redação:** Visão geral e referências aos capítulos 3 e 4.

### 5.1 Caracterização das campanhas e dos casos

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P03 | Identificar as três campanhas finais, seus modelos e condições comuns, separando-as dos pilotos e de outras execuções. |
| C5-P04 | Apresentar os 78 casos e sua distribuição por tipo e categoria, explicando informações ausentes quando relevantes. |
| C5-P05 | Apresentar as classificações registradas na triagem e seus limites, sem tratá-las como validação humana já comprovada. |
| C5-P06 | Explicar quantos casos e tentativas foram analisados por modelo e qual definição de F orienta os resultados principais. |

**Apresentação sugerida:** Tabela de identificação das campanhas e tabela de composição dos casos.

**Fontes/condição para redação:** Contratos, catálogo, metricas.json, tentativas.csv e casos.csv de cada campanha.

### 5.2 Resultados gerais do pipeline

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P07 | Apresentar a proporção de casos aceitos e a TRV por tentativa, explicando com clareza a diferença entre essas medidas. |
| C5-P08 | Apresentar a remoção de alertas, a preservação do funcionamento e a ausência de novos alertas, com os totais considerados. |
| C5-P09 | Explicar as tentativas que não puderam ser aplicadas ou avaliadas e como elas afetam a interpretação dos resultados. |
| C5-P10 | Mostrar como os resultados mudam conforme o tratamento dos testes ligados às vulnerabilidades, usando uma tabela resumida. |

**Apresentação sugerida:** Tabela geral por modelo e tabela compacta das definições de F. Acrescentar gráfico somente se facilitar a comparação.

**Fontes/condição para redação:** metricas_gerais.csv, metricas_por_caso e populacoes de metricas.json; registros de aplicação e testes.

### 5.3 Comparação das estratégias de prompt

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P11 | Apresentar os resultados de P1–P4 por modelo, informando quantos casos chegaram a cada estratégia. |
| C5-P12 | Explicar a contribuição das estratégias posteriores para os casos ainda não aceitos, sem contar repetidamente o mesmo caso. |
| C5-P13 | Discutir as diferenças observadas entre instrução direta, roteiro e contexto, lembrando que diagnóstico e documentos foram acrescentados juntos. |
| C5-P14 | Explicar que as estratégias recebem casos diferentes ao longo da sequência, o que limita conclusões sobre qual é melhor. |

**Apresentação sugerida:** Tabela por estratégia e modelo, com tamanho de cada população; gráfico de aceites incrementais por etapa, se os dados sustentarem.

**Fontes/condição para redação:** metricas_por_estrategia.csv, tentativas.csv e casos.csv; script comparar_modelos.py como ferramenta disponível, não prova de análise já realizada.

### 5.4 Comparação entre modelos de linguagem

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P15 | Comparar os três modelos pelos casos aceitos e pela TRV, mantendo explícitas as condições e os totais da comparação. |
| C5-P16 | Mostrar quais casos foram aceitos por vários modelos e quais foram aceitos apenas por um deles. |
| C5-P17 | Examinar em quais critérios os modelos diferiram: aplicação da alteração, remoção do alerta, testes e novos alertas. |
| C5-P18 | Comparar custos e consumo registrado, incluindo custo por caso aceito quando possível, explicando o que não foi contabilizado. |
| C5-P19 | Comparar o tempo de resposta e a duração das campanhas e discutir sua relação com custo e eficácia, sem atribuir todo o tempo ao modelo. |

**Apresentação sugerida:** Tabela comparativa de eficácia, custo e tempo. Mostrar casos em comum por tabela ou figura simples, se a análise acrescentar informação relevante.

**Fontes/condição para redação:** Contratos, casos.csv, tentativas.csv, custos_tempos e operacional_llm; comparar_modelos.py pode apoiar análises adicionais.

### 5.5 Resultados por tipo de vulnerabilidade e categoria

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P20 | Apresentar os resultados por tipo de vulnerabilidade e regra, informando o tamanho de cada grupo. |
| C5-P21 | Discutir dificuldades recorrentes por grupo e diferenças entre modelos, apenas quando houver observações suficientes. |
| C5-P22 | Apresentar a distribuição e os resultados por OWASP, explicando casos sem categoria e mantendo os critérios de contagem. |

**Apresentação sugerida:** Tabela com contagens e taxas por grupo; agrupar a discussão para evitar uma tabela extensa para cada CWE.

**Fontes/condição para redação:** metricas_por_cwe.csv, metricas_por_regra.csv, metricas_por_owasp.csv, metricas_por_auditoria.csv e catálogo.

### 5.6 Análise de correções e falhas representativas

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P23 | Explicar a escolha dos exemplos de sucesso e falha, evitando selecionar apenas resultados favoráveis. |
| C5-P24 | Analisar uma correção aceita: problema, alteração e evidências de avaliação, reconhecendo o alcance da verificação realizada. |
| C5-P25 | Analisar uma tentativa rejeitada ou inconclusiva e explicar a causa documentada, sem transformar suspeitas em conclusões. |
| C5-P26 | Comparar propostas para um mesmo caso e discutir o papel do contexto e dos testes, quando a inspeção tiver sido realizada. |

**Apresentação sugerida:** Dois ou três exemplos com diff reduzido e tabela de evidências; usar o exemplo do capítulo 4 somente se acrescentar análise dos resultados.

**Fontes/condição para redação:** Prompts, respostas_llm, patches, sast_depois, comparacoes e testes dos IDs de tentativa escolhidos; seleção e inspeção ainda pendentes.

### 5.7 Redução conjunta de alertas e RRIS

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P27 | Apresentar quais correções foram aplicadas em conjunto e quais não puderam ser integradas. |
| C5-P28 | Apresentar a quantidade de alertas antes e depois e a RRIS de cada modelo, com uma tabela comparativa. |
| C5-P29 | Explicar a situação dos testes do conjunto e por que reduzir alertas não garante, por si só, preservar o funcionamento. |

**Apresentação sugerida:** Tabela com patches selecionados/aplicados, contagens de alertas, RRIS e situação funcional conjunta.

**Fontes/condição para redação:** outputs/rris, metricas.json com RRIS e artefatos da avaliação conjunta; não somar R ou aceites isolados.

### 5.8 Respostas às perguntas de pesquisa

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P30 | Responder Q1 com os resultados do pipeline e os limites do significado de correção válida adotado no estudo. |
| C5-P31 | Responder Q2 com o que foi observado sobre as estratégias e os limites da comparação sequencial e do efeito isolado do RAG. |
| C5-P32 | Responder Q3 com as diferenças por tipo e categoria que os dados permitem sustentar. |
| C5-P33 | Responder Q4 com as dificuldades práticas documentadas e seus efeitos no experimento. |
| C5-P34 | Responder Q5 comparando eficácia, custo e tempo dos modelos nas condições avaliadas. |

**Apresentação sugerida:** Uma resposta sintética por pergunta, citando as seções anteriores; tabela pergunta → achado → evidência → limite pode apoiar a leitura.

**Fontes/condição para redação:** Introdução com Q1–Q5 e análises verificadas das seções 5.1–5.7.

### 5.9 Discussão com a literatura e implicações

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P35 | Relacionar os achados aos trabalhos do referencial, explicando semelhanças e diferenças de avaliação antes de comparar números. |
| C5-P36 | Discutir o que a combinação de SAST e testes permitiu observar, apoiando a explicação nos resultados e exemplos apresentados. |
| C5-P37 | Explicar as implicações práticas dos achados para o uso de modelos no apoio à correção, reconhecendo a necessidade de revisão. |

**Apresentação sugerida:** Selecionar poucos estudos diretamente pertinentes; não acrescentar afirmações bibliográficas sem verificação nem repetir todo o referencial.

**Fontes/condição para redação:** Referências do capítulo 2 a conferir e evidências interpretadas nas seções anteriores.

### 5.10 Ameaças à validade e síntese do capítulo

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C5-P38 | Apresentar os limites da medição: detector, testes, classificação dos alertas, sequência de estratégias e seleção dos exemplos. |
| C5-P39 | Explicar os limites de generalização de um alvo e uma campanha por modelo, incluindo diferenças de configuração e de ambiente. |
| C5-P40 | Sintetizar os achados e suas limitações e preparar a conclusão geral. Tratar a possibilidade de replicação apenas brevemente. |

**Fontes/condição para redação:** Protocolo, contratos e limites efetivamente identificados nas análises. A síntese não substitui o capítulo de conclusão.

## Números de referência já localizados

Consulta direta aos consolidados, população `real_desenho`, F=`criterio`.
Os valores abaixo orientam a redação e devem ser acompanhados de sua proveniência.
A tabela não constitui por si só uma conclusão sobre superioridade dos modelos.

| Modelo | Tentativas na população | Aceites por caso | TRV por tentativa | Custo conhecido (US$) | RRIS | Conjunto funcionalmente validado |
|---|---:|---:|---:|---:|---:|---|
| GPT-4.1 mini | 241 | 38/78 (48.72%) | 38/241 (15.77%) | 0.433169 | 78 → 40 (48.72%) | Não |
| GPT-5.6 Luna | 223 | 51/78 (65.38%) | 51/223 (22.87%) | 0.314826 | 78 → 23 (70.51%) | Não |
| GPT-6 Luna | 221 | 49/78 (62.82%) | 49/221 (22.17%) | 0.138800 | 78 → 31 (60.26%) | Não |

O custo é o total conhecido registrado pelo consolidado, não o custo integral
de infraestrutura. RRIS é redução estática conjunta e não deve ser confundida
com aceite por caso ou preservação funcional dos patches integrados.

**Fontes por modelo:**
- GPT-4.1 mini: `outputs/campanha_docker/AMP_REAL_20261106T151004Z_f49ac0d2/contrato_execucao.json` e `outputs/rris/AMP_REAL_20261106T151004Z_f49ac0d2_METRICAS/`.
- GPT-5.6 Luna: `outputs/campanha_docker/AMP_REAL_20261106T125801Z_0eb68fe4/contrato_execucao.json` e `outputs/rris/AMP_REAL_20261106T125801Z_0eb68fe4_METRICAS/`.
- GPT-6 Luna: `outputs/campanha_docker/AMP_REAL_20261106T105533Z_aa697342/contrato_execucao.json` e `outputs/rris/AMP_REAL_20261106T105533Z_aa697342_METRICAS/`.

## Análises e materiais ainda a preparar

1. Conferir proveniência e integridade dos artefatos usados no capítulo e reconciliar população principal, registros totais e pós-aceites.
2. Produzir tabelas e gráficos a partir dos arquivos citados, conservando fontes, definições e denominadores; figuras não são resultados novos de geração.
3. Derivar a sobreposição dos casos aceitos entre modelos e, se desejado, comparações pareadas, documentando a população. A existência de comparar_modelos.py não prova execução ou validade de um teste estatístico.
4. Selecionar e inspecionar exemplos qualitativos com registro de autoria, método e limites; não afirmar inspeção humana que ainda não tenha ocorrido.
5. Examinar o conjunto de patches e falhas funcionais da RRIS antes de explicar suas causas.
6. Verificar a literatura realmente usada na discussão, sem comparar taxas de desenhos ou denominadores incompatíveis.
7. Alinhar eventuais análises adicionais com o método do capítulo 3. Não introduzir testes estatísticos nem novas condições experimentais como se fossem decisões prévias.
8. Conferir na introdução a formulação final de Q1–Q5 e o objetivo de comparar modelos.

## Orientação de redação

Cada seção deve apresentar a evidência e desenvolver sua interpretação, com
limites proporcionais ao que foi medido. Evitar repetir todos os valores em
prosa: selecionar os que sustentam o argumento e deixar os demais nas tabelas.
Gráficos devem identificar modelo, unidade, população e definição de F e
distinguir medições indisponíveis de zero. Não generalizar uma campanha por
modelo no Juice Shop para desempenho universal. IDs C5-Pxx servem apenas ao plano.
