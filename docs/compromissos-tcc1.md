# Matriz do que foi proposto no TCC1

Leitura do PDF fornecido, especialmente §§1.2–1.4, capítulo 3 e considerações
finais. Páginas abaixo são **impressas**; entre parênteses está a página física do
PDF. A coluna de situação é um diagnóstico inicial de 19/10/2026, não aceite final.

## Perguntas e objetivos

| ID | Pergunta resumida | Evidência necessária para responder no TCC2 |
|---|---|---|
| Q1 | O pipeline gera correções válidas combinando LLM, SAST e testes? (14 / PDF 15) | Tentativas, R/F/M, regra de aceite, denominadores, falhas e inspeção de exemplos |
| Q2 | Como prompt simples, raciocínio guiado e RAG influenciam as correções? (14 / PDF 15) | Estratégias realmente executadas, cadeia de seleção, contexto e contratos; comparação descritiva respeitando seleção sequencial |
| Q3 | O desempenho varia por tipo de vulnerabilidade/OWASP? (14 / PDF 15) | Casos e tentativas por regra, CWE/OWASP, ausências e tamanho dos grupos; sem inferir diferenças robustas de grupos mínimos |
| Q4 | Quais limitações práticas surgem numa base real? (15 / PDF 16) | Falhas de ambiente, patch, compilação, testes, cobertura, parsing, custo e tempo com evidências |

Objetivo geral (§1.3.1, 15 / PDF 16): investigar a eficácia do fluxo integrado na
remoção de alertas, preservação funcional e não introdução de issues. Objetivos
específicos: **OE1** implementar o pipeline; **OE2** definir/aplicar estratégias;
**OE3** avaliar com SAST e testes; **OE4** analisar taxas, tipos de issues, falhas
e limitações. Código implementado satisfaz uma parte de OE1; não responde sozinho
a Q1–Q3.

## Compromissos e rastreabilidade inicial

Os caminhos da última coluna são relativos ao repositório `experimento` da
configuração efetiva (`fontes.json` ou substituição local/`--config`, conforme
`AGENTS.md`). Consulte seus SHAs completos no inventário Git da coleta.

| ID / vínculo | Proposta no TCC1 | Situação e diferença a explicar | Evidência inicial / próximo passo |
|---|---|---|---|
| C01 / OE1, Q1 | Aplicar ao Juice Shop, v20.1.1, com gpt-4.1-mini (§§3.2–3.3, 34–36 / PDF 35–37) | Alvo e pipeline documentados; Qwen/Colab é extensão posterior, não substituição silenciosa do modelo proposto | `docs/protocolo_experimental.md` §§1,9; `docs/modelo_colab.md`; `d03fe57`; identificar modelo por execução |
| C02 / Q3 | Todos os alertas detectados, metadados CWE/OWASP quando disponíveis (§3.4, 36–37 / PDF 37–38) | Catálogo histórico filtrado e ampliado por ocorrência têm populações distintas; 78 ocorrências não são 78 falhas confirmadas | `ccea1c9`; protocolo §11; `outputs/catalogos/`; explicitar inclusões/exclusões e versão |
| C03 / OE1, OE3 | Semgrep antes e depois, JSON, remoção e novas issues (§3.5, 37 / PDF 38) | Comparador evoluiu e tem estados indeterminados; reanálise por arquivos tem alcance menor que scan global | `932bd44`; `src/pipeline/sast/`; auditar perfil, parsing e alcance nos contratos |
| C04 / OE2, Q2 | P1 simples; P2 guiado; P3 RAG; P4 RAG+guiado (§3.6, 38 / PDF 39) | Builder e RAG implementados; P1L é diagnóstico adicional. P3/P4 acrescentam também diagnóstico SAST, fator combinado | `1dc0147`; protocolo §13; `src/pipeline/prompts/builder.py`; verificar estratégias observadas na campanha escolhida |
| C05 / OE2 | Recuperação por categoria de documentos Markdown, sem exigir embeddings (§3.7, 39–40 / PDF 40–41) | Recuperação determinística com hashes e fallback documentada; preflight não comprova eficácia | `src/pipeline/rag/retriever.py`, `knowledge_base/`, `features/03-rag-prompts/ENTREGA.md` |
| C06 / OE1, Q4 | Resposta JSON, patch em cópia isolada, restauração (§§3.6,3.8, 38,41 / PDF 39,42) | Worktrees e âncoras evoluíram; fallback de indentação muda aplicabilidade, exigindo identidade nova | `69bfb2a`, `eeb5f8d`, `94c74d7`; `docs/aplicacao_ancoras.md`; separar replay de validação completa |
| C07 / Q2 | P1→P2→P3→P4, parar no aceite; paralelizar casos (§3.8, 42–43 / PDF 43–44) | Desenho sequencial já estava prometido; número de workers e F de parada precisam constar por execução | `6d4b6b3`; `src/pipeline/execucao_ampliada.py`; contratos/sessões; taxas não são comparação causal balanceada |
| C08 / OE3, Q1 | R=remoção, F=testes aprovados, M=nenhuma nova issue; TRV=Σ(RFM)/m (§3.9, 43 / PDF 44) | F/D, falhas preexistentes, testes relacionados e indeterminação refinam a operacionalização | `92d3229`, `f2179c6`, `8da402b`; `docs/criterios_conjunto_d.md`; declarar F principal e sensibilidade |
| C09 / OE4 | TRI, TPF, TNINI por total de tentativas e TFF=1−TPF (§3.9, 43–44 / PDF 44–45) | No ampliado, TRI/TPF/TNINI usam apenas medições disponíveis; TRV mantém total. Mudança de denominador precisa ser descrita | protocolo §14; `src/pipeline/metrics/calculator.py`; apresentar n/d e política em cada tabela |
| C10 / Q1 | RRIS antes/depois das correções aceitas (§3.9, 44 / PDF 45) | Há implementação; esta análise não verificou execução conjunta suficiente. Não marcar compromisso cumprido por existir calculador | `src/pipeline/metrics/rris.py`; localizar scans globais e patches compatíveis; manter pendência se ausentes |
| C11 / OE1, OE4 | Identificador por tentativa; prompts, respostas, patches, SAST, testes, tempos e CSV (§3.10, 44–46 / PDF 45–47) | Contratos, manifestos e CSVs existem; completude deve ser conferida por execução | `112a4e4`, `features/04-metricas-consolidacao/`; `outputs/campanha_docker/`; hash não prova validade científica |
| C12 / OE4, Q1–Q4 | Comparar estratégias/tipos e analisar dificuldades (§3.11, 46–47 / PDF 47–48) | Há dados históricos e recentes; seleção da campanha e consolidação final para o texto ainda não feitas aqui | Inventário de execuções; redigir resultados apenas após reconciliação das populações |
| C13 / Q4 | Explicitar falsos positivos/negativos, não determinismo, RAG simplificado e projeto único (§3.12, 47–48 / PDF 48–49) | Auditoria posterior classifica alertas, regras locais e testes de desafio ampliam as ameaças; isso deve ser narrado como evolução | `docs/auditoria/`, `docs/cobertura_funcional.md`, caderno; preservar falsos positivos no denominador aplicável |
| C14 / autoria | Declarar apoio de IA e responsabilidade dos autores (§3.13, 48 / PDF 49) | Atualizar declaração ao uso efetivo de Claude/Codex e revisão humana; agentes não aprovam em nome dos autores | Registros de revisão e tarefas; não copiar afirmação de que tudo foi revisado sem confirmação |
| C15 / planejamento | Preparação em agosto; pipeline/RAG em setembro; experimentos out.–nov.; redação até dezembro (§3.14, 49 / PDF 50) | Cronograma é previsão, não comprovação de execução ou data de defesa confirmada | Datas autor/commit, caderno e sessões; registrar diferenças entre data do evento e commit |

## Decisões necessárias antes de fechar resultados

1. Identificar a campanha principal e seu estado de encerramento a partir de
   contrato, sessões e registros; justificar o recorte de 52/78 se adotado.
2. Documentar F principal, parada, denominadores e versões de comparador/aplicador.
3. Verificar se Q2 tem observações suficientes das quatro estratégias e como
   apresentar a seleção sequencial sem atribuição causal indevida.
4. Localizar ou registrar a ausência de RRIS conjunta, inspeção de patches e
   reprodução independente. Ausência é uma limitação legítima, não um resultado zero.
5. Escolher o template acadêmico efetivo e obter os fontes editáveis do TCC1 se
   a versão final continuar em LaTeX. A redação em Markdown pode avançar antes disso.
