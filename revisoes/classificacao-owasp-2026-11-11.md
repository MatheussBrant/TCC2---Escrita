# Revisão documental da classificação complementar OWASP

Escopo: 49 casos sem categoria no catálogo original, preservação dos 29 rótulos
existentes e integração do agrupamento derivado aos capítulos 3 e 5.
Revisão realizada com apoio automatizado; não é revisão humana independente.

## Achados e encaminhamentos

| Gravidade | Trecho / problema | Fonte de contraste | Correção realizada |
|---|---|---|---|
| Relevante | Proposta inicial atribuía os quatro CWE-20 a A05 apenas pela taxonomia. Isso não expressava os mecanismos particulares descritos. | Código do alvo fixado, trechos e justificativas arquivados no catálogo; descrições de A01, A06 e A07. | Decisões por caso em `decisoes-contextuais.json`: propriedade do carrinho em A01, nota/quantidade em A06 e cadastro em A07. A associação taxonômica permanece em coluna separada. |
| Relevante | Quatro CWE-943 não têm correspondência explícita na lista A05 consultada. | Lista e descrição oficial de A05; consultas de `chat.ts`, `showProductReviews.ts`, `trackOrder.ts` e `updateProductReviews.ts`. | Associação contextual a A05 documentada; falso positivo em `chat.ts` preservado. Não se apresenta como correspondência oficial de CWE-943. |
| Relevante | Complementar o agrupamento poderia ocultar os 49 rótulos originalmente ausentes. | Catálogo e Tabela 10 anteriores. | Preservada a Tabela 10; acrescentada Tabela 10a e explicado o procedimento posterior às campanhas na seção 3.10. |

## Conferências concluídas

- 78 IDs únicos e categorizados na análise derivada; 29 categorias originais mantidas.
- 41 associações explícitas e oito contextuais entre os 49 casos complementares.
- Hashes e trechos das fontes conferidos contra objetos Git para os 78 casos.
- Dez documentos oficiais OWASP arquivados em revisão fixa, com hashes.
- 234 pares caso/modelo conferidos nos CSVs originais; população de 78 por modelo.
- Totais de aceites por F=`criterio` mantidos: 38, 51 e 49.
- Preservada a triagem de 55 confirmados, 21 falsos positivos e dois inconclusivos.
- Tabela 10a do manuscrito igual à tabela derivada; hashes das seis saídas conferidos.
- `git diff --check` sem erros; repositório experimental sem alterações locais.

As modificações que já existiam em `00-elementos-pre-textuais.md` e em outras
passagens da metodologia não foram revertidas. O texto novo foi acrescentado
ao manuscrito existente. Os documentos históricos de contexto e matriz citados
nas instruções locais não estão disponíveis nesta cópia; foram usadas as fontes
diretas do experimento, o catálogo e os documentos oficiais.

## Limites e avaliação acadêmica

As oito decisões contextuais são interpretações fundamentadas, sujeitas à
avaliação dos autores. O enquadramento em A06 considera restrições de negócio
ausentes; o código não permite determinar por si só a história do projeto nem
se a causa nasceu no desenho ou na implementação. A justificativa deve ser lida
como critério descritivo de agrupamento, não diagnóstico causal independente.

Não foi feita reclassificação integral dos 29 rótulos originais nem nova auditoria
de explorabilidade. A cobertura dos 78 casos não implica cobertura das dez
categorias: esta partição contém sete. Não houve execução de modelos, SAST ou
testes. Eventuais ajustes interpretativos requerem nova consolidação derivada,
sem repetir as campanhas. As evidências e o procedimento de reprodução estão
em `evidencias/classificacao-owasp-complementar-2026-11-11/LEITURA.md`.
