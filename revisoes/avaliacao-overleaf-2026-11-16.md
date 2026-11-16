# Avaliação do TCC — versão Overleaf de 16/11/2026

Parecer sobre os seis capítulos ativos de `TCC2-OVERLEAF/tcc.tex`, resumo, abstract e elementos de apoio. Revisão científica e textual com a skill `tcc2-revisar`. Os arquivos do TCC e o registro `ajustes-tcc2-overleaf.md` não foram alterados.

**Avaliação geral:** o trabalho tem um núcleo experimental consistente e uma contribuição adequada a um TCC em Engenharia de Software. A implementação, a organização das evidências e a distinção entre aceite individual e integração são os principais pontos fortes. A versão atual já apresenta uma pesquisa concluída. Ainda exige ajustes de precisão e explicitação de decisões metodológicas antes de ser considerada pronta para entrega.

A contribuição sustentada é a implementação e avaliação de um processo de geração e verificação automatizada de propostas, incluindo a identificação de seus limites. A ausência de aprovação funcional das composições é um resultado relevante: demonstra que aceitar alterações isoladas não assegura uma versão integrada funcional.

## Avaliação por parte

| Parte | Avaliação | Prioridade |
|---|---|---|
| Resumo e abstract | Contextualizados, concisos e coerentes com o estudo; apresentam a limitação da integração. Não precisam de um ranking numérico para cumprir sua função. | Manter o formato atual. |
| Introdução | Problema pertinente, objetivos claros, Q1–Q5 presentes e organização atualizada. | Delimitar melhor o sentido de “influência” em Q2 e de “fluxo iterativo”. |
| Referencial teórico | Boa cobertura conceitual, mas contém linguagem de proposta, afirmações excessivas e uma citação inadequada. | Revisão prioritária de precisão e da relação com o método realizado. |
| Metodologia | Explica unidades, critérios, ausências de medição, sequência e populações. | Tornar os critérios de D verificáveis no documento e esclarecer os casos em testes. |
| Implementação | Concreta, compreensível e vinculada a artefatos. | Corrigir a interpretação de `keyServer.ts` e limitar a promessa de equivalência com Docker. |
| Resultados e discussão | Parte mais madura: separa métricas, populações, sensibilidade e avaliação conjunta; responde às cinco perguntas. | Fortalecer a interpretação científica e reduzir repetições de valores. |
| Considerações finais | Concisas, compatíveis com os resultados e com trabalhos futuros pertinentes. | Acrescentar, se desejado, uma breve delimitação a uma aplicação e uma campanha por modelo. |

## Achados prioritários

### 1. Alta — critérios do conjunto D insuficientemente explícitos no TCC

**Natureza:** lacuna metodológica; não demonstra erro nos totais.

**Local:** `editaveis/consideracoes.tex:349–368`; sensibilidade em `editaveis/resultado-discussoes.tex:130–155`; histórico mencionado em `:622`.

**Problema:** o texto explica por que testes dependentes de vulnerabilidades precisam de tratamento próprio, mas remete a “critérios documentados” sem apresentar claramente todas as regras de inclusão. Essa classificação tem efeito central: no GPT-5.6 Luna, a mesma população passa de 22 para 51 aceites ao trocar a definição funcional. A ordem dos modelos também muda.

**Fonte de contraste:** `tcc2-llm-sast-juiceshop/docs/criterios_conjunto_d.md`, no SHA indicado ao final. O documento distingue (a) desafio resolvido, (b) ataque com resposta de sucesso, (c) evidência de interpretação da carga, (d) asserção que exige o mecanismo inseguro, vinculada a determinados casos, e (e) teste cuja finalidade é a própria falha, com alcance geral. O critério (e) foi acrescentado após uma campanha descartada. A discussão atual reconhece essa evolução, o que deve ser preservado.

**Correção proposta:** incluir uma tabela curta dos cinco critérios, exemplos de inclusão e exclusão, distinção entre alcance por caso e geral, responsáveis pela classificação e referência versionada para a lista completa. Explicitar quais testes adicionais protegem os comportamentos legítimos. Uma revisão independente fortaleceria a validade; sua ausência deve continuar declarada.

### 2. Alta — escopo e restrição de não alterar testes precisam ser conciliados

**Natureza:** inconsistência demonstrada entre a descrição simplificada e os casos efetivamente avaliados.

**Local:** `editaveis/consideracoes.tex:127` e `:197`.

**Problema:** o escopo é apresentado como código das funcionalidades, e os prompts orientam a não modificar testes. Entretanto, o catálogo inclui três ocorrências em dois arquivos de teste: `app.guard.spec.ts` e `last-login-ip.component.spec.ts`. Os registros contêm propostas aceitas que modificam esses arquivos: dois casos no GPT-5.6 Luna e três no GPT-6 Luna. Os três casos são rotulados como falsos positivos na triagem.

**Fontes de contraste:** catálogo ampliado; registros e patches das campanhas finais; `src/pipeline/etapas/e04_prompt/montagem.py:46–54`, que efetivamente inclui a proibição de alterar testes. Casos: `AMPdbe817f9e31f0aa0`, `AMP986bde724bde5588` e `AMP755998f61209381a`.

O caderno de laboratório, na entrada de 02/11/2026 “Fechamento dos seis casos restantes do catálogo”, documenta avaliadores externos para esses arquivos, com inventário, mutações e grupo Angular independente. Portanto, não se pode concluir que os testes modificados tenham sido a única evidência da própria validade. A limitação está na contradição da instrução e na explicação incompleta do recorte no TCC.

**Correção proposta:** declarar a presença desses três casos, a tensão com a restrição do prompt e o mecanismo independente de avaliação. Discutir seu significado no processamento de falsos positivos. Não excluir silenciosamente registros nem reescrever a campanha como se a restrição tivesse sido cumprida em todas as tentativas.

### 3. Alta — exemplo de path traversal afirma mais do que a evidência permite

**Natureza:** divergência demonstrada de interpretação.

**Local:** `editaveis/elementosdotexto.tex:95`, também anunciado na abertura do capítulo.

**Problema:** o texto afirma que o trecho de `routes/keyServer.ts` caracteriza uma vulnerabilidade de path traversal. O catálogo registra expressamente: “e exposicao de chaves, nao prova de path traversal”. O alerta e sua CWE não bastam para comprovar exploração por travessia de diretórios.

**Fonte de contraste:** `outputs/catalogos/ampliado_v1/catalogo_issues.json`, caso `AMP95adf572d3c6677f`, campo `justificativa_auditoria`.

**Correção proposta:** apresentar como alerta de possível path traversal emitido pela regra, explicar o risco identificado pela triagem e limitar o resultado à remoção do alerta com aprovação das verificações. O patch pode continuar como exemplo do fluxo, sem afirmar comprovação de exploração ou eliminação de toda exposição de chaves.

### 4. Média — referencial ainda apresenta decisões como propostas futuras

**Natureza:** desalinhamento textual demonstrado.

**Local:** `editaveis/aspectosgerais.tex:77–81` e `:146–148`.

**Problema:** permanecem expressões como “será utilizada”, “poderão orientar” e “será analisado”, inclusive para possibilidades de few-shot que não correspondem à descrição dos tratamentos P1–P4. É adequado apresentar técnicas possíveis na teoria; o problema surge quando são atribuídas a “este trabalho” sem distinguir o que foi executado.

O texto também aproxima o pipeline de fluxos de autorreparo que reutilizam o feedback da tentativa anterior. A montagem consultada produz cada prompt a partir do código original, do alerta e dos blocos da estratégia; não incorpora respostas ou diagnósticos da tentativa anterior. Os testes decidem a continuidade da sequência, mas isso não equivale a entregar seus erros ao modelo para refinar o patch anterior.

**Fontes de contraste:** método P1–P4, restauração das worktrees e `src/pipeline/etapas/e04_prompt/montagem.py:159–195`.

**Correção proposta:** separar exposição conceitual das decisões do estudo e esclarecer o sentido de iteração: novas tentativas com estratégias diferentes sobre o código original. Manter a descrição de feedback de outros trabalhos como característica deles.

### 5. Média — atribuição bibliográfica inadequada sobre fidelidade do CoT

**Natureza:** referência incompatível com a afirmação que acompanha.

**Local:** `editaveis/aspectosgerais.tex:59`.

**Problema:** a ressalva sobre a cadeia textual não representar fielmente o processo interno é acompanhada de `lester_power_2021`. O artigo é sobre aprendizado de soft prompts com modelos congelados, conforme o registro e resumo primários consultados na [ACL Anthology](https://aclanthology.org/2021.emnlp-main.243/).

**Correção proposta:** utilizar uma fonte específica sobre fidelidade de explicações de CoT. A mesma referência de Lester permanece pertinente à distinção entre prompt engineering e prompt tuning na linha 47. Não se trata das chaves duplicadas que o autor pediu para restaurar.

### 6. Média — contribuição comparativa exige delimitação firme

**Natureza:** limite do desenho, já reconhecido em boa parte do texto.

**Locais:** Q2 em `editaveis/introducao.tex:34`; limitações em `consideracoes.tex:485`; resposta em `resultado-discussoes.tex:590`; comparação de modelos em `:602`.

**Avaliação:** a resposta atual à Q2 corretamente descreve acréscimos na sequência. Não há erro em relatar mais aceites ao continuar as tentativas. Porém, isso não isola o benefício do raciocínio guiado ou do RAG: as populações são diferentes, diagnóstico e documento entram juntos e não existe comparação com repetir P1 sob o mesmo orçamento de chamadas. A suposição de que uma estratégia posterior preservaria os sucessos anteriores também não foi verificada.

Na comparação dos modelos, a diferença de dois casos entre os Luna é descritiva. Uma campanha por modelo não permite estimar a estabilidade dessa ordem. Casos da mesma aplicação, inclusive do mesmo arquivo e regra, também compartilham características; o número de tentativas não equivale a réplicas independentes.

**Correção proposta:** formular o objetivo de comparação de prompts em termos de contribuição observada na sequência e preservar “nas campanhas avaliadas” ao indicar preferências entre modelos. Não é necessário realizar novos experimentos para apresentar corretamente o estudo existente.

## Melhorias de discussão e apresentação

- **Trabalhos relacionados:** `aspectosgerais.tex:153–163` resume estudos, mas explicita pouco o que este trabalho acrescenta. Uma tabela com alvo, contexto fornecido, uso de feedback, validação funcional e avaliação conjunta ajudaria a mostrar a contribuição sem sugerir ineditismo não demonstrado.
- **Linguagem de garantias:** revisar “impede que etapas importantes sejam omitidas” (`aspectosgerais.tex:57`), “máxima eficácia” (`:161`) e avaliar se a LLM “compreende a causa” (`:120`). As verificações observam propostas e comportamentos; não medem compreensão interna nem asseguram que o roteiro seja seguido corretamente.
- **Docker:** `elementosdotexto.tex:48` afirma que qualquer computador executa nas mesmas condições. O empacotamento padroniza software e dependências; hardware, rede, recursos disponíveis e serviço remoto ainda variam. Ajustar especialmente porque o trabalho compara tempos.
- **Reprodutibilidade:** reunir em um quadro/apêndice os identificadores exatos dos modelos e parâmetros, tarifas efetivamente utilizadas, recursos da máquina e revisões dos artefatos. Os custos atuais estão corretamente identificados como calculados, sem conferência de faturamento.
- **Resultados:** é possível condensar explicações que repetem as tabelas. Priorizar interpretações: por que remover o alerta foi insuficiente, o que muda com D e o que a reprovação conjunta revela. O texto já distingue essas dimensões; convém valorizá-las na defesa.
- **Aprovação:** `editaveis/informacoes.tex:19` ainda contém 16 de julho de 2026, enquanto as campanhas são de novembro. Confirmar os dados da entrega atual, sem presumir nova data ou aprovação.
- **Bibliografia:** permanecem cinco chaves duplicadas: `owasp_top10_2025_intro`, `stackoverflow_survey_ai_2025`, `openai_gpt5`, `openai_introducing_gpt5_2025` e `owasp_api_bola_2023`. É uma pendência técnica conhecida, preservada conforme solicitação do autor; nenhuma entrada foi alterada nesta revisão.

## Perguntas para preparar a defesa

1. O que uma correção “válida” significa no estudo, e o que os critérios não demonstram?
2. Como foi decidido que um teste podia falhar sem representar regressão funcional legítima?
3. Por que falsos positivos e três casos em arquivos de teste participaram da campanha?
4. Como distinguir o benefício de mudar o prompt do benefício de simplesmente tentar novamente?
5. Por que propostas aceitas isoladamente falharam quando reunidas, e até onde os dados permitem explicar as causas?
6. O que foi demonstrado sobre cada modelo nesta campanha e o que dependeria de repetições?

## Verificações e limites deste parecer

Fonte experimental consultada: `../tcc2-llm-sast-juiceshop`, HEAD `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`. As notas iniciais dos capítulos 3–5 citam `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`; o histórico posterior inclui a classificação complementar e reorganização dos artefatos. O HEAD é o mesmo consultado na revisão de 15/11. As fontes atuais foram reabertas, sem usar apenas os pareceres anteriores como evidência.

Campanhas verificadas:

| Modelo | Execução | Registros | Tentativas até o primeiro aceite | Casos aceitos | Aceitos entre os confirmados | Alertas na avaliação conjunta |
|---|---|---:|---:|---:|---:|---|
| GPT-4.1 mini | `AMP_REAL_20261106T151004Z_f49ac0d2` | 283 | 241 | 38/78 | 32/55 | 78 → 40 |
| GPT-5.6 Luna | `AMP_REAL_20261106T125801Z_0eb68fe4` | 277 | 223 | 51/78 | 39/55 | 78 → 23 |
| GPT-6 Luna | `AMP_REAL_20261106T105533Z_aa697342` | 274 | 221 | 49/78 | 36/55 | 78 → 31 |

Foi feita leitura e recontagem dos JSONL em `outputs/campanha_docker/<execução>/resultados_consolidados/execucoes.jsonl`, agrupando casos e estratégias até o primeiro aceite com proposta aplicada e R=F_criterio=M=1. Foram conferidos os primeiros aceites por estratégia, os aceites confirmados, a soma dos custos e a média das latências. Os totais coincidem com o LaTeX. Os CSVs de métricas e os arquivos de RRIS e validação funcional também foram consultados: nenhum dos três conjuntos recebeu aprovação funcional. **Sem achados numéricos nessas conferências.**

Também foram abertos o catálogo, o documento dos critérios de D, trechos do protocolo e do caderno de laboratório, a montagem de prompts e um patch aceito que altera arquivo de teste. Essa amostragem identifica inconsistências específicas; não constitui auditoria integral dos patches ou demonstração independente da segurança das correções.

O rastreamento estático encontrou 20 arquivos TeX ativos, nenhuma entrada de arquivo ausente, nenhuma chave citada sem registro, nenhum label explícito duplicado e todas as nove imagens referenciadas presentes. `LastPage` é fornecido pelo pacote carregado. As cinco duplicações bibliográficas permanecem.

Uma tentativa de compilação com `pdflatex`, em cópia temporária fora do projeto e com execução de shell desabilitada, parou porque o ambiente local não possui `abntex2.cls`. Isso é uma limitação do ambiente consultado, não demonstra falha no Overleaf. Não foram avaliados o PDF final, paginação, legibilidade das figuras reduzidas ou conformidade integral ao template institucional. A bibliografia teve conferência pontual, não auditoria de todas as fontes.

Não foram executadas campanhas, chamadas a modelos, Semgrep ou testes do alvo. O único arquivo produzido no repositório foi este parecer.
