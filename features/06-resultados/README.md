---
id: F06
tipo: secao
capitulo: 4
destino: Resultados e discussão — resultados observados
saida: manuscrito/06-resultados
inicio: imediato
fechamento_depende_de: [F04]
---

# F06 — Resultados

## Objetivo e escopo

Escrever a parte de resultados do Capítulo 4, com observações verificadas, tabelas e respostas descritivas
às Q1–Q4. É responsável por C09/C10/C12 e pela referência numérica da rodada.
Ler o [contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Identificação da campanha e justificativa de seu uso; separar antecedentes,
   pilotos, diagnósticos, replays e preflight.
2. Fluxo da amostra: catálogo → casos preparados/solicitados → observados/concluídos
   → tentativas/gerações → aceite por caso, com exclusões e ausências explicadas.
3. Q1: métricas globais e suas sensibilidades, preservação funcional, indeterminações
   e disponibilidade de RRIS; distinguir tentativas aceitas de casos aceitos.
4. Q2: resultados por estratégia e quantos casos alcançaram cada estágio da cadeia;
   taxas condicionais, sem interpretação causal da seleção sequencial.
5. Q3: distribuição por regra/CWE/OWASP e classificação de auditoria, com tamanho
   dos grupos, metadados ausentes e limites para grupos pequenos.
6. Q4: aplicação de patch, falhas funcionais/operacionais, cobertura SAST/testes,
   custos conhecidos/ausentes e tempo acumulado versus tempo de parede.
7. Exemplos rastreáveis de aceite/rejeição quando existirem, selecionados por
   critério declarado. Diferenciar inspeção estática do patch e validação dinâmica existente.

Não transformar o capítulo numa discussão geral de literatura (F07). Pode explicar
como ler tabelas e por que um número está indisponível, evitando especulação sobre
causas não observadas.

## Fontes para começar sem outras entregas

- Todos os artefatos da campanha listados na base comum: contrato, sessões,
  JSONL, CSVs, catálogo, manifestos e evidências individuais referenciadas.
- `src/pipeline/metrics/` e `scripts/reports/consolidate_metrics.py` na revisão fixada.
- Protocolo, critérios F/D e cobertura para interpretar os campos antes de F04 existir.
- Usar `tcc2-resultados` para reconciliação e `tcc2-redigir` para a apresentação.

## Entregáveis e paralelismo

Criar `manuscrito/06-resultados/texto.md`, `auditoria-resultados.md`,
`evidencias.md`, `entrega.md`, tabelas em `tabelas/` e scripts de derivação em
`scripts/` quando necessários. Scripts devem trabalhar offline, ler fontes e
gravar somente nesta pasta; não executar o pipeline ou substituir dados originais.
Se as tabelas forem transpostas dos CSVs oficiais sem transformação, registrar
arquivo, filtro e hash de origem já permite sua reprodução.

`auditoria-resultados.md` informa a seleção/reconciliação e é consumido por F07–F10.
A feature começa diretamente pelos artefatos. Para fechar, confrontar todas as
políticas com `operacionalizacao.md` de F04; divergências voltam à descrição do
método, não são resolvidas por escolher o denominador mais conveniente.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F06-AC01:** contrato, sessões, registros, CSVs e manifestos foram reconciliados;
  explica os 52 casos e 191 registros da base ou documenta divergência sem mascará-la.
- [ ] **F06-AC02:** identifica populações incluídas/excluídas e distingue tentativas,
  gerações, cache, replays e registros pós-aceite; não há duplicação silenciosa.
- [ ] **F06-AC03:** cada taxa apresenta n/d, população, F e política; valores
  ausentes/indeterminados não viram zero, e sensibilidades não são misturadas.
- [ ] **F06-AC04:** as quatro estratégias aparecem com sua exposição observada e
  seleção sequencial; estratégia sem observações não recebe sucesso/fracasso inventado.
- [ ] **F06-AC05:** tabelas por tipo incluem tamanho dos grupos, ausências e
  tratamento de múltiplas CWEs, sem inflar totais nem tratar falso positivo como falha confirmada.
- [ ] **F06-AC06:** RRIS é sustentada por evidência conjunta válida ou reportada
  como indisponível com razão; aceites isolados não são somados para fabricá-la.
- [ ] **F06-AC07:** custos/tempos têm unidade, completude e método; falhas de
  infraestrutura não são convertidas automaticamente em reprovação funcional.
- [ ] **F06-AC08:** exemplos de patches têm IDs, critério de seleção e evidência;
  seu alcance ilustrativo não é apresentado como auditoria de todos os reparos.
- [ ] **F06-AC09:** todas as tabelas/gráficos são regeneráveis ou rastreáveis por
  filtro/hash; totais e texto conferem, e `auditoria-resultados.md` registra D01–D08.
- [ ] **F06-AC10:** responde descritivamente Q1–Q4, inclusive quando a resposta
  for inconclusiva; o fechamento está coerente com a versão revisada de F04.

## Pedido de execução

Execute a auditoria e a escrita desta feature pelas skills `tcc2-resultados` e
`tcc2-redigir`, produzindo seus próprios artefatos sem alterar o experimento.
