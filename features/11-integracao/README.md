---
id: F11
tipo: integracao
capitulo: null
saida: manuscrito/11-integracao
inicio: apos_entregas_revisadas
fechamento_depende_de: [F01, F02, F03, F04, F05, F06, F07, F08, F09, F10]
evolucoes: conforme_registro_e_recorte
---

# F11 — Integração editorial e conferência final

## Objetivo e pré-requisitos

Integrar as entregas em uma monografia coerente, com referências e remissões
resolvidas. Esta é uma tarefa editorial além dos cinco capítulos. Ler o [contrato](../CONTRATO.md)
e a [base comum](../BASE_COMUM.md).

Definir primeiro o recorte de integração: base de referência e evoluções incluídas,
adiadas ou excluídas, com justificativas, consultando o [registro](../EVOLUCOES.md).
Uma evolução planejada pode permanecer fora desta versão, sem bloquear toda a
monografia; sua exclusão e efeito sobre as conclusões devem ficar explícitos.

Começar após F01–F10 e as evoluções selecionadas entregarem texto, evidências, autoavaliação e parecer real,
com critérios atendidos e dependências reconciliadas. Confirmar que as versões
incorporadas não estão sendo alteradas; registrar seus hashes. Uma montagem
parcial solicitada antes disso deve ser identificada como parcial e não atende
ao aceite desta feature.

## O que fazer

1. Conferir a cobertura dos critérios, Q1–Q4, OE1–OE4 e C01–C15, incluindo
   compromissos parcialmente atendidos ou não medidos.
2. Incorporar os textos: resumo/abstract, capítulos 1–5, referências e apêndices.
   Posicionar a declaração de IA conforme o template adotado.
   Reunir F02/F03 no Capítulo 2, F04/F05 no 3, F06/F07 no 4 e F08 no 5.
   Criar aberturas e transições dos capítulos compartilhados, evitando introduções
   repetidas. Aplicar as operações de acréscimo/substituição das evoluções.
3. Uniformizar termos, remissões, figuras e tabelas, preservando o sentido
   científico e o contexto de cada população, contrato e definição de F.
4. Unificar bibliografia por DOI/identidade, mapear chaves antigas para finais
   e atualizar todas as citações na cópia integrada.
5. Conferir números repetidos entre introdução, método, resultados, discussão,
   conclusão e resumos; encaminhar divergências de conteúdo aos responsáveis.
6. Aplicar o template efetivamente fornecido. Na ausência dele, entregar a
   integração Markdown e declarar a adequação institucional ainda pendente.

Não resolver divergências científicas apenas pela escolha editorial de uma frase.
Devolver o problema à feature responsável com fontes e impacto. Correções locais
de estilo são feitas na cópia integrada e registradas; o integrador não edita
simultaneamente as pastas dos redatores.

## Entradas

- Entregas F01–F10, seus arquivos de evidência e pareceres em `revisoes/Fxx/`.
- Registro de evoluções, especificações selecionadas, `impacto.md`, textos,
  evidências e pareceres E001 em diante. Para trechos sobrepostos, conferir a
  ordem de incorporação; divergências científicas retornam aos responsáveis.
- Base comum, matriz de compromissos e fontes originais necessárias à conferência.
- Template e orientações institucionais efetivamente disponíveis, sem presumir
  fontes LaTeX ou aprovação apenas pela aparência do PDF do TCC1.

## Entregáveis

Criar, em `manuscrito/11-integracao/`, `tcc2.md`, `referencias.bib`,
`mapa-integracao.md`, `evidencias.md`, `entrega.md` e recursos utilizados.
`tcc2.md` contém o texto integrado, não apenas uma lista de links para capítulos.
Se houver projeto LaTeX institucional, preservar sua estrutura na saída e
registrar qual formato constitui a entrega principal, evitando cópias divergentes.

O mapa registra arquivos de origem e hashes, versões e pareceres aceitos, cobertura
dos compromissos, remissões, equivalência de chaves bibliográficas e ajustes
editoriais. Referências a recursos devem funcionar a partir da pasta integrada.
Incluir a base de cada contribuição, o recorte final, as evoluções incluídas ou
excluídas e a reconferência de afirmações afetadas. Resultados anteriores conservam
suas identidades; uma nova implementação não reescreve uma campanha já executada.
A revisão desta feature usa `revisoes/F11/parecer.md`.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F11-AC01:** F01–F10 e as evoluções selecionadas têm versões identificadas, pareceres reais e critérios
  atendidos; nenhum conflito material de fechamento está oculto na integração.
- [ ] **F11-AC02:** a entrega contém os cinco capítulos e complementos previstos,
  com texto completo, sem seções representadas apenas por links ou placeholders.
- [ ] **F11-AC03:** o mapa demonstra cobertura de Q1–Q4, OE1–OE4 e C01–C15,
  preservando distinções entre implementado, observado, parcial e não demonstrado.
- [ ] **F11-AC04:** valores, populações, unidades e políticas coincidem entre
  partes; nenhuma diferença científica foi resolvida sem fonte e registro.
- [ ] **F11-AC05:** citações resolvem para entradas verificadas, duplicatas foram
  tratadas e o mapa permite rastrear as chaves originais e finais.
- [ ] **F11-AC06:** figuras, tabelas e remissões apontam para destinos existentes;
  recursos necessários são acessíveis e marcadores internos saíram do texto final.
- [ ] **F11-AC07:** o template aplicado é identificado e verificável; sem template,
  a entrega se declara integração Markdown, sem alegar conformidade institucional.
- [ ] **F11-AC08:** o mapa registra versões e ajustes, e o parecer final relata
  verificações reais, sem substituir ou simular aprovação dos autores ou da banca.
- [ ] **F11-AC09:** o mapa relaciona todas as evoluções registradas como incluídas,
  adiadas ou excluídas, com justificativa; nenhuma adição selecionada ficou sem destino.
- [ ] **F11-AC10:** os impactos das evoluções foram reconciliados em método,
  resultados, discussão, conclusão e resumos; diferenças de base/campanha estão
  identificadas e não restam afirmações atuais contraditórias.

## Pedido de execução

Use `tcc2-coordenar` para conferir as entregas e integrar, e `tcc2-revisar` para
avaliar a versão resultante. A pasta F11 é exclusiva do integrador; seu revisor
trabalha no parecer separado.
