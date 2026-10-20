# Escrita do TCC2 — Caio Lamego e Matheus Brant

Este repositório organiza a redação do TCC2 sobre correção de vulnerabilidades com
LLMs, Semgrep e testes no OWASP Juice Shop. Trabalhe em português brasileiro.

## Começo de uma tarefa

Leia [contexto](docs/contexto.md) e escolha somente a skill pertinente abaixo.
Para planejar capítulos ou avaliar cumprimento, consulte a
[matriz do TCC1](docs/compromissos-tcc1.md). Resolva os caminhos pela configuração
efetiva: `--config` explícito, senão `fontes.local.json` quando existir, senão
`fontes.json`. Os caminhos são relativos ao diretório do arquivo escolhido.

As tarefas de redação estão no [índice de features](features/README.md). Para
executar uma delas, leia sua especificação, o [contrato](features/CONTRATO.md)
e a [base comum](features/BASE_COMUM.md). Respeite sua pasta `saida`, entregáveis
e critérios; registre progresso no `entrega.md` da própria pasta. F01–F10 podem
começar em paralelo; as dependências de fechamento exigem reconciliação antes do
aceite. F11 integra as versões revisadas. Não substitua uma feature por um roteiro
genérico nem altere especificações compartilhadas durante sua execução.

O texto final tem cinco capítulos. IDs de features e números de pastas identificam
tarefas: F02/F03 compõem o Capítulo 2, F04/F05 o 3, F06/F07 o 4 e F08 o 5.
Novas adições ao experimento geram features E001 em diante pelo
[fluxo de evoluções](features/EVOLUCOES.md), usando `tcc2-evoluir`. Podem ser
planejadas antes da implementação; só descrevem resultados realizados quando
houver evidência. F11 incorpora também as evoluções selecionadas para seu recorte.

O layout compartilhado coloca o clone `tcc2-llm-sast-juiceshop/` e o PDF
`TCC1___Caio_Lamego_e_Matheus_Brant-11.pdf` **dentro da raiz de escrita**.
O clone `PoC-TCC-Matheus-e-Caio/` é opcional: sua ausência não bloqueia a escrita
do experimento principal; registre a limitação quando precisar de fontes da PoC.
Essas fontes locais estão no `.gitignore` da escrita, mas devem ser consultadas
diretamente pelos caminhos configurados. O clone experimental tem seu próprio
Git; use `git -C <raiz-do-experimento>` para consultá-lo, mantendo a sessão de
escrita nesta raiz. Veja a montagem do workspace no [README](README.md).

Antes de descrever o estado atual, compare HEAD, refs e alterações locais das
fontes com o manifesto da coleta usada. Se houver evolução, examine os novos
commits e produza uma nova coleta quando necessário, preservando a anterior.
Caminhos gravados em coletas históricas documentam o ambiente daquela coleta;
localize as fontes nesta máquina pela configuração efetiva, sem editar o histórico.
Fontes ausentes são uma lacuna, não autorização para reconstruir resultados de memória.

Em uma rodada com base fixada, novos commits não substituem automaticamente o
recorte escolhido: consulte o SHA especificado e registre a evolução encontrada.
Qualquer atualização da base deve ser coordenada entre as entregas afetadas,
sem checkout/reset no clone experimental compartilhado.

| Tarefa | Skill canônica |
|---|---|
| Relacionar promessas, perguntas e evidências | [.agents/skills/tcc2-planejar/SKILL.md](.agents/skills/tcc2-planejar/SKILL.md) |
| Criar features para evoluções existentes ou planejadas | [.agents/skills/tcc2-evoluir/SKILL.md](.agents/skills/tcc2-evoluir/SKILL.md) |
| Recuperar commits e decisões de implementação | [.agents/skills/tcc2-historico/SKILL.md](.agents/skills/tcc2-historico/SKILL.md) |
| Interpretar execuções, CSVs e métricas | [.agents/skills/tcc2-resultados/SKILL.md](.agents/skills/tcc2-resultados/SKILL.md) |
| Redigir uma seção com evidências | [.agents/skills/tcc2-redigir/SKILL.md](.agents/skills/tcc2-redigir/SKILL.md) |
| Verificar referências e sustentar fundamentação | [.agents/skills/tcc2-bibliografia/SKILL.md](.agents/skills/tcc2-bibliografia/SKILL.md) |
| Revisar consistência científica e textual | [.agents/skills/tcc2-revisar/SKILL.md](.agents/skills/tcc2-revisar/SKILL.md) |
| Coordenar agentes em uma entrega de escrita | [.agents/skills/tcc2-coordenar/SKILL.md](.agents/skills/tcc2-coordenar/SKILL.md) |

## Regras de evidência

- Vincule afirmações empíricas a repositório, SHA, caminho e execução; números
  precisam de população, definição de F, numerador, denominador e política.
- Diferencie proposta do TCC1, implementação, execução observada e interpretação.
  Mensagem de commit e checklist de entrega não comprovam eficácia experimental.
- Separe PoC Python/Bandit, histórico JS001–JS012, catálogo ampliado, pilotos,
  diagnósticos P1L, preflight, dry-run, replay e campanhas Docker. Não agregue
  ambientes, contratos ou modelos diferentes sem justificar comparabilidade.
- Não invente resultados, referências, DOI, aprovação da orientadora ou experimentos.
  Use `[PENDENTE: evidência necessária]` em rascunhos quando faltar fonte.
- As estratégias P1–P4 são sequenciais com parada no aceite; taxas brutas não
  isolam causalmente o efeito do prompt. Ausência de medição não significa zero.
- Preserve a diferença entre remover um alerta e demonstrar uma correção segura.
  RRIS requer aplicação conjunta e scans comparáveis; não some aceites isolados.
- Consulte a revisão da fonte que sustenta a afirmação. Documentos antigos podem
  ter pendências já resolvidas; registre a mudança, sem reescrever o passado.

## Trabalho nos arquivos

Escreva rascunhos em `manuscrito/`, pareceres em `revisoes/` e evidências derivadas
em `evidencias/`. Crie diretórios apenas quando houver conteúdo. O formato inicial
é Markdown; preserve o projeto LaTeX e o estilo bibliográfico se forem adicionados.
Não afirme conformidade ABNT sem conferir o template institucional adotado.

Dentro de uma feature, todo material produzido pelo redator, inclusive análises
derivadas e bibliografia, fica na pasta exclusiva `saida`. O revisor escreve em
`revisoes/<ID>/parecer.md` e encaminha correções ao responsável, sem disputar o
manuscrito. As pastas gerais acima continuam disponíveis para tarefas avulsas.

Os repositórios experimentais são fontes de consulta para esta tarefa de escrita.
Não execute a LLM nem altere seus resultados para preencher uma lacuna do texto.
Uma solicitação explícita de novo experimento é uma tarefa distinta. Não leia nem
copie `.env` ou credenciais para o corpus. Commit e push não fazem parte da rotina
automática de redação.

Edite skills em `.agents/skills/`; depois execute
`python3 scripts/sincronizar_skills.py` e `python3 scripts/sincronizar_skills.py --check`.
`.claude/skills/` é um espelho versionável, sem dependência de symlinks.
Encerrando uma tarefa, informe arquivos produzidos, evidências verificadas e
pendências concretas. Quando houver agentes simultâneos, use a divisão de arquivos
da skill de coordenação; não atribua a agentes revisões que não ocorreram.
