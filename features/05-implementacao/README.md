---
id: F05
tipo: secao
capitulo: 3
destino: Metodologia e desenvolvimento — implementação e evolução
saida: manuscrito/05-implementacao
inicio: imediato
fechamento_depende_de: [F04]
---

# F05 — Implementação e evolução do pipeline

## Objetivo e escopo

Escrever a parte de implementação e evolução do Capítulo 3, explicando como o software concretiza o método e quais
problemas orientaram sua evolução. Vínculos: Q1/Q4; responsável por C06/C11/C15.
Ler o [contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Visão arquitetural: entradas, módulos, fluxos e artefatos de uma tentativa.
2. Catálogo/identidade, coleta SAST, prompts/RAG e interface dos provedores.
3. Resposta estruturada, aplicação por âncoras, isolamento/restauração das worktrees
   e mudanças de aplicabilidade, incluindo a política de indentação quando pertinente.
4. Validação funcional, comparação de achados, estados de erro, cache e concorrência.
5. Registro de tentativas, contratos, hashes, sessões, consolidação e painel como apoio.
6. Evolução motivada por problemas: testes e ambiente, F/D, cobertura, comparador,
   Docker/safetyMode e extensão de provedor; separar entrega implementada de avaliação observada.
7. Cronograma previsto versus marcos observados, sem confundir data de commit com
   evento experimental nem inventar datas de defesa ou justificativas dos autores.

Organizar por decisões e mecanismos, usando o Git para sustentar a narrativa.
Não reproduzir todos os commits em prosa; o inventário completo é material de apoio.
Evitar tutorial de instalação (F09), repetição do desenho científico (F04) e
conclusões de eficácia (F06/F07).

## Fontes para começar sem outras entregas

- [Evolução sintetizada](../../docs/evolucao.md) e JSONL Git da coleta validada.
- Experimento: `docs/estrutura_projeto.md`, `docs/caderno_de_laboratorio.md`,
  `docs/aplicacao_ancoras.md`, `docs/auditoria/comparador_v2.md`, `docs/docker.md`.
- Código em `src/pipeline/`, `docker/`, `scripts/reports/` e contratos na revisão fixada.
- TCC1 §3.14 e datas dos registros/commits para C15; documentação da PoC quando disponível.

## Entregáveis e paralelismo

Criar `manuscrito/05-implementacao/texto.md`, `evidencias.md`, `entrega.md`
e um diagrama arquitetural editável em `figuras/`. Referências externas ficam
em `referencias.bib` quando utilizadas. A partir do código é possível começar
sem F04; para fechar, conferir se o diagrama/descrição implementa a operacionalização
descrita nela, registrando discrepâncias em vez de escondê-las.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F05-AC01:** o leitor consegue seguir uma tentativa desde o catálogo até
  o registro final; módulos e interfaces descritos existem na revisão citada.
- [ ] **F05-AC02:** o diagrama tem fonte editável e coincide com código/método,
  incluindo isolamento, validação e armazenamento, sem componentes fictícios.
- [ ] **F05-AC03:** decisões de evolução têm problema, alteração, fonte e efeito
  delimitado; mensagens de commit sozinhas não são usadas como prova de funcionamento.
- [ ] **F05-AC04:** diferencia replay/aplicabilidade, testes de software, validação
  experimental e geração LLM; não atribui eficácia a um benchmark ou preflight.
- [ ] **F05-AC05:** formatos de identificação e proveniência são explicados com
  exemplo rastreável, sem incorporar credenciais ou dados de `.env`.
- [ ] **F05-AC06:** C15 relaciona previsão e marcos documentados, identificando
  divergência temporal sem narrar intenção dos autores como fato não registrado.
- [ ] **F05-AC07:** limites da implementação e diferença entre suporte a provedores
  e campanhas executadas estão explícitos; o texto foi confrontado com F04.

## Pedido de execução

Use `tcc2-historico` e `tcc2-redigir` para produzir a seção e o diagrama com
evidências de código/commits na pasta exclusiva desta feature.
