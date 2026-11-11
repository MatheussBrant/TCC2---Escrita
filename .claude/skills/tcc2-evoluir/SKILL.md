---
name: tcc2-evoluir
description: Registra mudanças do experimento, a partir de commits ou de adições planejadas, e mapeia o impacto em cada capítulo e plano de parágrafos da monografia.
---

# Incorporar evoluções do experimento ao texto

Use quando o experimento mudar depois da revisão usada no texto ou quando uma adição
estiver planejada. Localize o experimento conforme o `AGENTS.md` e compare a revisão
registrada nas notas dos capítulos com o SHA pedido ou com o HEAD do clone.
Confira o estado local, a ancestralidade, os commits, os diffs, a documentação e os
artefatos; use `tcc2-historico` e `tcc2-resultados` quando necessário. Não faça
checkout nem reset no clone. Mudanças não commitadas e intenções não têm a mesma
proveniência de um SHA publicado.

Classifique o impacto em método, implementação, dados, medição e interpretação.
Agrupe as mudanças por assunto de escrita e indique, para cada uma, os capítulos,
seções e parágrafos afetados (pelos IDs dos planos em `docs/`), a operação
necessária (acrescentar, substituir ou remover) e a evidência que a sustenta.
Verifique efeitos indiretos na discussão, na conclusão e nos resumos. Uma campanha
continua descrita pela revisão em que rodou, mesmo que o código posterior mude.

Grave o registro em `evidencias/evolucao-AAAA-MM-DD.md`. Se a adição ainda for uma
ideia, registre-a como planejada, com as evidências necessárias para liberar a
redação, sem descrever resultados. Atualize os planos de parágrafos só quando isso
for pedido.

Nesta tarefa, não redija os capítulos nem execute experimentos. A redação acontece
depois, com `tcc2-redigir`. Ao encerrar, informe o intervalo analisado, as partes
afetadas, as fontes verificadas e os impedimentos. Se nenhuma mudança afetar o
texto, explique com evidência.
