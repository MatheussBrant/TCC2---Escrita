---
name: tcc2-coordenar
description: Coordena agentes ou papéis sequenciais em uma entrega de escrita com vários capítulos, com arquivos exclusivos, revisão separada e integração reconciliada.
---

# Coordenar uma entrega de escrita

Use quando o pedido envolver agentes, divisão de trabalho ou vários capítulos ao
mesmo tempo. Uma correção curta pode ser feita diretamente. Leia as
[diretrizes](../../../docs/diretrizes-escrita.md), os
[critérios](../../../docs/criterios-escrita.md), o
[índice do manuscrito](../../../manuscrito/README.md) e o escopo pedido.

Divida o trabalho pelos arquivos atuais: cada capítulo de `manuscrito/` tem um único
responsável por vez, com seu plano em `docs/` e suas notas em `evidencias/`. Nunca
coloque dois agentes editando o mesmo arquivo. Pareceres vão para `revisoes/`, e as
correções voltam ao responsável pelo capítulo.

Informe a cada agente a raiz da escrita e o caminho do experimento (conforme o
`AGENTS.md`), a revisão (SHA) e o recorte de execuções a usar, e confira o HEAD do
clone antes de distribuir tarefas baseadas em evidências. Se o HEAD tiver avançado,
mantenha a revisão escolhida e registre a mudança. Cada agente recebe:

- objetivo e perguntas (Q1–Q5) atendidas;
- fontes, revisões a consultar e a skill pertinente;
- lista exclusiva de arquivos que pode editar, ou indicação de somente leitura;
- entrega esperada, com evidências, lacunas e critérios de conclusão.

Sem ferramentas de subagentes, execute os papéis em sequência e declare o modo
usado. Claude e Codex não compartilham memória: passe o contexto em arquivos e nas
mensagens das tarefas.

O integrador confere os retornos, resolve divergências com as fontes e mantém
vocabulário, versões e denominadores consistentes entre os capítulos, inclusive
resumo, introdução e conclusão. Uma revisão separada recebe texto e fontes suficientes
para testar as afirmações, sem ser conduzida a confirmar a conclusão do redator.

Entregue os textos, o registro de evidências e o parecer. Informe quais papéis foram
realmente executados e quais decisões permanecem com os autores. Não simule aprovação
humana nem consenso entre agentes; não publique, não envie mensagens externas e não
execute experimentos como efeito de uma tarefa de redação.
