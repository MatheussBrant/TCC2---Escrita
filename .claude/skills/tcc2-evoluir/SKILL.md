---
name: tcc2-evoluir
description: Cria features de escrita para novas evoluções do experimento do TCC2, a partir de commits ou adições planejadas, com impacto nos capítulos, fontes versionadas e critérios de aceitação.
---

# Incorporar evoluções ao planejamento de escrita

Use para transformar mudanças do experimento em novas tarefas de escrita.
Leia o [fluxo de evoluções](../../../features/EVOLUCOES.md), o
[modelo](../../../features/MODELO_EVOLUCAO.md), o
[plano de capítulos](../../../docs/plano-redacao.md) e a
[base comum](../../../features/BASE_COMUM.md). Resolva os clones e PDF conforme
`AGENTS.md`; o layout padrão usa o clone experimental dentro da escrita.

Para mudanças existentes, compare a base anterior com o SHA de destino solicitado
ou o HEAD local. Confira estado local, ancestralidade, commits, diffs, documentação
e artefatos; use `tcc2-historico` e `tcc2-resultados` quando necessários. Não faça
checkout/reset no clone compartilhado. Mudanças não commitadas e intenções precisam
ser identificadas; não recebem a mesma proveniência de um SHA publicado no histórico.

Classifique impacto em método, implementação, dados, medição e interpretação.
Prepare uma nova base com ID inédito e coleta nova quando houver fontes novas
a incorporar. Preserve as anteriores; atualize o índice ativo na preparação
coordenada da rodada, sem mudar a base de entregas em andamento. A base de uma
campanha descreve sua execução, mesmo quando o código posterior é diferente.

Agrupe mudanças por tópico de escrita e crie o próximo ID E001 em diante,
seguindo o modelo e registrando-o em `features/EVOLUCOES.md`. Cada especificação
tem pasta de saída exclusiva, bases, fontes, destinos Fxx, operações de atualização,
entregáveis, dependências e critérios próprios verificáveis. Preserve os cinco
capítulos: uma adição costuma gerar seção ou revisão de seção existente.
Verifique impactos transitivos em discussão, conclusão e resumos, além do arquivo
diretamente modificado. Registre ordem de incorporação para trechos sobrepostos.

Se a adição ainda for uma ideia, crie uma feature `planejada`, sem base de destino
inventada. Liste as evidências necessárias para liberar sua execução; descreva
comportamento esperado como proposta. Concretize os critérios conforme a adição.
Não declare eficácia, novos resultados ou reprodução sem os registros necessários.

Nesta tarefa de planejamento, altere somente as especificações, índice, registros
de fontes e documentação pertinente. A escrita ocorre quando solicitada, usando
`tcc2-redigir` nas pastas das evoluções; sua integração cabe à F11, incluindo
reconciliação e revisão das partes afetadas. Não execute experimentos como efeito
automático da atualização do planejamento.

Ao encerrar, informe intervalo analisado, base preparada/ativada, features criadas,
partes afetadas, fontes verificadas e impedimentos. Se nenhuma mudança merecer
nova feature, explique com evidência em vez de criar uma tarefa vazia.
