# Reavaliação da versão exportada do Overleaf — 15/11/2026

**Fonte principal:** `../../TCC2___Caio_Lamego_e_Matheus_Brant(1)/`, indicada pelo autor como a versão atual. Foram considerados os arquivos efetivamente incluídos por `tcc.tex`. Os nomes internos não indicam necessariamente o capítulo: `consideracoes.tex` contém a metodologia, `elementosdotexto.tex` contém a implementação e `elementosdopostexto.tex` contém as considerações finais.

Esta avaliação substitui o parecer dos Markdown para julgar essa versão. Os arquivos do projeto Overleaf não foram alterados. O roteiro local `tcc2-revisar` foi mantido, adaptando a fonte principal aos arquivos LaTeX indicados pelo usuário.

## Parecer geral

O núcleo experimental continua consistente e tem conteúdo para uma defesa fundamentada. Os capítulos 3–6 descrevem método, implementação, resultados e conclusão de uma pesquisa realizada. O capítulo 5 está mais conciso que o Markdown anteriormente avaliado e delimita melhor a resposta à Q2. As capturas do painel estão incluídas e foram inspecionadas.

Entretanto, o documento completo ainda não está editorialmente integrado: resumo, abstract e introdução permanecem associados à proposta anterior, enquanto o restante apresenta as campanhas concluídas. A introdução anuncia quatro perguntas e cinco capítulos, mas o corpo trabalha com cinco perguntas e seis capítulos. Essa é agora a prioridade principal, acima das sugestões de concisão feitas no parecer anterior.

Não considero esta exportação pronta para entrega final sem corrigir essas inconsistências. Isso não significa que falte executar a pesquisa: o problema mais evidente é fazer a abertura e os elementos auxiliares representarem a pesquisa já documentada nos capítulos seguintes.

## O que muda em relação ao parecer anterior

| Tema | Situação nesta versão |
|---|---|
| Unidade entre introdução, método e resultados | Há um problema novo e prioritário: a introdução e os resumos descrevem trabalho futuro e uma PoC inicial. |
| Presença de Q1–Q5 | Q5 está ausente da introdução e dos objetivos específicos, mas aparece no método e nos resultados. |
| Resposta à Q2 | Melhorou: o texto agora explicita que mede o acréscimo na sequência, não uma comparação direta das estratégias. A crítica anterior precisa ser reduzida. |
| Capturas do painel | Resolvido nesta exportação: três figuras foram incluídas, com texto explicativo e fonte. |
| Repetição no capítulo 5 | Reduzida: há remissões ao método e respostas mais compactas; a sugestão anterior não deve ser repetida com a mesma intensidade. |
| Critérios do conjunto D | A necessidade de documentação mais explícita permanece. |
| Exemplo de `keyServer.ts` | Permanece a divergência entre afirmar path traversal e a justificativa registrada na triagem. |
| Referência sobre fidelidade de CoT | Permanece a atribuição inadequada a Lester, Al-Rfou e Constant. |
| Formatação das referências Markdown | Não se aplica automaticamente ao `.bib`. Foram encontrados problemas próprios da exportação: cinco chaves duplicadas. |
| Numeração local dos elementos | O projeto utiliza captions, labels e referências automáticas. Não há motivo para transportar a crítica à numeração dos Markdown como se fosse o mesmo problema. |

## Achados demonstrados e correções propostas

Os caminhos desta seção são relativos à pasta exportada do Overleaf. As linhas correspondem aos arquivos consultados nesta revisão.

### 1. Alta — introdução apresenta uma pesquisa futura e uma organização incompatível com o documento

**Local:** `editaveis/introducao.tex:59–70` e `:83`.

**Problema:** a seção de metodologia diz “Inicialmente, será selecionado um projeto público”, distingue “TCC 1” e “TCC 2” e apresenta a aplicação em uma base real como intenção futura. A organização anuncia o capítulo 4 como prova de conceito e o capítulo 5 como considerações finais. Contudo, os arquivos incluídos por `tcc.tex` contêm implementação no capítulo 4, resultados no capítulo 5 e considerações finais no capítulo 6.

**Fonte de contraste:** `tcc.tex`, `editaveis/consideracoes.tex:4–7`, `editaveis/resultado-discussoes.tex:11` e `editaveis/elementosdopostexto.tex:9–17`.

**Correção proposta:** reescrever apenas as partes desatualizadas da abertura para apresentar o estudo realizado: Juice Shop, 78 alertas, três modelos, sequência P1–P4, validação R/F/M e avaliação conjunta. Apresentar a monografia como pesquisa única e atualizar a descrição dos seis capítulos. As seções de contexto e problema podem ser aproveitadas, com revisão de precisão.

### 2. Alta — Q5 e o objetivo de comparação entre modelos não estão na introdução

**Local:** `editaveis/introducao.tex:31–55`.

**Problema:** a lista termina em Q4, e os objetivos específicos não incluem a comparação de modelos por eficácia, custo e tempo. A metodologia afirma que existem cinco perguntas na introdução (`consideracoes.tex:45`) e descreve a resposta à Q5 (`:474`). O capítulo 5 formula e responde Q5 (`resultado-discussoes.tex:600–602`).

**Correção proposta:** incorporar à introdução a Q5 efetivamente utilizada e seu objetivo específico. Conferir os enunciados em todas as ocorrências. O problema é de alinhamento do documento, não de ausência de resultados para essa pergunta.

### 3. Alta — resumo e abstract não resumem a pesquisa apresentada

**Local:** `editaveis/resumo.tex:2` e `editaveis/abstract.tex:3`.

**Problema:** os dois textos descrevem a preparação de uma PoC e a avaliação futura no TCC 2. Não identificam os três modelos, o conjunto de casos nem os resultados centrais. O leitor recebe uma descrição de etapa preparatória, embora a conclusão apresente a avaliação concluída.

**Correção proposta:** apresentar objetivo, método executado, principais resultados e conclusão delimitada. Selecionar poucas informações: os 78 alertas, os três modelos, a diferença de desempenho observada e a ausência de aprovação funcional dos conjuntos integrados. Manter o sentido operacional de “aceite”. Atualizar português e inglês de forma equivalente.

### 4. Média — o referencial ainda atribui ao próprio estudo procedimentos futuros ou não demonstrados

**Local:** `editaveis/aspectosgerais.tex:59`, `:77–79` e `:146–148`.

**Problema:** o texto anuncia que as etapas apresentadas pela LLM “deverão ser confrontadas” com diagnósticos e testes, menciona exemplos few-shot que “poderão” ser usados e descreve a execução SAST como futura. No método executado, a avaliação recai sobre os patches e as verificações R/F/M; não foi demonstrada uma avaliação sistemática das etapas textuais de raciocínio.

**Correção proposta:** manter as possibilidades gerais como discussão teórica e identificar explicitamente quais foram adotadas. Nos parágrafos iniciados por “Neste trabalho”, descrever o realizado. Não converter previsões em passado sem conferir que foram implementadas. A base RAG contém exemplos genéricos, o que não basta para afirmar uma condição experimental específica de few-shot sem descrevê-la.

### 5. Alta — exemplo de implementação continua afirmando mais do que a triagem sustenta

**Local:** `editaveis/elementosdotexto.tex:95`, referente ao caso `AMP95adf572d3c6677f`.

**Problema:** o texto caracteriza o caso como uma vulnerabilidade de path traversal. A justificativa do catálogo experimental, reaberta nesta revisão, afirma que a rota pública expõe arquivos de chaves e distingue essa exposição de uma prova de path traversal.

**Fonte de contraste:** `../tcc2-llm-sast-juiceshop/outputs/catalogos/ampliado_v1/catalogo_issues.json`, SHA experimental `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`. A justificativa do caso foi preservada integralmente no JSON de conferência desta revisão.

**Correção proposta:** descrever um alerta de possível path traversal, separar o diagnóstico do Semgrep da conclusão da triagem e manter o resultado do patch restrito ao que foi verificado. A aprovação em R/F/M, relatada na linha 290, não precisa ser removida. Não afirmar que a exposição de chaves foi solucionada sem evidência correspondente.

### 6. Alta — permanece a citação inadequada sobre fidelidade de CoT

**Local:** `editaveis/aspectosgerais.tex:59`, chave `lester_power_2021`.

**Problema:** a citação sustenta a afirmação de que a cadeia textual pode ser uma justificativa posterior que não representa o processo interno. O artigo de Lester, Al-Rfou e Constant trata de aprendizado de soft prompts, não fornece sustentação direta para essa afirmação específica.

**Fonte de contraste:** [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/html/2104.08691v2), consultado na revisão anterior desta mesma sessão. A utilização do artigo para definir prompt tuning na linha 47 continua pertinente.

**Correção proposta:** usar uma fonte diretamente relacionada à fidelidade das explicações ou reformular o trecho como delimitação operacional do presente estudo. Não basta trocar a chave por outra referência de engenharia de prompt sem verificar seu conteúdo.

### 7. Média — a lista de símbolos troca a unidade de análise

**Local:** `editaveis/simbolos.tex:3–5` versus `editaveis/consideracoes.tex:382`.

**Problema:** a lista define Rj, Fj e Mj em relação à “issue real j”. Na metodologia, j indexa cada tentativa. Um mesmo caso pode gerar várias tentativas, e parte do catálogo é composta por falsos positivos ou inconclusivos. Essa diferença interfere na leitura das equações por tentativa.

**Correção proposta:** definir os três símbolos em relação à tentativa j e ao alerta-alvo, de acordo com a metodologia. Completar a lista com D e os conjuntos/denominadores usados nas fórmulas, se a lista se destinar a reunir toda a notação. Acrescentar TRV, TRI, TPF, TFF e TNINI à lista de siglas também melhoraria a consulta.

### 8. Média — bibliografia contém cinco chaves duplicadas

**Local:** `bibliografia.bib`.

| Chave | Linhas |
|---|---|
| `owasp_top10_2025_intro` | 198 e 545 |
| `stackoverflow_survey_ai_2025` | 497 e 725 |
| `openai_gpt5` | 505 e 693 |
| `openai_introducing_gpt5_2025` | 513 e 701 |
| `owasp_api_bola_2023` | 601 e 749 |

**Problema:** as entradas não têm identidade única. A chave OWASP é citada ativamente no referencial; suas duas entradas ainda apresentam datas de acesso diferentes. As demais duplicações também devem ser saneadas, embora nem todas sejam citadas no texto ativo.

**Correção proposta:** consolidar cada obra em uma entrada, preservando os metadados verificados e atualizando as citações se necessário. Não foi executado BibTeX nesta revisão; o achado é a duplicação demonstrada no arquivo, não uma alegação de falha observada na compilação do Overleaf.

### 9. Média — data de aprovação aparenta pertencer à entrega anterior

**Local:** `editaveis/informacoes.tex:19`; uso em `fixos/folhaDeAprovacao.tex:19`.

**Problema:** a folha ativa apresenta “Trabalho aprovado” com data de 16 de julho de 2026, enquanto os resultados centrais decorrem de campanhas concluídas em novembro de 2026. Isso sugere um dado herdado da etapa anterior.

**Correção proposta:** conferir a adequação da data e dos dados de banca para esta entrega. Não substituir por uma data presumida e não afirmar aprovação da versão final com base no campo antigo. Este é um item a confirmar, não uma conclusão sobre o estado acadêmico real do trabalho.

## Limitações metodológicas que permanecem

### Conjunto D e procedência da triagem

A seção de validação (`consideracoes.tex:349–368`) explica o princípio do conjunto D e mantém as três interpretações de F. A discussão (`resultado-discussoes.tex:622`) informa que os critérios evoluíram após uma execução exploratória descartada. Isso é positivo, mas ainda falta uma apresentação compacta dos critérios (a) a (e), seu alcance por caso ou geral, exemplos e responsabilidade pela classificação.

A tabela de sensibilidade mostra a importância da decisão: no GPT-5.6 Luna há 22 aceites sem separação e 51 por critérios na mesma população. Recomenda-se uma tabela de critérios no método e um apêndice ou referência versionada para a lista completa. A ausência de inspeção manual dos patches está declarada; deve permanecer clara, especialmente diante da necessidade de conferência manual mencionada nos registros históricos de preparação.

Os 55 confirmados são rótulos da triagem, não uma verdade de referência independente. A versão atual faz essa distinção no método e nos resultados; convém mantê-la também nas sínteses e documentar melhor autoria e revisão dos rótulos. Esses pontos limitam a interpretação, mas não demonstram que os números estejam errados.

### Comparação de prompts — crítica anterior parcialmente atendida

A resposta atual à Q2 (`resultado-discussoes.tex:590`) declara expressamente que descreve o acréscimo na sequência e não uma comparação direta. A metodologia (`consideracoes.tex:485`) também reconhece as populações diferentes e a inclusão conjunta de diagnóstico e documentação. Portanto, não seria correto repetir que essa ressalva está ausente da resposta.

Permanece uma oportunidade de alinhar o enunciado e o objetivo da introdução à contribuição incremental observada. O desenho também não compara a sequência com repetir P1 sob igual orçamento de chamadas. Esse limite deve orientar a defesa: mais aceites ao prolongar o processo não isola o efeito de cada componente do prompt. Não há necessidade automática de novas campanhas para relatar corretamente o estudo realizado.

### Comparação de modelos

A versão atual reconhece a pequena diferença entre os Luna e uma campanha por modelo. Preservar o caráter descritivo. Para reprodução, reunir identificadores exatos dos modelos, seed ou ausência desse parâmetro, tarifas usadas e recursos da máquina em um quadro/apêndice. A seed 42 do mini está no contrato experimental, mas não aparece no texto lido. A afirmação de que qualquer computador com Docker executa “nas mesmas condições” (`elementosdotexto.tex:48`) deve ser limitada à padronização de software e dependências.

## Escrita, discussão e figuras

- **Resultados mais concisos:** os parágrafos de TFF, sobreposição, RRIS e respostas às perguntas estão mais compactos. A conclusão repetida ao final de 5.10 foi retirada. Ainda cabe condensar leituras de tabelas, mas isso deixou de ser prioridade principal.
- **Trabalhos relacionados:** a seção 2.5 ainda resume estudos sem mostrar suficientemente a lacuna específica. Uma comparação de alvo, contexto, feedback, validação funcional e integração de patches tornaria a contribuição mais defensável. A discussão em 5.9 acerta ao não comparar diretamente taxas obtidas em desenhos distintos.
- **Precisão do referencial:** permanecem expressões fortes, como “impede que etapas importantes sejam omitidas”, “máxima eficácia” e avaliar se a LLM “compreende a causa”. Preferir orientar, observar e avaliar a adequação da alteração. A proposta original do Transformer é de 2017; o registro de 2023 corresponde a uma revisão do artigo, distinção a explicitar. [Fonte primária consultada na sessão](https://arxiv.org/abs/1706.03762).
- **Categorias OWASP:** A02, A06 e A08 aparecem nos resultados, mas não recebem explicação equivalente às categorias selecionadas no referencial; A10 é desenvolvida sem casos no experimento. Uma tabela das categorias e do recorte do estudo ajudaria.
- **Figuras do painel:** `painel.png`, `escolha-llm.png` e `execucao.png` existem e correspondem ao conteúdo descrito. O texto distingue a escolha para a próxima execução dos resultados de uma campanha no histórico, o que evita confusão entre modelos. A antiga pendência está resolvida.
- **Fluxograma do método:** a ordem testes → SAST coincide com a descrição. A legenda delimita a parada estrita, mas o losango diz apenas “Correção válida?”. Renomeá-lo para a regra de parada estrita e trocar “encerrar pipeline” por “encerrar tentativas do caso” reduziria a ambiguidade. É uma melhoria de precisão da figura, não um erro demonstrado da execução.
- **Legibilidade:** o diagrama `etapas-pipeline.png` é muito horizontal, e as capturas do painel contêm texto pequeno. Conferir a leitura no PDF em tamanho normal de página; a resolução isolada da imagem não garante legibilidade após redução. Não foi inspecionada a paginação final.
- **Listagem JSON:** `elementosdotexto.tex:173–178` quebra fisicamente as strings para caber na página. O comentário explica isso no fonte, mas não aparece ao leitor. Identificar no texto que é uma apresentação abreviada ou usar quebra visual que preserve a sintaxe do exemplo.
- **Conclusão:** os cinco parágrafos são suficientes e coerentes com os resultados. Uma frase sobre aplicação única, campanha única e definição funcional reforçaria sua autonomia. A reprovação conjunta deve continuar explícita.

## Avaliação por parte do documento

| Parte | Avaliação atual |
|---|---|
| Resumo e abstract | Desatualizados em relação ao estudo concluído; precisam ser reescritos. |
| Introdução | Contexto aproveitável; método resumido, perguntas, objetivos e organização precisam de integração prioritária. |
| Referencial | Boa cobertura de conceitos; corrigir atribuições, promessas futuras e relação com o método efetivo. |
| Metodologia | Detalhada e predominantemente coerente; fortalecer a documentação de D e da triagem. |
| Implementação | Explicação concreta e agora ilustrada com painel; corrigir caracterização do exemplo. |
| Resultados | Parte mais madura; melhorou a concisão e a delimitação de Q2. |
| Considerações finais | Compatíveis com os resultados e com contribuição delimitada ao aceite individual. |

## Conferências realizadas e limites

Foram lidos os seis capítulos ativos, resumo, abstract, listas, dados de aprovação e estrutura do projeto. Foram inspecionadas as nove imagens PNG incluídas no corpo do documento. O rastreamento dos inputs, citações e remissões encontrou:

- nenhum arquivo de input ausente;
- nenhuma chave citada sem entrada no `.bib`;
- nenhum label explícito duplicado;
- nenhuma remissão interna sem definição, descontado `LastPage`, gerado pelo pacote `lastpage` já carregado;
- todos os arquivos de imagem referenciados presentes;
- cinco chaves bibliográficas duplicadas, listadas acima.

Essas são verificações estáticas, não uma compilação. A exportação não contém o PDF final, e não havia compilador TeX disponível nos comandos locais verificados. Não foram certificados paginação, margens, ausência de avisos de compilação ou conformidade integral ao template/ABNT. Não houve acesso ao projeto remoto do Overleaf; a fonte é a pasta indicada pelo autor.

As tabelas centrais do LaTeX foram confrontadas novamente com os CSVs e consolidados das campanhas no HEAD experimental `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`:

| Modelo | Tentativas principais | Aceites / 78 | Aceites / 55 confirmados | Aceites P1/P2/P3/P4 | Alertas antes → depois |
|---|---:|---:|---:|---|---|
| GPT-4.1 mini | 241 | 38 | 32 | 16 / 4 / 15 / 3 | 78 → 40 |
| GPT-5.6 Luna | 223 | 51 | 39 | 18 / 5 / 25 / 3 | 78 → 23 |
| GPT-6 Luna | 221 | 49 | 36 | 21 / 5 / 18 / 5 | 78 → 31 |

Os valores conferidos coincidem com o texto e a figura. Os consolidados continuam indicando ausência de aprovação funcional conjunta nos três modelos. Sem achados numéricos nesses pontos nesta revisão; isso não equivale a uma auditoria integral de segurança.

Nenhuma campanha, chamada LLM, execução SAST ou teste do alvo foi realizada. A bibliografia não foi integralmente auditada; a reavaliação reutiliza as fontes primárias já consultadas nesta sessão para os pontos que permaneceram iguais. A evidência está em [conferencia.json](../evidencias/reavaliacao-overleaf-2026-11-15/conferencia.json), com resultados das verificações e hashes dos arquivos lidos.

**Ordem recomendada:** integrar resumo/abstract e introdução; incluir Q5 e seu objetivo; corrigir símbolos e bibliografia; resolver as duas afirmações sem sustentação identificadas; documentar melhor D e triagem; revisar discussão, figuras e PDF final. A versão possui um bom núcleo experimental, mas a abertura ainda precisa representar esse núcleo.
