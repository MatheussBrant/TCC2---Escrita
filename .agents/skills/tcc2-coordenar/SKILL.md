---
name: tcc2-coordenar
description: Coordena features de escrita do TCC2 em paralelo ou papéis sequenciais, com pastas exclusivas, base comum, revisão por critérios e integração das entregas reconciliadas.
---

# Coordenar uma entrega de escrita

Use quando o pedido envolver agentes, divisão de trabalho ou uma entrega de
múltiplas seções. Leia [plano de redação](../../../docs/plano-redacao.md),
[contexto](../../../docs/contexto.md) e o escopo solicitado. Uma revisão curta
ou correção de frase pode ser feita diretamente sem coordenação adicional.

Para as features existentes, leia o [índice](../../../features/README.md),
o [contrato](../../../features/CONTRATO.md), a [base comum](../../../features/BASE_COMUM.md)
e as especificações selecionadas. Reutilize seus IDs e pastas; não invente um
segundo plano de capítulos. Um pedido para definir features autoriza produzir
as especificações; a execução dos capítulos ocorre quando solicitada.

Consulte também o [registro de evoluções](../../../features/EVOLUCOES.md).
E001 em diante podem acrescentar ou substituir partes de F01–F10. Confirme se a
especificação está pronta e se sua base de destino existe antes de distribuí-la.
Informe a cada agente o ID de base: use a base já registrada em uma entrega
existente ou a explicitamente escolhida para a nova rodada. O índice ativo é
uma seleção para novas tarefas, sem alterar agentes que já começaram.

O workspace previsto é a escrita com `tcc2-llm-sast-juiceshop/` clonado dentro
dela e o PDF do TCC1 na raiz. Resolva a configuração efetiva conforme `AGENTS.md`
e informe a cada agente as raízes exatas de escrita e experimento. O clone
interno é fonte de consulta com Git próprio; as entregas vão para a escrita.
Não exija a PoC opcional para tarefas que não dependem dela. Compare os commits
atuais com a coleta escolhida antes de distribuir tarefas baseadas em evidências.

Defina uma entrega concreta e confira estado, fontes e saídas nos `entrega.md`
das features. F01–F10 podem iniciar seus rascunhos a partir das fontes originais,
sem aguardar outro agente produzir texto. Respeite as dependências de fechamento:
conclusões provisórias não viram afirmações aceitas antes da reconciliação.
Se o HEAD tiver avançado, mantenha o SHA fixado e registre a mudança; uma nova
base exige atualização coordenada das entregas afetadas.

Quando o ambiente permitir delegação e o pedido autorizar agentes, distribua
subtarefas independentes: recuperação de histórico, auditoria de resultados,
verificação bibliográfica, redação de seção e revisão. Cada agente recebe:

- objetivo e Q/C atendidos;
- fontes e SHAs a consultar, além da skill pertinente;
- lista exclusiva de arquivos que pode editar ou indicação de somente leitura;
- entrega esperada com evidências, lacunas e critérios de conclusão.

Na execução de features, atribua um redator por pasta `saida`, distribuindo em
lotes conforme as vagas reais do cliente. O agente recebe também a especificação,
G01–G06, seus critérios por ID e dependências de fechamento. Não edite progresso
nos READMEs nem atribua bibliografia global compartilhada. Os revisores escrevem
apenas em `revisoes/<ID>/parecer.md`; correções retornam ao redator.

Não suponha que Claude e Codex compartilhem memória ou sessões. Transfira o
contexto necessário em arquivos e mensagens de tarefa. Se ferramentas de
subagentes não estiverem disponíveis, execute esses papéis em sequência e
declare o modo usado. Esta skill não instala um servidor de agentes nem altera
permissões globais dos clientes.

O integrador confere os retornos, resolve divergências com as fontes e mantém
vocabulário, versões e denominadores consistentes. Atribua um único responsável
por cada feature/pasta; capítulos compartilhados são reunidos por F11. Não lance
agentes editando o mesmo manuscrito ao mesmo tempo.
Uma revisão separada deve receber texto e fontes suficientes para testar as
afirmações, sem ser conduzida a confirmar a conclusão do redator.

F04 verifica a operacionalização e F06 reconcilia os registros; divergências
voltam aos responsáveis antes de fechar as entregas afetadas. Só execute F11 após
F01–F10 e as evoluções selecionadas revisadas e reconciliadas. Defina o recorte
de integração e registre também as evoluções adiadas/excluídas com razão.
Reconcilie os efeitos sobre discussão, conclusão e resumos. Registre as versões
incorporadas; F11 escreve
na própria pasta e não altera capítulos concorrentes. Se o pedido cobrir apenas
algumas features, entregue esse escopo sem iniciar automaticamente toda a monografia.

Entregue os textos integrados, o registro de evidências e o parecer. Informe
quais papéis foram realmente executados, quais perguntas foram respondidas e
quais decisões permanecem para os autores. Não simule aprovação humana ou consenso
entre agentes; não publique, envie mensagens externas ou execute experimentos
por consequência automática de uma tarefa de redação.
