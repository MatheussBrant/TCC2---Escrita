# Capítulo 4 — notas de evidência e revisão do primeiro rascunho

**Estado:** rascunho produzido a pedido do autor, sem revisão independente ou
aprovação da orientadora. O texto descreve a implementação e exemplos registrados;
não equivale a auditoria de segurança do código ou dos patches.

## Entrega e recorte

- Manuscrito: [04-implementacao.md](../manuscrito/04-implementacao.md).
- Plano: [plano-paragrafos-capitulo-4.md](../docs/plano-paragrafos-capitulo-4.md).
- Linguagem: [criterios-escrita.md](../docs/criterios-escrita.md).
- Continuidade: [metodologia](../manuscrito/03-metodologia.md).
- Fonte experimental: `../../tcc2-llm-sast-juiceshop`, revisão
  `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas na consulta.
- O capítulo original [04-prova-de-conceito.md](../manuscrito/04-prova-de-conceito.md)
  e os demais manuscritos existentes foram preservados.
- Não foram realizadas chamadas a LLMs, análises Semgrep, testes do alvo, preparação de worktrees ou
  nova campanha. Também não foi iniciado o painel ou produzida captura de tela.
- Consulta de código e artefatos selecionados, sem inspeção integral do repositório.
- Foram usados o plano atual e a skill de redação espelhada em `.claude/skills/`.
  Arquivos antigos de contexto, matriz e features não estão disponíveis na árvore
  atual; o pedido avulso define explicitamente os destinos desta entrega.

## Mapa de evidências por parágrafo

Os caminhos abaixo são relativos à raiz do experimento na revisão registrada.
Nos grupos de código, nomes abreviados compartilham o diretório do primeiro
arquivo indicado; os módulos de etapas e de orquestração ficam sob src/pipeline/.

| Plano / seção | Conteúdo sustentado | Fontes e limites |
|---|---|---|
| C4-P01–P05 / abertura e 4.1 | Visão geral, dutos e filtros e fluxo | `src/pipeline/README.md`, `orquestracao/campanha.py`, organização real de `src/pipeline/`. O mapa de arquitetura tem referências antigas ao comparador e à ausência de RRIS; foi usado para organização, não para perpetuar essas afirmações. |
| C4-P06–P09 / 4.2 | Tecnologias, diretórios e Docker | README, Dockerfile, compose.yaml, Makefile e docs/docker.md. Código do pipeline montado fora da imagem; dependências e alvo preparados na referência. Não foram lidas credenciais nem executadas rotinas que carreguem .env. |
| C4-P10–P14 / 4.3 | SAST e catálogo | `etapas/e01_analise_sast/semgrep.py`, `perfil.py`, `etapas/e02_catalogo/catalogo.py`, `scripts/experimento/gerar_catalogo_ampliado.py`, `scripts/auditoria/classificar_scan_combinado.py`. O gerador utiliza classificação arquivada; não comprova sua autoria humana. |
| C4-P11 / 4.3 | Exemplo de regra local | `rules/rodada4/dynamic-mongodb-where.yaml` e `.ts`; caso AMP20721d202c8b96d6. Regra busca find com $where construído por concatenação ou interpolação. O texto não afirma exploração demonstrada nem equivalência funcional automática. |
| C4-P15–P18 / 4.4 | Prompt, janela e recuperação | `etapas/e04_prompt/montagem.py`, `e03_contexto_rag/recuperacao.py`, knowledge_base/_index.yaml e manifesto.json. P1 do exemplo recebeu arquivo completo de 29 linhas, sem RAG e sem bloco do alerta; abertura reproduzida literalmente. |
| C4-P19–P22 / 4.5 | Provedor, modelos e schema | `etapas/e05_geracao_llm/provedor.py`, `modelos.py`, `cliente_openai.py`, `esquema.py` e contratos finais. Suporte Colab não é condição da campanha final; cache de respostas e validação desligados. JSON reproduz somente o campo edicoes de resposta real. |
| C4-P23–P25 / 4.6.1 | Worktrees e preparação | `etapas/e06_aplicacao/worktrees.py`, `docker/workspace.py`, `scripts/preparacao/preparar_alvo.sh`. Preparação Docker copia conteúdo verificado da referência; o script fora do Docker usa outro fluxo. Não afirmar que a preparação Docker instala novamente dependências em cada tentativa. |
| C4-P26–P28 / 4.6.2 | Reserva e restauração | `worktrees.py`: fila, verificação de commit e dependências, reserva entre processos e limpeza. Restauração usa checkout e clean de não ignorados com preservação explícita de node_modules; não equivale a eliminar todos os artefatos ignorados ou isolar rede. |
| C4-P29–P31 / 4.6.3 | Aplicação e diff | `aplicador.py`, `indentacao.py`, `orquestracao/campanha.py` e patch do exemplo. O aplicador planeja edições antes da gravação; não se afirmou transação de escrita atômica entre múltiplos arquivos. Correspondência e aplicação não comprovam validade da correção. |
| C4-P32–P37 / 4.7 | Comparador e avaliação funcional | `e07_validacao/medicao.py`, `cobertura.py`, `execucao_cobertura.py`, `conjunto_d.py`; `e01_analise_sast/comparacao.py`; mapas, baseline e contrato. Comparador v3 e política relacionada_v2; não foi afirmada execução da suíte ampla por tentativa. |
| C4-P37 / 4.7 | Teste adicional de CAPTCHA | `tests/functional/juice_shop/captcha_arithmetic.test.ts`. Caso 2+3*4=14 está na lista; asserções verificam expressão, resposta, persistência, rejeição de resposta incorreta e feedback aceito. O texto descreve a verificação implementada, não uma nova execução nesta tarefa. |
| C4-P38–P42 / 4.8 | Coordenador, retomada, lançador e painel | `orquestracao/campanha.py`, `preflight.py`, `executar.py`, `painel.py`, `painel/controle.py`, `servidor.py`, `web/` e docs/guias/painel_local.md. Parada sem_separacao e classificação criterio; painel usa comandos comuns. Parada é cooperativa; não atribuir ao painel retomada automática de processos de outro terminal. |
| C4-P39 / 4.8 | Alcance da concorrência | `campanha.py`, `worktrees.py`, cliente_openai.py e componentes de testes. Existem controles adicionais para recursos comuns; cliente coordena envios e orçamento. O texto não afirma chamadas paralelas irrestritas nem speedup medido. |
| C4-P43–P45 / 4.9 | Registro e consolidação | `e08_registro/registro.py`, `e09_metricas/leitura.py`, `calculo.py`, `publicacao.py`, `outputs/README.md` e registro do exemplo. JSONL conserva uma linha por tentativa; classificação de pós-aceite pertence à consolidação. |
| C4-P46 / 4.9 | Avaliação conjunta | `scripts/experimento/avaliacao_conjunta_rris.py`, `e09_metricas/rris.py` e outputs/rris. Incompatibilidades são registradas, sem afirmar integração de todos os aceites. Taxas e situação funcional agregada ficam para o capítulo 5. |
| C4-P47 / 4.9 | Possibilidade de replicação | `docker/referencia.py`, ações exportar/importar, Makefile e docs/docker.md. Código implementa docker image save/load com conferência da referência. Não houve exportação/importação nesta tarefa ou comprovação de reprodução em outra máquina. |

## Caso ilustrativo selecionado

- Campanha: `AMP_REAL_20261106T151004Z_f49ac0d2`.
- Modelo solicitado: GPT-4.1 mini; estratégia P1; resposta registrada sem cache.
- Caso: `AMP20721d202c8b96d6`, arquivo `routes/trackOrder.ts`, alerta na linha 18.
- Regra: `tcc.mongodb.security.dynamic-where`, associada a CWE-943.
- Classificação arquivada do caso: confirmado; esse rótulo não comprova revisão humana.
- Tentativa: `AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2`.
- Critério de seleção editorial: patch de uma linha e artefatos completos que
  permitem explicar entrada, prompt, resposta, aplicação e avaliação de forma curta.
  Não foi selecionado para sustentar uma conclusão de eficácia ou representatividade
  estatística; o capítulo usa-o como ilustração de funcionamento.
- Registro: R=1, M=1, F_criterio=1, F_sem_separacao=0. A classificação principal
  é aceita, mas não houve aceite estrito nessa tentativa. Esse fato é coerente
  com a distinção descrita no capítulo 3; os valores não foram usados para
  antecipar comparação de resultados no capítulo 4.
- A resposta chama a consulta de MongoDB; o texto acadêmico se limita à expressão
  presente na coleção de pedidos, sem assumir todas as alegações semânticas do modelo.
- Conferidos existência e hashes dos sete artefatos listados pelo registro.

**Arquivos do exemplo:** relativos a `outputs/campanha_docker/` seguido do nome
 da campanha acima. As notas permitem recuperar o conteúdo integral dos excertos.

| Artefato | SHA-256 registrado e conferido |
|---|---|
| `prompts/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2.json` | `77dece2b7db73152d51851ce096194e83dcabd544c826e783b33ffc91613b1ce` |
| `respostas_llm/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2.json` | `3fda83bf5d9278275ccaf939ab2c296ce493ea4c6f8d0ea1dd005f477d5a63c9` |
| `patches/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2.diff` | `ce9d415053cd9d7dd5c457f72de04ddac4b979e3f1979a7c3718c97ea02a7641` |
| `sast_depois/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2_raw_evidencia_funcional.json` | `f909bfed32fe4b378afed960554f9f9c53ea1946b9652cdde8c706758dae6dfd` |
| `comparacoes/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2.json` | `655e181a78c18809ce89ad5253f53b9824959e87abd41bf71ee118c930c0aa73` |
| `sast_depois/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2_raw.json` | `f83cfb2e3feee5f799113598b9dd5f88942d3afc84d13517a838f9db3fb1d5df` |
| `testes/AMP20721d202c8b96d6_SEMOWASP_OUTRO_P1_AMP_REAL_20261106T151004Z_f49ac0d2.json` | `3af98e822ce488f3d60ec178297046d55019a5adcfbc5ad55555e948356a9704` |

## Recursos usados no texto

- Figura 1: diagrama Mermaid dos componentes principais, elaborado a partir do código.
- Figura 2: diagrama Mermaid das worktrees; não representa máquinas independentes.
- Tabelas 1–3: tecnologias, diretórios e grupos de arquivos de resultados.
- Excerto do prompt: início literal da mensagem P1, arquivo completo com 29 linhas.
- Excerto JSON: somente edicoes, extraído da resposta arquivada sem inventar campos.
- Excerto diff: linhas removida/adicionada do patch arquivado.

As figuras são diagramas explicativos, não capturas de execução. A numeração é
local ao capítulo e deverá ser reconciliada com os demais capítulos na integração.
Não foi afirmada conformidade com template ou ABNT. Nenhuma imagem de painel foi
simulada ou inserida como se fosse captura real.

## Pendências para revisão

| ID | Local | Ação necessária |
|---|---|---|
| PE4-01 | 4.8 / C4-P42 | Inserir uma ou duas capturas reais do painel, identificando contexto e informações exibidas. Pendente também no manuscrito. |
| PE4-02 | Integração | Conferir a posição de referências conceituais de arquitetura e Git worktrees no capítulo 2; bibliografia externa não foi verificada nesta tarefa. |
| PE4-03 | Integração | Exportar os diagramas no formato exigido pelo template e reconciliar numeração de figuras, tabelas e excertos. |
| PE4-04 | Estrutura | Decidir o destino da apresentação detalhada da PoC do TCC1, preservada em arquivo separado. |
| PE4-05 | Revisão dos autores | Conferir clareza, profundidade, terminologia e adequação do exemplo ao argumento final. Não há aprovação ou revisão humana integral pressuposta. |

A autoria da triagem e o uso de IA no desenvolvimento continuam como pendências
da metodologia, sem terem sido preenchidos por inferência neste capítulo.

## Verificações e limites da entrega

- Plano coberto por 47 parágrafos, nove seções e três subseções de 4.6.
- Continuidade com a metodologia: mesmos modelos e critérios, incluindo parada
  estrita distinta da definição principal de F.
- Exemplo selecionado com prompt, resposta, patch, comparação e testes reais.
- Sete hashes de artefatos do exemplo conferidos contra o registro.
- Descrição de capacidades implementadas separada do uso nas campanhas finais.
- Sem taxas agregadas, conclusões de eficácia ou respostas a Q1–Q5 no capítulo.
- Sem novas inferências, scans, testes ou mutações do experimento.
- Revisão de consistência pelo redator, sem revisor independente.

## Mapa de abertura dos parágrafos

- **C4-P01 — Abertura:** Este capítulo apresenta o desenvolvimento do pipeline utilizado para executar o experimento descrito no Capítu…
- **C4-P02 — Abertura:** A exposição começa pela visão geral da solução e pela organização do projeto. Em seguida, são descritas a prep…
- **C4-P03 — 4.1 Visão geral da solução:** O pipeline foi desenvolvido para transformar alertas identificados no Juice Shop em tentativas de correção que…
- **C4-P04 — 4.1 Visão geral da solução:** A solução foi organizada no estilo dutos e filtros, em que cada etapa possui uma responsabilidade e produz inf…
- **C4-P05 — 4.1 Visão geral da solução:** As entradas principais foram o código do alvo, o catálogo de casos, o perfil de regras e as configurações da c…
- **C4-P06 — 4.2 Tecnologias e organização do projeto:** A automação foi desenvolvida principalmente em Python, responsável por preparar as chamadas, coordenar os proc…
- **C4-P07 — 4.2 Tecnologias e organização do projeto:** O repositório foi dividido para separar implementação, configuração e evidências de execução. Essa organização…
- **C4-P08 — 4.2 Tecnologias e organização do projeto:** Dentro do código principal, as etapas do pipeline foram organizadas em módulos que acompanham o fluxo do exper…
- **C4-P09 — 4.2 Tecnologias e organização do projeto:** O ambiente Docker reuniu as ferramentas e uma referência do Juice Shop com as dependências preparadas. O repos…
- **C4-P10 — 4.3 Detecção e preparação dos casos:** A integração com o Semgrep foi responsável por executar a ferramenta com o perfil selecionado e interpretar su…
- **C4-P11 — 4.3 Detecção e preparação dos casos:** As regras locais foram organizadas em arquivos próprios, acompanhados por exemplos de código. No caso ilustrat…
- **C4-P12 — 4.3 Detecção e preparação dos casos:** A formação do catálogo foi implementada em uma rotina que leu o scan e a classificação arquivada dos alertas. …
- **C4-P13 — 4.3 Detecção e preparação dos casos:** Cada ocorrência recebeu um identificador associado à regra e à sua localização no código fixado. Também foram …
- **C4-P14 — 4.3 Detecção e preparação dos casos:** No exemplo selecionado, o catálogo apontou uma consulta em que o identificador do pedido era incorporado a uma…
- **C4-P15 — 4.4 Construção dos prompts e recuperação de contexto:** A montagem dos prompts reuniu uma instrução de tarefa, o código selecionado, as restrições de alteração e o fo…
- **C4-P16 — 4.4 Construção dos prompts e recuperação de contexto:** As diferenças entre as estratégias P1–P4 foram implementadas pela inclusão dos blocos previstos para cada uma.…
- **C4-P17 — 4.4 Construção dos prompts e recuperação de contexto:** O recuperador de contexto consultou o índice da base e selecionou o documento correspondente à primeira CWE ma…
- **C4-P18 — 4.4 Construção dos prompts e recuperação de contexto:** No exemplo de acompanhamento de pedidos, P1 recebeu o arquivo completo, com 29 linhas, e a instrução direta de…
- **C4-P19 — 4.5 Integração com os modelos de linguagem:** A integração com os modelos foi separada do restante do processamento para permitir selecionar a geração sem r…
- **C4-P20 — 4.5 Integração com os modelos de linguagem:** As configurações foram convertidas para os parâmetros esperados por cada modelo, mantendo uma interface comum …
- **C4-P21 — 4.5 Integração com os modelos de linguagem:** A resposta foi definida por uma estrutura com campos descritivos e uma lista de edições. Cada edição informou …
- **C4-P22 — 4.5 Integração com os modelos de linguagem:** O cliente também registrou as respostas, os tokens, o tempo de geração e o custo calculado a partir dos preços…
- **C4-P23 — 4.6.1 Isolamento com Git worktrees:** As worktrees foram utilizadas como cópias de trabalho separadas, ligadas ao mesmo repositório Git. Cada uma di…
- **C4-P24 — 4.6.1 Isolamento com Git worktrees:** A preparação partiu da mesma revisão fixada do Juice Shop. No ambiente Docker, as worktrees receberam as depen…
- **C4-P25 — 4.6.1 Isolamento com Git worktrees:** Esse isolamento se refere aos arquivos utilizados por cada tentativa e não cria, por si só, uma máquina indepe…
- **C4-P26 — 4.6.2 Gerenciamento das worktrees:** O gerenciamento manteve um conjunto de worktrees disponíveis e entregou uma delas ao trabalho que precisava ap…
- **C4-P27 — 4.6.2 Gerenciamento das worktrees:** O ciclo de uso incluiu restauração antes da entrega e após a conclusão, com a devolução da cópia ao conjunto d…
- **C4-P28 — 4.6.2 Gerenciamento das worktrees:** Além da reserva de cada cópia, o sistema impediu que processos diferentes utilizassem o mesmo conjunto de work…
- **C4-P29 — 4.6.3 Aplicação das edições:** Antes de modificar o código, o aplicador verificou se o caminho informado estava dentro da cópia de trabalho e…
- **C4-P30 — 4.6.3 Aplicação das edições:** A substituição utilizou o trecho original da resposta como ponto de referência, denominado âncora. Uma corresp…
- **C4-P31 — 4.6.3 Aplicação das edições:** No caso ilustrativo, a edição substituiu a consulta com $where por um filtro direto no campo orderId. Após a g…
- **C4-P32 — 4.7 Implementação da validação:** A validação reuniu a reanálise de segurança e os testes para produzir os valores de R, F e M definidos no Capí…
- **C4-P33 — 4.7 Implementação da validação:** O comparador SAST procurou acompanhar as ocorrências entre o código original e o alterado. Para isso, consider…
- **C4-P34 — 4.7 Implementação da validação:** A verificação funcional utilizou uma referência dos testes e um mapa que relaciona arquivos alterados a grupos…
- **C4-P35 — 4.7 Implementação da validação:** As verificações incluíram compilação e execução dos grupos selecionados, com preparação das condições locais e…
- **C4-P36 — 4.7 Implementação da validação:** As falhas registradas foram classificadas automaticamente segundo o conjunto D, preservando as três interpreta…
- **C4-P37 — 4.7 Implementação da validação:** Entre os testes adicionais, o conjunto de CAPTCHA aritmético verificou a geração da expressão, o resultado cal…
- **C4-P38 — 4.8 Orquestração e execução das campanhas:** O coordenador conectou as etapas e organizou o processamento dos casos. Antes da geração, a verificação inicia…
- **C4-P39 — 4.8 Orquestração e execução das campanhas:** Os casos foram distribuídos entre trabalhos de execução que utilizaram as worktrees disponíveis. Dentro de cad…
- **C4-P40 — 4.8 Orquestração e execução das campanhas:** A decisão de interromper as estratégias foi implementada a partir do aceite sem separação das falhas do conjun…
- **C4-P41 — 4.8 Orquestração e execução das campanhas:** A execução por terminal foi disponibilizada por um lançador que reuniu as configurações e preparou os comandos…
- **C4-P42 — 4.8 Orquestração e execução das campanhas:** O painel web local ofereceu a seleção do modelo e do modo, o início e a parada cooperativa, além do acompanham…
- **C4-P43 — 4.9 Registro, métricas e reprodução:** Os arquivos foram organizados por execução e vinculados aos identificadores das tentativas. Essa estrutura per…
- **C4-P44 — 4.9 Registro, métricas e reprodução:** O contrato de execução e as verificações de integridade identificaram os componentes utilizados, incluindo cat…
- **C4-P45 — 4.9 Registro, métricas e reprodução:** A consolidação leu os registros e os artefatos associados para produzir métricas em JSON e tabelas CSV. O proc…
- **C4-P46 — 4.9 Registro, métricas e reprodução:** A avaliação conjunta da RRIS foi implementada em uma rotina separada, que selecionou patches aceitos individua…
- **C4-P47 — 4.9 Registro, métricas e reprodução:** A organização também permite repetir o procedimento em outra máquina compatível mediante a imagem Docker expor…

SHA-256 do rascunho: `ba63d3922589df9acb9c367424101bcf4243493455cc00fc0336c8029f2bc70f`.
SHA-256 da PoC preservada: `9605651e22a395f253a96e67b6592d343222a6771a9c4485c21779abf62b6df9`.
