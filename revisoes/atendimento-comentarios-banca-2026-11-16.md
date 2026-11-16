# Atendimento aos comentários da banca — 16/11/2026

Comparação entre `../../Versão-comentada-banca.pdf` e os seis capítulos ativos de `../TCC2-OVERLEAF/tcc.tex`. Revisão documental com a skill `tcc2-revisar`, complementada por amostragem dos artefatos experimentais. Nenhum arquivo do trabalho ou do registro de ajustes foi alterado.

**Parecer:** o texto atual atende à maior parte das preocupações centrais da banca. A escolha do SAST, a descrição dos testes, os critérios de aceite, o limite de tentativas e os exemplos de correção no RAG estão substancialmente esclarecidos. O atendimento ainda não é integral: falta o modelo de dados solicitado; a tabela de ferramentas está incompleta; tamanho dos patches e ponderação por severidade não foram apresentados como resultados. O tratamento dos falsos positivos e o alcance da validação funcional merecem respostas explícitas na defesa.

As 30 anotações extraídas incluem observações positivas, perguntas, sugestões e uma síntese final com sete itens. Não representam 30 correções obrigatórias. Uma sugestão não implementada pode ser respondida por uma delimitação fundamentada; não é necessário ampliar artificialmente o experimento para declarar atendimento.

## Localização e critérios de leitura

As páginas abaixo são as **impressas no documento**. A posição no leitor PDF é uma unidade maior: a página impressa 67 corresponde à página 68 do arquivo.

Abreviações dos arquivos atuais, todos em `TCC2-OVERLEAF/editaveis/`:

- **INT:** `introducao.tex`, capítulo 1.
- **REF:** `aspectosgerais.tex`, capítulo 2.
- **MET:** `consideracoes.tex`, capítulo 3.
- **IMP:** `elementosdotexto.tex`, capítulo 4.
- **RES:** `resultado-discussoes.tex`, capítulo 5.
- **CON:** `elementosdopostexto.tex`, capítulo 6.

Os números após os nomes indicam linhas da versão consultada. “Atendido” significa que existe uma resposta documental compatível com a preocupação, não que se comprovou segurança absoluta. “Parcial” indica uma resposta existente com lacuna identificável. “Observação” identifica anotação que não solicita mudança.

## Conferência das 30 anotações

| Nº | Página | Comentário ou questão da banca | Situação no texto atual |
|---|---:|---|---|
| 1 | 13 | Dificuldade de gerar correções efetivas, apesar da detecção. | **Observação contemplada.** INT:19 mantém o problema; RES:81 distingue remoção, funcionalidade e novos alertas. A anotação menciona 60%, enquanto o texto assinalado se refere a outro valor; esta revisão não adotou a anotação como correção do resultado bibliográfico. |
| 2 | 13 | “O TCC2 deve argumentar sobre a prova de que não houve perda de funcionalidade.” | **Atendido com alcance delimitado.** MET:347 explica baseline e comparação; IMP:111–119 detalha testes e exemplo de D; RES:510 demonstra rejeição por regressão. Há evidência das funcionalidades testadas, sem prova universal. A reprovação funcional da integração é declarada em RES:549 e CON:15. |
| 3 | 15 | Interesse na Q4 e na construção/autorreparo. | **Observação positiva.** Q4 permanece em INT:36 e recebe resposta em RES:602. Não exige implementar autorreparo com feedback. |
| 4 | 15 | O desenvolvimento do pipeline será objeto da PoC. | **Observação contemplada.** IMP descreve a implementação e RES apresenta campanhas finais; a versão atual supera a descrição de uma proposta. |
| 5 | 19 | A metodologia seguirá o modelo de geração contextualizada descrito? | **Atendido.** REF:29 relaciona geração e SAST; MET:174–214 identifica modelos e componentes dos prompts. REF:81 esclarece que não são reutilizados erros ou respostas anteriores. A pesquisa não compara arquiteturas de redes. |
| 6 | 21 | Como CVE, CWE e CVSS serão utilizados? CVSS ponderará as correções? | **Parcial.** MET:245–277 e IMP:152 explicam o uso de CWE na recuperação. Não há explicitação equivalente de que CVE/NVD não constituíram mecanismo de recuperação do experimento e de que CVSS não ponderou os resultados. |
| 7 | 22 | Como a análise da causa raiz aparecerá no trabalho? | **Atendido na operacionalização, com limite.** MET:193 exige explicação da causa em P2/P4; MET:201–209 define os campos; MET:251–263 descreve mitigação e exemplos. IMP:95 e :290 distinguem alerta de causa comprovada. Não houve validação independente de toda causa alegada pelo modelo. |
| 8 | 25 | Registro das etapas possíveis do CoT. | **Observação contemplada.** MET:193 apresenta o roteiro efetivamente utilizado, com cinco etapas; a validação externa é distinta do texto produzido pelo modelo. Não é necessário afirmar que todos os sete passos da observação foram implementados literalmente. |
| 9 | 25 | Publicar prompts ou exemplos para permitir replicação. | **Atendido pelos artefatos; localização pode melhorar.** MET:193 e IMP:124–132 explicam montagem e exemplo; IMP:195 referencia o repositório; IMP:277 indica a pasta de prompts. Foram encontrados 834 JSONs de prompts nas três campanhas finais e abertos exemplos reais P2/P3. Um caminho direto para os modelos de prompt facilitaria a consulta sem reproduzi-los integralmente no texto. |
| 10 | 26 | Explicação do RAG e remissão ao pedido anterior. | **Atendido.** MET:245 explicita recuperação por associação, sem embeddings; MET:265–277 apresenta o fluxo e o registro. Não se deve exigir banco vetorial: a simplificação é expressa. |
| 11 | 27 | A base de conhecimento responde parte da pergunta da página 21. | **Observação contemplada.** MET:249–263 e IMP:150–152 descrevem documentos e seleção. Permanece a ressalva sobre CVE/CVSS do item 6. |
| 12 | 27 | Registro da proposta: RAG, few-shot/formato, retestes e CoT. | **Atendido com mudança de escopo explicitada.** REF:77–81 e MET:191–214 descrevem as combinações realmente avaliadas. Há exemplos na documentação recuperada, mas não um tratamento experimental separado de few-shot. Formato JSON não deve ser apresentado como equivalente a few-shot. |
| 13 | 29 | Quem faz a análise léxica: SAST ou prompt? | **Atendido.** REF:132 atribui expressamente a análise léxica à ferramenta SAST. IMP:249 descreve ainda uma conferência sintática do aplicador, etapa distinta da detecção. |
| 14 | 30 | O contexto do SAST responde parte da pergunta da página 21. | **Observação contemplada.** REF:146 e MET:195 identificam o diagnóstico fornecido em P3/P4. |
| 15 | 32 | Registro da proposta de integração. | **Observação contemplada.** REF:161 apresenta a implementação e avaliação concluídas, incluindo aplicação conjunta. |
| 16 | 33 | Quantos ciclos? Qual o limite? Risco de loop/alucinação? | **Atendido quanto ao procedimento.** MET:330 limita a sequência a P4; IMP:161 distingue repetição de comunicação, com até três envios e timeout, de nova estratégia. MET:334 e IMP:247 tratam saídas não aplicáveis. Isso limita o processo, mas não elimina alucinações semanticamente plausíveis. |
| 17 | 34 | Detalhar critérios para aprovar uma correção e testes. | **Atendido.** MET:339–377 define R/F/M, indeterminações e interpretações de F; IMP:111–119 explica a execução. A transparência de D permanece relevante para interpretar a aprovação. |
| 18 | 34 | Condensar repetições sobre o Juice Shop. | **Parcial; sugestão editorial.** MET:56 remete à caracterização específica, mas MET:97–103 ainda reúne quatro parágrafos sobre o objeto. Cabe redução localizada; não há exigência metodológica de remover toda caracterização. |
| 19 | 35 | Remissão à condensação sobre o Juice Shop. | **Mesmo diagnóstico do item 18.** MET:99 concentra tecnologias e sua pertinência. |
| 20 | 35 | Remissão à condensação da descrição de desafios. | **Mesmo diagnóstico do item 18.** MET:101 mantém 113 desafios e referências de classificação. |
| 21 | 36 | Remissão à condensação dos Coding Challenges. | **Mesmo diagnóstico do item 18.** MET:103 e :127 hoje explicam uma decisão de exclusão relevante; podem ser articulados sem repetir a descrição. |
| 22 | 36 | Remissão à condensação da seleção pelo SAST. | **Reorganizado.** MET:118–169 possui seção própria para seleção e triagem, incluindo exclusões. A redação atual não promete processar indiscriminadamente todos os alertas. |
| 23 | 40 | Incluir exemplos de correções nos documentos Markdown do RAG. | **Atendido.** MET:259 menciona código vulnerável e corrigido; o documento `knowledge_base/injection.md` contém exemplos de SQL parametrizado e outros mecanismos. O prompt P3 examinado inclui o exemplo do documento recuperado. |
| 24 | 41 | Esclarecer ferramentas, escopo da suíte e eventual fuzzing. | **Atendido no núcleo.** IMP:111–117 identifica Node.js, Vitest, compilação, tipos de testes, grupos, seleção e testes adicionais. Não apresenta fuzzing/Burp/ZAP como procedimentos empregados. A ausência de percentual de cobertura não impede explicar a cobertura funcional, mas quantidade de testes não equivale a percentual de linhas ou ramos. |
| 25 | 42 | Importância de cada prompt partir de uma instância limpa. | **Observação preservada.** MET:328 e IMP:243 descrevem restauração e isolamento. |
| 26 | 43 | Interesse em observar R=F=M=1 na prática. | **Atendido.** RES:46–152 apresenta aceites, critérios e sensibilidade à definição de F; não fica apenas na formulação booleana. |
| 27 | 45 | Criar diagrama de dados com armazenamentos, tipos, campos, chaves e relações. | **Parcial; falta o modelo solicitado.** MET:447–470 apresenta identificação; IMP:259–277 mostra diretórios e artefatos. A figura de nomenclatura explica um nome, não as relações entre entidades e seus campos. |
| 28 | 47 | Espera-se uma correção mesmo para falsos positivos? | **Parcial.** MET:163–169 e RES:13 declaram sua inclusão; RES:49 separa os 55 confirmados; RES:510 discute uma modificação desnecessária. Falta responder diretamente que o objetivo nesse grupo foi observar o processamento de alertas e que um aceite não demonstra correção de vulnerabilidade real. |
| 29 | 55 | Definir o SAST e tabelar componentes/ferramentas com versões. | **SAST atendido; tabela parcial.** MET:75 e :108 fixam Semgrep 1.177.0; IMP:50 identifica ambiente e revisão. A tabela de MET:60 não reúne versões de todas as ferramentas de validação/execução mencionadas no capítulo 4. |
| 30 | 67 | Síntese final, com sete recomendações. | **Atendimento misto.** Conferência separada abaixo; não deve ser contabilizada como uma única pendência nem como sete novas exigências independentes dos comentários anteriores. |

## Síntese dos sete itens da anotação final

| Item | Recomendação | Atendimento |
|---|---|---|
| 1 | Definir a ferramenta SAST adequada ao alvo. | **Atendido:** Semgrep, compatibilidade JS/TS, versão e perfil fixado; não há obrigação de demonstrar superioridade sobre todos os SAST. |
| 2 | Informar framework, cobertura e ferramentas de testes. | **Atendido no escopo funcional:** ferramentas, tipos, seleção por arquivo e baseline descritos. Não houve demonstração de cobertura integral da aplicação. |
| 3 | Explicar elaboração dos testes e preservação funcional. | **Atendido com ressalva:** testes adicionais e exemplo concreto estão descritos, e o aceite é limitado às verificações. D continua uma decisão central a defender. |
| 4 | Condensar descrições repetidas. | **Parcial/editorial:** houve reorganização, mas ainda cabem cortes locais. |
| 5 | Tabela de produtos e versões. | **Parcial:** tabela existente, porém incompleta em relação às ferramentas citadas. |
| 6 | Modelo de dados com atributos e relações. | **Pendente quanto ao produto solicitado:** há organização de arquivos, mas não o modelo de dados. |
| 7 | Analisar ciclos, linhas modificadas e severidade. | **Parcial:** tentativas e primeiros aceites por estratégia estão em RES:154–236; casos explicativos estão em RES:476. Não há análise sistemática do tamanho dos patches nem ponderação por severidade nos resultados apresentados. |

## Ajustes mínimos que responderiam às lacunas

### 1. Modelo de dados — prioridade média, lacuna demonstrada

**Pedido:** página 45 e item 6 da página 67: “tipo”, “chaves”, “campos” e “relação”.

**Local atual:** MET:444 e IMP:238. A árvore de pastas e a figura de nomenclatura não atendem integralmente a esse pedido específico.

**Proposta:** uma única figura compacta relacionando catálogo/caso, campanha, tentativa e artefatos, com identificadores reais e formatos JSON, JSONL, Markdown e patch conforme os arquivos efetivos. Um pequeno quadro de campos essenciais pode acompanhar a figura ou substituí-la se a orientadora aceitar. Não exige banco SQL nem mudança do armazenamento implementado. O desenho precisa respeitar o compartilhamento de casos entre campanhas, em vez de inventar uma hierarquia estrita de propriedade.

### 2. Tamanho dos patches e severidade — prioridade média, recomendações não concluídas

**Pedido:** item 7 da página 67.

**Local atual:** RES:154 já permite discutir em qual tentativa ocorreu o primeiro aceite; os exemplos de RES:476 vão além de R/F/M. Isso atende parte importante do pedido. Entretanto, não há tabela ou discussão sistemática de linhas adicionadas/removidas, nem resultado ponderado por severidade.

**Fonte de contraste:** a implementação possui cálculo opcional de `TRV-P`, mas os arquivos `metricas.json` das três campanhas finais registram `indisponivel`, com motivo `politica_pesos_ausente`. Ter a rotina não significa ter produzido a análise. Agrupar resultados por severidade também é diferente de ponderá-los.

**Proposta:** para o tamanho, uma tabela curta obtida dos patches arquivados, com regra explícita sobre linhas adicionadas/removidas e população selecionada, poderia atender sem nova campanha. Não se deve tratar número de linhas como qualidade ou eficiência por si só. Para a ponderação, a alternativa mínima é declarar que não foi adotada uma política de pesos e delimitar a interpretação. Atender integralmente à sugestão de ponderar exigiria justificar pesos e produzir uma análise complementar identificada como posterior; não cabe inventar pesos retroativamente como se fossem parte do desenho original.

### 3. Ferramentas e versões — prioridade média, documentação parcial

**Pedido:** página 55 e item 5 da página 67.

**Local atual:** MET:60, IMP:50 e IMP:111. Já há aplicação, Node.js, npm e Semgrep na tabela; Python aparece em prosa, e Vitest/TypeScript/Angular são citados na validação.

**Proposta:** completar a tabela existente com as principais ferramentas efetivamente usadas, suas funções e versões recuperáveis nos artefatos do ambiente. Não é necessário listar todas as dependências transitivas. Se alguma versão não estiver preservada, registrar a lacuna em vez de atribuir a versão instalada hoje. Não foram auditadas todas essas versões nesta revisão.

### 4. Falsos positivos e uso das classificações — prioridade média, explicação ainda indireta

**Pedido:** páginas 21 e 47.

**Local atual:** MET:163, MET:245 e RES:13. A triagem e o uso de CWE estão descritos, mas a pergunta sobre a necessidade de corrigir falsos positivos merece resposta direta.

**Proposta curta, sujeita à revisão dos autores:** “Os falsos positivos foram mantidos para observar o comportamento do pipeline diante dos alertas do SAST; seu eventual aceite não foi interpretado como correção de uma vulnerabilidade real.” Essa frase descreve o tratamento observado, sem afirmar que o prompt dispunha de uma instrução explícita para rejeitar falsos positivos. A tarefa comum consultada pede identificar e corrigir uma vulnerabilidade.

Também caberia explicitar que CWE orientou a recuperação/classificação e que não foram utilizadas pontuações CVSS para ponderar as métricas. Referências a CVE/NVD no referencial não implicam que essas bases tenham sido consultadas automaticamente pelo pipeline.

### 5. Preservação funcional — prioridade alta de interpretação, não ausência de testes

**Pedido:** páginas 13, 34, 41 e 67.

**Resposta que o trabalho sustenta:** foram usadas comparações com baseline, testes relacionados aos arquivos modificados, compilação, controles e testes adicionais. O teste do CAPTCHA consultado possui resultados esperados independentes do cálculo da aplicação, além de verificações de persistência e de aceitação/rejeição de respostas. Isso responde concretamente à preocupação da banca sobre apagar código para retirar alertas.

**Limite:** passar nessas verificações não prova preservação de toda funcionalidade. D permite que determinados testes falhem sem reprovar F; RES:123–152 mostra seu impacto. As composições de patches foram reprovadas funcionalmente. Portanto, a defesa deve explicar o alcance do aceite individual e essa reprovação conjunta, sem prometer o que os dados não demonstram.

**Proposta:** preservar as ressalvas atuais e preparar a justificativa de D com exemplos e documentação. Não foi proposta nem realizada ampliação desse trecho do TCC, respeitando a decisão anterior dos autores de mantê-lo conciso.

### 6. Prompts e concisão — prioridade baixa, melhoria de acesso

Os prompts completos já estão preservados e versionados no clone do repositório indicado pelo TCC. O requisito documental está substancialmente atendido. Uma referência direta a `config/prompts/roteiro_raciocinio_guiado.md` e aos prompts das campanhas ajuda o leitor a localizar a resposta à banca. Não é necessário acrescentar várias páginas de prompts nem criar outra seção extensa.

A condensação do referencial/objeto é uma sugestão editorial. Priorizar pequenas substituições e remissões, mantendo os elementos que explicam escolhas experimentais, como a exclusão dos Coding Challenges.

## Evidências e limites da revisão

- PDF examinado: 72 páginas, 30 anotações nativas — 28 destaques com conteúdo e duas notas de texto. Foram lidos os conteúdos das 30 anotações e os trechos associados; a página final de recomendações também foi renderizada e inspecionada. SHA-256: `b4bee9adac2882d349c4b92d3e67e995b6360e5168bb17f822154905974a166b`.
- Escrita: HEAD `db6ee2437868620122bae6e986a6d438e8e77ea0`, árvore limpa antes da criação deste parecer. Conferência dirigida dos seis arquivos ativos, com foco nos pontos assinalados; não se usou o Markdown antigo como substituto do LaTeX atual.
- Experimento: HEAD `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`. Coincide com as verificações recentes das notas; é posterior ao SHA inicial `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`. A consulta atual não reescreveu as evidências históricas.
- Fontes reabertas: `config/execucao_docker_78.yaml`, `config/mapa_testes_relacionados_v9.yaml`, `config/prompts/roteiro_raciocinio_guiado.md`, `knowledge_base/injection.md`, `src/pipeline/etapas/e04_prompt/montagem.py`, `tests/functional/juice_shop/captcha_arithmetic.test.ts` e `src/pipeline/etapas/e09_metricas/calculo.py`.
- Foram contados 283, 277 e 274 prompts nas campanhas finais do GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna, respectivamente, sob `outputs/resultados_finais/OWASP_20261111_V2/<campanha>/campanha/prompts/`. A presença de arquivos rastreados foi verificada com Git. Foram abertos os prompts P2/P3 do caso `AMP95adf572d3c6677f` da campanha `AMP_REAL_20261106T151004Z_f49ac0d2`. Isso verifica preservação no clone consultado, sem auditar a disponibilidade remota de cada arquivo no GitHub.
- Foram consultados os resultados `TRV-P` dos três `outputs/rris/<campanha>_METRICAS/metricas.json`, todos indisponíveis por ausência de política de pesos. Não se recalcularam todas as métricas nem se realizou nova análise de linhas modificadas.
- Não foram executados experimentos, chamadas a LLMs, SAST ou testes. Não houve validação de todas as referências bibliográficas, compilação integral ou avaliação da paginação do PDF final do TCC2. Não foi inferida aprovação da banca a partir deste parecer.

**Arquivo produzido:** somente este parecer. O registro `ajustes-tcc2-overleaf.md` permanece inalterado porque não houve alteração no TCC.
