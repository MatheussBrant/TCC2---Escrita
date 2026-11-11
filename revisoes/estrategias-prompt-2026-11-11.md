# Conferência da seção 3.7 contra a implementação

Escopo: fidelidade da descrição das estratégias, seleção de contexto e formato
de resposta. Leitura de código e artefatos, com apoio automatizado. Não houve
execução de modelos, novos scans ou novos testes do alvo.

## Fontes

- `src/pipeline/etapas/e04_prompt/montagem.py`: montagem e política de contexto.
- `config/prompts/roteiro_raciocinio_guiado.md`: cinco etapas do roteiro P2/P4.
- `src/pipeline/etapas/e05_geracao_llm/esquema.py`: seis campos de resposta e
  estrutura de cada edição.
- Contratos e prompts das três campanhas finais de 06/11/2026 em
  `outputs/campanha_docker/AMP_REAL_20261106T*/`.

Os caminhos acima são relativos ao repositório experimental irmão.

## Resultado da conferência

| Afirmação da seção | Evidência | Resultado |
|---|---|---|
| P1 recebe código e instrução, sem bloco explícito SAST ou RAG | Conjuntos `COM_ALERTA`, `COM_RAG` e mensagens arquivadas | Compatível |
| P2 acrescenta roteiro ao conteúdo de P1 | `COM_ROTEIRO`, montagem e texto efetivamente inserido | Compatível após explicitar a etapa de impacto |
| P3 recebe diagnóstico e documento recuperado | `bloco_alerta`, recuperação e mensagens arquivadas | Compatível |
| P4 combina P3 com o roteiro de P2 | Ordem de montagem e mensagens arquivadas | Compatível |
| Política comum de código: arquivo até 250 linhas; janela de até 60 linhas de cada lado nos demais | `_contexto` e metadados arquivados | Compatível |
| Papel, tarefa, restrições e formato comuns | Constantes e mensagens das quatro estratégias | Compatível |
| JSON com seis campos e edições contendo arquivo, trecho original e substituto | Classes `Correcao` e `Edicao` | Compatível como formato solicitado; não implica que todas as respostas recebidas fossem válidas |

Foram conferidos **834 prompts**: P1=234, P2=218, P3=207 e P4=175.
Por campanha: 274 no GPT-6 Luna, 277 no GPT-5.6 Luna e 283 no GPT-4.1 mini.
Incluem os registros posteriores ao primeiro aceite; essas contagens não são
os denominadores da população principal de análise.

Para cada prompt, foram verificados o hash das mensagens, papel, tarefa,
restrições, formato e presença/ausência do diagnóstico SAST, do documento
recuperado e do roteiro conforme a estratégia. Os hashes dos componentes de
prompt dos três contratos coincidiram com os calculados pelo código consultado.

## Correção realizada e limites

O texto anterior omitia a etapa de descrever o impacto de segurança e incluía
as limitações na enumeração do roteiro. A seção passou a apresentar as cinco
etapas efetivamente implementadas, separando o campo de limitações do JSON,
comum a todas as estratégias. O impacto não tem campo exclusivo no schema.

A conferência verifica o conteúdo solicitado aos modelos e o formato esperado,
não a qualidade das respostas nem o cumprimento de cada instrução. A seção
preserva a ressalva de que P3/P4 acrescentam diagnóstico e documentação em
conjunto, sem isolar causalmente um efeito do RAG. Não houve revisão humana
independente nesta conferência.
