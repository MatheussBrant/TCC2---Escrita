# Escrita do TCC2 — Caio Lamego e Matheus Brant

Este repositório guarda a redação da monografia sobre correção de vulnerabilidades
com LLMs, Semgrep e testes no OWASP Juice Shop. Trabalhe em português brasileiro.

## Começo de uma tarefa

Leia somente o que a tarefa pedir, nesta ordem:

1. [Diretrizes de escrita](docs/diretrizes-escrita.md): decisões dos autores,
   organização dos capítulos e a pergunta Q5.
2. [Critérios de escrita](docs/criterios-escrita.md): linguagem, unidade do
   trabalho e profundidade de cada capítulo.
3. O plano de parágrafos do capítulo em questão, quando existir.
4. As notas de evidência do capítulo, em `evidencias/capitulo-N-notas.md`.
5. O texto atual em `manuscrito/`, a partir do [índice](manuscrito/README.md).

O [Markdown completo do TCC1](TCC1___Caio_Lamego_e_Matheus_Brant-11.md), com as
figuras em `TCC1___Caio_Lamego_e_Matheus_Brant-11_assets/`, é a referência de
linguagem e dos compromissos assumidos na proposta. Ele não integra o texto final.

## Organização atual

| Capítulo | Texto | Plano | Evidências |
|---|---|---|---|
| Pré-textuais | `manuscrito/00-elementos-pre-textuais.md` | — | — |
| 1 — Introdução | `manuscrito/01-introducao.md` | — | — |
| 2 — Referencial teórico | `manuscrito/02-referencial-teorico.md` | — | — |
| 3 — Metodologia | `manuscrito/03-metodologia.md` | `docs/plano-paragrafos-capitulo-3.md` | `evidencias/capitulo-3-notas.md` |
| 4 — Implementação | `manuscrito/04-implementacao.md` | `docs/plano-paragrafos-capitulo-4.md` | `evidencias/capitulo-4-notas.md` |
| 5 — Resultados e discussão | `manuscrito/05-resultados-discussao.md` | `docs/plano-paragrafos-capitulo-5.md` | `evidencias/capitulo-5-notas.md` e `evidencias/capitulo-5-apoio/` |
| 6 — Conclusão e trabalhos futuros | ainda não redigido | — | — |
| Referências | `manuscrito/referencias.md` | — | — |

As perguntas de pesquisa são Q1–Q5, conforme a introdução; Q5 compara os modelos.
Ficam fora do texto final, como fontes históricas: `manuscrito/04-prova-de-conceito.md`,
`manuscrito/05-consideracoes-finais.md` e o Markdown do TCC1. Não os concatene nem
os edite. `manuscrito/03-metodologia copy.md` é uma cópia de trabalho: confirme
com os autores antes de usá-la como fonte ou apagá-la.

Comparações com a proposta original ficam em documentos de apoio, como
[docs/comparacao-capitulo-3-tcc1-tcc2.md](docs/comparacao-capitulo-3-tcc1-tcc2.md),
e pareceres datados em `revisoes/`.

## Onde estão as fontes

O experimento é o clone `tcc2-llm-sast-juiceshop`, na pasta irmã da raiz da escrita
(`../tcc2-llm-sast-juiceshop`). Os scripts de `evidencias/` usam esse caminho. Se o
clone estiver em outro lugar nesta máquina, use o caminho informado pelo usuário;
fonte ausente é uma lacuna, não autorização para reconstruir resultados de memória.

Consulte o clone com `git -C <caminho-do-clone>` e não faça nele checkout, reset,
commit nem execução de experimento. As notas de cada capítulo registram a revisão
(SHA) consultada; antes de descrever o estado atual, compare-a com o HEAD do clone
e registre a evolução encontrada, sem reescrever notas antigas.

No clone, as fontes principais são: `docs/protocolo_experimental.md` e
`docs/caderno_de_laboratorio.md` para o método e as decisões;
`outputs/campanha_docker/<EXECUCAO>/` para as tentativas; e
`outputs/rris/<EXECUCAO>_METRICAS/` para as métricas consolidadas com a RRIS.
O recorte de execuções usado no texto está nas notas do capítulo 5.

## Regras de evidência

- O texto acadêmico apresenta uma única pesquisa completa e autônoma. Não mencionar
  TCC1/TCC2 como trabalhos separados ou etapas de entrega. A origem dos trechos e a
  comparação entre versões ficam nos planos e nas notas, conforme
  `docs/criterios-escrita.md` (diretriz do autor de 09/11/2026).
- Vincule afirmações empíricas a repositório, SHA, caminho e execução; números
  precisam de população, definição de F, numerador, denominador e política.
- Diferencie proposta original, implementação, execução observada e interpretação.
  Mensagem de commit e checklist não comprovam eficácia experimental.
- Separe PoC Python/Bandit, histórico JS001–JS012, catálogo ampliado, pilotos,
  diagnósticos P1L, preflight, dry-run, replay e campanhas Docker. Não agregue
  ambientes, contratos ou modelos diferentes sem justificar a comparabilidade.
- Não invente resultados, referências, DOI, aprovação da orientadora ou experimentos.
  Use `[PENDENTE: evidência necessária]` em rascunhos quando faltar fonte.
- As estratégias P1–P4 são sequenciais, com parada no aceite: as taxas de P2–P4 são
  condicionais aos casos restantes e não isolam o efeito do prompt. P1 e P2 recebem
  só o código; P3 e P4 recebem também o alerta do Semgrep e o documento do RAG.
  Ausência de medição não significa zero.
- Preserve a diferença entre remover um alerta e demonstrar uma correção segura.
  A RRIS exige aplicação conjunta e scans comparáveis; não some aceites isolados.
- Consulte a revisão da fonte que sustenta a afirmação. Documentos antigos podem ter
  pendências já resolvidas; registre a mudança, sem reescrever o passado.

## Trabalho nos arquivos

Escreva o texto em `manuscrito/`, os pareceres em `revisoes/` e as evidências
derivadas em `evidencias/`. Ao alterar um capítulo, atualize suas notas de evidência
e, se o estado mudar, a tabela de [manuscrito/README.md](manuscrito/README.md).
Análises novas ficam em pastas datadas, como `evidencias/<assunto>-AAAA-MM-DD/`.
Crie diretórios apenas quando houver conteúdo. O formato é Markdown; preserve um
projeto LaTeX e o estilo bibliográfico se forem adicionados. Não afirme conformidade
ABNT sem conferir o template institucional.

Os repositórios experimentais são fontes de consulta. Não execute a LLM nem altere
seus resultados para preencher uma lacuna do texto; um novo experimento é uma tarefa
distinta, pedida explicitamente. Não leia nem copie `.env` ou credenciais. Commit e
push não fazem parte da rotina de redação.

Ao encerrar uma tarefa, informe os arquivos produzidos, as evidências verificadas e
as pendências concretas. Com agentes simultâneos, cada um edita arquivos exclusivos.

## Skills

As skills ficam em `.claude/skills/`. No Codex, que lê este arquivo, copie a pasta
para `.agents/skills/` se quiser usá-las também.

| Tarefa | Skill |
|---|---|
| Relacionar compromissos, perguntas e evidências e planejar capítulos | [tcc2-planejar](.claude/skills/tcc2-planejar/SKILL.md) |
| Registrar mudanças do experimento e o impacto no texto | [tcc2-evoluir](.claude/skills/tcc2-evoluir/SKILL.md) |
| Recuperar commits e decisões de implementação | [tcc2-historico](.claude/skills/tcc2-historico/SKILL.md) |
| Interpretar execuções, CSVs e métricas | [tcc2-resultados](.claude/skills/tcc2-resultados/SKILL.md) |
| Redigir uma seção com evidências | [tcc2-redigir](.claude/skills/tcc2-redigir/SKILL.md) |
| Verificar referências e sustentar a fundamentação | [tcc2-bibliografia](.claude/skills/tcc2-bibliografia/SKILL.md) |
| Revisar consistência científica e textual | [tcc2-revisar](.claude/skills/tcc2-revisar/SKILL.md) |
| Coordenar agentes em uma entrega de escrita | [tcc2-coordenar](.claude/skills/tcc2-coordenar/SKILL.md) |
