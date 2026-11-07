# Capítulo 3: o que manter, modificar e acrescentar

**Orientação de uso:** esta comparação é um documento de apoio à revisão do
conteúdo. Os termos internos e os caminhos citados ajudam a verificar as fontes;
o texto final seguirá os [critérios de escrita](criterios-escrita.md), com linguagem
próxima à do TCC1 e apenas o detalhamento técnico necessário à compreensão.

Comparação elaborada em 07/11/2026, preservando a divisão do capítulo 3 do TCC1.
Complementa o roteiro anterior por parágrafos: antes de definir outra estrutura,
os autores podem decidir as alterações a partir das seções já escritas.
O manuscrito não foi reescrito nesta tarefa.

Atualização posterior: o autor aceitou a inclusão de Q5 sobre comparação entre
modelos, uma seção própria de modelos e parâmetros no capítulo 3 e uma seção de
comparação no capítulo 5. A Q5 e o objetivo correspondente já foram acrescentados
à introdução de trabalho; Q1–Q4 e o Markdown completo do TCC1 foram preservados.
O capítulo 3 ainda aguarda adaptação. Ver [diretrizes](diretrizes-escrita.md).

## Base verificada

- Texto de partida: [03-metodologia.md](../manuscrito/03-metodologia.md).
- Experimento: `../../tcc2-llm-sast-juiceshop`, HEAD
  `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações locais rastreadas
  na consulta desta tarefa.
- Recorte observado: três campanhas Docker de 06/11/2026, com 78 casos cada,
  identificadas no índice de resultados e nos respectivos contratos.
- Consulta offline de documentação, código e contratos selecionados. Não houve
  nova execução do pipeline, revisão integral dos patches nem verificação de
  bibliografia externa.

## Comparação pela estrutura original

| Trecho atual | O que aproveitar | O que modificar ou acrescentar |
|---|---|---|
| Abertura | Finalidade de avaliar o pipeline no Juice Shop. | Descrever procedimentos realizados e tratar o objeto observado como alertas/casos, sem equiparar automaticamente todo alerta a vulnerabilidade real. |
| 3.1 Plano metodológico | Caracterização aplicada, empírica, quantitativa e avaliativa; fluxo geral e critérios simultâneos. | Atualizar para o estudo executado, distinguir caso, tentativa e campanha e incluir a avaliação dos três modelos. Evitar chamar cache ou repetição operacional de réplica independente. |
| 3.2 Contexto de aplicação | Justificativa do projeto e passagem da PoC ao sistema completo. | Atualizar a descrição que previa apenas gpt-4.1-mini: foram executadas campanhas com gpt-4.1-mini, gpt-5.6-luna e gpt-6-luna. Justificativas e parâmetros devem refletir cada modelo; acrescentar ambiente Docker. Separar justificativa originalmente documentada de explicações posteriores dos autores. |
| 3.3 Objeto de estudo | Apresentação do Juice Shop, tecnologias e finalidade didática. | Explicitar commit fixado f915bddd82790d0f3018902d36ae9b4241a5f51f, escopo de código analisado e distinção entre desafios pedagógicos e ocorrências do catálogo. Conferir as contagens de desafios na revisão usada antes de mantê-las. |
| 3.4 Seleção das vulnerabilidades | Seleção guiada pelos alertas e registro de metadados. | Descrever 124 alertas brutos, 46 fora do escopo e 78 ocorrências incluídas. Não afirmar que todo alerta bruto foi submetido ao pipeline. Explicar identidade por ocorrência, ausência de deduplicação no catálogo ampliado e inclusão de falsos positivos/inconclusivos conforme a política arquivada. |
| 3.5 Ferramenta de análise estática | Escolha do Semgrep, suporte JS/TS, JSON e análise antes/depois. | Acrescentar versão 1.177.0, regras remotas e locais, perfil congelado e limites de parsing. Explicar como se comparam ocorrências após mudanças de código, conforme ocorrencias_contexto_v3; detalhes do algoritmo cabem no capítulo 4. |
| 3.6 Estratégias de prompt | P1–P4, raciocínio guiado, contextualização e JSON estruturado. | Especificar que P1/P2 não recebem bloco explícito do alerta, enquanto P3/P4 recebem diagnóstico e documentação juntos. Registrar restrições comuns, política de janela e o formato efetivo de edições por trecho original/corrigido. |
| 3.7 RAG simplificado | Justificativa de recuperação documental sem embeddings e finalidade do contexto. | Substituir a estrutura hipotética contextos_rag pela base knowledge_base, versão 2.1 e 14 documentos. Explicar prioridade de CWE, categoria e fallback genérico, conteúdo efetivamente enviado e hashes. A árvore de diretórios fica no capítulo 4. |
| 3.8 Pipeline | Fluxo de geração, aplicação, reanálise, testes, isolamento e ordem P1–P4. | Descrever preflight, contrato, K=4, restauração, erros e retomada. Distinguir a parada estrita, baseada em classificacao_sem_separacao, da classificação principal criterio. Atualizar os passos e o diagrama para as condições reais. |
| 3.9 Métricas | R/F/M, fórmula principal da TRV e conceitos de TRI, TPF, TNINI, TFF e RRIS. | Explicar baseline, testes relacionados, conjunto D, três definições de F e medições indeterminadas. TRV mantém todas as tentativas da população; TRI/TPF/TNINI usam denominadores medidos. Acrescentar aceite por caso, custos/tempos e aplicação conjunta da RRIS. |
| 3.10 Armazenamento | Rastreabilidade por identificador e associação entre artefatos. | Atualizar para pastas por execução, contrato, JSONL, hashes, sessões e métricas consolidadas. IDs dos casos são AMP… e identificam ocorrências. Transferir a árvore detalhada e explicação dos diretórios para o capítulo 4. |
| 3.11 Análise dos dados | Comparar estratégias e tipos e responder Q1–Q4. | Incluir comparação dos modelos, população principal e sensibilidades de F, tamanho dos grupos e valores ausentes. Explicar seleção sequencial e efeito conjunto de SAST/documentação em P3/P4; não atribuir causalidade isolada ao RAG. |
| 3.12 Limitações | Um objeto de estudo, SAST imperfeito, não determinismo e RAG simplificado. | Corrigir a frase de que não houve identificação prévia de falsos positivos: existe uma triagem arquivada, mas sua autoria e validação humana não estão demonstradas pelas fontes consultadas. Acrescentar limites dos testes relacionados, regras locais, comparador e seleção sequencial. |
| 3.13 Uso de IA | Declaração de responsabilidade dos autores. | Atualizar ao uso real no desenvolvimento e na escrita. A afirmação de revisão e validação de todo conteúdo precisa de confirmação dos autores; não reproduzi-la automaticamente. |
| 3.14 Cronograma | Pode servir de registro histórico do planejamento. | Recomenda-se retirar o cronograma prospectivo do corpo final ou substituí-lo por etapas realizadas com datas comprovadas, se isso contribuir para explicar o método. Decisão editorial, não mudança exigida pelo experimento. |

## Acréscimos que merecem espaço próprio

### Ambiente e condições de execução

Explicar no método por que o ambiente foi padronizado, qual identidade foi usada
pelas campanhas e quais variáveis ficaram fixas. Detalhes de construção da imagem,
comandos e arquivos pertencem ao capítulo 4 ou a apêndice de reprodução.

Os contratos registram temperatura 0 e limite de 4096 tokens de completamento
nos três modelos. Os Luna registram reasoning_effort=none; gpt-4.1-mini registra
seed=42. Não dizer que todos receberam seed ou parâmetros idênticos. Cache LLM e
cache de validação estão desligados nas campanhas finais consultadas.

### Validação funcional

O texto original define F como testes passando, mas não explica o procedimento
atual. Acrescentar uma subseção que apresente baseline, grupos de testes
relacionados, cobertura, testes próprios, conjunto D, sensibilidades e resultados
indeterminados. A configuração final usa relacionada_v2, revisão funcional v8 e
mapa de testes v9; esses identificadores devem ser associados aos contratos.

Não afirmar que toda a suíte de regressão foi aprovada a cada tentativa: F é
limitado à cobertura efetivamente selecionada e medida.

### Parada operacional e população de análise

O orquestrador define classificacao_final por criterio, mas interrompe a cadeia
por classificacao_sem_separacao. As métricas delimitam sua cadeia pela primeira
classificação original de aceite e conservam registros posteriores separadamente.
Explicar essas duas decisões evita que número de registros, número de tentativas
analisadas e número de casos aceitos sejam confundidos. A frase genérica
“parou na primeira correção válida” é insuficiente sem a definição usada.

### Avaliação conjunta da RRIS

O TCC1 previa medir a redução após aplicar as correções aceitas. Existem agora
evidências conjuntas nos três modelos. Os artefatos consultados registram redução
estática disponível e conjunto_funcionalmente_validado=false nas três execuções.
Descrever o procedimento no capítulo 3; apresentar falhas, números e interpretação
no capítulo 5. Não equiparar aceites individuais à compatibilidade funcional de
todos os patches aplicados em conjunto.

## Pontos cuja decisão ainda depende dos autores

- Justificativa efetiva da inclusão dos dois modelos posteriores.
- Origem e nível de revisão humana das classificações da triagem.
- Procedimento de inspeção de patches efetivamente realizado.
- Uso de IA e validações humanas que podem ser declarados.
- Manutenção de cronograma histórico e organização final das novas subseções.

## Fontes para conferir durante a redação

Caminhos abaixo relativos à raiz do experimento na revisão indicada:

- `docs/protocolo_experimental.md`: catálogo (§11), integração (§12), RAG (§13),
  consolidação (§14), testes relacionados, comparador de 06/11 e Docker.
- `config/execucao_docker_78.yaml`: seleção e condições da configuração final.
- `outputs/campanha_docker/AMP_REAL_20261106T105533Z_aa697342/contrato_execucao.json`.
- `outputs/campanha_docker/AMP_REAL_20261106T125801Z_0eb68fe4/contrato_execucao.json`.
- `outputs/campanha_docker/AMP_REAL_20261106T151004Z_f49ac0d2/contrato_execucao.json`.
- `src/pipeline/etapas/e04_prompt/montagem.py`: informação fornecida por estratégia.
- `src/pipeline/etapas/e05_geracao_llm/esquema.py`: resposta estruturada.
- `src/pipeline/orquestracao/campanha.py`: classificações e parada estrita.
- `src/pipeline/etapas/e01_analise_sast/comparacao.py`: comparador v3.
- `src/pipeline/etapas/e09_metricas/calculo.py`: denominadores e populações.
- `outputs/README.md`: distinção entre campanhas, pilotos e entradas geradas.
- `outputs/rris/<EXECUCAO>_METRICAS/metricas.json`: situação da RRIS conjunta.

A documentação mistura registros históricos com atualizações posteriores.
Para descrever as campanhas finais, os contratos e artefatos específicos têm
precedência sobre afirmações antigas de uma seção do protocolo ou de um README.
