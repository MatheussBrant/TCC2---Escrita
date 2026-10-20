# Plano de capítulos e features de escrita

A redação está dividida em cinco capítulos, oito features de conteúdo, duas
entregas complementares e uma integração final. Cada tarefa tem uma especificação executável por uma LLM no
[índice de features](../features/README.md), com escopo, fontes, pasta exclusiva,
entregáveis e critérios de aceitação. A estrutura é uma base de trabalho,
ajustável ao template e às orientações institucionais efetivamente fornecidas.

## Estrutura da monografia

| Capítulo | Feature | Pergunta que a parte deve responder |
|---|---|---|
| 1. Introdução | [F01](../features/01-introducao/README.md) | Qual problema foi investigado, com quais perguntas, objetivos e recorte? |
| 2. Referencial teórico | [F02](../features/02-fundamentacao/README.md) + [F03](../features/03-trabalhos-relacionados/README.md) | Quais conceitos e trabalhos anteriores sustentam o estudo? |
| 3. Metodologia e desenvolvimento | [F04](../features/04-metodologia/README.md) + [F05](../features/05-implementacao/README.md) | Como o experimento foi desenhado, implementado e avaliado? |
| 4. Resultados e discussão | [F06](../features/06-resultados/README.md) + [F07](../features/07-discussao/README.md) | O que foi observado sobre Q1–Q4, como interpretar e quais limites existem? |
| 5. Conclusão e trabalhos futuros | [F08](../features/08-conclusao/README.md) | Quais respostas e contribuições foram sustentadas, e o que permanece aberto? |

## Por que reduzir de oito para cinco

O sumário do TCC1 (páginas físicas 11–12 do PDF) tem cinco capítulos:
Introdução, Referencial Teórico, Metodologia, Prova de Conceito e Considerações
Finais. A seção 2.5 já reúne os trabalhos relacionados no referencial. A seção
1.5 (página impressa 16 / PDF 17) explica essa organização; o Capítulo 3 inclui
pipeline, métricas e armazenamento, além do desenho experimental. Conferência
no [texto extraído](../evidencias/coleta-validada/tcc1.txt) e no PDF identificado
pela [base comum](../features/BASE_COMUM.md).

No TCC2, reunir conceitos e relacionados preserva essa continuidade. Metodologia
e implementação descrevem o mesmo experimento e podem ficar em seções do
Capítulo 3. Resultados, interpretação e ameaças ficam em seções distintas do
Capítulo 4. A PoC torna-se antecedente da evolução, enquanto a avaliação no
Juice Shop ocupa o centro do trabalho. Cinco capítulos reduzem fragmentação e
repetições; não há evidência de uma exigência institucional de quantidade fixa.

Os IDs F01–F11 permanecem estáveis: **feature não corresponde obrigatoriamente
a capítulo**. F02/F03, F04/F05 e F06/F07 escrevem partes independentes, integradas
depois. A introdução de cada capítulo compartilhado e as transições ficam com
F11, que evita repetir definições e separa observações de interpretação.

[F09](../features/09-reproducao/README.md) produz apêndices, reprodução e declaração
de IA. [F10](../features/10-resumos/README.md) produz resumo, abstract e palavras-chave.
[F11](../features/11-integracao/README.md) integra e confere a monografia; não é um
capítulo adicional. Cada redator mantém suas referências, depois unificadas na F11.
A PoC entra como antecedente histórico quando pertinente, sem misturar sua
população com a avaliação do Juice Shop.

## Trabalho simultâneo e fechamento

F01–F10 podem começar em paralelo, lendo as fontes originais da
[base comum](../features/BASE_COMUM.md). Não precisam esperar que outro agente
escreva um arquivo. Cada responsável trabalha em sua própria pasta e registra
as afirmações provisórias que ainda dependem de conferência.

A independência de redação não elimina a coerência científica: F04 verifica o
método, F06 reconcilia os resultados, e discussão, conclusão e resumos conferem
suas afirmações contra essas entregas antes do fechamento. As dependências
específicas estão no frontmatter de cada feature. F11 começa após as entregas
revisadas e reconciliadas. A capacidade do cliente determina os lotes de agentes.

O [contrato comum](../features/CONTRATO.md) define propriedade dos arquivos,
rastreabilidade, convenções e critérios gerais. O
[modelo de entrega](../features/MODELO_ENTREGA.md) registra estado, provas de
aceitação, dependências e pareceres, sem um arquivo de progresso disputado por
todos. Se não houver ferramenta de subagentes, executar os papéis em sequência
e registrar o modo realmente usado.

Esta etapa define as tarefas de escrita; não representa capítulos já redigidos
ou aprovação da estrutura pela orientadora.

## Evoluções posteriores do experimento

O planejamento permanece aberto. O [fluxo de evoluções](../features/EVOLUCOES.md)
orienta comparar a base anterior com novos commits, classificar o impacto e criar
features adicionais por tópico. Cada uma aponta os trechos afetados, evidências,
critérios e se acrescenta, substitui ou apenas contextualiza conteúdo anterior.
Não crie capítulo novo automaticamente para cada evolução técnica.
