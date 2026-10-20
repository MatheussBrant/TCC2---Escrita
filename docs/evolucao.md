# Evolução técnica que pode sustentar a narrativa do TCC2

Esta síntese interpreta marcos selecionados. O índice completo está nos arquivos
`git-experimento.md` e `git-poc.md` da [coleta validada](../evidencias/coleta-validada/manifesto.json).
Use data de evento do caderno/registro quando existir; data de commit não substitui
data de execução. Commits paralelos e merges não devem ser tratados como uma única
sequência linear de decisões dos autores.

| Etapa | Commits localizados | Relevância para a escrita |
|---|---|---|
| PoC, junho/2026 | `eab59b6`, `be893ce`, `823f4ae`, `82f54ed`, `9df85cb`, `d399ea6` (poc) | Python/Bandit, três casos, quatro prompts, evolução da regra de aceite e do nome da métrica; antecedente da proposta |
| Ambiente real, setembro | `341eca3`, `9d646b2`, `697f816`, `f3919d7` | Preparação do Juice Shop, worktrees, custos de validação e caderno |
| SAST e catálogo inicial | `c50fd9b`, `1ebb3ab`, `cd93708`, `969356c` | Normalização de alertas, metadados e relação com marcadores do alvo |
| Geração/aplicação e validação, outubro | `69bfb2a`, `eeb5f8d`, `799e956` | Transição de pipeline preparado para tentativas registradas; falhas também são evidência |
| F/D e execução histórica | `92d3229`, `6d4b6b3`, `3b7ef48`, `da10b26` | Separação de testes funcionais e testes dependentes da vulnerabilidade; E01/E02 têm critérios históricos |
| Ampliação da amostra | `ccea1c9`, `41eebfa`, `1dc0147` | 78 ocorrências, integração ao pipeline e contextualização recuperada; não confundir com 78 desafios |
| Métricas e custo de validação | `34e0b3d`, `fa04444`, `c1e1f44`, `112a4e4` | Consolidação, cache, contratos e novas definições; preflight/benchmark não medem eficácia da LLM |
| Revisão de validação e piloto | `f2179c6`, `932bd44`, `f8a1f12`, `9d7286e`, `8da402b` | Testes relacionados, comparação SAST, cobertura e correções de medição; preservar resultados originais e revalidações |
| Provedor adicional | `db70ab7`, `d03fe57`, `85ee214`, `fa7b644` | Qwen/Colab e execuções registradas; separar identidade de inferência e ambiente ao comparar |
| Docker e baseline | `1cea0e7`, `48ff5bc`, `fd1e1d1`, `517385e` | Lockfiles, safetyMode e equivalência de baseline; ameaça de validade interna observada |
| Referência e indentação | `94c74d7` | Baseline padronizado e mudança no aplicador; replay de oito patches demonstra aplicabilidade, sem provar segurança/funcionalidade |
| Encerramento de campanha Docker | `e2394d2` | Novo commit durante a configuração da escrita: 191 registros/52 casos e métricas consolidadas na execução `183425Z_282e13b4`; auditar denominadores e validade antes de incorporá-los às conclusões |

Para aprofundar um marco, recupere o SHA completo no JSONL e inspecione, por
exemplo, no layout padrão interno:
`git -C tcc2-llm-sast-juiceshop show ccea1c9 -- docs/protocolo_experimental.md`.
Se houver `fontes.local.json`, use o caminho efetivo nele configurado. Antes de
tratar esta síntese como atual, compare o HEAD e as refs com o manifesto e examine
eventuais commits posteriores; esta tabela não se atualiza sozinha.
Para localizar movimentos de arquivos use `git log --all --follow -- caminho`
quando aplicável. Não execute checkout/reset nas fontes para ler versões antigas:
`git show SHA:caminho` é suficiente. O nome atual de um arquivo pode não existir
na revisão antiga; consulte `git show --name-status SHA` antes de concluir ausência.
