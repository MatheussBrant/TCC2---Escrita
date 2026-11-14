## 5 Resultados e discussão

Este capítulo apresenta e discute os resultados das campanhas finais do pipeline no OWASP Juice Shop. A análise considera a geração de propostas, sua aplicação e a avaliação dos critérios de remoção do alerta, preservação funcional e ausência de novos alertas. A expressão correção válida corresponde ao aceite definido nas Seções 3.10 e 3.11: uma proposta aplicada ao código com R=F=M=1, segundo a interpretação principal de F. Esse aceite se refere às verificações realizadas sobre a alteração, sem demonstrar a segurança de toda a aplicação.

Inicialmente, são caracterizados os casos e as campanhas. Em seguida, são apresentados os resultados gerais, as diferenças entre estratégias e modelos e os recortes por tipo de alerta. A discussão é complementada por exemplos reais, pela avaliação conjunta dos patches e pelas respostas às perguntas de pesquisa. Os limites das evidências são considerados ao longo da interpretação.

### 5.1 Caracterização das campanhas e dos casos

Foram consideradas três campanhas reais concluídas em 6 de novembro de 2026, uma por modelo: GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna. Elas compartilharam a revisão do Juice Shop, o catálogo, o perfil SAST, a base de contexto, o baseline e a política de validação descritos anteriormente. Todas utilizaram quatro worktrees e a sequência P1–P4. Pilotos, simulações e diagnósticos adicionais não foram reunidos com esses resultados. Os contratos e os registros de sessão permitiram conferir essas condições e a conclusão das execuções.

O catálogo reuniu 78 ocorrências elegíveis a partir de 124 alertas. Foram excluídos 31 alertas em exemplos dos Coding Challenges, 13 em arquivos de automação do GitHub e dois em configurações do npm, totalizando 46 exclusões. Conforme a Seção 3.5, os exemplos continham alternativas de correção dos exercícios pedagógicos, enquanto os arquivos de automação e configuração tratavam de aspectos não avaliados pelos testes da aplicação. O recorte concentrou a avaliação no código das funcionalidades do Juice Shop.

Na classificação OWASP Top 10:2025 utilizada na análise final, os 78 casos foram distribuídos em sete categorias: A01, com 26 casos; A05, com 22; A06, com 12; A07, com sete; A04, com cinco; e A02 e A08, com três cada. Essa classificação preservou as 29 associações originais e complementou os 49 casos sem categoria após as campanhas, sem alterar as tentativas ou seus resultados. A Seção 5.5 apresenta os aceites por categoria OWASP e, separadamente, pelos tipos de alerta do catálogo.

A classificação arquivada da triagem identificou 55 casos como confirmados, 21 como falsos positivos e dois como inconclusivos. Os 21 falsos positivos foram revisados e confirmados pelos dois autores, mediante exame do código, do contexto dos alertas e das regras do Semgrep. As classificações dos 55 casos confirmados e dos dois inconclusivos foram mantidas conforme os registros de triagem e suas justificativas, cuja origem e consolidação são descritas na Seção 3.5. As campanhas abrangeram os três grupos, totalizando 78 casos. Os resultados gerais descrevem, assim, o processamento desse catálogo de alertas. Para examinar também o desempenho no grupo classificado como confirmado na triagem, a Seção 5.2 apresenta seus aceites separadamente, com denominador de 55 casos.

Todos os casos receberam tentativas nas três campanhas. A Tabela 1 distingue o total de registros produzidos das tentativas incluídas na análise principal. Conforme a Seção 3.9, a execução avançava para a estratégia seguinte quando havia uma nova falha persistente em qualquer teste, inclusive naqueles que dependiam da manutenção de uma vulnerabilidade intencional. Na análise principal, as falhas desses testes, reunidos no conjunto D, não reprovaram F por si só. Por exemplo, uma proposta que impedisse um ataque poderia fazer falhar o teste que esperava sua exploração e levar o pipeline a tentar outra estratégia, embora já atendesse aos critérios de aceite da análise principal.

Por essa razão, a população principal incluiu as tentativas até o primeiro aceite por critérios de cada caso ou até P4, quando não houve aceite. As tentativas executadas depois desse primeiro aceite foram identificadas como pós-aceite e ficaram separadas no cálculo das taxas principais. Todos esses registros foram preservados; a separação apenas delimitou quais tentativas entraram em cada análise.

**Tabela 1 — Registros das campanhas finais e população de análise**

| Modelo | Registros totais | População principal | Pós-aceite |
|---|---|---|---|
| GPT-4.1 mini | 283 | 241 | 42 |
| GPT-5.6 Luna | 277 | 223 | 54 |
| GPT-6 Luna | 274 | 221 | 53 |

Fonte: registros e consolidados das campanhas de 06/11/2026. Todos os 78 casos receberam tentativas em cada campanha; a população principal usa o primeiro aceite registrado por caso, com F por critérios.


### 5.2 Resultados gerais do pipeline

O pipeline produziu pelo menos uma tentativa aceita para parte dos casos em todos os modelos, conforme a Tabela 2. O GPT-5.6 Luna apresentou o maior número de casos aceitos, seguido pelo GPT-6 Luna e pelo GPT-4.1 mini. Essa proporção difere da TRV por tentativa, pois um caso pode demandar várias propostas antes de obter aceite. No recorte separado dos casos rotulados como confirmados, o GPT-4.1 mini obteve 32/55 aceites (58,18%), o GPT-5.6 Luna 39/55 (70,91%) e o GPT-6 Luna 36/55 (65,45%). A ordem dos modelos nesse grupo foi a mesma observada no catálogo completo; o termo confirmado mantém o significado da triagem descrita na Seção 3.5.

**Tabela 2 — Aceites por caso e por tentativa**

| Modelo | Casos aceitos / solicitados | TRV por tentativa |
|---|---|---|
| GPT-4.1 mini | 38/78 (48,72%) | 38/241 (15,77%) |
| GPT-5.6 Luna | 51/78 (65,38%) | 51/223 (22,87%) |
| GPT-6 Luna | 49/78 (62,82%) | 49/221 (22,17%) |

Fonte: consolidados conferidos, população principal de tentativas reais do desenho, F por critérios. A TRV inclui tentativas não aplicadas e medições indeterminadas no denominador.


A avaliação dos critérios isolados mostrou que remover o alerta e preservar o funcionamento foram obstáculos diferentes. A TRI permaneceu próxima entre os modelos, enquanto a TPF variou mais, conforme a Tabela 3. A ausência de novos alertas foi observada na maior parte das tentativas com M medido, mas esse resultado se limita ao alcance do perfil SAST. Houve sete, quatro e cinco tentativas com M=0, respectivamente. Assim, o aceite não poderia ser deduzido apenas do desaparecimento do alerta original.

**Tabela 3 — Critérios de avaliação e medições ausentes**

| Modelo | TRI | TPF | TFF | TNINI | Ausentes R/M; F |
|---|---|---|---|---|---|
| GPT-4.1 mini | 85/221 (38,46%) | 145/218 (66,51%) | 73/218 (33,49%) | 214/221 (96,83%) | 20; 23 |
| GPT-5.6 Luna | 82/216 (37,96%) | 154/212 (72,64%) | 58/212 (27,36%) | 212/216 (98,15%) | 7; 11 |
| GPT-6 Luna | 77/203 (37,93%) | 154/199 (77,39%) | 45/199 (22,61%) | 198/203 (97,54%) | 18; 22 |

Fonte: população principal, F por critérios. TRI, TPF, TFF e TNINI consideram somente as medições disponíveis para cada critério. As ausências podem se sobrepor e não representam falhas medidas.


Parte das propostas não chegou à avaliação completa. No GPT-4.1 mini, 17 tentativas não foram aplicadas; no GPT-5.6 Luna, foram sete; e, no GPT-6 Luna, 16. Entre os motivos documentados estiveram ausência de edições, trechos de referência não encontrados, correspondências ambíguas e resposta inválida. Após a aplicação, também houve avaliações estáticas indeterminadas: três, zero e duas, respectivamente. As ausências de R, F ou M foram mantidas como tal, sem convertê-las em falhas observadas. Nas métricas complementares, cada tentativa entra no denominador apenas quando o critério correspondente foi medido. Na TRV, todas as tentativas da população principal entram no denominador, inclusive as não aplicadas ou com resultados indeterminados; somente as aplicadas com R=F=M=1 entram no numerador, conforme a Seção 3.11.

Os resultados variaram conforme o tratamento dos testes que dependiam das vulnerabilidades intencionais. Como definido na Seção 3.10, a interpretação por critérios considera o conteúdo das asserções para identificar os testes do conjunto D, incluindo os que exigem uma resposta insegura ou o mecanismo apontado pelo alerta. Suas falhas não reprovam F por si só; falhas novas persistentes nos testes de comportamento legítimo continuam reprovando. A alternativa por marcador faz essa separação apenas nos testes que afirmam explicitamente a resolução de um desafio, enquanto a interpretação sem separação considera também essas falhas na reprovação funcional.

A Tabela 4 compara as três interpretações sobre as mesmas tentativas da população principal. As alternativas sem separação e por marcador produziram o mesmo total de aceites em cada modelo. Com a interpretação por critérios, os totais aumentaram para 38, 51 e 49. No GPT-6 Luna, por exemplo, a TRV passou de 23/221 (10,41%) para 49/221 (22,17%). A diferença mostra o efeito de distinguir falhas nos testes dependentes da vulnerabilidade de regressões no comportamento legítimo, mantendo as exigências de remoção do alerta e ausência de novos alertas.

**Tabela 4 — Sensibilidade da TRV à definição de F**

| Modelo | F sem separação | F por marcador | F por critérios (principal) |
|---|---|---|---|
| GPT-4.1 mini | 17/241 (7,05%) | 17/241 (7,05%) | 38/241 (15,77%) |
| GPT-5.6 Luna | 22/223 (9,87%) | 22/223 (9,87%) | 51/223 (22,87%) |
| GPT-6 Luna | 23/221 (10,41%) | 23/221 (10,41%) | 49/221 (22,17%) |

Fonte: registros das campanhas finais; tentativas aceitas/total de tentativas da população principal (%). Para cada modelo, o denominador e as tentativas são os mesmos nas três colunas; varia somente a interpretação de F. Trata-se da reavaliação dos registros existentes, sem simular quais estratégias seriam executadas sob outra regra de parada.


### 5.3 Comparação das estratégias de prompt

As estratégias foram comparadas dentro de cada modelo, preservando o número de casos que alcançou cada etapa. Como mostra a Tabela 5, P1 recebeu os 78 casos, enquanto P2–P4 tiveram denominadores progressivamente menores na população principal. A proporção de aceites em P3 foi superior à de P2 nos três modelos e, no GPT-5.6 Luna, correspondeu a 25 dos 55 casos que chegaram a essa estratégia. Esse resultado descreve a contribuição observada da etapa, sem constituir uma comparação entre amostras equivalentes.

**Tabela 5 — Primeiros aceites e tentativas por estratégia**

| Modelo | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| GPT-4.1 mini | 16/78 (20,51%) | 4/62 (6,45%) | 15/58 (25,86%) | 3/43 (6,98%) |
| GPT-5.6 Luna | 18/78 (23,08%) | 5/60 (8,33%) | 25/55 (45,45%) | 3/30 (10,00%) |
| GPT-6 Luna | 21/78 (26,92%) | 5/57 (8,77%) | 18/52 (34,62%) | 5/34 (14,71%) |

Fonte: população principal, F por critérios. Cada célula informa aceites/tentativas da estratégia (%); os denominadores de P2–P4 correspondem aos casos que chegaram à etapa na cadeia delimitada pelo primeiro aceite principal.


As estratégias posteriores contribuíram com casos que não haviam recebido aceite nas etapas anteriores. Além dos aceites de P1, P2–P4 acrescentaram 22 casos no GPT-4.1 mini, 33 no GPT-5.6 Luna e 28 no GPT-6 Luna. A Figura 1 permite visualizar essa composição sem contar o mesmo caso mais de uma vez. Ela também evidencia que permaneceram casos sem aceite após o percurso completo, de modo que ampliar a sequência não eliminou todas as dificuldades de correção.

![Primeiro aceite por estratégia para os 78 casos de cada modelo](assets/capitulo-5/aceites-por-estrategia.png)

**Figura 1 — Distribuição dos casos pelo primeiro aceite e pela ausência de aceite.** Cada barra representa os 78 casos solicitados, com F por critérios. Os segmentos mostram quantos tiveram o primeiro aceite em cada estratégia; os casos sem aceite completam o total.

Fonte: elaboração a partir dos registros conferidos. Dados e script de geração preservados nas notas de evidência.

A interpretação do conteúdo dos prompts exige considerar o que mudou entre as condições. P2 acrescentou o roteiro de resposta, enquanto P3 acrescentou o diagnóstico SAST e a documentação recuperada; P4 reuniu esses componentes. Os registros mostram que as etapas com contexto produziram aceites adicionais, mas não permitem atribuir esse ganho exclusivamente ao RAG.

A sequência P1–P4 ampliou o número de casos aceitos nos três modelos, com destaque para a contribuição de P3 entre os casos remanescentes. Como cada etapa posterior recebeu os casos ainda sem aceite na análise principal, suas taxas expressam a capacidade de obter aceites adicionais ao longo desse percurso. A comparação entre as etapas deve considerar esses denominadores: avaliar cada estratégia isoladamente sobre os mesmos 78 casos exigiria outro desenho experimental.

### 5.4 Comparação entre modelos de linguagem

A comparação entre modelos indicou diferenças no desempenho observado sob as condições compartilhadas. O GPT-5.6 Luna alcançou 51 casos aceitos e TRV de 22,87%, enquanto o GPT-6 Luna alcançou 49 e TRV de 22,17%. O GPT-4.1 mini apresentou 38 casos e TRV de 15,77%. A proximidade dos dois Luna deve ser interpretada junto dos demais critérios, pois a diferença foi de dois casos em uma campanha por modelo. Não foi estabelecida significância estatística nem superioridade geral a partir desses totais.

Os aceites apresentaram sobreposição, mas não foram idênticos. Conforme a Tabela 6, 32 casos foram aceitos pelos três modelos e 58 por pelo menos um; em 20, nenhum obteve aceite. O GPT-6 Luna apresentou cinco aceites exclusivos, o GPT-5.6 Luna quatro e o GPT-4.1 mini um. Assim, maior número total de aceites não significou incluir todos os casos resolvidos pelos demais. A união de 58 casos descreve a diversidade das respostas, sem demonstrar que suas correções poderiam ser integradas ou que a seleção combinada teria o mesmo custo.

**Tabela 6 — Sobreposição dos casos aceitos**

| Conjunto exclusivo de modelos | Casos |
|---|---|
| Três modelos | 32 |
| GPT-4.1 mini e GPT-5.6 Luna | 4 |
| GPT-4.1 mini e GPT-6 Luna | 1 |
| GPT-5.6 Luna e GPT-6 Luna | 11 |
| Somente GPT-4.1 mini | 1 |
| Somente GPT-5.6 Luna | 4 |
| Somente GPT-6 Luna | 5 |
| Nenhum modelo | 20 |

Fonte: derivação dos identificadores de casos aceitos, F por critérios. As linhas são mutuamente exclusivas e somam os mesmos 78 casos; não representam aplicação conjunta de patches.


Os critérios intermediários ajudam a compreender essas diferenças. O GPT-5.6 Luna apresentou a maior proporção de propostas aplicadas, com 216/223 (96,86%), enquanto o GPT-4.1 mini teve 224/241 (92,95%) e o GPT-6 Luna 205/221 (92,76%). A TRI ficou entre 37,93% e 38,46%, mas a TPF por critérios foi maior no GPT-6 Luna. Portanto, diferenças de aceite envolveram a combinação entre aplicabilidade, remoção, funcionamento e novos alertas, e não apenas a capacidade de fazer desaparecer o padrão detectado. As populações distintas e as medições ausentes impedem interpretar esses critérios como um experimento isolado sobre cada capacidade.

O menor custo registrado foi o do GPT-6 Luna, que também apresentou o menor quociente entre custo da campanha e casos aceitos, conforme a Tabela 7. Esses valores consideram todas as chamadas registradas, incluindo as posteriores ao aceite principal; os custos restritos à população principal ficaram separados nos arquivos de apoio. O cálculo utilizou tokens e tarifas configuradas, inclusive os campos de cache informados pelo provedor, distintos da reutilização local de respostas. Não houve contabilização integral de infraestrutura nem conferência com faturamento externo. A comparação econômica, portanto, refere-se ao custo calculado e registrado pelo pipeline.

**Tabela 7 — Consumo e custos registrados das campanhas**

| Modelo | Tokens de entrada | Tokens de saída | Custo total (US$) | Custo total / caso aceito (US$) |
|---|---|---|---|---|
| GPT-4.1 mini | 587207 | 155015 | 0,433169 | 0,011399 |
| GPT-5.6 Luna | 574447 | 156186 | 0,314826 | 0,006173 |
| GPT-6 Luna | 563266 | 153481 | 0,138800 | 0,002833 |

Fonte: todas as respostas registradas de cada campanha, incluindo pós-aceite; custos calculados pelo pipeline com as tarifas configuradas. O último indicador divide o custo total pelos 38, 51 e 49 casos aceitos, respectivamente; não inclui infraestrutura nem representa conferência de faturamento.


Os tempos mostraram outra dimensão da comparação. O GPT-4.1 mini apresentou a menor latência média de geração, enquanto a sessão do GPT-6 Luna teve a menor duração total, conforme a Tabela 8. Essa diferença é compatível com o fato de a campanha incluir aplicação, análise estática e testes, além da geração. A quantidade de tentativas e a coordenação de recursos compartilhados também precisam ser consideradas na interpretação. Como houve processamento concorrente, a soma das latências ou das durações individuais não equivale à duração da sessão. Os tempos observados não devem ser atribuídos integralmente ao modelo.

**Tabela 8 — Latência de geração e duração das campanhas**

| Modelo | Chamadas registradas | Latência média (s) | Mediana (s) | Duração da campanha (min) |
|---|---|---|---|---|
| GPT-4.1 mini | 283 | 5,85 | 5,22 | 129,24 |
| GPT-5.6 Luna | 277 | 6,92 | 6,71 | 130,77 |
| GPT-6 Luna | 274 | 6,04 | 5,75 | 121,34 |

Fonte: todas as chamadas registradas e uma sessão por modelo. A duração corresponde ao tempo decorrido da sessão; médias e medianas se referem à latência individual da geração. A avaliação conjunta da RRIS foi realizada separadamente e não integra essa duração.


### 5.5 Resultados por tipo de vulnerabilidade e categoria

A distribuição dos aceites variou entre os tipos de alerta catalogados, como mostra a Tabela 9. Os três modelos tiveram oito aceites entre os 12 casos de XSS; em IDOR, os totais foram diferentes, com maior número no GPT-5.6 Luna. Nos sete casos de travessia de diretórios, o GPT-4.1 mini e o GPT-6 Luna tiveram cinco aceites cada. Esses resultados descrevem o conjunto estudado, mas os grupos pequenos exigem cautela: o aceite do único caso de SSRF, por exemplo, não sustenta uma estimativa geral de eficácia para esse tipo de problema.

**Tabela 9 — Casos aceitos por tipo de alerta catalogado**

| Tipo de alerta | GPT-4.1 mini | GPT-5.6 Luna | GPT-6 Luna |
|---|---|---|---|
| Scripting entre sites (XSS) | 8/12 | 8/12 | 8/12 |
| Referência direta insegura a objetos (IDOR) | 3/8 | 7/8 | 6/8 |
| Travessia de diretórios | 5/7 | 3/7 | 5/7 |
| Credenciais fixas | 0/4 | 0/4 | 0/4 |
| Injeção de código | 3/4 | 3/4 | 4/4 |
| Exposição de informações | 0/4 | 3/4 | 2/4 |
| Negação de serviço por expressão regular | 0/2 | 1/2 | 0/2 |
| Redirecionamento aberto | 1/2 | 1/2 | 1/2 |
| Injeção SQL | 1/2 | 2/2 | 2/2 |
| Requisição indevida pelo servidor (SSRF) | 1/1 | 1/1 | 1/1 |
| Outros rótulos do catálogo | 16/32 | 22/32 | 20/32 |

Fonte: catálogo e primeiros aceites na definição por critérios. Células apresentam casos aceitos/total de casos do tipo. Os grupos são descritivos e não comprovam a existência de vulnerabilidade explorável em todas as ocorrências.


O agrupamento por regra refinou essa descrição. Na regra relacionada ao uso de HTML tratado como confiável no Angular, os três modelos obtiveram oito aceites em nove casos. Já na regra de consulta sem delimitação pelo identificador da requisição, os aceites foram um, três e dois, em quatro casos, na ordem dos modelos das tabelas. Nenhum modelo obteve aceite nos quatro casos rotulados como credenciais fixas. Esses contrastes indicam dificuldades distintas no conjunto observado, mas não permitem atribuí-las automaticamente à complexidade de uma vulnerabilidade. Uma explicação de causa exige examinar a proposta, a aplicação e os testes, como nos exemplos da seção seguinte.

A Tabela 10 apresenta os aceites segundo a classificação OWASP Top 10:2025 dos 78 casos. A classificação foi concluída após as campanhas, preservando as 29 associações originais e complementando os 49 casos sem categoria. Entre os complementares, 41 foram associados pelas listas oficiais de CWEs e oito por análise contextual do alerta e do código. Quatro decisões contextuais envolveram consultas NoSQL com CWE-943, e as outras quatro envolveram CWE-20, para os quais o contexto permitiu uma associação mais específica. Esse agrupamento manteve os rótulos de triagem e os resultados das verificações.

**Tabela 10 — Casos aceitos por categoria OWASP na classificação final**

| Categoria OWASP 2025 | GPT-4.1 mini | GPT-5.6 Luna | GPT-6 Luna |
|---|---|---|---|
| A01 | 9/26 | 18/26 | 16/26 |
| A02 | 1/3 | 2/3 | 1/3 |
| A04 | 2/5 | 4/5 | 4/5 |
| A05 | 15/22 | 17/22 | 18/22 |
| A06 | 8/12 | 7/12 | 7/12 |
| A07 | 3/7 | 3/7 | 3/7 |
| A08 | 0/3 | 0/3 | 0/3 |

Fonte: classificação complementar por caso e registros de aceite das campanhas finais. Células apresentam casos aceitos/total da categoria, com F por critérios. As linhas particionam os 78 casos e incluem os rótulos confirmados, falsos positivos e inconclusivos da triagem. Os totais permanecem 38, 51 e 49 aceites, respectivamente.

A01 e A05 concentraram os maiores grupos, com 26 e 22 casos. Em A01, o GPT-5.6 Luna obteve 18 aceites, seguido pelo GPT-6 Luna, com 16, e pelo GPT-4.1 mini, com nove. Em A05, o GPT-6 Luna apresentou 18 aceites, o GPT-5.6 Luna 17 e o GPT-4.1 mini 15. Os três modelos obtiveram três aceites nos sete casos de A07 e nenhum nos três casos de A08. Assim, os contrastes entre modelos também dependeram da categoria analisada.

Não foram atribuídos casos a A03, A09 ou A10 nessa distribuição. Os resultados por OWASP descrevem as sete categorias representadas no catálogo, com grupos de tamanhos distintos. A classificação posterior ampliou a cobertura do agrupamento sem acrescentar tentativas ou verificações das correções; as decisões contextuais e os grupos pequenos devem ser considerados na interpretação das diferenças.

<!-- Evidência: experimento@2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59; config/classificacao_owasp/v1/classificacao-78-casos.csv, idêntico ao derivado em evidencias/classificacao-owasp-complementar-2026-11-11/; outputs/rris/AMP_REAL_20261106T{151004Z_f49ac0d2,125801Z_0eb68fe4,105533Z_aa697342}_METRICAS/tentativas.csv; Q3. Tabela 10 utiliza a classificação complementar posterior às campanhas. Distribuição original preservada nas evidências de 11/11/2026. -->

### 5.6 Análise de correções e falhas representativas

Foram selecionados dois casos para examinar quatro tentativas com resultados contrastantes. A seleção considerou a disponibilidade dos artefatos, a clareza da alteração e a possibilidade de confrontar remoção do alerta com preservação funcional. A Tabela 11 reúne as evidências. A leitura documental dos patches, das comparações e dos testes foi realizada para esta discussão, com apoio automatizado. Os autores não realizaram inspeção manual dos patches; a avaliação das correções utilizou as verificações automatizadas e as métricas definidas no Capítulo 3. Os exemplos têm finalidade explicativa e não constituem uma amostra representativa de todas as correções.

**Tabela 11 — Evidências dos exemplos selecionados**

| Caso e tentativa | R | F por critérios | F sem separação | M | Classificação principal |
|---|---|---|---|---|---|
| Pedidos — GPT-4.1 mini/P1 | 1 | 1 | 0 | 1 | Aceita |
| CAPTCHA — GPT-4.1 mini/P1 | 1 | 0 | 0 | 1 | Rejeitada |
| CAPTCHA — GPT-6 Luna/P1 | 1 | 0 | 0 | 1 | Rejeitada |
| CAPTCHA — GPT-6 Luna/P2 | 1 | 1 | 1 | 1 | Aceita |

Fonte: registros, patches, comparações e testes das quatro tentativas identificadas nas notas de evidência. Seleção ilustrativa de dois casos, sem auditoria humana independente.


O primeiro caso foi uma consulta de acompanhamento de pedidos que utilizava uma expressão dinâmica com $where. Na tentativa P1 do GPT-4.1 mini, o patch substituiu a expressão dinâmica com $where por um filtro direto em orderId. A comparação registrou R=1 e M=1. A falha nova identificada no teste que obtinha todos os pedidos por injeção foi separada no conjunto D, resultando em F por critérios igual a 1 e F sem separação igual a 0. O aceite, portanto, dependeu da definição principal. O exemplo mostra por que um teste vinculado ao ataque pode reprovar após uma alteração, sem que isso comprove, isoladamente, regressão de comportamento legítimo ou segurança completa.

No segundo caso, o alerta incidiu sobre eval no cálculo do CAPTCHA. A tentativa P1 do GPT-4.1 mini substituiu a avaliação dinâmica por operações aritméticas explícitas. Entretanto, o código calculou os operadores da esquerda para a direita: para 2+3*4, essa ordem produz 20, enquanto o teste esperava 14. Foram registradas falhas nas expressões 2+3*4 e 2-3*4, com R=1, M=1 e F=0. O caso tinha rótulo arquivado de falso positivo, pois a expressão original era formada por números e operadores internos. Assim, ilustra tanto a diferença entre retirar um padrão e preservar o comportamento quanto o risco de modificar código a partir de um alerta cuja necessidade de correção não foi demonstrada.

**Excerto da proposta P1 do GPT-4.1 mini para o CAPTCHA:**

```typescript
      let result = numbers[0];
      if (operators[0] === '+') result += numbers[1];
      else if (operators[0] === '-') result -= numbers[1];
      else if (operators[0] === '*') result *= numbers[1];
      if (operators[1] === '+') result += numbers[2];
      else if (operators[1] === '-') result -= numbers[2];
      else if (operators[1] === '*') result *= numbers[2];
```

Fonte: trecho literal do patch arquivado. A função completa e os resultados dos testes estão identificados nas notas de evidência.

Para o mesmo alerta do CAPTCHA, a tentativa P1 do GPT-6 Luna também foi rejeitada pelos testes, mas P2 produziu uma proposta que tratou a precedência da multiplicação e recebeu R=F=M=1 nas duas interpretações funcionais apresentadas. O GPT-4.1 mini permaneceu sem aceite para esse caso nas quatro estratégias. A comparação mostra que propostas diferentes podem receber avaliações distintas para uma mesma entrada, e que os testes adicionais impediram o aceite de alterações que apenas removiam eval. Esse exemplo não prova efeito causal do roteiro de P2 nem transforma a alteração aceita em correção de uma vulnerabilidade comprovada, dado o rótulo original do caso.

**Excerto da proposta P2 do GPT-6 Luna para o mesmo CAPTCHA:**

```typescript
    const answer = (secondOperator === '*'
      ? calculate(firstTerm, firstOperator, calculate(secondTerm, secondOperator, thirdTerm))
      : calculate(calculate(firstTerm, firstOperator, secondTerm), secondOperator, thirdTerm)).toString()
```

Fonte: trecho literal do patch arquivado; a função auxiliar calculate realiza as operações aritméticas explícitas.

### 5.7 Redução conjunta de alertas e RRIS

A avaliação conjunta partiu dos primeiros aceites por caso e tentou integrar os patches em uma cópia limpa do projeto. Parte deles não pôde ser aplicada após as alterações anteriores, conforme a Tabela 12. O GPT-4.1 mini teve quatro conflitos, o GPT-5.6 Luna oito e o GPT-6 Luna nove. Os registros apontaram falhas de aplicação de trechos no estado já alterado dos arquivos. Dessa forma, o número de patches integrados foi menor do que o de aceites individuais; estes não poderiam ser somados para estimar a redução conjunta dos alertas.

**Tabela 12 — Aplicação conjunta dos patches e redução dos alertas**

| Modelo | Selecionados | Aplicados | Conflitos | Alertas antes → depois | RRIS | Aprovação funcional |
|---|---|---|---|---|---|---|
| GPT-4.1 mini | 38 | 34 | 4 | 78 → 40 | 38/78 (48,72%) | Não |
| GPT-5.6 Luna | 51 | 43 | 8 | 78 → 23 | 55/78 (70,51%) | Não |
| GPT-6 Luna | 49 | 40 | 9 | 78 → 31 | 47/78 (60,26%) | Não |

Fonte: avaliações conjuntas arquivadas, seleção pelo primeiro aceite por caso com F por critérios. RRIS calculada a partir dos scans globais comparáveis; aprovação funcional refere-se ao conjunto integrado.


Os scans globais registraram 78 alertas antes da aplicação conjunta. Após a integração possível, os totais foram 40, 23 e 31, respectivamente, resultando nas RRIS apresentadas na tabela. O GPT-5.6 Luna teve a maior redução estática observada. Essa medida considera a variação do total de alertas e pode diferir do número de patches aplicados, pois uma alteração pode afetar várias ocorrências. Os scans também registraram limitações de análise, preservadas nos artefatos, que restringem o alcance da evidência estática.

Nenhum dos três conjuntos integrados recebeu aprovação funcional, inclusive na definição por critérios. Entre as falhas documentadas, os três apresentaram problema no teste de login de um usuário recém-criado e no teste adicional de persistência e listagem de feedback normal. Nos dois Luna também houve falha na verificação independente da integridade dos cenários de último endereço IP. Esses registros mostram que aceites individuais não asseguraram o funcionamento da composição. Não foi realizada uma atribuição causal completa de cada falha a um patch; por isso, as RRIS devem ser interpretadas como redução estática observada em conjuntos não validados funcionalmente.

### 5.8 Respostas às perguntas de pesquisa

Em relação à Q1, foi possível produzir tentativas aceitas pelo pipeline segundo a definição operacional adotada: houve pelo menos um aceite em 38, 51 e 49 dos 78 casos, conforme o modelo. Mesmo na interpretação funcional sem separação, permaneceram 17, 22 e 23 tentativas aceitas nas respectivas populações principais. A resposta é, portanto, positiva quanto à possibilidade de obter aceites sob critérios explícitos de SAST e testes. Ela não equivale à correção demonstrada de todas as ocorrências nem à obtenção de uma versão integrada funcionalmente aprovada, que não foi alcançada nas avaliações conjuntas.

Para a Q2, as estratégias contribuíram de forma diferente ao longo da sequência: P1 produziu aceites iniciais e P2–P4 acrescentaram outros casos, com contribuição expressiva de P3 nos três modelos. Os dados sustentam a utilidade observada de ampliar o percurso de geração, mas não isolam a influência causal de cada estratégia. P2–P4 receberam casos remanescentes, e P3/P4 acrescentaram diagnóstico e documentação simultaneamente. Assim, não foi demonstrado um ganho atribuível exclusivamente ao RAG ou ao roteiro, nem uma estratégia universalmente superior.

Quanto à Q3, o desempenho variou descritivamente conforme os tipos e as regras, como nos contrastes entre XSS, IDOR e travessia de diretórios. A classificação final por OWASP agrupou os 78 casos em sete categorias, preservando os resultados e os rótulos da triagem. Esse recorte também apresentou diferenças, mas depende das associações adotadas e contém grupos pequenos. A resposta sustentada é que o desempenho não foi uniforme no catálogo analisado; os resultados não permitem generalizar uma ordem de dificuldade entre vulnerabilidades nem estimar a eficácia para todas as categorias OWASP.

Para a Q4, foram identificadas limitações práticas na aplicação das edições, na avaliação funcional e na integração das propostas. Referências ausentes ou ambíguas impediram aplicações; alterações que removiam alertas falharam nos testes; definições diferentes de F mudaram os aceites; e patches aceitos separadamente encontraram conflitos ou falhas quando reunidos. A coordenação das dependências e dos recursos de execução também compôs o tempo das campanhas. Esses resultados reforçam que o desafio envolveu manter o funcionamento e a rastreabilidade, além de gerar um trecho de código plausível.

Em resposta à Q5, o GPT-5.6 Luna apresentou o maior número de casos aceitos e a maior TRV, enquanto o GPT-6 Luna teve o menor custo registrado e a menor duração total da sessão. O GPT-4.1 mini teve a menor latência média de geração, mas menos aceites e maior custo calculado da campanha. A escolha entre os modelos depende, portanto, da medida considerada nas condições estudadas. A diferença de dois casos entre os Luna, os parâmetros específicos e a ausência de réplicas independentes impedem interpretar esses achados como superioridade geral de um modelo.

### 5.9 Discussão com a literatura e implicações

Os achados dialogam com a discussão do referencial sobre contexto e validação externa. Khan, Liu e Gao (2025) investigaram reparo de estouro de buffer com GitHub Copilot e contexto de segurança; Sriram et al. (2026) propuseram um fluxo de geração e reparo com recuperação semântica, compilador, CodeQL e execução simbólica. Esses desenhos diferem do presente estudo em alvo, ferramentas, recuperação e critérios de avaliação, de modo que suas taxas não foram tratadas como diretamente comparáveis. A aproximação é conceitual: informação contextual e verificação por ferramentas compõem o processo, mas sua contribuição precisa ser examinada no desenho em que foi medida. [Khan, Liu e Gao (2025)](https://arxiv.org/abs/2409.18395v2), [Sriram et al. (2026)](https://arxiv.org/abs/2601.00509v1).

Neste experimento, a combinação de SAST e testes permitiu distinguir situações que uma única verificação não separaria. O exemplo do CAPTCHA mostrou remoção de alerta acompanhada de falha funcional, enquanto o acompanhamento de pedidos evidenciou a influência dos testes associados ao ataque. A avaliação conjunta acrescentou um terceiro nível, ao revelar falhas na composição de alterações aceitas isoladamente. A contribuição observada do pipeline esteve também nessa capacidade de registrar diferentes formas de insucesso, evitando reduzir a avaliação à presença ou ausência de um alerta.

Como implicação prática, os modelos puderam apoiar a elaboração de propostas, mas os resultados não sustentaram sua adoção automática como versão final da aplicação. A existência de um aceite exclusivo do GPT-4.1 mini e de aceites exclusivos dos Luna sugere diversidade de soluções, sem validar uma política combinada de uso. Os custos calculados ajudam a dimensionar a geração, mas não incluem o trabalho necessário para revisar propostas e resolver incompatibilidades. A utilização das correções em outro contexto exigiria examinar sua adequação e sua integração, atividades que não foram demonstradas por uma revisão humana integral neste estudo.

### 5.10 Ameaças à validade e síntese do capítulo

A validade das medidas depende do alcance das regras e dos testes e da qualidade das classificações utilizadas. A remoção do alerta não prova eliminação de todas as formas do problema, e a ausência de novos alertas não significa ausência de novas vulnerabilidades. A triagem arquivada e o conjunto D afetam a interpretação; os critérios de D evoluíram durante a preparação, inclusive após execução exploratória descartada. A sensibilidade de F torna essa dependência visível, mas não substitui revisão independente. A seleção documental de dois exemplos também limita qualquer generalização qualitativa, e a sequência das estratégias impede separar seus efeitos causais.

A generalização foi limitada a uma aplicação deliberadamente vulnerável, uma revisão do alvo e uma campanha final por modelo. O Juice Shop possui comportamentos e testes orientados a desafios de segurança, que diferem dos requisitos de um sistema em produção. Além disso, parâmetros de geração, trajetórias pelas estratégias, tarifas configuradas e condições de execução podem influenciar os resultados. Sem réplicas independentes, não foi estimada a estabilidade das diferenças observadas; tempos e custos não devem ser projetados diretamente para outros projetos ou equipamentos.

Os resultados indicaram que o pipeline produziu aceites individuais e reduções estáticas conjuntas, com diferenças entre modelos, estratégias e grupos de alertas. Também mostraram que esses êxitos foram condicionados pela definição funcional e não resultaram em um conjunto integrado aprovado. A disponibilização da imagem Docker, do repositório e das configurações apoia a repetição do procedimento, sem constituir replicação independente já demonstrada. Esses achados e limites fornecem a base para a conclusão geral do trabalho e para a definição de melhorias futuras.
