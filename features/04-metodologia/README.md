---
id: F04
tipo: secao
capitulo: 3
destino: Metodologia e desenvolvimento — desenho e avaliação
saida: manuscrito/04-metodologia
inicio: imediato
fechamento_depende_de: []
---

# F04 — Metodologia experimental

## Objetivo e escopo

Escrever a parte de desenho experimental e avaliação do Capítulo 3, descrevendo o método efetivamente aplicado e suas diferenças
em relação ao TCC1. Vínculos: Q1–Q4; responsável por C01–C05/C07/C08, com apoio
a C09/C10/C13. Ler o [contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Natureza do estudo, perguntas, unidades de análise e recorte do Juice Shop.
2. Catálogos e amostra: histórico, ampliado, classificação da auditoria, exclusões,
   cobertura funcional e justificativa do recorte da campanha candidata.
3. Ambiente e identidades: alvo, ferramentas, modelo/provedor, parâmetros e
   versão de contrato. Distinguir configuração prevista e valores observados.
4. Estratégias P1–P4, diagnóstico P1L separado, recuperação por categoria e fatores
   adicionados a cada prompt; isolamento, ordem, parada e paralelização por caso.
5. Avaliação: aplicação do patch, R/F/M, F/D, baseline, falhas preexistentes,
   testes relacionados, comparabilidade SAST e resultados indeterminados.
6. Métricas e análise: fórmulas, numeradores/denominadores, população, estados
   ausentes, sensibilidade de F, aceite por caso, custo/tempo e requisitos da RRIS.
7. Mudanças do plano original e limites do desenho, remetendo à discussão aprofundada.

Criar `operacionalizacao.md` com as decisões D01–D08, definições, fontes e estado
de verificação. Explicitar separadamente regra de parada e F usado nas tabelas.
Esse arquivo é a referência metodológica que F06 deve confrontar com os registros.
Não declarar coleta aleatória, experimento balanceado, replicação independente
ou congelamento a priori quando as fontes não demonstrarem isso.

## Fontes para começar sem outras entregas

- TCC1, capítulo 3, especialmente §§3.4–3.12, e matriz de compromissos.
- Experimento: `docs/protocolo_experimental.md`, `docs/criterios_conjunto_d.md`,
  `docs/cobertura_funcional.md`, `docs/validacao_baseline_docker.md` e caderno.
- Contrato, catálogo e manifestos da campanha da base comum; registros e sessões
  para conferir o procedimento efetivo, sem esperar tabelas de F06.
- `src/pipeline/execucao_ampliada.py`, `src/pipeline/metrics/`,
  `src/pipeline/validation/` e `src/pipeline/sast/` na revisão fixada.

## Entregáveis e paralelismo

Criar `manuscrito/04-metodologia/texto.md`, `operacionalizacao.md`,
`evidencias.md`, `entrega.md` e referências/diagrama metodológico se usados.
Pode fechar sua primeira revisão pelas fontes originais, sem outro capítulo.
Se a reconciliação de F06 revelar divergência, atualizar a descrição afetada e
registrar a nova versão; não manter definições concorrentes entre capítulos.
F05 trata como o software implementa o método; F06 relata seus resultados.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F04-AC01:** método proposto e executado são distinguidos, com fonte para
  as mudanças de catálogo, ambiente, validação e denominadores.
- [ ] **F04-AC02:** unidade experimental, critérios de inclusão/exclusão e recorte
  da campanha candidata estão justificados, preservando falsos positivos e casos sem mapeamento.
- [ ] **F04-AC03:** modelo/provedor, alvo, parâmetros, regras, baseline e contrato
  são identificados pela campanha correta; não transporta configuração do preflight.
- [ ] **F04-AC04:** descreve P1–P4, contexto de cada estratégia, ordem e parada,
  deixando explícita a seleção sequencial e seus limites comparativos.
- [ ] **F04-AC05:** R/F/M e F/D, sensibilidades, indeterminação e falhas operacionais
  estão operacionalizados; a regra de parada não é confundida com F de apresentação.
- [ ] **F04-AC06:** a tabela de métricas informa fórmula, unidade, população,
  denominador e ausentes; RRIS tem seus requisitos próprios de medição.
- [ ] **F04-AC07:** `operacionalizacao.md` cobre D01–D08 com evidências, incluindo
  decisões ainda não justificáveis, e não declara resolvida uma escolha apenas por estar no código.
- [ ] **F04-AC08:** não apresenta resultados de eficácia nem detalhes extensos
  de implementação; as remissões a F05/F06 têm finalidade clara.

## Pedido de execução

Use `tcc2-historico`, `tcc2-resultados` para conferir o método nos registros e
`tcc2-redigir` para escrever esta feature. Produza somente sua pasta de saída.
