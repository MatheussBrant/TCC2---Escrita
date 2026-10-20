---
name: tcc2-redigir
description: Executa features de escrita e redige seções acadêmicas do TCC2 com fontes verificadas, entregáveis próprios e critérios de aceitação, mantendo rastreabilidade e lacunas explícitas.
---

# Redigir uma seção sustentada por evidências

Leia [plano de redação](../../../docs/plano-redacao.md), [contexto](../../../docs/contexto.md)
e apenas os compromissos pertinentes da [matriz](../../../docs/compromissos-tcc1.md).

Quando o pedido indicar uma feature, localize-a no [índice](../../../features/README.md)
e leia sua especificação, o [contrato](../../../features/CONTRATO.md) e a
[base comum](../../../features/BASE_COMUM.md). Use o argumento, fontes e escopo
ali definidos. Escreva somente em sua pasta `saida`, inclusive evidências,
referências e recursos. Mantenha os arquivos compartilhados como entradas de leitura.

Features E001 em diante estão no [registro de evoluções](../../../features/EVOLUCOES.md).
Leia seu mapa de destinos e bases; uma especificação `planejada` ainda depende
das evidências declaradas para liberar a redação de fatos realizados. Quando
pronta, produza `texto.md` e `impacto.md` na pasta exclusiva, sem editar diretamente
as features de destino. F11 aplica a atualização na cópia integrada.

Uma feature pode escrever apenas parte de um capítulo. Respeite `tipo`,
`capitulo` e `destino`: F02/F03, F04/F05 e F06/F07 compartilham capítulos, com
títulos de seção conforme o contrato. Numeração de pasta não define capítulo.

No layout padrão, leia o PDF na raiz da escrita e as evidências no clone interno
`tcc2-llm-sast-juiceshop/`; respeite `fontes.local.json` ou `--config` quando usados.
Confira se a coleta citada corresponde à revisão discutida, pois novos commits
podem atualizar resultados. Grave o manuscrito na escrita, preservando as fontes
do clone interno. A ausência da PoC opcional só limita afirmações dependentes dela.
Para uma feature, mantenha o recorte da base fixada; relate commits posteriores
sem trocar silenciosamente o SHA ou a campanha da rodada.

Defina a seção, seu argumento e as Qs que atende. Reúna as fontes antes de escrever
afirmações factuais: TCC1 para a proposta, código no SHA citado para implementação,
contrato/registros para método executado e dados auditados para resultados.
Use as skills de histórico/resultados/bibliografia somente quando a tarefa
depender de evidência ainda não preparada.

Escreva em português acadêmico claro. Desenvolva problema, decisão, funcionamento,
evidência e implicação conforme a seção; não converta o capítulo em um changelog.
Use passado para o que foi executado e futuro/condicional para pendências. Preserve
a terminologia: issue/alerta SAST, ocorrência, caso, tentativa, execução e desafio
não são sinônimos. Raciocínio guiado é uma estrutura solicitada de resposta,
não observação ou validação do raciocínio interno do modelo.

Para cada afirmação empírica importante, deixe uma nota de trabalho ou comentário
como `<!-- Evidência: experimento@SHA; caminho; execução; Q1/C08 -->`.
Tabelas de taxas exigem n/d, população, F e política. Referências acadêmicas
devem ter metadados conferidos; um hash Git não substitui literatura científica.
Use `[PENDENTE: fonte ou decisão específica]` quando necessário, sem preencher
com dados plausíveis. Não generalize resultados do Juice Shop para software em geral.

Em uma feature, crie os arquivos especificados em sua pasta e preencha
`evidencias.md` e `entrega.md` conforme o [modelo](../../../features/MODELO_ENTREGA.md).
Relacione G01–G06 e todos os critérios da feature (F04-ACnn ou E001-ACnn, por
exemplo) às provas de atendimento. Registre o ID da base resolvida e preserve-o
durante a entrega, mesmo se o índice ativo avançar. As
dependências de fechamento permitem começar o rascunho com fontes originais,
mas exigem conferência entre entregas antes de declarar a feature `revisada`.
Não marque revisão inexistente nem atualize checklists na especificação compartilhada.

Para seções avulsas, crie `manuscrito/<secao>.md` quando não houver um manuscrito
existente. Quando houver LaTeX, preserve estrutura, comandos, labels e chaves bibliográficas; não
invente normas ABNT, estilos da UnB ou fontes `.tex` a partir apenas do PDF.
Evite duplicar a mesma seção em Markdown e LaTeX sem uma finalidade definida.

Entregue o texto solicitado, a trilha de fontes e pendências precisas. Não marque
“revisado pelos autores” nem “aprovado pela orientadora” sem evidência. A declaração
de uso de IA deve refletir o trabalho efetivo e a responsabilidade dos autores.
