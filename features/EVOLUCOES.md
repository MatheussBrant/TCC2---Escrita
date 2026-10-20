# Evoluções do experimento e novas features de escrita

Use este fluxo quando `tcc2-llm-sast-juiceshop` receber adições, correções,
novos dados ou campanhas. A skill `tcc2-evoluir` transforma essas mudanças em
tarefas de escrita. Features de software continuam no experimento; aqui são
especificados os textos e análises necessários para documentá-las no TCC2.

## Como incorporar uma evolução

1. **Identificar o intervalo.** Resolver os caminhos configurados e ler a base
   anterior pelo ID. Registrar SHA anterior, SHA de destino, refs e estado local.
   Examinar commits, diffs, documentação e artefatos. Se os históricos divergirem,
   registrar a divergência em vez de assumir uma sequência linear.
2. **Classificar o impacto.** Distinguir planejamento, código implementado,
   execução observada, alteração de avaliação e correção de medição. Um commit
   de implementação não comprova ganho experimental. Mudança só editorial pode
   não exigir nova feature; justificar essa decisão.
3. **Definir as fontes da rodada.** Quando houver evidência nova a incorporar,
   criar outra coleta com ID inédito pelo coletor existente e uma base `R2`, `R3`
   etc. em `features/bases/`. A nova base registra fontes completas, SHAs, hashes,
   coleta, campanhas, políticas e diferenças em relação à anterior. Não sobrescrever
   bases/coletas. Uma campanha antiga continua ligada ao código/contrato de sua
   execução; novo código não muda retroativamente o método realizado.
4. **Criar tarefas por tópico.** Usar o [modelo](MODELO_EVOLUCAO.md), atribuindo
   o próximo ID livre `E001`, `E002` etc. e uma pasta
   `features/evolucoes/E001-assunto/README.md`. Não criar uma tarefa por commit
   automaticamente: agrupar mudanças que sustentam o mesmo argumento de escrita.
5. **Registrar o impacto.** Indicar capítulo, features Fxx afetadas, trechos a
   acrescentar/substituir e efeitos sobre tabelas, discussão, conclusão e resumo.
   Usar IDs de features como destinos; seção exata pode ser indicada quando existir.
   Registrar a feature na tabela abaixo, antes de distribuir redatores.
6. **Distribuir sem colisão.** Cada E trabalha em
   `manuscrito/evolucoes/E001-assunto/`, com texto, evidências, mapa de atualização
   e entrega. O revisor usa `revisoes/E001/parecer.md`. Features sobrepostas podem
   investigar em paralelo, mas precisam de ordem explícita de incorporação.
7. **Integrar e reconferir.** F11 aplica os acréscimos/substituições na cópia
   integrada e confere efeitos diretos e transitivos. Não basta anexar o novo
   texto e conservar números/conclusões incompatíveis no restante da monografia.

Preparar e ativar a nova base é responsabilidade do coordenador da rodada.
`BASE_COMUM.md` aponta para a escolhida para novas tarefas; cada entrega registra
seu próprio ID. Agentes em andamento conservam a base com que começaram. Quando
uma entrega já existir, sua base registrada prevalece; em uma tarefa nova, o
coordenador informa a base antes da distribuição. Evitar troca do índice durante
a distribuição de um mesmo lote.

## Adições ainda planejadas

É possível especificar uma evolução antes de implementá-la. Nesse caso, registrar
`estado_planejamento: planejada`, `base_destino: null` e
`inicio: apos_base_definida`, com as evidências necessárias para liberar a escrita.
A descrição do comportamento esperado não é tratada como resultado realizado.
Quando os commits/artefatos existirem, conferir as fontes, fixar a base, ajustar
os critérios ao comportamento observado e marcar a especificação como `pronta`.
Uma intenção sem evidências não cria uma nova base experimental.

Se não houver campanha para avaliar uma implementação nova, a feature pode
descrever o código e sua limitação de avaliação. Não solicitar nem executar um
experimento apenas para permitir a redação.

## Registro de evoluções

| ID e especificação | Tópico | Base anterior → destino | Destinos Fxx | Planejamento | Relação com outras E |
|---|---|---|---|---|---|

Nenhuma evolução adicional foi especificada até esta configuração. As onze
features iniciais permanecem no [índice principal](README.md). Os estados de
execução das evoluções ficam em seus `entrega.md`, sem edição concorrente desta tabela.

O registro informa também exclusões justificadas do recorte de integração. F11
deve relacionar todas as entradas existentes: incluída nesta versão, adiada ou
fora do recorte, com razão. Uma pendência não pode desaparecer por omissão.

## Pedidos de exemplo

Codex, após novos commits:

```text
$tcc2-evoluir Compare a base atual com o HEAD do experimento. Crie features de
escrita para as mudanças relevantes, com fontes, impacto e critérios de aceitação.
Prepare a próxima base sem alterar entregas em andamento.
```

Antes de implementar uma ideia:

```text
$tcc2-evoluir Crie uma feature planejada para documentar a evolução que descrevo
a seguir: [descrever a adição]. Liste as evidências necessárias para liberar a escrita.
```

No Claude Code, use `/tcc2-evoluir`.
