---
id: F01
tipo: capitulo
capitulo: 1
destino: Introdução
saida: manuscrito/01-introducao
inicio: imediato
fechamento_depende_de: [F04, F06]
---

# F01 — Introdução

## Objetivo e escopo

Escrever o Capítulo 1 apresentando o problema, a justificativa, as questões de
pesquisa e o recorte efetivamente investigado. O leitor deve entender por que
integrar LLM, SAST e testes e o que este trabalho pretende avaliar.

Preservar Q1–Q4 e OE1–OE4 do TCC1, identificando evoluções de escopo sem reescrever
os objetivos para caberem em resultados favoráveis. Vínculos: todas as Qs/OEs;
apoio a C01/C02. Consulte o [contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Contextualização do reparo de vulnerabilidades e o papel complementar das ferramentas.
2. Problema de pesquisa: remoção de alerta não basta para validar a correção.
3. Justificativa acadêmica/prática, sustentada por fontes verificadas.
4. Questões Q1–Q4 e objetivos geral/específicos, coerentes com o TCC1.
5. Delimitação: Juice Shop, alertas/ocorrências, avaliação operacional, estudo em
   um projeto e distinção entre antecedente PoC e experimento do TCC2.
6. Organização dos cinco capítulos, sem descrever capítulos que não fazem parte do plano.

Não aprofundar teoria (F02), comparações com literatura (F03), fórmulas (F04) ou
taxas de resultado (F06). Pode apresentar contribuições realizadas com evidência,
sem anunciar superioridade de prompts ou correção segura universal.

## Fontes para começar sem outras entregas

- TCC1, §§1.2–1.5, páginas impressas 14–16 e continuação da organização do texto.
- [Matriz de compromissos](../../docs/compromissos-tcc1.md) e [contexto](../../docs/contexto.md).
- No experimento fixado: `docs/protocolo_experimental.md`, contrato da campanha e
  `docs/validacao_baseline_docker.md` para delimitar a execução realizada.
- Fontes primárias das afirmações de motivação; usar `tcc2-bibliografia` quando necessário.

## Entregáveis e paralelismo

Criar `manuscrito/01-introducao/capitulo.md`, `evidencias.md`, `entrega.md` e
`referencias.bib` se houver citações externas. É sua única pasta de edição.
Comece pelas fontes brutas. Para fechar, confira a descrição do recorte com F04
e as contribuições empíricas mencionadas com F06. Até lá, deixe as diferenças
registradas como pendências, sem depender da existência desses capítulos para começar.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F01-AC01:** o problema e a justificativa estão encadeados em prosa e
  sustentam a escolha da avaliação integrada; afirmações externas têm fonte conferida.
- [ ] **F01-AC02:** Q1–Q4 e OE1–OE4 correspondem à matriz/PDF; qualquer adaptação
  textual conserva o significado e não elimina compromissos sem explicar a mudança.
- [ ] **F01-AC03:** o recorte distingue projeto, catálogo, casos e tentativas e
  coincide com a descrição reconciliada de F04/F06.
- [ ] **F01-AC04:** separa a PoC do estudo no Juice Shop e não trata alerta como
  vulnerabilidade confirmada nem ausência de alerta como prova de segurança.
- [ ] **F01-AC05:** contribuições anunciadas apontam evidências; não antecipa
  conclusões ou comparações causais sem apoio nos resultados.
- [ ] **F01-AC06:** a organização do trabalho corresponde aos cinco capítulos do plano,
  com remissões verificáveis e sem duplicar fundamentação ou metodologia.

## Pedido de execução

Use `tcc2-redigir` para executar esta feature e entregue texto, evidências e
autoavaliação dos critérios na pasta definida. Não escreva outras features.
