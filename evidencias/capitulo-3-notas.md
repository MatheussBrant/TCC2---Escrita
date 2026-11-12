# Capítulo 3 — notas de evidência e revisão do primeiro rascunho

**Estado:** primeiro rascunho produzido a pedido do autor. Não constitui revisão
humana do experimento, validação dos patches ou aprovação da orientadora.

## Entrega e recorte

- Texto: [03-metodologia.md](../manuscrito/03-metodologia.md).
- Plano: [plano-paragrafos-capitulo-3.md](../docs/plano-paragrafos-capitulo-3.md).
- Linguagem: [criterios-escrita.md](../docs/criterios-escrita.md).
- Fonte original: [Markdown completo do TCC1](../TCC1___Caio_Lamego_e_Matheus_Brant-11.md).
- Experimento consultado: `../../tcc2-llm-sast-juiceshop`, revisão
  `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas na consulta.
- Campanhas finais: 06/11/2026, três modelos, 78 casos por campanha.
- Foram consultados código, documentação, contratos e artefatos selecionados.
  Não foram executados LLM, SAST, testes do alvo, inspeção integral de patches,
  novos experimentos ou verificações de referências externas nesta redação.
- Os documentos antigos de contexto, matriz e features citados pelo AGENTS.md
  continuam ausentes. Foram usados os planos atuais e a skill espelhada em
  `.claude/skills/tcc2-redigir/SKILL.md`. A solicitação é avulsa e determina
  explicitamente o manuscrito de destino.

## Mapa dos parágrafos e afirmações

Os IDs correspondem aos 54 parágrafos do plano. Tabelas, equações e diagrama
são elementos de apoio, não parágrafos adicionais. Os caminhos desta tabela
são relativos à raiz do experimento no SHA indicado acima.

| Plano / seção | Afirmação ou procedimento | Fonte e limite |
|---|---|---|
| P01–P05 / abertura e 3.1 | Desenho, unidades e Q5 | TCC1, plano atual, introdução de trabalho e decisão do autor nesta conversa. Q1–Q4 preservadas; Q5 é ampliação aceita pelo autor, não aprovação da orientadora. |
| P06–P09 / 3.2 | Alvo fixado e ambiente | `docs/protocolo_experimental.md` §1 e seção Docker; `Dockerfile`; `docker/referencia.json`; contratos finais; `outputs/cobertura_funcional/IMAGEM_81FE_D3_20261106/baseline/baseline_testes.json`. Baseline registra Node 24.14.0, npm 11.9.0 e UTC. Não atribuir às campanhas antigas a imagem atual. |
| P08 / 3.2 | Relação com PoC | Capítulo 4 do TCC1 e `outputs/README.md`. Usados como antecedentes; sem agregação de resultados com campanhas finais. |
| P10–P15 / 3.3 | Semgrep, regras e catálogo | `config/perfis/ampliado_piloto_v1/perfil.json`; `outputs/catalogos/ampliado_v1/`; `scripts/experimento/gerar_catalogo_ampliado.py`; protocolo §11. Perfil final reúne exportação de p/default e regras locais, sem repetir os filtros históricos de severidade/CWE como seleção do ampliado. |
| P13–P15 / 3.3 | 124/46/78 e triagem | `outputs/auditoria_sast/combinado-hZGD7r/triagem-final/resumo.json`, `alertas_classificados.json` e catálogo. 55/21/2 são rótulos arquivados; autoria/revisão humana pendentes. A classificação não exclui falsos positivos ou inconclusivos do recorte de 78. |
| P14 / 3.3 | 52 para 78 | `outputs/README.md`, configuração final, entradas de cobertura e contratos. Evolução de preparação, não mudança retroativa do conjunto da campanha antiga. |
| P16–P19 / 3.4 | Modelos e geração | `src/pipeline/etapas/e05_geracao_llm/modelos.py`; `cliente_openai.py`; contratos finais, campo inferencia. Temperatura 0 e máximo 4096 nos três; seed 42 apenas no mini; reasoning_effort=none nos Luna; cache LLM e cache de validação desligados. Justificativa específica da seleção dos Luna pendente. |
| P20–P25 / 3.5 | Prompts e resposta | `src/pipeline/etapas/e04_prompt/montagem.py`; `config/prompts/roteiro_raciocinio_guiado.md`; `src/pipeline/etapas/e05_geracao_llm/esquema.py`. Arquivo completo até 250 linhas, janela de 60 por lado; P1/P2 sem bloco do alerta, P3/P4 com diagnóstico e documentação. As restrições são instruções; o texto não afirma cumprimento garantido pelo modelo. |
| P26–P28 / 3.6 | RAG | `knowledge_base/README.md`, `_index.yaml`, `manifesto.json`; `src/pipeline/etapas/e03_contexto_rag/recuperacao.py`; protocolo §13. Base 2.1, 14 documentos; seleção CWE → categoria → genérico. Não foi auditada externamente a bibliografia dos documentos nesta tarefa. |
| P29–P34 / 3.7 | Fluxo, preparação e isolamento | `src/pipeline/orquestracao/preflight.py`, `campanha.py`; `src/pipeline/etapas/e06_aplicacao/worktrees.py`, `aplicador.py`; configuração final e contratos. Preflight não é tentativa de correção. Gerenciador restaura cópia antes/depois. |
| P32 / 3.7 | Parada versus classificação | `campanha.py`, `_aceita_estrita` e classificação final: parada usa sem_separacao; classificação_final usa criterio. Métricas delimitam a população no aceite original, não no instante da parada estrita. Isso explica possíveis registros pós-aceite sem atribuir problema à sequência do programa. |
| P35–P36 / 3.8 | R e M | `src/pipeline/etapas/e01_analise_sast/comparacao.py` (ocorrencias_contexto_v3), `semgrep.py`, `e07_validacao/medicao.py`; contratos. A v3 combina pareamento e contagem de mesma regra/arquivo; redução de contagem com alvo sem par permanece inconclusiva. R/M observam o detector, não equivalência semântica ou segurança absoluta. |
| P37–P39 / 3.8 | Baseline e cobertura | `config/cobertura_funcional_v8.yaml`, `mapa_testes_relacionados_v9.yaml`; baseline final; `e07_validacao/execucao_cobertura.py`, `cobertura.py`. Política relacionada_v2, testes por arquivos alterados; evidência insuficiente impede F positivo. Controles documentados em `outputs/cobertura_funcional/FINAIS_20261102/controles/controles.json` e etapas de ampliação. |
| P39 / 3.8 | Controles de testes | `scripts/experimento/validar_controles_cobertura.py` e relatórios arquivados. Alteração deliberada e expectativa de teste falho; não equivale a cobertura total nem a auditoria dos patches LLM. |
| P40–P41 / 3.8 | Conjunto D e sensibilidade | `docs/criterios_conjunto_d.md`; `config/conjunto_d_cobertura_v3.json`; `e07_validacao/conjunto_d.py`, `execucao_cobertura.py`. Critérios d/e são posteriores aos a/b/c; e surgiu após campanha descartada. Não afirmar pré-registro integral do conjunto final. Reexecução compara interseção das falhas novas e verifica comparabilidade dos testes. |
| P42–P45 / 3.9 | Métricas, populações e custo | `e09_metricas/calculo.py`, `normalizacao.py`, `leitura.py`; consolidados finais. TRV considera todas as tentativas da população; TRI/TPF/TNINI usam medidos; ausência não é medição negativa. CR usa casos solicitados. Custo e tempos podem considerar registros além da população científica, conforme o campo do consolidado; manter esse escopo explícito nas tabelas futuras. |
| P46 / 3.9 | Avaliação conjunta | `scripts/experimento/avaliacao_conjunta_rris.py`, seleção, aplicação e validação; `e09_metricas/rris.py`; `outputs/rris/`. Perfil é conferido contra o contrato; conflitos são registrados. Nas três evidências atuais o conjunto não é funcionalmente validado; esse resultado pertence ao capítulo 5 e não foi antecipado numericamente. |
| P47–P51 / 3.10 | Registro e análise | `e08_registro/registro.py`, `e09_metricas/calculo.py`, consolidados, contratos e plano da escrita. Registro original, população principal e alternativas de F têm escopos distintos. Inspeção qualitativa não foi afirmada como concluída. |
| P52–P54 / 3.11 | Limites e IA | Condições do recorte, código e documentação anteriores; uso de IA na escrita observado nesta conversa. Ferramentas e revisão do desenvolvimento dependem dos autores. Não foi alegada replicação independente em outra máquina. |

## Identificação das campanhas

| Modelo | Execução |
|---|---|
| GPT-6 Luna | AMP_REAL_20261106T105533Z_aa697342 |
| GPT-5.6 Luna | AMP_REAL_20261106T125801Z_0eb68fe4 |
| GPT-4.1 mini | AMP_REAL_20261106T151004Z_f49ac0d2 |

Contratos: `outputs/campanha_docker/<EXECUCAO>/contrato_execucao.json`.
Métricas com evidência conjunta: `outputs/rris/<EXECUCAO>_METRICAS/metricas.json`.
As três campanhas registram o mesmo alvo, perfil SAST, comparador, baseline,
base RAG e política funcional. As configurações de geração dos modelos diferem.

## Elementos de apoio

- Tabela 1: alvo e ambiente; parâmetros lidos do baseline e contratos.
- Tabela 2: composição do catálogo; método, não taxa de correções.
- Tabela 3: parâmetros de geração por modelo; contratos de inferência.
- Tabela 4: presença dos elementos em P1–P4; montador de prompts.
- Figura 1: diagrama Mermaid do procedimento; substituir as imagens antigas do
  fluxo evita conservar uma descrição que não explicita a regra de parada.
- Tabela 5: três interpretações de F; critérios do conjunto D.
- Tabela 6 e equações: métricas; denominadores atuais conferidos no calculador.

A numeração de tabelas e figuras é local ao rascunho e deverá ser reconciliada
na integração com os demais capítulos. O diagrama deverá ser exportado no
formato necessário ao template final. Não foi afirmada conformidade ABNT.

## Mudanças em relação ao TCC1

1. Procedimentos propostos passaram a descrições da execução observada.
2. Contexto e objeto foram reunidos em 3.2, com ambiente Docker.
3. Seleção e SAST foram reunidos em 3.3, explicitando escopo, regras locais,
   perfil fixado, catálogo por ocorrência e triagem que o texto antigo não previa.
4. Foi criada seção própria dos modelos e da comparação associada à Q5.
5. Prompts e RAG foram atualizados ao conteúdo e à base realmente utilizados.
6. Fluxo e parada foram precisados; não se afirmou que a classificação principal
   e o critério operacional de parada são idênticos.
7. Foi criada seção de validação com baseline, cobertura relacionada, controles,
   testes adicionais e evolução do conjunto D.
8. Foram corrigidos os denominadores das métricas complementares e acrescentadas
   as distinções por caso, por tentativa e por avaliação conjunta.
9. Rastreabilidade permaneceu, mas árvore de diretórios e detalhes de aplicação
   foram reservados ao capítulo 4. Taxas de eficácia ficaram para o capítulo 5.
10. O cronograma prospectivo foi retirado deste rascunho conforme a recomendação
    do plano; os autores ainda podem solicitar uma síntese histórica em apêndice.
11. A declaração de revisão integral do conteúdo gerado por IA não foi transposta.

## Pendências para os autores

| ID | Local | Informação necessária |
|---|---|---|
| PE01 | 3.3 / P15 | Resolvida para a descrição do procedimento em 09/11/2026: origem dos 55 confirmados e dois inconclusivos rastreada nos registros de triagem e no código de consolidação. Revisão humana dos 21 falsos positivos confirmada pelo autor. Não foi inferida revisão humana nominal dos demais grupos; ver atualizações abaixo. |
| PE02 | 3.4 / P16 | Justificativa específica da escolha dos dois modelos Luna e contexto dessa decisão. |
| PE03 | 3.10 / P51 | Se a inspeção qualitativa dos patches foi feita, por quem, com qual método e sobre quais casos. |
| PE04 | 3.11 / P54 | Ferramentas e atividades de IA no desenvolvimento e nível de revisão humana realizado. |
| PE05 | Integração | Posição definitiva da declaração de IA, da PoC e do cronograma histórico; revisão da organização do trabalho na introdução. |
| PE06 | Pesquisa | Alinhamento acadêmico da Q5 com a orientadora; a aceitação do autor não foi tratada como aprovação dela. |

Os itens ainda pendentes mantêm marcações específicas no manuscrito; PE01 foi esclarecida nas atualizações de 09/11/2026.
Esta versão não inventa motivos de escolha ou validações para preencher lacunas.

## Verificações desta entrega

- Cobertura dos 54 parágrafos do plano, com 11 seções e abertura.
- Preservação de Q1–Q4; inclusão da comparação dos modelos conforme Q5.
- Conferência de parâmetros e condições comuns nos contratos das três campanhas,
  incluindo hashes do perfil, baseline, índice e manifesto do RAG contra os arquivos atuais.
- Separação de definições funcionais, parada operacional e população de análise.
- Ausência de taxas de sucesso e conclusões comparativas no capítulo metodológico.
- Conferência estrutural de tabelas, equações e diagrama e das pendências no texto.
- Fonte Markdown integral do TCC1 e repositório experimental preservados.
- Leitura crítica de consistência pelo próprio redator; não houve revisor independente.

## Mapa de abertura dos parágrafos

- **P01 — Abertura:** Este capítulo apresenta os procedimentos metodológicos utilizados para avaliar um pipeline automatizado de cor…
- **P02 — Abertura:** O experimento foi conduzido no OWASP Juice Shop, a partir dos alertas identificados pela ferramenta SAST. As s…
- **P03 — 3.1 Caracterização e desenho da pesquisa:** Esta pesquisa é um estudo empírico de natureza aplicada, com abordagem predominantemente quantitativa. Seu car…
- **P04 — 3.1 Caracterização e desenho da pesquisa:** O desenho do estudo manteve as perguntas de pesquisa do TCC1 sobre a viabilidade do pipeline, as estratégias d…
- **P05 — 3.1 Caracterização e desenho da pesquisa:** Foram adotadas três unidades de organização dos dados. Um caso corresponde a uma ocorrência de alerta identifi…
- **P06 — 3.2 Objeto de estudo e ambiente experimental:** O OWASP Juice Shop foi selecionado por ser uma aplicação web de código aberto, deliberadamente vulnerável, com…
- **P07 — 3.2 Objeto de estudo e ambiente experimental:** Foi utilizada a versão 20.1.1 do projeto, implementada principalmente em JavaScript e TypeScript, com Node.js,…
- **P08 — 3.2 Objeto de estudo e ambiente experimental:** A prova de conceito do TCC1 utilizou casos reduzidos em Python e análise estática com Bandit para verificar a …
- **P09 — 3.2 Objeto de estudo e ambiente experimental:** As campanhas finais foram executadas em um ambiente Docker padronizado, com o projeto-alvo e suas dependências…
- **P10 — 3.3 Análise estática e constituição do catálogo:** O Semgrep foi utilizado como ferramenta SAST por oferecer regras compatíveis com JavaScript e TypeScript e per…
- **P11 — 3.3 Análise estática e constituição do catálogo:** A detecção combinou regras disponibilizadas pelo Semgrep e regras locais elaboradas no desenvolvimento do expe…
- **P12 — 3.3 Análise estática e constituição do catálogo:** Para as campanhas finais, o conjunto de regras e as exclusões foram reunidos em um perfil fixado e identificad…
- **P13 — 3.3 Análise estática e constituição do catálogo:** O scan combinado arquivado produziu 124 alertas, dos quais 46 foram classificados como fora do escopo. Os 78 r…
- **P14 — 3.3 Análise estática e constituição do catálogo:** A preparação do catálogo e a preparação da avaliação funcional ocorreram em etapas distintas. Uma campanha ant…
- **P15 — 3.3 Análise estática e constituição do catálogo:** Para cada caso, foram registrados identificador, regra, arquivo e localização, mensagem, severidade, trecho de…
- **P16 — 3.4 Modelos de linguagem e condições de geração:** O experimento incluiu os modelos GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna. O GPT-4.1 mini já havia sido previst…
- **P17 — 3.4 Modelos de linguagem e condições de geração:** As condições de geração foram registradas para cada modelo. Foram mantidos temperatura zero e limite de 4.096 …
- **P18 — 3.4 Modelos de linguagem e condições de geração:** Cada modelo foi executado em uma campanha própria sobre os mesmos 78 casos, com as estratégias P1 a P4 e o mes…
- **P19 — 3.4 Modelos de linguagem e condições de geração:** As chamadas foram submetidas a limites configuráveis de quantidade e consumo, com registro de tokens, custo in…
- **P20 — 3.5 Estratégias de prompt:** Foram utilizadas quatro estratégias de prompt, mantendo os elementos previstos no TCC1. Todas receberam uma de…
- **P21 — 3.5 Estratégias de prompt:** A estratégia P1 correspondeu ao prompt simples. O modelo recebeu o código e uma instrução direta para identifi…
- **P22 — 3.5 Estratégias de prompt:** A estratégia P2 acrescentou um roteiro de raciocínio guiado ao conteúdo de P1. O roteiro orientou a análise da…
- **P23 — 3.5 Estratégias de prompt:** A estratégia P3 incluiu o diagnóstico SAST e um documento técnico recuperado da base de conhecimento. O diagnó…
- **P24 — 3.5 Estratégias de prompt:** A estratégia P4 combinou o conteúdo de P3 com o roteiro de raciocínio guiado. Em todas as estratégias, foram m…
- **P25 — 3.5 Estratégias de prompt:** As respostas foram solicitadas em JSON, com campos para identificação do problema, causa, estratégia de correç…
- **P26 — 3.6 Recuperação de contexto por RAG simplificado:** O RAG foi implementado por recuperação de documentos técnicos em Markdown, sem utilização de embeddings ou bus…
- **P27 — 3.6 Recuperação de contexto por RAG simplificado:** A seleção do documento seguiu uma ordem definida. Primeiro, o pipeline procurou uma correspondência para as CW…
- **P28 — 3.6 Recuperação de contexto por RAG simplificado:** A escolha do RAG simplificado manteve o foco na avaliação do contexto fornecido ao modelo, em vez de transform…
- **P29 — 3.7 Procedimento de execução do pipeline:** O pipeline automatizou a preparação das entradas, a geração das correções e sua avaliação. Para cada caso, o f…
- **P30 — 3.7 Procedimento de execução do pipeline:** Antes das tentativas, foi realizada uma verificação inicial, denominada preflight. Nessa etapa, foram conferid…
- **P31 — 3.7 Procedimento de execução do pipeline:** As tentativas utilizaram cópias de trabalho separadas do projeto, gerenciadas por Git worktrees. Cada cópia fo…
- **P32 — 3.7 Procedimento de execução do pipeline:** As estratégias foram executadas na ordem P1, P2, P3 e P4. A interrupção operacional de um caso exigiu aceite n…
- **P33 — 3.7 Procedimento de execução do pipeline:** Respostas com formato inválido, edições que não encontravam o trecho original e alterações fora do escopo perm…
- **P34 — 3.7 Procedimento de execução do pipeline:** As campanhas finais foram configuradas para até quatro casos em paralelo, mantendo sequenciais as estratégias …
- **P35 — 3.8 Validação das correções:** O critério R representou a remoção do alerta original. Para verificá-lo, foram comparadas as ocorrências ident…
- **P36 — 3.8 Validação das correções:** O critério M representou a ausência de novos alertas na reanálise do projeto sob o perfil fixado. A avaliação …
- **P37 — 3.8 Validação das correções:** A preservação funcional foi avaliada em relação a uma execução de referência dos testes, denominada baseline. …
- **P38 — 3.8 Validação das correções:** Em cada tentativa, foram selecionados os grupos de testes relacionados aos arquivos efetivamente alterados, in…
- **P39 — 3.8 Validação das correções:** Durante a preparação, foram acrescentados testes para ampliar a avaliação de comportamentos que não estavam su…
- **P40 — 3.8 Validação das correções:** A natureza deliberadamente vulnerável do Juice Shop exigiu distinguir testes funcionais de testes que dependia…
- **P41 — 3.8 Validação das correções:** Foram mantidas três interpretações de F: sem separação, por marcador e por critérios, resumidas na Tabela 5. A…
- **P42 — 3.9 Métricas de avaliação:** A métrica principal foi a Taxa de Remediação Validada (TRV), mantendo o conceito apresentado no TCC1. Para cad…
- **P43 — 3.9 Métricas de avaliação:** As métricas complementares foram a Taxa de Remoção de Issues (TRI), a Taxa de Preservação Funcional (TPF), a T…
- **P44 — 3.9 Métricas de avaliação:** Também foi calculada a proporção de casos com pelo menos uma tentativa aceita em relação aos casos solicitados…
- **P45 — 3.9 Métricas de avaliação:** A comparação entre modelos considerou ainda tokens de entrada e saída, custo conhecido das chamadas, tempo de …
- **P46 — 3.9 Métricas de avaliação:** A Redução Relativa de Issues de Segurança (RRIS) foi utilizada para examinar a variação dos alertas após a apl…
- **P47 — 3.10 Registro e análise dos dados:** Os dados foram organizados para permitir o acompanhamento de cada caso desde o alerta inicial até sua avaliaçã…
- **P48 — 3.10 Registro e análise dos dados:** A população principal foi formada pelas tentativas reais das estratégias previstas, delimitadas conforme o pri…
- **P49 — 3.10 Registro e análise dos dados:** A análise das estratégias e dos tipos de problema foi organizada por modelo, regra, CWE e categoria OWASP, qua…
- **P50 — 3.10 Registro e análise dos dados:** Para responder à Q5, a comparação entre os três modelos foi organizada a partir dos mesmos casos solicitados e…
- **P51 — 3.10 Registro e análise dos dados:** As taxas por estratégia foram interpretadas considerando que P2, P3 e P4 recebem os casos que não interrompera…
- **P52 — 3.11 Limitações metodológicas e uso de inteligência artificial:** A utilização de uma única aplicação deliberadamente vulnerável limita a generalização dos resultados para outr…
- **P53 — 3.11 Limitações metodológicas e uso de inteligência artificial:** A sequência das estratégias, a variabilidade das respostas e as diferenças de parâmetros entre modelos também …
- **P54 — 3.11 Limitações metodológicas e uso de inteligência artificial:** Ferramentas de inteligência artificial generativa foram utilizadas como apoio à organização e à redação deste …

SHA-256 do manuscrito antes da redação: `ec63f064779f5fa508eb9153b91a9c788cfaf8e9500c8e5dd525f7ef45d3fe7e`.
SHA-256 do rascunho: `879ace966216f4eb109f76732a1192f782e63251e1a8f437eeabe70bd6de46f9`.

## Atualização de 09/11/2026 — revisão dos falsos positivos

O usuário confirmou que os 21 casos apontados pela LLM como falsos positivos
foram revisados e confirmados por ambos os autores, com exame do código, contexto
do alerta e regra do Semgrep. A seção 3.3 foi atualizada com essa informação e
exemplos das justificativas arquivadas. A origem e o procedimento de revisão dos
rótulos confirmados e inconclusivos permanecem pendentes. Ver
[registro da confirmação e dos limites](triagem-revisao-humana-2026-11-09.md).
As notas anteriores e o hash do primeiro rascunho correspondem à versão original
da redação, anterior a essa atualização. Não houve nova campanha ou mudança de métricas.

## Complemento de 09/11/2026 — origem dos confirmados e inconclusivos

A pendência de descrever a origem e o procedimento documentado desses rótulos
foi resolvida por rastreamento de 57 casos: 56 com referências históricas diretas
e um com revisão explícita. Os status constam das entradas de triagem versionadas,
são aplicados por identidade do alerta e transferidos ao catálogo com os motivos.
Foram explicitadas no texto as razões dos dois inconclusivos e o alcance do
rótulo confirmado, sem alegar exploração dinâmica ou revisão humana de todos.
Ver [rastreio, fontes e limites](triagem-origem-2026-11-09/LEITURA.md).
A ausência de comprovação nominal de revisão humana dos demais grupos não foi
preenchida por inferência; o texto passou a descrever a evidência disponível.


## Conferência das três campanhas — 10/11/2026

Revisão documental individual registrada em [revisao-campanhas-2026-11-10/LEITURA.md](revisao-campanhas-2026-11-10/LEITURA.md), com script e resultados rastreáveis. Confirmados término, cobertura dos 78 casos por campanha, igualdade das condições comuns, parâmetros de geração e integridade de 5.623 referências de artefatos. A Seção 3.7 passou a nomear as campanhas por modelo e explicitar as condições compartilhadas. A revisão não altera os resultados nem resolve a pendência de exclusão dos falsos positivos das métricas.


## Revisão de clareza e fórmulas — 10/11/2026

A pedido do autor, foram ajustadas as Seções 3.8–3.11:

- F foi definido como preservação funcional, com explicação dos valores 1, 0 e indeterminado. “Regressões” no trecho apontado foi substituído pela descrição de novos problemas no funcionamento.
- Foram retiradas a ressalva solicitada sobre cobertura completa e a narrativa de ampliação do conjunto D após exploração descartada. O histórico permanece nas evidências anteriores; a retirada editorial não altera a origem dos critérios.
- A Tabela 5 passou a explicar diretamente o efeito das falhas em F.
- Foram recuperadas as fórmulas e definições de R, F, M, índice j, total m, TRV, TRI, TPF, TNINI, TFF e RRIS da seção 3.9 original, adaptando os denominadores às medições disponíveis. A lista de tabelas foi sincronizada.
- A soma da TRV foi restrita ao conjunto de tentativas aplicadas com R/F/M medidos; o denominador continua incluindo todas as tentativas da população. Essa notação evita multiplicar valores indeterminados e é equivalente à regra de contagem já utilizada. Os conjuntos e seus tamanhos foram definidos antes das fórmulas.
- A suposição de que o sucesso em Pₓ seria mantido em uma estratégia posterior foi declarada pelo autor nesta conversa. Foi registrada como suposição do desenho, não como resultado demonstrado. O código comprova a parada sequencial; não comprova o sucesso nas estratégias não executadas.

Fontes: texto integral original, Seção 3.9; experimento no commit `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, `src/pipeline/etapas/e07_validacao/execucao_cobertura.py` e `src/pipeline/orquestracao/campanha.py`; fórmulas e denominadores conferidos contra os CSVs da análise existente no apoio do Capítulo 5.

Não foram alterados resultados, gráficos ou dados experimentais. A pendência de exclusão dos falsos positivos continua separada desta revisão textual.


## Resolução da pendência de inspeção dos patches — 10/11/2026

O autor informou que não houve inspeção manual dos patches: a avaliação utilizou as métricas e verificações automatizadas. Resolvida a pendência sobre esse procedimento (PE03 / PE5-03), com alinhamento das Seções 3.10 e 5.6. Os exemplos permanecem como análise documental com apoio automatizado, sem revisão humana das correções. A revisão humana dos falsos positivos é uma atividade distinta e não foi alterada. Ver [declaração, casos e limites](analise-patches-2026-11-10.md).


## Declaração de uso de IA — 10/11/2026

PE04 resolvida mediante confirmação do autor: Codex e Claude Code apoiaram a escrita de código e testes, com revisão humana, e a revisão gramatical dos textos. Atualizada a Seção 3.11, preservando a distinção entre revisão do desenvolvimento e avaliação automatizada dos patches das campanhas. Ver [confirmação e limites](uso-ia-2026-11-10.md). Não foi declarada validação integral de conteúdo ou código.

## Ordem entre testes e reanálise SAST na Seção 3.9 — 12/11/2026

Corrigida a pedido do Caio. A lista de etapas trazia a reanálise SAST (etapa 10) antes da compilação e dos testes
(etapa 11), e o parágrafo após a Figura 2 afirmava que a reanálise foi executada antes dos testes. Nas três campanhas
finais (`politica_validacao: relacionada_v2` nos contratos), a ordem foi compilação, grupos de testes e só depois o
Semgrep: `src/pipeline/etapas/e07_validacao/execucao_cobertura.py`, função `validar`, chama o `callback` do SAST depois
do laço dos grupos (experimento em `2e8f9a9`). A Figura 2 já mostrava essa ordem. As etapas 10 e 11 foram trocadas e o
parágrafo passou a dizer que a reanálise veio depois das verificações de compilação e dos testes, como na figura.
Nenhuma outra parte do capítulo foi alterada. SHA-256 do capítulo após a correção:
`cc8753e396122cb8f957b67a43dc65567cfc9fae16c1dc42f0e621d141288b3b`.
