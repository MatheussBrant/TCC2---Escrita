---
id: F02
tipo: secao
capitulo: 2
destino: Referencial teórico — conceitos
saida: manuscrito/02-fundamentacao
inicio: imediato
fechamento_depende_de: []
---

# F02 — Fundamentação teórica

## Objetivo e escopo

Escrever a parte conceitual do Capítulo 2 com os conceitos necessários para compreender o método e
suas limitações. Vínculos: Q1–Q4; apoio a C03–C05/C08/C13. Ler o
[contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Vulnerabilidades, CWE/OWASP e diferença entre categoria, alerta e falha efetiva.
2. Análise estática/SAST: funcionamento conceitual, cobertura, falsos positivos,
   falsos negativos e limitações de inferir segurança pelo desaparecimento do alerta.
3. LLMs aplicadas a código e reparo: geração condicionada, variabilidade e limites.
4. Estratégias de instrução e raciocínio guiado como estrutura de resposta; não
   apresentar a saída textual como acesso ao raciocínio interno do modelo.
5. Contextualização por recuperação: princípio de RAG e recuperação determinística
   por categoria, com distinção em relação a embeddings e ranqueamento semântico.
6. Validação de reparos: testes funcionais/de segurança, regressões e necessidade
   de avaliar mais de um sinal de qualidade.

Selecionar a profundidade pelo uso desses conceitos nos capítulos seguintes.
Não escrever um catálogo enciclopédico de IA/segurança. A comparação entre artigos
fica em F03; implementação específica do código fica em F05; fórmulas operacionais
da pesquisa ficam em F04.

## Fontes para começar sem outras entregas

- Capítulo 2 e referências do TCC1, como ponto de partida para verificar originais.
- Fontes primárias dos conceitos: artigos e documentação oficial de SAST,
  CWE/OWASP e testes, com versão/data identificadas.
- `knowledge_base/README.md` e `src/pipeline/rag/retriever.py` do experimento
  apenas para alinhar a terminologia ao sistema, sem usá-los como prova teórica.
- Usar `tcc2-bibliografia` para conferir autores, metadados e trechos de apoio.

## Entregáveis e paralelismo

Criar `manuscrito/02-fundamentacao/texto.md`, `evidencias.md`, `entrega.md` e
`referencias.bib`. A bibliografia é local desta feature. Não aguardar F03 nem
editar suas citações; possíveis fontes duplicadas serão unificadas na F11.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F02-AC01:** os seis grupos de conceitos estão cobertos e cada um tem
  função explícita na compreensão do estudo, sem seções genéricas sem uso posterior.
- [ ] **F02-AC02:** diferencia alerta, vulnerabilidade, ocorrência e categoria,
  com fontes primárias e versões das taxonomias utilizadas.
- [ ] **F02-AC03:** explica o que SAST e testes permitem observar e suas limitações;
  nenhum dos dois é apresentado como prova absoluta de ausência de vulnerabilidades.
- [ ] **F02-AC04:** caracteriza corretamente o raciocínio guiado e o RAG por
  categoria efetivamente proposto, sem inventar busca vetorial no pipeline.
- [ ] **F02-AC05:** todas as citações possuem entrada bibliográfica conferida e
  localização de apoio em `evidencias.md`; fonte não acessada não aparece como verificada.
- [ ] **F02-AC06:** não incorpora resultados da campanha nem uma revisão comparativa
  disfarçada; usa remissões para F03/F04/F05 quando necessário.

## Pedido de execução

Use `tcc2-bibliografia` e `tcc2-redigir` para executar esta feature, produzindo
somente os arquivos da sua pasta e a autoavaliação dos critérios.
