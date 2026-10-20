---
name: tcc2-revisar
description: Revisa rascunhos do TCC2 quanto a evidência, coerência entre método e resultados, perguntas de pesquisa, referências e clareza acadêmica.
---

# Revisar texto e validade das afirmações

Leia o trecho solicitado, [contexto](../../../docs/contexto.md) e compromissos
relevantes da [matriz](../../../docs/compromissos-tcc1.md). A revisão precisa abrir
fontes amostrais, não apenas conferir que há uma citação ou hash escrito.

Quando revisar uma feature, leia sua especificação no [índice](../../../features/README.md),
o [contrato](../../../features/CONTRATO.md), a [base comum](../../../features/BASE_COMUM.md)
e os arquivos `entrega.md`/`evidencias.md` do redator. Verifique cada G01–G06 e
critério específico por ID com prova concreta, indicando atendido, parcial ou não atendido e o
trecho/fonte que justifica o julgamento. A autoavaliação não substitui a revisão.

Localize o PDF e o clone experimental interno pela configuração efetiva do
`AGENTS.md`. Compare a revisão discutida com a coleta e os commits posteriores:
distinga uma afirmação histórica válida de uma descrição desatualizada do estado
atual. Fontes opcionais ausentes limitam a verificação, sem invalidar por si só
as demais seções.
Uma base fixada pode representar legitimamente uma revisão anterior ao HEAD;
avalie sua coerência e não substitua o recorte sem registrar a mudança.

Priorize problemas que mudam as conclusões: valor ausente tratado como zero,
preflight como experimento, aceites isolados como RRIS, catálogo como quantidade
de vulnerabilidades confirmadas, cache como réplica, mistura de ambientes/modelos,
mudança de F/denominador oculta, falha de infraestrutura como falha funcional e
comparação causal de estratégias sequenciais. Confira coerência de tabelas e texto.

Verifique se a descrição do método executado coincide com contratos e código da
revisão citada. Uma pendência antiga do guia não prova que algo segue ausente;
uma feature implementada também não comprova execução final. Na discussão,
preserve limites de cobertura, SAST, seleção, projeto único e recuperação por categoria.

Confira se Q1–Q4 recebem respostas compatíveis com os dados, se a conclusão
introduz fatos novos e se citações sustentam exatamente as afirmações. Avalie
clareza e consistência terminológica depois das falhas de evidência.

Entregue um parecer com gravidade, arquivo/trecho, problema, fonte de contraste e
correção proposta. Separe erro demonstrado de dúvida e de sugestão de estilo.
Use “sem achados nesta revisão” quando aplicável, sem prometer validação integral
do estudo. Informe fontes não disponíveis e verificações não realizadas.
Para uma feature, produza `revisoes/<ID>/parecer.md`, identificando a versão
revisada, a cobertura dos critérios e as dependências reconciliadas. Declare
se há condições para fechar ou quais impedimentos permanecem. Não edite o texto
ou o estado do redator simultaneamente; encaminhe as correções ao responsável.
Uma feature ainda dependente de reconciliação pode receber parecer de rascunho,
mas não deve ser apresentada como aceita. A revisão da F11 também confere as
versões, referências e remissões incorporadas. Para evoluções E001 em diante,
confira o contraste de bases, as operações de `impacto.md`, sua sustentação nas
fontes e os efeitos nas demais partes. Na F11, confira todas as evoluções
registradas e as justificativas de inclusão/adiamento/exclusão, sem presumir que
a lista inicial F01–F10 esgota o recorte.

Para uma revisão avulsa, produza `revisoes/<secao>-<id>.md`; edite o manuscrito
quando correções também tiverem sido solicitadas, sem conflito de responsabilidade.
