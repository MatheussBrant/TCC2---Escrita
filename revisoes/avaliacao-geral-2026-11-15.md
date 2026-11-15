# Avaliação geral dos seis capítulos — 15/11/2026

Parecer solicitado pelos autores, elaborado com o roteiro local `tcc2-revisar`. Os capítulos não foram alterados. A avaliação distingue divergências demonstradas, limitações metodológicas e sugestões editoriais; não equivale a uma auditoria integral dos patches ou da bibliografia.

## Avaliação geral

O trabalho apresenta uma pesquisa implementada, com perguntas explícitas, critérios de avaliação definidos, registros experimentais e discussão dos resultados. A estrutura introdução → fundamentação → metodologia → implementação → resultados → conclusão funciona. A contribuição mais convincente é a construção e avaliação de um processo que distingue geração, aplicação, remoção de alertas, comportamento verificado pelos testes e integração das alterações.

A parte empírica está mais madura que a fundamentação e a formulação de algumas conclusões. Os ajustes prioritários são delimitar a resposta à Q2, tornar a classificação funcional mais auditável, corrigir uma divergência no exemplo de implementação e revisar a correspondência entre afirmações e referências. Não identifiquei, na amostra numérica conferida, motivo para descartar as campanhas ou recalcular as métricas com outra definição. A revisão sugerida é principalmente de sustentação e interpretação.

## Pontos fortes

- Q1–Q5 reaparecem explicitamente nos resultados, e a conclusão é compatível com os principais achados.
- R, F e M têm definições operacionais; as medições ausentes não são confundidas com reprovações observadas.
- A distinção entre taxa por caso e por tentativa está clara e exemplificada.
- Os 78 alertas e os 55 confirmados na triagem são separados. O texto reconhece a participação de falsos positivos.
- A análise de sensibilidade de F expõe uma dependência importante dos resultados, inclusive a mudança do modelo com maior TRV.
- A avaliação conjunta é uma contribuição relevante: reduzir alertas não bastou para aprovar o conjunto nos testes.
- O exemplo do CAPTCHA explica de forma concreta por que remover um padrão pode produzir uma alteração inadequada.
- Código, contratos e dados arquivados permitem conferir as principais contagens.

## Achados prioritários

### 1. Alta — divergência demonstrada na caracterização do exemplo do capítulo 4

**Local:** `manuscrito/04-implementacao.md:83`, com repercussão na apresentação do caso nas linhas 5 e 253.

**Trecho:** o texto afirma que o código “caracteriza uma vulnerabilidade de path traversal”.

**Contraste:** no catálogo experimental, o caso `AMP95adf572d3c6677f` está classificado como confirmado, mas sua justificativa diz: “Rota publica serve arquivos de encryptionkeys por nome e server.ts ainda expoe listagem desse diretorio; e exposicao de chaves, nao prova de path traversal.” Fonte: `outputs/catalogos/ampliado_v1/catalogo_issues.json`, no SHA experimental indicado abaixo.

**Problema:** o manuscrito transforma o tipo de alerta em uma vulnerabilidade específica comprovada, enquanto a própria triagem distingue os dois. O aceite P3 está registrado e não foi contestado por esta revisão; a divergência é sobre o que foi demonstrado em segurança.

**Correção proposta:** apresentar o exemplo como “alerta de possível travessia de diretórios na entrega de arquivos”, explicar a justificativa da triagem e limitar o resultado à alteração aplicada e à aprovação em R/F/M. A exposição de chaves deve permanecer distinta da contenção do caminho. Não afirmar que o patch eliminou a exposição sem evidência específica.

### 2. Alta — Q2 promete uma comparação que o desenho responde apenas parcialmente

**Locais:** `01-introducao.md:33` e `:51`; `03-metodologia.md:375`; `05-resultados-discussao.md:97`, `:134` e `:341`.

**Problema:** “influenciam a taxa” e “comparar seu impacto” sugerem isolamento do efeito das estratégias. Os dados mostram o ganho acumulado de uma política sequencial: P2–P4 recebem casos remanescentes, P3 acrescenta diagnóstico e documentação simultaneamente e não há controle que repita P1 com o mesmo orçamento de tentativas. Portanto, mais aceites não demonstram quanto decorre da mudança do prompt, do contexto ou de novas oportunidades de geração.

**Contraste:** a própria metodologia reconhece esse limite. Os CSVs confirmam os ganhos da sequência e a contribuição incremental de P3. O montador `src/pipeline/etapas/e04_prompt/montagem.py` recebe caso, cópia de trabalho e estratégia e monta os blocos previstos; não incorpora, nessa função, o diagnóstico da tentativa anterior.

**Correção proposta:** enquadrar a pergunta como contribuição de cada estratégia dentro da sequência, ou conservar Q2 e declarar explicitamente que sua resposta é parcial e descritiva. Uma formulação possível é: “Qual é a contribuição incremental das estratégias P1–P4 para o aceite de casos no fluxo sequencial avaliado?” Na resposta, manter o achado positivo e acrescentar uma frase sobre seu alcance. Não é necessário refazer o experimento para relatar corretamente o que foi medido.

**Observação:** “fluxo iterativo” pode ser mantido se definido como repetição com mudança de estratégia sobre o código original. Evitar sugerir que o pipeline refina o patch anterior com feedback dos testes, como alguns trabalhos relacionados fazem.

### 3. Alta — falta tornar os critérios do conjunto D suficientemente auditáveis no manuscrito

**Locais:** `03-metodologia.md:267–279`; `05-resultados-discussao.md:83–93` e `:371`.

**Problema:** o texto explica a ideia do conjunto D, mas não apresenta com precisão seus cinco critérios, a vinculação de alguns testes a casos específicos e a evolução da classificação. Essa decisão é central: no GPT-5.6 Luna, os aceites na mesma população passam de 22 para 51; ela também muda o modelo com maior TRV. Um leitor precisa entender como se distingue um teste dependente da falha de um teste legítimo que apenas deixa de passar após uma alteração.

**Contraste:** `docs/criterios_conjunto_d.md` registra os critérios (a) a (e). O critério (d), de 05/11, é ligado ao caso; o (e), de 06/11, é geral e foi acrescentado após uma campanha descartada. O caderno de laboratório documenta a revisão após observar resultados, a criação de testes de comportamento legítimo e, no registro de 05/11, a necessidade de conferência manual dos aceites. O manuscrito informa que os autores não inspecionaram manualmente os patches. Essa diferença precisa ser reconciliada como evolução do procedimento ou limitação, sem presumir que a revisão foi realizada.

**Correção proposta:** acrescentar uma tabela curta com critério, exemplo, alcance e justificativa; remeter a um apêndice versionado com a lista completa. Informar quando a versão final foi fixada em relação às campanhas analisadas e quem classificou/revisou os testes, conforme evidência disponível. Explicar o alcance dos testes adicionais e reconhecer a ausência da revisão manual prevista no registro histórico. Preservar a tabela de sensibilidade; ela é um ponto forte.

**Natureza do achado:** insuficiência de documentação e risco de validade de construto, não demonstração de que a classificação ou os números estejam errados. Não há base nesta revisão para acusar manipulação dos resultados.

### 4. Alta — referência inadequada para uma afirmação sobre CoT

**Local:** `02-referencial-teorico.md:53`.

**Problema:** a afirmação de que a cadeia textual de raciocínio pode não representar fielmente o processo do modelo é atribuída a Lester, Al-Rfou e Constant (2021). O trabalho citado trata de treinamento de soft prompts com os parâmetros do modelo congelados, e não sustenta diretamente essa afirmação sobre fidelidade de CoT.

**Fonte de contraste:** [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/html/2104.08691v2), texto consultado em 15/11/2026.

**Correção proposta:** substituir por pesquisa diretamente pertinente à fidelidade das explicações ou reformular o trecho como delimitação operacional do presente estudo, sem atribuição bibliográfica inadequada. A utilização de Lester na distinção de prompt tuning na linha 41 é pertinente.

### 5. Média — os 55 “confirmados” precisam de procedência mais clara

**Locais:** `03-metodologia.md:113–117`; `05-resultados-discussao.md:13` e `:240`; `06-consideracoes-finais.md:5`.

**Problema:** o texto esclarece que a confirmação veio da triagem e que os autores revisaram os falsos positivos, mas não permite identificar com a mesma clareza autoria, procedimento e revisão das classificações positivas. O recorte confirmado é usado para sustentar comparações mais próximas de “vulnerabilidades”.

**Contraste:** catálogo e notas registram as justificativas e a distinção entre revisão dos 21 falsos positivos e origem dos demais rótulos. A mera presença de justificativa versionada não equivale a validação independente.

**Correção proposta:** informar o procedimento e a responsabilidade efetivamente documentados. Manter “classificados como confirmados na triagem”, inclusive na síntese, sem converter o grupo em verdade de referência independente. A divergência do caso keyServer reforça a importância dessa distinção. Uma auditoria adicional seria uma melhoria empírica, não algo já demonstrado pelo material.

### 6. Média — faltam detalhes compactos para reproduzir as comparações de custo e tempo

**Locais:** `03-metodologia.md:119–133`; `04-implementacao.md:139–141`; `05-resultados-discussao.md:167–195`.

**Problema:** o texto informa temperatura, limite de tokens e esforço de raciocínio, mas não apresenta a seed 42 registrada no contrato do GPT-4.1 mini, nem reúne os identificadores exatos dos modelos, tarifas utilizadas e características da máquina das campanhas. Docker padroniza parte do ambiente, mas CPU, memória, concorrência e infraestrutura influenciam o tempo observado.

**Contraste:** `outputs/campanha_docker/AMP_REAL_20261106T151004Z_f49ac0d2/contrato_execucao.json`, campo `inferencia`, contém seed e preços. As métricas arquivadas informam custo calculado, sem comprovação de faturamento, corretamente reconhecida na Tabela 7.

**Correção proposta:** incluir quadro de configuração ou apêndice com IDs, parâmetros enviados e não enviados, tarifas e unidade, origem/data dos preços e ambiente físico disponível nos registros. Não inventar informação faltante. Manter a comparação como resultado observado de uma campanha por modelo, sem promover a diferença de dois casos entre os Luna a superioridade estável. Não é necessário acrescentar teste estatístico apenas para dar aparência de rigor.

### 7. Média — o referencial precisa explicitar melhor a lacuna e a contribuição específica

**Locais:** `02-referencial-teorico.md:143–153`; `05-resultados-discussao.md:355–361`.

**Problema:** a seção de trabalhos relacionados resume estudos, mas a transição para a contribuição própria permanece genérica. O leitor pode concluir que a contribuição é apenas combinar LLM, RAG e SAST, combinação já presente nos estudos citados. A discussão com a literatura é curta em relação ao espaço dedicado às definições.

**Correção proposta:** comparar os estudos por alvo, geração/reparo, contexto, feedback, validação funcional, avaliação conjunta e limites. Explicitar o recorte próprio: aplicação com múltiplos módulos, testes selecionados, particularidades do Juice Shop, análise de sensibilidade funcional, comparação entre configurações de modelos e integração de patches. Não alegar ineditismo sem revisão suficiente.

**Verificação bibliográfica adicional:** os 76%, 15% e 63% atribuídos a Khan são compatíveis com o resumo da [versão consultada](https://arxiv.org/abs/2409.18395v2). O resultado de 96% de Sriram aparece no resumo para DeepSeek; convém informar essa condição em vez de deixá-lo como resultado genérico do método. [Fonte](https://arxiv.org/abs/2601.00509v1). Isso não valida as demais atribuições bibliográficas do capítulo.

## Sugestões de precisão e redação

1. **História do Transformer — `02-referencial-teorico.md:7`.** O registro de Vaswani distingue submissão em 2017 e revisão em 2023. A referência a 2023 pode identificar a versão consultada, mas a origem da arquitetura é de 2017. Explicitar essa diferença, sem substituir automaticamente todos os anos bibliográficos. [Registro primário](https://arxiv.org/abs/1706.03762).
2. **Generalizações no referencial — linhas 51, 111 e 151.** “Impede que etapas importantes sejam omitidas”, “se ela compreende a causa” e “máxima eficácia” são mais fortes que as evidências apresentadas. Preferir “orienta”, “adequação da correção à causa” e resultados delimitados às condições do estudo citado.
3. **SonarQube versus Semgrep — capítulo 2, linhas 133–135.** Ready/Beta/Deprecated são apresentados como propriedades gerais das regras, embora a fonte seja SonarQube e o experimento use Semgrep. Identificar explicitamente o exemplo e sua relevância, ou concentrar o espaço nas propriedades utilizadas no experimento.
4. **Cobertura do OWASP — capítulo 2, linhas 99–109.** A10 é desenvolvida, mas não tem casos; A02, A06 e A08 aparecem nos resultados sem explicação equivalente. Uma tabela das categorias de 2025 com indicação das avaliadas tornaria a conexão mais clara.
5. **Garantia de ambiente — `04-implementacao.md:41`.** “Qualquer computador ... nas mesmas condições” excede o que o uso de Docker sustenta e conflita com a ressalva de `03-metodologia.md:373`. Descrever padronização das versões e dependências, mantendo as condições de plataforma e recursos.
6. **Repetições.** Encurtar a retomada dos mesmos resultados em 5.2, 5.4, 5.8, 5.10 e capítulo 6. Manter em 5.8 a resposta direta às perguntas; reservar 5.10 para alcance e continuidade. Reduzir expressões repetidas como “A conclusão é que” e comentários que apenas leem as tabelas.
7. **Capítulos 3 e 4.** O método está detalhado, mas pode evitar repetir regras de execução e definições já estabelecidas. O capítulo 4 funciona melhor quando explica decisões concretas e dificuldades da implementação. O parágrafo sobre âncoras/indentação é candidato a condensação ou apêndice parcial.
8. **Cronograma.** A seção 3.15 distingue corretamente planejamento e execução. Ainda assim, avaliar sua utilidade no corpo da monografia concluída, conforme exigência institucional; não é um erro de resultado.
9. **Pendências formais.** Há marcação explícita de captura do painel em `04-implementacao.md:276`. As referências contêm duplicações, “Citado na página” herdado e um URL com espaço em `http: //`; o capítulo 2 contém “ests trabalhos”. Revisar numeração local das figuras/tabelas na integração. Não foi conferida conformidade ABNT.
10. **Conclusão.** Os cinco parágrafos são suficientes para uma conclusão concisa e não introduzem resultados centrais novos. Acrescentar uma frase que recorde aplicação única/campanha única e a dependência da definição funcional daria maior autonomia ao capítulo. A reprovação conjunta deve permanecer visível: é parte da contribuição científica.

## Avaliação por capítulo

| Capítulo | Avaliação | Prioridade de ajuste |
|---|---|---|
| 1 — Introdução | Problema, objetivos e perguntas estão claros; o resumo do método está alinhado ao realizado. | Delimitar Q2 e tornar a contribuição específica mais explícita. |
| 2 — Referencial | Cobertura ampla, mas precisa de revisão crítica das fontes e maior ligação com o experimento. | Corrigir citação de CoT, calibrar afirmações, comparar trabalhos e alinhar categorias. |
| 3 — Metodologia | É um dos pontos fortes; define unidades, medições ausentes, parada e populações. | Documentar D, procedência da triagem e parâmetros de forma compacta e auditável. |
| 4 — Implementação | Explica bem isolamento, aplicação e rastreabilidade; o exemplo facilita a leitura. | Corrigir caracterização do exemplo, moderar garantia sobre Docker e concluir as figuras. |
| 5 — Resultados | É a parte mais convincente: contagens explícitas, sensibilidade, exemplos e avaliação conjunta. | Delimitar Q2, aprofundar interpretação e reduzir repetição; manter diferenças descritivas. |
| 6 — Considerações finais | Conciso e coerente com o capítulo 5. | Acrescentar uma frase sobre o alcance empírico e preservar o sentido operacional do aceite. |

## Perguntas prováveis de banca

- Por que manter falsos positivos no experimento, e o que significa aceitar uma alteração nesses casos?
- Quem definiu o conjunto D e como impedir que ele exclua regressões legítimas?
- O que permite atribuir os aceites adicionais ao prompt se houve mais tentativas e populações diferentes?
- O pipeline usa o feedback da tentativa anterior ou apenas muda a estratégia sobre o código original?
- Dois casos de diferença sustentam uma preferência geral entre modelos com apenas uma campanha?
- Por que patches aprovados individualmente falharam em conjunto, e até onde a causa foi investigada?
- Qual é a contribuição específica em relação aos fluxos já publicados?

## Evidências e limites da revisão

Foram lidos os seis capítulos, as referências locais e documentos de orientação; planos e notas foram consultados como apoio, incluindo atualizações posteriores às primeiras versões. As fontes experimentais foram abertas por amostragem, com leitura do catálogo, CSVs das três campanhas, métricas consolidadas, contrato do mini, montador de prompts, critérios D, trechos do protocolo e caderno de laboratório.

O HEAD experimental consultado foi `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`, sem alterações indicadas por `git status --short`. As primeiras notas usam `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`; entre essas revisões há inclusão da classificação OWASP e mudanças de consolidação/publicação associadas. A descrição posterior da classificação no manuscrito está coerente com essa evolução; não foi tratado o primeiro SHA como estado atual.

| Modelo | Registros / população principal | Aceites / confirmados aceitos | Aceites P1/P2/P3/P4 | Alertas antes → depois | Patches aplicados / conflitos |
|---|---|---|---|---|---|
| GPT-4.1 mini | 283 / 241 | 38 / 32 | 16 / 4 / 15 / 3 | 78 → 40 | 34 / 4 |
| GPT-5.6 Luna | 277 / 223 | 51 / 39 | 18 / 5 / 25 / 3 | 78 → 23 | 43 / 8 |
| GPT-6 Luna | 274 / 221 | 49 / 36 | 21 / 5 / 18 / 5 | 78 → 31 | 40 / 9 |

Também foram recontados R/F/M e os aceites nas três definições de F. Os valores centrais conferidos coincidem com o manuscrito. Custo total, tokens, duração e reprovação conjunta foram confrontados com os consolidados arquivados. O resumo dos cálculos e os hashes das fontes estão em [conferencia.json](../evidencias/avaliacao-geral-2026-11-15/conferencia.json).

Não foram executados modelos, campanhas, SAST ou testes do alvo. Não foram auditados todos os patches, reproduzidas as chamadas, verificados faturamento ou disponibilidade comercial dos modelos, revisadas todas as referências, renderizadas todas as figuras ou conferida a versão LaTeX. A constatação de consistência numérica não demonstra, por si só, segurança dos patches. Nenhuma fonte indispensável à amostra escolhida esteve ausente.

Prioridade sugerida: corrigir os achados 1 e 4; alinhar Q2; documentar D e triagem; fortalecer trabalhos relacionados; completar parâmetros, figuras e revisão editorial. Essas mudanças melhoram a defesa do trabalho preservando o experimento efetivamente realizado.
