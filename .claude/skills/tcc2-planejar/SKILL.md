---
name: tcc2-planejar
description: Relaciona as promessas do TCC1 às evidências do TCC2 e planeja capítulos, lacunas e respostas às perguntas de pesquisa.
---

# Planejar o TCC2 a partir dos compromissos

Leia [contexto](../../../docs/contexto.md), [matriz](../../../docs/compromissos-tcc1.md)
e [plano de redação](../../../docs/plano-redacao.md). Os caminhos de comandos são
relativos à raiz do repositório de escrita.

Consulte também o [índice de features](../../../features/README.md), o
[contrato](../../../features/CONTRATO.md) e a [base comum](../../../features/BASE_COMUM.md).
A estrutura atual tem cinco capítulos: F02/F03 compõem o 2, F04/F05 o 3,
F06/F07 o 4 e F08 o 5. F09/F10 são complementares e F11 faz a integração.
Ao planejar ou revisar especificações, preserve a correspondência entre capítulos,
IDs, pastas exclusivas e critérios verificáveis. Não redija capítulos em resposta
a um pedido restrito à definição de tarefas.

Quando o pedido for planejar a execução de uma feature existente, leia a
especificação e apresente argumento, fontes, etapas, saídas, dependências e
verificação dos critérios. Entregue o plano na conversa ou no mecanismo de
planejamento do cliente. Se for solicitado persistir no repositório, grave
`plano.md` somente na pasta `saida` da feature, respeitando o modo do cliente.
Não atualize a matriz compartilhada automaticamente nesse escopo. A redação
do texto ocorre no pedido de execução; preserve a separação quando solicitada.

Para permitir trabalho simultâneo, cada feature precisa de fontes originais
acessíveis sem depender da entrega de outro redator. Separe dependência para
começar de conferência necessária para fechar; F01–F10 iniciam com a base comum,
F11 integra versões revisadas. Durante uma execução, não altere contratos
compartilhados sem coordenar as consequências para as entregas afetadas.

Quando o planejamento envolver uma adição ao experimento, use `tcc2-evoluir`
e o [fluxo](../../../features/EVOLUCOES.md) para especificar E001 em diante,
com impacto nos textos existentes. Planejar uma nova feature não exige um
capítulo novo. Conserve a rastreabilidade entre bases e a distinção entre
adição pretendida, código implementado e resultado observado.

Resolva as fontes pelo layout e prioridade de configuração do `AGENTS.md`:
clone experimental dentro da escrita, PDF na raiz e PoC opcional. Antes de
classificar um compromisso como pendente, procure commits posteriores à coleta
consultada; uma lista histórica de pendências não descreve necessariamente o HEAD.

Recupere no PDF ou em `evidencias/<coleta>/tcc1.paginas.jsonl` os trechos que
sustentam a promessa em análise. Preserve Q1–Q4 e OE1–OE4; não reescreva uma
pergunta de pesquisa para acomodar resultados favoráveis. Proponha mudanças de
escopo como mudanças explícitas, com justificativa e efeitos na análise.

Para cada compromisso, registre o proposto, o realizado, a evidência com SHA e
caminho, a diferença metodológica e a próxima ação de escrita ou verificação.
Classifique como proposto, implementado, observado, parcialmente verificado ou
não verificado, conforme o objeto da afirmação. Não transforme uma classificação
de implementação em confirmação experimental.

O planejamento deve distinguir o recorte histórico de 12 casos, catálogo ampliado
de 78 ocorrências, conjunto preparado de 52 e pilotos/campanhas efetivamente
executados. Confira esses números nas fontes da revisão utilizada; eles não são
constantes permanentes da skill. Falsos positivos não equivalem a falhas reais.

Entregue uma matriz atualizada e uma sequência de seções que já podem ser escritas,
com lacunas concretas. Fontes editáveis LaTeX ou um template podem faltar sem
impedir rascunhos em Markdown. Não declare data de defesa ou aprovação da
orientadora com base no cronograma previsto no TCC1.
