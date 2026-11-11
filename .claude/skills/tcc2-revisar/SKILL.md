---
name: tcc2-revisar
description: Revisa capítulos da monografia quanto a evidência, coerência entre método e resultados, perguntas de pesquisa, referências e clareza acadêmica, gravando o parecer em revisoes/.
---

# Revisar texto e validade das afirmações

Leia o trecho solicitado em `manuscrito/`, as notas de evidência do capítulo, o plano
de parágrafos e os [critérios de escrita](../../../docs/criterios-escrita.md). A revisão
precisa abrir fontes por amostragem, não apenas conferir que há uma nota ou um hash.

Localize o experimento conforme o `AGENTS.md`. Compare a revisão citada nas notas com
o HEAD do clone: distinga uma afirmação histórica válida de uma descrição
desatualizada do estado atual. Fontes ausentes limitam a verificação, sem invalidar
por si só as demais seções.

Priorize problemas que mudam as conclusões: valor ausente tratado como zero,
preflight tratado como experimento, aceites isolados somados como RRIS, catálogo
tratado como quantidade de vulnerabilidades confirmadas, cache tratado como réplica,
mistura de ambientes ou modelos, mudança oculta da definição de F ou do denominador,
falha de infraestrutura tratada como falha funcional e comparação causal entre
estratégias sequenciais. Confira a coerência entre tabelas e texto.

Verifique se o método descrito coincide com o protocolo, o caderno de laboratório e o
código da revisão citada. Na discussão, preserve os limites de cobertura funcional,
do SAST, da seleção dos casos, do projeto único e da recuperação por categoria.
Confira se Q1–Q5 recebem respostas compatíveis com os dados, se a conclusão traz
fatos novos e se as citações sustentam exatamente as afirmações. Confira também a
unidade do trabalho: o texto não deve citar TCC1 ou TCC2. Avalie clareza e
terminologia depois das falhas de evidência.

Grave o parecer em `revisoes/<assunto>-AAAA-MM-DD.md`, com gravidade, arquivo e
trecho, problema, fonte de contraste e correção proposta. Separe erro demonstrado
de dúvida e de sugestão de estilo. Use "sem achados nesta revisão" quando aplicável,
sem prometer validação integral do estudo. Informe fontes indisponíveis e
verificações não realizadas.

Só edite o manuscrito quando as correções também forem pedidas. Com outro agente
redigindo o mesmo arquivo, encaminhe as correções em vez de editar.
