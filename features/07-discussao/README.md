---
id: F07
tipo: secao
capitulo: 4
destino: Resultados e discussão — interpretação e ameaças à validade
saida: manuscrito/07-discussao
inicio: imediato
fechamento_depende_de: [F03, F04, F05, F06]
---

# F07 — Discussão e ameaças à validade

## Objetivo e escopo

Escrever a parte de discussão e validade do Capítulo 4, interpretando os resultados e delimitando o que pode ser
concluído. Vínculos: Q1–Q4; responsável por C13. Ler o [contrato](../CONTRATO.md)
e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Interpretação organizada por Q1–Q4, distinguindo observação e hipótese explicativa.
2. Relação com trabalhos pertinentes, respeitando diferenças de corpus/desenho.
3. Limites do critério de correção: remover alerta, passar testes e não detectar
   novas issues não equivalem a prova irrestrita de segurança.
4. Ameaças à validade de construção, interna, externa e de conclusão, associadas
   a mecanismos concretos: F/D, cobertura, regras locais, parsing, falsos positivos,
   amostra preparada, seleção sequencial, ambiente, variabilidade e projeto único.
5. Implicações para uso do pipeline e para estudos futuros, proporcionais às evidências.

Criar uma matriz ameaça → mecanismo → evidência → mitigação realizada → risco
residual. Medidas apenas propostas são trabalhos futuros; não apresentá-las como
mitigações executadas. Possível contaminação de treinamento é ameaça, não fato
demonstrado sobre um modelo sem evidência específica.

## Fontes para começar sem outras entregas

- TCC1 §3.12, protocolo/caderno, auditorias SAST, cobertura e validação Docker.
- Artefatos e métricas da campanha da base comum, com a cautela de `tcc2-resultados`.
- Literatura primária pertinente, sem precisar aguardar a bibliografia de F03.
- Se F03–F06 ainda não existirem, elaborar análise preliminar e registrar pontos
  que precisarão ser reconciliados, evitando cristalizar conclusões não verificadas.

## Entregáveis e paralelismo

Criar `manuscrito/07-discussao/texto.md`, `ameacas.md`, `evidencias.md`,
`entrega.md` e `referencias.bib` quando usado. A matriz de ameaças deve ser
incorporada ou referenciada pelo capítulo. Para fechar, confrontar interpretação,
literatura, mecanismos e números com F03/F04/F05/F06 revisadas.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F07-AC01:** cada Q tem interpretação ligada a observações verificadas ou
  limitação explícita; hipóteses explicativas são identificadas como hipóteses.
- [ ] **F07-AC02:** não atribui efeito causal independente ao prompt/RAG nem
  extrapola uma aplicação para todos os projetos de software.
- [ ] **F07-AC03:** a matriz cobre as quatro classes de validade com ameaças
  concretas do estudo, evidências, mitigação efetiva e risco residual.
- [ ] **F07-AC04:** diferenças de F, reanálise limitada, regras exploratórias,
  seleção de casos, falsos positivos e mudanças de ambiente são discutidas quando aplicáveis.
- [ ] **F07-AC05:** a comparação com literatura sustenta o argumento sem comparar
  taxas incompatíveis como ranking controlado ou afirmar ineditismo absoluto.
- [ ] **F07-AC06:** limitações e resultados negativos são preservados; não inventa
  inspeção completa, revisão humana ou reprodução independente.
- [ ] **F07-AC07:** interpretações finais foram reconciliadas com F03–F06 e não
  introduzem métricas inéditas ou números diferentes da referência de F06.

## Pedido de execução

Use `tcc2-redigir`, consultando as skills de resultados e bibliografia quando
necessário. Produza a discussão e a matriz de ameaças em sua pasta exclusiva.
