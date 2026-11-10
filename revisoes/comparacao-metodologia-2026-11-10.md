# Comparação entre a metodologia original e a versão atual

Comparação textual e editorial em 10/11/2026, seguindo a skill
`.claude/skills/tcc2-revisar/SKILL.md`. Não foram alterados os manuscritos nesta
comparação. Não foi realizada nova avaliação do experimento ou dos patches.

## Fontes e método de contagem

- Original: `TCC1___Caio_Lamego_e_Matheus_Brant-11.md`, linhas 402–825, desde
  “3 Metodologia” até imediatamente antes do Capítulo 4.
- Atual: `manuscrito/03-metodologia.md`, linhas 1–277, incluindo as revisões
  confirmadas pelo autor até esta consulta.
- Apoio: `manuscrito/04-implementacao.md`, para conferir o destino de detalhes
  de diretórios, aplicação e registro.
- [Arquivos comparados, script e contagens](../evidencias/comparacao-metodologia-2026-11-10/contagens.json).
- [Diferenças linha a linha](../evidencias/comparacao-metodologia-2026-11-10/comparacao.diff).

As linhas são físicas do Markdown, incluindo linhas vazias, títulos, tabelas e
blocos de código. Não equivalem a linhas diagramadas do PDF. As palavras foram
contadas por separação por espaços, incluindo marcação Markdown, sem pretensão
de contagem editorial exata. Os snapshots e hashes permitem reproduzir a
comparação mesmo após outras revisões.

## Dimensão do texto

| Medida | Original | Atual | Diferença |
|---|---:|---:|---:|
| Linhas totais | 424 | 277 | −147 (−34,7%) |
| Linhas não vazias | 230 | 164 | −66 |
| Palavras por separação por espaços | 4.408 | 6.390 | +1.982 (+45,0%) |
| Palavras sem blocos de código e comentários HTML | 4.387 | 6.238 | +1.851 (+42,2%) |
| Seções de terceiro nível | 14 | 11 | −3 |
| Tabelas identificadas por legenda | 1 | 6 | +5 |
| Figuras raster referenciadas | 3 | 0 | −3 |
| Diagramas Mermaid | 0 | 1 | +1 |

O diff calculado com `difflib.SequenceMatcher`, sem a heurística `autojunk`,
contabiliza 312 linhas removidas, 165 adicionadas e 112 literalmente iguais.
O saldo é −147. A maioria das linhas iguais é vazia; as sete iguais não vazias
são títulos e delimitadores, não parágrafos de prosa. Isso evidencia uma ampla
reformulação da redação, embora várias ideias tenham sido preservadas.
Não se deve interpretar 312 remoções como 312 linhas de conteúdo abandonado:
um parágrafo editado aparece como remoção e adição, e o alinhamento depende
do algoritmo. As duas versões mantêm majoritariamente um parágrafo por linha.
A conversão de listas em prosa explica parte da queda de linhas com aumento
de palavras. As contagens sem código e comentários mostram que o crescimento
não decorre apenas do Mermaid e dos comentários de evidência.

## Correspondência entre as seções

Cada quantidade inclui título, linhas vazias e elementos até a seção seguinte.
As seções foram fundidas e divididas; a tabela não implica correspondência de
um para um nem permite somar indiscriminadamente as linhas da coluna atual.

| Seção original e linhas | Destino atual e linhas | Diferença de conteúdo |
|---|---|---|
| Abertura: 8 | Abertura: 6 | Manteve finalidade e objeto; passou do planejamento ao estudo realizado, com remissões aos capítulos de implementação e resultados. |
| 3.1 Plano metodológico: 27 | 3.1: 8; fluxo em 3.7 | Manteve natureza aplicada, empírica, quantitativa, exploratória e avaliativa. Acrescentou as unidades caso, tentativa e campanha e a comparação entre modelos. A lista de etapas e figura geral deixaram de aparecer como elementos separados. |
| 3.2 Contexto de aplicação: 10 | 3.2: 25 e 3.4: 38 | Separou apresentação do alvo e escolha dos modelos. Retirou a narrativa de transição entre entregas e ampliou as condições do ambiente. |
| 3.3 Objeto de estudo: 8 | 3.2: 25 | Manteve Juice Shop e tecnologias. Acrescentou loja virtual, funcionalidades, fork, commit, Docker e versões de referência. Não repetiu os números de 113 desafios, 16 categorias e 33 Coding Challenges. |
| 3.4 Seleção: 28 | 3.3: 36 | Trocou a previsão genérica de tratar os alertas pela descrição do catálogo efetivo: 124 alertas, 46 fora do escopo e 78 ocorrências. Acrescentou triagem e revisão dos 21 falsos positivos. |
| 3.5 Ferramenta estática: 28 | 3.3: 36 e validação em 3.8: 28 | Manteve Semgrep, JS/TS, dados estruturados e análise antes/depois. Acrescentou regras locais, perfil fixado e limites da comparação entre ocorrências. Seleção e ferramenta agora dividem a mesma seção. |
| 3.6 Prompts: 28 | 3.5: 25 | Preservou P1–P4 e saídas JSON. Explicitou janela de código, restrições e edições por trechos. Esclareceu que P1/P2 não recebem diagnóstico explícito e que P3/P4 acrescentam diagnóstico e documento juntos. |
| 3.7 RAG: 67 | 3.6: 8; organização técnica em 4.4 | Preservou recuperação documental sem embeddings. Substituiu proposta de árvore e listas por descrição da base efetiva: 14 documentos, versão 2.1, seleção por CWE, categoria e documento genérico. |
| 3.8 Pipeline: 42 | 3.7: 35 e 3.8: 28 | Preservou geração, aplicação, SAST, testes, isolamento, restauração e sequência P1–P4. Acrescentou preflight, contrato, worktrees e distinção entre parada e análise. A validação passou a ter seção própria. |
| 3.9 Métricas: 61 | 3.9: 47 | Preservou R/F/M, TRV, TRI, TPF, TNINI, TFF e RRIS. As fórmulas e variáveis estão novamente explícitas. Adaptou denominadores às medições disponíveis e acrescentou aceite por caso, custo, tempo e tratamento de tentativas posteriores ao aceite. |
| 3.10 Armazenamento: 61 | 3.10: 14; detalhamento em 4.2 e 4.9 | Preservou rastreabilidade por tentativa. Acrescentou contratos e integridade. A árvore, a figura do identificador e a lista de 15 campos não foram reproduzidas integralmente no Capítulo 3. O Capítulo 4 apresenta a organização implementada em tabelas e prosa. |
| 3.11 Análise: 18 | 3.10: 14 | Preservou comparação por estratégia e tipo de problema. Acrescentou Q5, modelos, dados ausentes, limitação da sequência e análise documental dos exemplos. |
| 3.12 Limitações: 10 | 3.11: 7, além de ressalvas em 3.3–3.10 | Manteve limites de SAST, modelos, RAG e aplicação única. Atualizou a existência de triagem e incluiu alcance dos testes e ausência de réplicas independentes. Várias ressalvas passaram a acompanhar o assunto correspondente. |
| 3.13 Uso de IA: 8 | Último parágrafo de 3.11 | Substituiu declaração genérica por Codex e Claude Code, atividades apoiadas e revisão humana do desenvolvimento confirmada pelo autor. Não repete validação integral de todo conteúdo. |
| 3.14 Cronograma: 20 | Sem seção correspondente | Cronograma prospectivo retirado do corpo da metodologia final. Não foi substituído por tabela de atividades realizadas. |

## Diferenças metodológicas que merecem atenção

1. **Um modelo para três.** A comparação entre GPT-4.1 mini, GPT-5.6 Luna e
   GPT-6 Luna e a Q5 ampliam efetivamente o objeto da avaliação. Não é apenas
   uma mudança de redação ou de tempo verbal.
2. **Alertas selecionados por escopo.** O original dizia que todos os alertas
   seriam submetidos ao pipeline; a versão atual registra o filtro de escopo
   e diferencia ocorrência de vulnerabilidade comprovada. O próprio original
   também previa filtrar problemas relevantes no fluxo: a redação atual torna
   o recorte preciso, em vez de preservar essa ambiguidade.
3. **F passou a ter procedimento explícito.** O original usava a ideia de
   testes passando. A versão atual descreve comparação com baseline, grupos
   relacionados, compilação, testes adicionais, conjunto D e três
   interpretações. A classificação principal admite falhas dependentes da
   vulnerabilidade intencional, sem tomá-las automaticamente como perda de
   funcionalidade legítima.
4. **Denominadores mudaram em relação às fórmulas propostas.** Antes TRI, TPF
   e TNINI usavam o total m. Agora utilizam apenas as tentativas com a
   respectiva medição disponível. TRV continua com todas as tentativas da
   população. Essa diferença altera o significado das taxas e está explícita.
5. **Parada e análise foram distinguidas.** O original já previa P1–P4
   sequenciais com parada após correção válida. A sequência não é novidade.
   A versão atual explicita que a parada exigia aceite sem separação e que
   a análise principal usa F por critérios, separando os registros posteriores.
   Acrescenta como limitação a suposição declarada pelo autor de que uma
   estratégia posterior manteria um sucesso anterior; não a apresenta como
   comportamento comprovado.
6. **Triagem passou a existir.** O original dizia que não haveria identificação
   prévia de falsos positivos. A versão atual descreve os rótulos e a revisão
   humana dos 21 falsos positivos. Isso não significa que foram excluídos das
   métricas: os resultados arquivados e atuais ainda incluem os 78 casos.
7. **RRIS ganhou procedimento concreto.** A ideia de aplicar correções aceitas
   já existia. Agora foram descritas aplicação conjunta, incompatibilidades,
   scans globais comparáveis e avaliação funcional separada da redução estática.
8. **A revisão humana foi delimitada.** O original cogitava inspeção manual e
   afirmava revisão de todo conteúdo produzido com IA. O texto atual registra
   o que foi confirmado: revisão dos falsos positivos e do material de
   desenvolvimento, sem inspeção manual dos patches das campanhas.

## Elementos que não foram preservados integralmente

- O cronograma e as referências às entregas separadas foram retirados.
- A justificativa de popularidade de OpenAI/ChatGPT e os dados citados de
  Similarweb/Stack Overflow não foram mantidos na seção de escolha do modelo.
  Permaneceram os argumentos de custo, contexto e saídas estruturadas, agora
  acompanhados das condições e dificuldades operacionais do projeto.
- A apresentação dos números de desafios do Juice Shop foi substituída pela
  identificação do alvo e pela distinção entre desafios e casos do catálogo.
- As três figuras originais não foram todas transportadas: o fluxo por caso
  foi representado em Mermaid; o panorama geral e a figura de nomenclatura
  deixaram de aparecer como figuras próprias no capítulo atual.
- As árvores hipotéticas de diretórios e listas extensas foram condensadas.
  A finalidade e a organização efetiva aparecem na implementação, mas não
  houve transposição literal de cada figura e campo.
- A formulação matemática foi inicialmente simplificada e posteriormente
  recuperada a pedido do autor. Na versão desta comparação, as seis métricas
  originais têm fórmulas e variáveis definidas, com adaptação das ausências.

## Avaliação e pendência

A proposta central permanece: corrigir alertas no Juice Shop com LLMs,
Semgrep, testes e P1–P4. Contudo, a versão atual é uma adaptação substancial e
uma reformulação da redação, não apenas a passagem dos verbos ao passado.
Ela cresce em palavras e detalha aspectos antes propostos genericamente.

Para aproximar o texto do original, a prioridade editorial seria decidir quais
explicações e figuras retiradas ainda ajudam o leitor, sem restaurar previsões
incompatíveis com o que ocorreu. Os conteúdos essenciais de métricas foram
recuperados; os demais itens listados acima ficam visíveis para decisão do autor.
Esta comparação não os repõe automaticamente.

**Pendência material:** a exclusão dos 21 falsos positivos solicitada pelo autor
continua exigindo um recorte analítico e a atualização coordenada de método,
tabelas e conclusões. Não foi realizada nesta tarefa, que compara os textos.

O mapa histórico em `docs/comparacao-capitulo-3-tcc1-tcc2.md` foi preservado:
suas pendências e previsões refletem uma data anterior. Esta revisão é o retrato
atual, com cópias das duas versões e contagens regeneráveis.
