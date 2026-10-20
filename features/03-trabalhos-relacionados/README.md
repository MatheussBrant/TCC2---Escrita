---
id: F03
tipo: secao
capitulo: 2
destino: Referencial teórico — trabalhos relacionados
saida: manuscrito/03-trabalhos-relacionados
inicio: imediato
fechamento_depende_de: []
---

# F03 — Trabalhos relacionados

## Objetivo e escopo

Escrever a seção de trabalhos relacionados do Capítulo 2, posicionando o estudo frente à literatura de reparo de
vulnerabilidades com LLMs, integração com ferramentas e avaliação de correções.
Vínculos: Q1/Q2/Q4, apoio a C13. Ler o [contrato](../CONTRATO.md) e a
[base comum](../BASE_COMUM.md).

## O que escrever

1. Delimitação e procedimento real de seleção de trabalhos: ponto de partida no
   TCC1, buscas complementares efetivamente realizadas, critérios e data de corte.
2. Abordagens de geração/reparo e uso de SAST ou outras ferramentas de feedback.
3. Estratégias de contexto/raciocínio guiado e seu papel nos estudos consultados.
4. Formas de avaliação: corpus, unidade de análise, testes, critérios de sucesso
   e limites de comparar números de desenhos diferentes.
5. Síntese das aproximações/diferenças e da lacuna que o TCC2 pode investigar.

Produzir uma tabela comparativa com estudo, problema, corpus/linguagem, modelo,
contextualização, ferramentas, validação, métricas, limitações e relação com este
TCC2. Use “não informado na fonte consultada” quando um campo não estiver disponível.
Não alegar revisão sistemática sem executar e documentar um protocolo compatível.
Não equiparar desempenho publicado a uma comparação controlada com nossa campanha.

## Fontes para começar sem outras entregas

- Trechos de trabalhos relacionados e referências do TCC1; conferir os artigos originais.
- Artigos primários acessíveis e registros editoriais para metadados/versionamento.
- A base comum e `docs/protocolo_experimental.md` do experimento para caracterizar
  nosso desenho provisório; não depende do texto pronto de F04 ou F06.
- Usar `tcc2-bibliografia`; registrar buscas realizadas, sem inventar strings ou etapas.

## Entregáveis e paralelismo

Criar `manuscrito/03-trabalhos-relacionados/texto.md`, `comparacao.md`,
`referencias.bib`, `evidencias.md` e `entrega.md`. A tabela em `comparacao.md`
deve ser citada/incorporada pelo capítulo. Não alterar bibliografia de F02.
F07 poderá consumir esta comparação posteriormente, sem ser requisito de início.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F03-AC01:** o procedimento de seleção é transparente e corresponde ao
  que foi realmente feito; alcance e limitações da revisão são declarados.
- [ ] **F03-AC02:** cada trabalho comparado tem fonte primária consultada,
  identidade bibliográfica válida e evidências para os campos preenchidos da tabela.
- [ ] **F03-AC03:** a comparação cobre geração/reparo, uso de contexto/ferramentas
  e validação; lacunas de cobertura são assumidas, sem incluir estudos fictícios.
- [ ] **F03-AC04:** métricas de estudos diferentes não são tratadas como diretamente
  comparáveis quando corpus, unidades e critérios divergem.
- [ ] **F03-AC05:** a lacuna e o posicionamento do TCC2 decorrem da comparação;
  não afirma ineditismo absoluto ou superioridade não demonstrada.
- [ ] **F03-AC06:** a prosa sintetiza relações entre estudos em vez de apenas
  listar resumos; os conceitos básicos permanecem no escopo de F02.

## Pedido de execução

Use `tcc2-bibliografia` e `tcc2-redigir` para produzir a seção comparativa,
tabela, referências e autoavaliação na pasta exclusiva desta feature.
