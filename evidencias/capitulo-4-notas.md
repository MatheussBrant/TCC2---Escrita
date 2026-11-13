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

## Reescrita de 11/11/2026

**Motivo:** revisão do autor (Caio) no Notion, com 27 comentários no capítulo anterior. Pontos principais: linguagem distante da usada no
restante do trabalho, uso de ponto e vírgula e travessões, termos usados sem explicação (painel, perfil, scan, worktree, revisão do alvo,
semente, coordenador, retomada) e trechos que pressupunham que a banca conhecia a implementação. Por orientação da professora, o capítulo
de implementação substitui o capítulo da prova de conceito e passou a seguir a sua estrutura (visão geral, elaboração, estrutura do
projeto, fluxo de execução e armazenamento, métricas, execução e contribuição). O conteúdo da prova de conceito foi retirado.

**Experimento consultado:** `../../tcc2-llm-sast-juiceshop`, revisão `36c554d`. Execução do exemplo:
`AMP_REAL_20261106T151004Z_f49ac0d2` (GPT-4.1 mini), caso `AMP95adf572d3c6677f` (`routes/keyServer.ts:14`, regra
`express-res-sendfile`, CWE-73). P1 e P2 rejeitadas por R=0 com F=1 e M=1; P3 aceita com todos os testes passando; P4 não executada.

**Fatos do texto e fontes (caminhos no experimento):**

| Afirmação | Fonte |
|---|---|
| Node.js 24.14.0, Python 3.11, Semgrep 1.177.0, Juice Shop v20.1.1 no commit `f915bddd8279` | `Dockerfile`, `config/perfis/ampliado_piloto_v1/perfil.json` |
| Cópia das dependências para as worktrees conferida por hash | `docker/workspace.py` |
| Perfil: 1.074 regras de `p/default` e 28 regras próprias, exclusões e limites de tempo | `config/perfis/ampliado_piloto_v1/` |
| Identificador AMP: hash de commit, regra, arquivo e coordenadas | `src/pipeline/etapas/e02_catalogo/catalogo.py` |
| 52 grupos (36 API, 7 servidor, 9 interface), 46 arquivos mapeados | `config/cobertura_funcional_v8.yaml`, `config/mapa_testes_relacionados_v9.yaml` |
| Linha de base com 574 testes executados | `outputs/cobertura_funcional/IMAGEM_81FE_D3_20261106/baseline/baseline_testes.json` |
| 16 arquivos de testes adicionais | `tests/functional/juice_shop/` |
| Arquivo completo até 250 linhas, janela de 60 linhas para cada lado, restrições e formato | `src/pipeline/etapas/e04_prompt/montagem.py` |
| Roteiro de cinco etapas | `config/prompts/roteiro_raciocinio_guiado.md` |
| 14 documentos, índice por CWE, documento genérico e manifesto com hashes | `knowledge_base/`, `src/pipeline/etapas/e03_contexto_rag/recuperacao.py` |
| Temperatura 0, 4.096 tokens, semente 42 no GPT-4.1 mini, raciocínio desativado nos Luna | `src/pipeline/etapas/e05_geracao_llm/modelos.py` |
| Chamadas uma de cada vez, 120 s, até três envios, limites de chamadas e custo, conferência do modelo retornado | `src/pipeline/etapas/e05_geracao_llm/cliente_openai.py` |
| Arquivos protegidos, âncora única, aplicação só depois de conferir todas as edições | `src/pipeline/etapas/e06_aplicacao/aplicador.py` |
| Recuo uniforme em blocos de duas ou mais linhas, conferência por analisador TypeScript | `src/pipeline/etapas/e06_aplicacao/indentacao.py`, `docs/aplicacao_ancoras.md` |
| Restauração preservando dependências e trava entre execuções | `src/pipeline/etapas/e06_aplicacao/worktrees.py` |
| Grupos de API executados um de cada vez | `src/pipeline/etapas/e07_validacao/execucao_cobertura.py` |
| Comparação por posição, contexto e contagem | `src/pipeline/etapas/e01_analise_sast/comparacao.py` |
| Modos de execução, contrato, retomada e conferência do ambiente na verificação inicial | `executar.py`, `src/pipeline/orquestracao/campanha.py`, `src/pipeline/orquestracao/preflight.py` |
| Painel local em 127.0.0.1, seleção de modelo e modo, interrupção que aguarda as tentativas em andamento | `src/pipeline/painel/` |
| RRIS por aplicação conjunta dos patches validados | `scripts/experimento/avaliacao_conjunta_rris.py` |

**Decisões de redação:** não usar ponto e vírgula nem travessão no texto. As legendas seguem o formato do trabalho original
("Figura 1 – ..."), gerado pelo modelo ABNT. Termos técnicos são explicados no primeiro uso. A regra de parada é descrita como na
metodologia original: a sequência termina quando a correção atende R, F e M. O conjunto D é apresentado como registro complementar,
com pendência para o Capítulo 3. Não foram mencionados a campanha descartada, o provedor adicional sem uso nem detalhes de depuração.

**Pendências:** 10 marcadores `[PENDENTE]` no texto, oito deles dependentes da versão final do Capítulo 3, além da referência ao
repositório e das capturas de tela do painel.

SHA-256 do texto reescrito: `722baa022acac304a9c519cc0c0bc55cd1ce8097dac4649b523b942ac90fb4bd`.

## Integração com a revisão do Matheus (12/11/2026)

O commit `e2982af` ("Retira referencias a sementes", Matheus, 11/11/2026) alterou um parágrafo da versão anterior do
capítulo, removendo a menção à semente usada no GPT-4.1 mini. Esse parágrafo já não existia na reescrita de 11/11.
Para manter a decisão dele, a frase equivalente da reescrita (definição de semente na subseção de integração com os
modelos) foi removida. O fato continua registrado no experimento, mas não aparece mais no texto.

SHA-256 do texto após a integração: `7fa8a24266f46d19e234ed8ea8b46863f92327e9d49b503ab9ec15161158f892`.

## Revisão dos autores e alinhamento com o Capítulo 3 (12/11/2026)

**Fonte do texto:** página "Cap 4 - Revisado" do Notion (`415a7d2d-0315-80de-8eda-f5960fdacd4c`), última edição em
12/11/2026 às 16:49 UTC, com os cortes feitos pelo Caio e 13 comentários. O Notion não foi alterado. O texto foi copiado
como estava e só então recebeu as correções abaixo. Referência do Capítulo 3: `manuscrito/03-metodologia.md` no commit
`345c9dc` (Matheus, 11/11/2026). Experimento consultado em `2e8f9a9` (branch `feat/reorganizacao-codigo`).

**Diferenças de forma em relação ao Notion:** o bloco da Figura 5 (worktrees) chegou vazio do Notion e foi
restaurado com o diagrama da versão anterior. Os blocos de código mantiveram as linguagens `typescript` e `text`, que o
Notion converte para `ts` e `txt`.

**Comentários atendidos no texto:**

| Comentário | O que foi feito |
|---|---|
| Resumir a lista da introdução | Frase trocada por "os principais passos da sua elaboração" |
| 4.1 repetitivo com o Capítulo 3 | Primeiro parágrafo trocado por uma remissão à Seção 3.9 e à Figura 2 |
| Dutos e filtros já está no Capítulo 3? | Não está. Parágrafo mantido |
| PENDENTE das regras próprias | A Seção 3.4 trata delas. Texto passou a dizer "regras locais", como no Capítulo 3, e remete à Seção 3.4 |
| PENDENTE do conjunto D | Parágrafo alinhado às Seções 3.9 e 3.10 e à Tabela 5: parada sem separação, F por critérios calculado na mesma validação |
| Quantos alertas usaram o documento genérico | Nenhum. Os 382 prompts P3/P4 recuperaram pelo CWE (`rag_motivo_recuperacao`). Frase acrescentada |
| Recuperação direta ficou ambígua | Reescrito: "Conforme definido na Seção 3.8, a recuperação é feita por essa associação direta, sem busca por similaridade" |
| PENDENTE da figura do fluxo | É a Figura 2 da Seção 3.9 |
| PENDENTE do repositório | Link no formato do Capítulo 3: `caiolamego/tcc2-llm-sast-juiceshop` (público) |
| Âncora como limitação, com contagem | Frase acrescentada na 4.4 com os números da população principal (tabela abaixo) |
| Analisador da linguagem | Texto passou a dizer que é o compilador do TypeScript do próprio Juice Shop e o que ele compara |
| Grupos de testes (estudo) | Sem mudança no texto. Resumo para estudo abaixo |
| PENDENTE das capturas do painel | Continua pendente |

**Ajustes para bater com o Capítulo 3:** figuras renumeradas para 4 e 5, continuando a numeração do Capítulo 3, com
legenda no formato dele (negrito, travessão e "Fonte: elaboração dos autores."). "Execução oficial" passou a "campanhas
finais", "linha de base" passou a _baseline_, "modo de verificação inicial" ganhou o nome _preflight_, "sem conclusão"
passou a "indeterminadas" e as falhas repetidas passaram a ser chamadas de persistentes. As passagens sobre o
encerramento do caso usam "regra de parada" (Seção 3.9). A frase da semente foi removida de novo, porque o Capítulo 3
não a menciona (decisão do Matheus em `e2982af`). A janela de código passou a "até 60 linhas antes e 60 depois das
linhas apontadas" (`montagem.py`, linhas 101 e 102). A seleção do RAG passou a "primeira CWE do alerta presente no
índice" (`recuperacao.py`, linha 179). A RRIS passou a "primeiro aceite de cada caso na análise principal, na ordem em
que as tentativas começaram" (`scripts/experimento/avaliacao_conjunta_rris.py`, função `selecionar`). A frase do
`SEMOWASP`, que tinha ficado solta depois do corte da nomenclatura, remete à Seção 3.12 e à Figura 3 e cita a pasta
`outputs/resultados_finais/`.

**Tentativas não aplicadas por âncora** (`status_aplicacao` igual a `ancora_nao_encontrada` ou `ancora_ambigua`,
população principal delimitada pelo primeiro aceite por critérios, igual à Tabela 1 do Capítulo 5):

| Modelo | População principal | Âncora (população) | Casos | Todos os registros |
|---|---:|---:|---:|---:|
| GPT-4.1 mini | 241 | 15 (8 não encontradas e 7 repetidas) | 7 | 15 |
| GPT-5.6 Luna | 223 | 4 | 3 | 6 |
| GPT-6 Luna | 221 | 1 | 1 | 1 |

No GPT-4.1 mini, nenhum dos 7 casos afetados obteve aceite. O ajuste de recuo foi usado em 24 edições, todas do
GPT-4.1 mini. Os outros dois modelos tiveram só correspondências exatas.

**Divergência encontrada no Capítulo 3 (não alterado):** a Seção 3.9 diz que a reanálise SAST foi executada antes dos
testes. Nas campanhas finais (`politica_validacao: relacionada_v2` nos três contratos), a ordem foi compilação, grupos de
testes e só depois o Semgrep: `src/pipeline/etapas/e07_validacao/execucao_cobertura.py`, função `validar`, chama o
`callback` do SAST depois do laço dos grupos. O Capítulo 4 segue o código.

**Para estudo dos autores (grupos de testes):** os grupos ficam em `config/cobertura_funcional_v8.yaml` e o mapa em
`config/mapa_testes_relacionados_v9.yaml`, as versões citadas em `config/execucao_docker_78.yaml`. São 52 grupos (36 de
API, 7 do servidor e 9 da interface), cada um com um arquivo de teste: 36 da suíte do Juice Shop e 16 escritos pelos
autores (`tests/functional/juice_shop`). Cada grupo declara o domínio, a compilação exigida (servidor, interface ou
ambas), os comportamentos que protege, os testes obrigatórios e as linhas de asserção usadas como evidência. O mapa
liga 46 arquivos a grupos: 34 a um grupo, 11 a dois e o `server.ts` a dez. O `routes/keyServer.ts` do exemplo está
ligado ao grupo `key`, que roda `test/api/file-serving.test.ts`. O conjunto D usado está em
`config/conjunto_d_cobertura_v3.json`.

**Para estudo dos autores (analisador):** `src/pipeline/etapas/e06_aplicacao/indentacao.py` chama
`src/pipeline/etapas/e01_analise_sast/estrutura.cjs`, que carrega o `typescript` instalado no Juice Shop, monta a árvore
sintática com `ts.createSourceFile` e guarda as folhas da árvore (nomes, operadores, sinais). A correspondência por recuo
só é aceita se essas listas forem iguais.

**Pendências:** capturas de tela do painel. A `main` do repositório do experimento está em `d645466` (13/10/2026),
55 commits atrás da branch de trabalho. O link do texto aponta para a raiz do repositório, que abre a `main`.

SHA-256 do texto após esta revisão: `24c3cfb051da2941779d79b21bee4efef2e0071b283d152cff427e1d7df771c5`.

**Decisões do Caio (12/11/2026):** a divergência da Seção 3.9 foi corrigida no Capítulo 3 (registro em
`capitulo-3-notas.md`). O link do repositório fica apontando para a `main`. O itálico será tratado na passagem para o
Overleaf. Os cortes feitos no Notion, inclusive as definições de _hash_ e _commit_, foram intencionais.

## Ajustes decorrentes da revisão do Capítulo 3 — 13/11/2026

A revisão do Caio no Capítulo 3 (registro completo em `capitulo-3-notas.md`, seção de 13/11/2026) retirou trechos
que já estavam no Capítulo 4 ou que pertencem à implementação. Neste capítulo:

- Remissões de tabela renumeradas: a interpretação sem separação passou a citar a Tabela 4, e as combinações de
  _prompt_ a Tabela 3 (a antiga Tabela 3 do Capítulo 3, de parâmetros de geração, saiu).
- 4.2.5: a base passou a ser descrita como "14 documentos escritos em português".
- 4.2.6: recebeu o esforço de raciocínio (desativado nos Luna, não enviado no GPT-4.1 mini) e o reaproveitamento de
  respostas e de validação desligado, os dois conferidos nos contratos das campanhas finais.
- 4.4: o `SEMOWASP` e a frase da nomenclatura passaram a remeter ao Capítulo 5, onde está a classificação complementar.
  A explicação de `A06` e `PATHTRAV` no exemplo foi trocada por remissão à Figura 3, que fica como a explicação única.
- 4.6: o _preflight_ deixou de remeter à Seção 3.9. Entraram a data de conclusão das três campanhas (6/11/2026) e a
  recusa da retomada quando as condições mudam (`src/pipeline/orquestracao/preflight.py`, linha 252).

SHA-256 do texto após estes ajustes: `8a3244dd3218653c98888c6deded264e830f2a99d72e92285b2e6c8b1d6188b7`.

## Revisão de redundâncias e contradições entre os Capítulos 3 e 4 — 13/11/2026

Pedido do Caio: deixar em um só capítulo os trechos grandes repetidos e apontar contradições. Regra usada: o que o
modelo recebe e como o resultado é medido fica no Capítulo 3. Como o _pipeline_ faz isso fica no Capítulo 4. Frases
curtas de remissão foram mantidas.

**Trechos que ficaram só em um capítulo:**

| Assunto | Ficou em | Retirado de | O que sobrou no outro |
|---|---|---|---|
| Base comum do _prompt_, restrições e os seis campos do JSON | 3.7 | 4.2.4 | Só o que é de implementação: papel, janela de código, leitura na _worktree_, exigência de âncora única, motivo da lista de edições e gravação do _prompt_ |
| Sete elementos dos documentos do RAG | 3.8 (lista) | 4.2.5 | Remissão à Seção 3.8 |
| Sequência do fluxo (bloco de texto da 4.2.7) | 3.9 (13 etapas e Figura 2) | 4.2.7 | Parágrafo com paralelismo, consolidação e RRIS |
| _Baseline_ e falhas persistentes | 3.10 | 4.2.3 | Origem do _baseline_ (574 testes) e motivo da reexecução |
| Motivo do conjunto D e uso na regra de parada | 3.9, 3.10 e Tabela 4 | 4.2.3 | Exemplo do teste, lista mantida e cálculo das três interpretações na mesma validação (`F_sem_separacao`, `F_marcador`, `F_criterio` em cada registro) |
| Procedimento da RRIS (integridade, ordem, conflitos) | 4.5 | 3.11 | Definição da métrica, fórmula e remissão à 4.5. A conferência do _hash_ dos _patches_ passou para a 4.5 (`avaliacao_conjunta_rris.py`, linha 39) |
| Versão final dos nomes e mapas de correspondência | 3.12 | 4.4 (duas frases) | `SEMOWASP` e pasta `outputs/resultados_finais/`, com remissão à 3.12 |

**Contradições corrigidas:**

- Figura 4: mostrava testes e reanálise SAST como ramos paralelos. Passou a mostrar testes e depois SAST, como a Figura 2,
  a Seção 3.9 e o código.
- Seção 3.1: dizia "executou novamente a análise estática e os testes". Passou a "executou os testes automatizados e,
  em seguida, uma nova análise estática".
- Seção 4.2.1: dizia que o Juice Shop vinha "do seu repositório". A Tabela 1 indica o _fork_, e o `Dockerfile` clona
  `caiolamego/juice-shop-tcc`. O texto passou a citar o _fork_ da Tabela 1.

**Conferido sem contradição:** o comparador (`comparacao.py`, linhas 197 a 201) deixa R indeterminado quando só a
contagem cai, como dizem a 3.10 e a 4.4. Os 78 casos estão em 46 arquivos distintos, como diz a 4.2.3. O perfil exclui
`.github/`, `.npmrc` e `data/static/codefixes/`, coerente com as exclusões da 3.5.

**Contradição apontada e não corrigida:** a Tabela 5 (cronograma) traz "Paralelização das chamadas à API da LLM", mas
as chamadas foram serializadas (`cliente_openai.py`, linha 29, trava única) e o paralelismo foi dos casos, como diz a
4.2.6. O Caio vai ajustar o cronograma.

SHA-256 após a revisão: capítulo 3 `98d97bd5e45367709102f8cbe6515bf1fbab1b5d73b4e1c47fb3674d1740125c`, capítulo 4
`b6fb92c3dd71c7c2f040c649345417c7a6ba2fc9ba1f6a8e7b4f10c575981515`.
