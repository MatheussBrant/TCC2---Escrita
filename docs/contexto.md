# Contexto e fontes

Diagnóstico inicial em **19/10/2026**, não um parecer de conclusão do TCC2.

O TCC1 de Matheus de Siqueira Brant e Caio Magalhães Lamego tem o título
“Correção de vulnerabilidades em código com LLMs: uma avaliação da integração
com ferramentas SAST, testes automatizados, estratégias de contextualização e
raciocínio guiado”. O PDF fornecido tem 72 páginas; a página física do PDF é uma
posição à frente da numeração impressa nos trechos analisados (por exemplo,
objetivos: PDF 16, página impressa 15). Sempre indique qual numeração utiliza.

## Fontes consultadas

| ID | Local padrão | Papel |
|---|---|---|
| TCC1 | `TCC1___Caio_Lamego_e_Matheus_Brant-11.pdf` | PDF colocado na raiz da escrita; compromissos, questões, método e PoC |
| experimento | `tcc2-llm-sast-juiceshop/` | Clone dentro da escrita, com Git próprio; código, protocolo, auditorias e execuções |
| poc | `PoC-TCC-Matheus-e-Caio/` (opcional) | Antecedente Python/Bandit; não pertence à população Juice Shop |
| escrita | Este repositório | Instruções, rastreabilidade, rascunhos e revisões |

O usuário vai clonar o repositório de escrita e, dentro dele, clonar o experimento
e colocar o PDF do TCC1. `fontes.json` representa esse layout. Para uma disposição
local diferente, `fontes.local.json` tem prioridade automática; `--config` explícito
prevalece sobre ambos. Caminhos são relativos ao arquivo de configuração escolhido.
O [README](../README.md) descreve a montagem e os nomes esperados. Fontes locais
ignoradas pelo Git da escrita continuam sendo entradas válidas para leitura.

Na máquina da configuração inicial, as fontes ainda estão em pastas irmãs;
`fontes.local.json` preserva esse acesso sem alterar o padrão para novos clones.
A PoC não precisa ser clonada para escrever sobre o experimento principal. Quando
ausente, registre essa limitação; as coletas anteriores continuam consultáveis.

A coleta validada da configuração inicial está em
[evidencias/coleta-validada](../evidencias/coleta-validada/manifesto.json).
Ela contém os 58 commits locais do experimento, 16 da PoC e o commit inicial da
escrita, alcançáveis por todas as refs locais. A primeira leitura tomou como base
`94c74d778e60e80dccbf2cf0f09ad716d6f46d9f` (57 commits); a coleta validada já inclui
`e2394d2ad737015d410f9da39b1151e36452fc84` (58 commits). O histórico completo foi inventariado;
a interpretação inicial inspecionou fontes e diffs selecionados, sem auditoria
linha a linha de todos os patches. O manifesto registra limites, estado local,
hashes e profundidade do clone. Não houve fetch dos remotos. A
[primeira coleta](../evidencias/coleta-inicial/manifesto.json) também foi preservada;
a coleta validada acrescenta os arquivos de sessão ao inventário e contém 727
arquivos identificados por hash.

Durante a configuração, a campanha recente recebeu novos registros locais e um
commit de resultados. A primeira coleta registra alterações locais; na coleta
validada o experimento estava limpo. Consulte estado Git e hashes: conteúdo
modificado/não rastreado não deve ser atribuído exclusivamente ao HEAD.

A PoC contém dois documentos não rastreados (`PROVA_DE_CONCEITO.md` e
`estrategias_prompt_atualizadas.md`); não os atribua a um commit. O PDF fornecido
foi gerado em outubro de 2026, depois dos commits da PoC de junho: trate-o como a
versão entregue para análise, sem presumir que retrata exatamente o plano existente
no começo da implementação de setembro.

## Onde buscar cada evidência no experimento

| Assunto | Caminhos relativos à raiz do experimento |
|---|---|
| Decisões e protocolo | `docs/protocolo_experimental.md`, `docs/caderno_de_laboratorio.md` |
| Seleção e amostra | `outputs/catalogos/`, `features/01-catalogo-ampliado/`, `config/` |
| Prompt e RAG | `src/pipeline/prompts/builder.py`, `src/pipeline/rag/retriever.py`, `knowledge_base/` |
| Orquestração e parada | `src/pipeline/execucao_ampliada.py`, `src/pipeline/run_pipeline.py` |
| Aplicação de patches | `src/pipeline/patching/`, `docs/aplicacao_ancoras.md` |
| R e M / limites do detector | `src/pipeline/sast/comparacao_v2.py`, `docs/auditoria/comparador_v2.md` |
| F e D / cobertura | `src/pipeline/validation/`, `docs/criterios_conjunto_d.md`, `docs/cobertura_funcional.md` |
| Métricas e denominadores | `src/pipeline/metrics/`, `scripts/reports/consolidate_metrics.py` |
| Docker e baseline | `docker/referencia.json`, `docs/validacao_baseline_docker.md`, `compose.yaml` |
| Execuções recentes | `outputs/campanha_docker/` e contratos de cada execução |
| Extensão Qwen/Colab | `docs/modelo_colab.md`, `src/pipeline/llm/colab_client.py` |

`docs/GUIA_CONTINUIDADE_TCC2.md` é uma fonte histórica útil, mas contém pendências
de etapas anteriores. Confirme o estado com código, commits e artefatos posteriores.

## Alertas concretos para a redação

- O catálogo ampliado registra **78 ocorrências**, incluindo **55 confirmadas,
  21 falsos positivos e 2 inconclusivas**, após 46 exclusões de escopo entre 124
  alertas. Não denomine os 78 casos “78 vulnerabilidades confirmadas”. Fonte:
  protocolo §11 e commit `ccea1c9`.
- O baseline Docker padronizado informa 39 grupos, 484 testes aprovados e seis
  ignorados. Há 52 casos preparados e 26 com lacunas de cobertura. Essas contagens
  são de preparação/cobertura, não de remediação. Fonte: `docs/validacao_baseline_docker.md`.
- O CSV aberto inicialmente,
  `outputs/campanha_docker/AMP_PAINEL_20261019T175741Z_d61671f5_METRICAS/metricas_gerais.csv`,
  tem TRV indisponível (`sem_denominador`); `tentativas.csv` tem zero registros e
  `casos.csv` tem 52. Não escreva “TRV de 0%”.
- As execuções `AMP_PAINEL_20261019T181245Z_1aca0df2` e
  `AMP_PAINEL_20261019T183425Z_282e13b4` têm registros posteriores (13 e 190 linhas
  JSONL na leitura inicial). O commit `e2394d2`, capturado ao final, acrescentou
  o encerramento e a consolidação: o JSONL passou a 191 registros, com 52 casos
  distintos, e `metricas.json` tem `status=consolidado`. Contagem de linhas não comprova sozinha encerramento,
  elegibilidade, número de gerações independentes ou taxa final; auditar contratos,
  sessões e artefatos antes de produzir conclusões. O diagnóstico de escrita não
  escolhe automaticamente qual campanha será a principal.
- No protocolo, o consolidado usa `criterio` como F principal, enquanto a cadeia
  observada pode parar sob aceite estrito. Explicitar regra de parada, F reportado
  e sensibilidades conforme a versão de cada contrato.
- Docker resolveu uma diferença documentada de `safetyMode`, mas a referência
  consultada ainda não comprova distribuição da imagem e reprodução em outro
  computador. “Ambiente fixado” não basta para declarar reprodução independente.

## Atualizar o corpus

Execute `python3 scripts/coletar_fontes.py --saida evidencias/coleta-NOVO-ID`.
Para outra disposição de pastas, copie `fontes.json` para `fontes.local.json` e
ajuste os caminhos; ela será selecionada automaticamente. `--config fontes.json`
força o layout interno. O coletor é offline,
exige Git, Python 3.10+ e `pdftotext`, não sobrescreve coletas e não executa o pipeline.
Os hashes não substituem os arquivos originais: mantenha os repositórios fonte
acessíveis para consultar diffs, tabelas e logs. Em outro computador, providencie
os mesmos commits e o PDF de mesmo hash; não há clone automático nem submódulo.
Repositórios opcionais ausentes aparecem no manifesto. Uma pasta vazia dentro
da escrita não conta como clone do experimento: o coletor verifica a raiz Git.

Antes de afirmar que uma descrição representa o estado atual, compare HEAD, refs
e estado local do clone com o manifesto. Confira commits novos e produza nova
coleta quando a evidência precisar ser atualizada. Não edite coletas anteriores
para trocar caminhos ou contagens; os caminhos nelas registrados são históricos.
Use o ID da fonte e a configuração efetiva para encontrá-la na máquina atual.
