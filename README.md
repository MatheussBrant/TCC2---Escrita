# Escrita do TCC2 com Claude Code e Codex

Repositório para transformar o TCC1, o histórico Git e as evidências do pipeline
LLM/SAST/Juice Shop em uma monografia rastreável. A configuração inicial inclui
análise dos compromissos do PDF, histórico local e oito skills de escrita.

Comece por [o que prometemos no TCC1](docs/compromissos-tcc1.md),
[contexto e fontes](docs/contexto.md), [evolução técnica](docs/evolucao.md) e
[plano de redação](docs/plano-redacao.md).

## Capítulos e features de escrita

A monografia está organizada em **cinco capítulos**, seguindo a organização mais
compacta do TCC1: Introdução; Referencial teórico; Metodologia e desenvolvimento;
Resultados e discussão; Conclusão e trabalhos futuros. A comparação com o PDF e
o agrupamento das seções estão no [plano de redação](docs/plano-redacao.md).

O [índice de features](features/README.md) contém **11 tarefas especificadas**:
F01–F08 para partes dos cinco capítulos, F09 para reprodução/apêndices/declaração de IA, F10 para
resumo/abstract e F11 para integração. Cada tarefa define o que escrever, fontes,
arquivos exclusivos, entregáveis e critérios de aceitação verificáveis.

F01–F10 podem iniciar a redação em paralelo usando a mesma
[base de fontes](features/BASE_COMUM.md). As dependências condicionam o fechamento:
os textos precisam concordar sobre método, resultados e conclusões. F11 integra
as versões revisadas. O [contrato](features/CONTRATO.md) evita conflitos entre
agentes; o [modelo de entrega](features/MODELO_ENTREGA.md) registra critérios e
evidências de cada tarefa. As especificações estão prontas para execução.

O planejamento aceita **novas features para futuras evoluções do experimento**.
Use `tcc2-evoluir` para analisar commits ou uma adição planejada, mapear o impacto
no texto e criar E001, E002 etc. O [fluxo de evoluções](features/EVOLUCOES.md)
define fontes versionadas, critérios e incorporação por F11. Bases anteriores
são preservadas; novos commits não alteram silenciosamente entregas em andamento.

## Usar no Codex ou Claude Code

Abra **este diretório** como projeto/raiz da sessão. Codex recebe `AGENTS.md` e
skills em `.agents/skills/`; Claude Code recebe `CLAUDE.md`, que importa as mesmas
instruções, e skills em `.claude/skills/`. Se a sessão já estava aberta antes da
configuração, abra uma nova sessão e confira a lista de skills. Abrir apenas a
pasta pai `TCC` pode não descobrir as skills deste repositório filho.

| Trabalho | Codex | Claude Code |
|---|---|---|
| Planejar capítulos e verificar compromissos | `$tcc2-planejar` | `/tcc2-planejar` |
| Criar features para novas evoluções | `$tcc2-evoluir` | `/tcc2-evoluir` |
| Reconstruir evolução e decisões pelo Git | `$tcc2-historico` | `/tcc2-historico` |
| Auditar métricas e interpretar resultados | `$tcc2-resultados` | `/tcc2-resultados` |
| Redigir uma seção | `$tcc2-redigir` | `/tcc2-redigir` |
| Verificar literatura e referências | `$tcc2-bibliografia` | `/tcc2-bibliografia` |
| Revisar evidência e texto | `$tcc2-revisar` | `/tcc2-revisar` |
| Coordenar agentes para uma entrega | `$tcc2-coordenar` | `/tcc2-coordenar` |

Exemplos de pedidos no Codex; no Claude Code, troque `$` por `/`:

```text
$tcc2-planejar Atualize a matriz do TCC1 e indique quais seções já podemos escrever.

$tcc2-evoluir Compare a base atual com o HEAD do experimento e crie features de escrita para as evoluções relevantes, com fontes, destinos e critérios de aceitação.

$tcc2-historico Explique a evolução da separação F/D com commits e consequências metodológicas.

$tcc2-resultados Audite a execução AMP_PAINEL_20261019T183425Z_282e13b4 antes de usá-la no capítulo de resultados.

$tcc2-redigir Execute a feature features/04-metodologia/README.md, seguindo o contrato comum e seus critérios de aceitação.

$tcc2-coordenar Execute F01–F10 de features/README.md em paralelo, respeitando as vagas disponíveis e as pastas exclusivas. Revise por critérios e integre com F11 após reconciliar as entregas.
```

As skills também têm descrições para seleção automática. Elas orientam os agentes
disponíveis no cliente; não iniciam serviços, instalam agentes ou chamam APIs por
conta própria. A configuração destina-se a **Claude Code/Codex com acesso aos
arquivos**, não implica instalação automática no chat comum do Claude.

## Montar o workspace depois de clonar a escrita

O layout padrão já corresponde ao uso previsto:

```text
TCC2---Escrita/
├── .git/                         # Git da escrita
├── AGENTS.md
├── CLAUDE.md
├── fontes.json
├── .agents/skills/
├── .claude/skills/
├── tcc2-llm-sast-juiceshop/       # Clone independente do experimento
│   └── .git/
├── TCC1___Caio_Lamego_e_Matheus_Brant-11.pdf
└── PoC-TCC-Matheus-e-Caio/        # Opcional
```

Depois de clonar e entrar em `TCC2---Escrita`, clone o experimento com o nome
esperado por [fontes.json](fontes.json):

```bash
git clone https://github.com/caiolamego/tcc2-llm-sast-juiceshop.git tcc2-llm-sast-juiceshop
```

Copie o PDF do TCC1 para a raiz com o nome mostrado acima. Abra Claude Code ou
Codex na **raiz da escrita**. O coletor usa o histórico Git completo disponível
localmente; evite `--depth 1` ao clonar se quiser analisar toda a evolução.

O clone experimental e o PDF fonte são ignorados pelo Git da escrita. Cada
repositório conserva seu histórico; os manuscritos, skills e inventários derivados
ficam no Git da escrita. Essa configuração não cria submódulos. A PoC é opcional:
sem esse clone, o coletor registra sua ausência no manifesto e continua com o
experimento e o PDF. Os inventários históricos da PoC já preservados permanecem
disponíveis, sem substituir os arquivos originais em análises que dependam deles.

Se o PDF ou a pasta do experimento tiver outro nome, ajuste `fontes.json` ou uma
cópia completa `fontes.local.json`, ignorada pelo Git. A prioridade é:
`--config CAMINHO` → `fontes.local.json` existente → `fontes.json`.
Os caminhos são relativos ao arquivo de configuração selecionado. Neste workspace
original foi criada uma configuração local que aponta para as fontes ainda nas
pastas irmãs. Ela não será levada em um novo clone; se reorganizar esta mesma
máquina, ajuste-a ou use `--config fontes.json` para selecionar o layout interno.

## Atualizar fontes e histórico

Requisitos do coletor: Python 3.10+, Git e `pdftotext` (Poppler). Nenhum pacote
Python externo nem chave de API é necessário.

Com o clone experimental e o PDF dentro da escrita, basta executar:

```bash
python3 scripts/coletar_fontes.py --saida evidencias/coleta-NOVO-ID
```

Antes de escrever sobre o estado atual, confira o HEAD/refs e o estado local do
clone experimental contra o manifesto utilizado. Novos commits exigem leitura
das mudanças e, quando necessário, uma nova coleta com outro ID. A coleta
`coleta-validada` já inclui `e2394d2`, que registra a consolidação da campanha
Docker de 52 casos e 191 tentativas. Coletas preservadas são retratos datados,
não indicadores automáticos do último estado do projeto.

Cada coleta nova preserva:

- texto do PDF com páginas físicas numeradas e hash do original;
- todos os commits alcançáveis pelas refs locais, pais, datas, mensagens e arquivos;
- estado Git, refs e indicação de clone shallow;
- inventário dos documentos/artefatos selecionados com SHA256 e contagens básicas.

O coletor não faz fetch, não sobrescreve coletas, não executa experimentos e não
copia credenciais. `arquivos.jsonl` é um índice: os artefatos grandes continuam nos
repositórios fonte. Todos os padrões incluídos estão em `fontes.json`. Dados
fora desses padrões e objetos Git inalcançáveis não entram. Consulte o
[manifesto validado](evidencias/coleta-validada/manifesto.json) para o recorte exato;
a primeira coleta também foi preservada.

## Manter as skills

Edite somente os arquivos canônicos em `.agents/skills/` e sincronize os espelhos
versionáveis do Claude, que têm o mesmo conteúdo e não dependem de symlinks:

```bash
python3 scripts/sincronizar_skills.py
python3 scripts/sincronizar_skills.py --check
python3 -m unittest discover -s tests -v
```

O sincronizador avisa sobre arquivos exclusivos do Claude para revisão manual;
não os apaga automaticamente. A revisão de compatibilidade está em
[revisoes/configuracao-inicial.md](revisoes/configuracao-inicial.md).

Os caminhos e formatos seguem a documentação oficial consultada em 19/10/2026:
[skills no Codex](https://learn.chatgpt.com/docs/build-skills),
[instruções AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[skills no Claude Code](https://code.claude.com/docs/en/skills) e
[importação pelo CLAUDE.md](https://code.claude.com/docs/en/memory).
