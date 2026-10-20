# Verificação da configuração — 19/10/2026

## Resultado

Sete skills criadas e validadas: planejamento, histórico, resultados, redação,
bibliografia, revisão e coordenação. As instruções comuns ficam no `AGENTS.md`,
importado pelo `CLAUDE.md`; os SKILL.md canônicos e os espelhos são idênticos.

## Verificações realizadas

- `quick_validate.py` da skill `skill-creator`: sete skills válidas.
- `python3 scripts/sincronizar_skills.py --check`: espelhos conferidos.
- `python3 -m unittest discover -s tests -v`: quatro testes aprovados. Cobrem
  commits exclusivos de branches, merges, Unicode, mensagens completas, CSV
  vazio, arquivo não rastreado, exclusão de `.env`, rejeição de symlink externo,
  extração PDF, integridade de hashes e recusa de sobrescrita sem alterar fontes.
- Coleta real: 72 páginas do TCC1; inicialmente 57 commits do experimento e 58
  na coleta validada, 16 da PoC e um da escrita, sem clones rasos. O histórico
  abrange refs locais, sem fetch.
- Descoberta real no `codex-cli 0.162.0-alpha.17.2`: chamada local `skills/list`
  via app-server, com a raiz deste repositório, encontrou as sete skills com
  `scope=repo`, `enabled=true` e nenhum erro de varredura. O processo de teste
  foi encerrado; nenhuma geração de modelo foi necessária para essa conferência.
- Links Markdown e `git diff --check` conferidos ao encerrar a configuração.

O Claude Code não está instalado neste ambiente. A configuração segue seus
formatos documentados e foi conferida estruturalmente; sua descoberta em runtime
ainda precisa ser observada ao abrir este repositório em uma instalação do Claude
Code. Não foi alegada execução de uma sessão Claude.

## Avaliação independente de comportamento

Um subagente recebeu a skill de resultados e a tarefa de escrever um parágrafo
de eficácia a partir do CSV `AMP_PAINEL_20261019T175741Z_d61671f5_METRICAS`.
Trabalhou em somente leitura e conferiu contratos, catálogo, métricas, hashes e
histórico do aplicador. Concluiu que se trata de um preflight com 52 casos,
208 prompts e zero tentativas; TRV está indisponível por denominador zero.
Assim, a evidência permite descrever preparação, sem estimar eficácia ou afirmar
TRV de 0%. O teste foi feito por um agente deste ambiente, não pelo Claude Code.

CSV verificado: SHA256
`bcc705f2c93874d28c0b4d0c56b5243a2e473fc90dcf5ab7ede3b008d143e861`.
Revisão do experimento que contém esses artefatos:
`94c74d778e60e80dccbf2cf0f09ad716d6f46d9f`.

A avaliação encontrou duas melhorias concretas, incorporadas:

1. Adicionar `outputs/**/*_sessoes.json` aos padrões de coleta.
2. Identificar preflight antes de procurar sessões/JSONL; ausência desses arquivos
   é esperada nesse modo e não implica, por si só, execução incompleta.

## Coletas e limites

`coleta-inicial` preserva o primeiro inventário, com 715 arquivos. Uma coleta
adicional, `coleta-validada`, inclui sessões, a configuração corrigida e 727
arquivos. Ela também capturou o novo commit externo `e2394d2`, com o encerramento
e a consolidação da campanha Docker (191 registros e 52 casos distintos).
Consulte seu manifesto para hashes. A primeira foi preservada para não apagar
o recorte anterior. As coletas inventariam arquivos externos; não são backups
completos desses artefatos nem auditam todos os diffs do Git.

A campanha experimental recebeu alterações locais durante o trabalho de
configuração, registradas nos estados Git dos manifestos. Elas não foram
produzidas por esta tarefa. Dados modificados após o commit precisam ser citados
pelo hash do arquivo e pela coleta, além do HEAD; não se pode atribuir todo o
conteúdo local exclusivamente à revisão Git.

Não houve execução do pipeline experimental, novas chamadas LLM desse pipeline,
commit, push, alteração de permissões globais ou instalação de clientes. Os
resultados científicos e as referências acadêmicas ainda exigem as revisões
descritas na matriz de compromissos antes de fechar a monografia.

## Ajuste para fontes dentro da escrita — 19/10/2026

O layout compartilhado foi atualizado a pedido do usuário: o clone
`tcc2-llm-sast-juiceshop/` e o PDF do TCC1 ficam dentro da raiz de escrita.
A PoC passou a opcional; sua ausência é registrada no manifesto. O Git da escrita
ignora esses insumos locais, mantendo separado o Git do experimento.

As sete skills e seus espelhos orientam a resolver a configuração efetiva e
conferir commits posteriores às coletas. `fontes.local.json`, ignorado pelo Git,
mantém o acesso às pastas irmãs nesta máquina; `fontes.json` já usa o layout
interno para novos clones. `--config` explícito prevalece sobre a seleção automática.
As coletas anteriores foram preservadas com seus caminhos e hashes históricos.

Os oito testes do coletor passaram, incluindo um workspace temporário com clone
Git interno, PDF na raiz e PoC ausente; seleção da configuração local; e rejeição
de uma pasta vazia que herdaria o Git da escrita. A sincronização das sete skills
também foi conferida. O commit local mais recente foi reconferido:
`e2394d2ad737015d410f9da39b1151e36452fc84`, já presente em `coleta-validada`.
