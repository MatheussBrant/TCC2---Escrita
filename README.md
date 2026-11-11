# Escrita do TCC2 com Claude Code e Codex

Repositório da redação da monografia sobre correção de vulnerabilidades com LLMs,
Semgrep e testes automatizados no OWASP Juice Shop. O texto é escrito em Markdown,
capítulo por capítulo, com as evidências de cada afirmação registradas ao lado.

## Como o repositório está organizado

| Pasta ou arquivo | Conteúdo |
|---|---|
| [manuscrito/](manuscrito/README.md) | Texto da monografia, um arquivo por capítulo, e o índice com o estado de cada um |
| [docs/](docs/) | [Diretrizes](docs/diretrizes-escrita.md) e [critérios](docs/criterios-escrita.md) de escrita, planos de parágrafos dos capítulos 3 a 5 e comparação com a proposta original |
| [evidencias/](evidencias/) | Notas de evidência por capítulo e análises de apoio com dados, scripts e hashes |
| [revisoes/](revisoes/) | Pareceres datados sobre o texto |
| `TCC1___Caio_Lamego_e_Matheus_Brant-11.md` | Texto completo da proposta original, usado como referência de linguagem e de compromissos |
| `.claude/skills/` | Skills de escrita para Claude Code |

O capítulo 6, de conclusão, ainda não foi redigido. Os arquivos
`manuscrito/04-prova-de-conceito.md` e `manuscrito/05-consideracoes-finais.md` são
fontes históricas e não entram no texto final.

## Fluxo de trabalho

1. **Planejar:** o plano de parágrafos do capítulo, em `docs/`, define o assunto de
   cada parágrafo e as fontes previstas.
2. **Redigir:** o texto vai para `manuscrito/`, seguindo os critérios de escrita.
3. **Registrar evidências:** cada número ou fato do experimento ganha fonte (SHA,
   caminho e execução) em `evidencias/capitulo-N-notas.md`.
4. **Revisar:** o parecer vai para `revisoes/`, com data no nome do arquivo.

## Montar o workspace

Clone o experimento **ao lado** desta pasta, com o nome esperado pelos scripts de
`evidencias/`:

```text
pasta-de-trabalho/
├── TCC2---Escrita/            # este repositório
└── tcc2-llm-sast-juiceshop/   # clone do experimento
```

```bash
git clone https://github.com/caiolamego/tcc2-llm-sast-juiceshop.git ../tcc2-llm-sast-juiceshop
```

Abra o Claude Code ou o Codex **nesta pasta**, não na pasta pai, para que as
instruções e as skills sejam encontradas. O experimento é apenas consultado:
nenhum script desta escrita chama modelos, roda o Semgrep ou altera seus resultados.

## Usar no Claude Code ou no Codex

O Claude Code lê `CLAUDE.md`, que importa `AGENTS.md`; o Codex lê `AGENTS.md`.
No Claude Code, digite `/tcc2-` no campo da conversa para ver as skills. Elas ficam
em `.claude/skills/`; para usá-las no Codex, copie a pasta para `.agents/skills/`.

| Trabalho | Claude Code |
|---|---|
| Planejar capítulos e verificar compromissos | `/tcc2-planejar` |
| Registrar mudanças do experimento e o impacto no texto | `/tcc2-evoluir` |
| Reconstruir decisões pelo histórico Git | `/tcc2-historico` |
| Auditar métricas e interpretar resultados | `/tcc2-resultados` |
| Redigir uma seção | `/tcc2-redigir` |
| Verificar literatura e referências | `/tcc2-bibliografia` |
| Revisar evidência e texto | `/tcc2-revisar` |
| Coordenar agentes em uma entrega | `/tcc2-coordenar` |

Exemplos de pedidos:

```text
/tcc2-redigir Revise a seção 3.6 de manuscrito/03-metodologia.md seguindo o plano do capítulo 3 e atualize as notas de evidência.

/tcc2-resultados Confira na campanha de 06/11/2026 os números da tabela de casos corrigidos por modelo do capítulo 5.

/tcc2-revisar Revise o capítulo 4 e grave o parecer em revisoes/capitulo-4-AAAA-MM-DD.md.
```

As skills orientam o agente; não instalam nada, não chamam APIs por conta própria e
não fazem commit nem push.
