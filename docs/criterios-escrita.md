# Critérios de linguagem e profundidade da escrita

Diretriz definida pelo autor para todos os planos e capítulos do TCC2: escrita
acadêmica, objetiva e explicativa, próxima ao estilo do TCC1, com leitura fluida
e detalhamento técnico proporcional ao que o leitor precisa compreender.

## Referência de estilo

Usar o TCC1 como referência de continuidade: apresentar o assunto, explicar a
decisão ou o funcionamento e conectar a explicação ao objetivo do trabalho.
Preservar o vocabulário já estabelecido quando adequado. Corrigir repetições,
imprecisões e problemas de redação do original durante a adaptação.

## Orientações para todos os capítulos

- Desenvolver uma ideia central por parágrafo e ligá-la ao argumento da seção.
- Preferir frases diretas e parágrafos de extensão moderada, sem impor tamanho fixo.
- Explicar o que foi feito e por que isso importa para o experimento.
- Apresentar siglas e termos especializados na primeira ocorrência; depois usar
  a mesma denominação de forma consistente.
- Usar exemplos curtos para esclarecer decisões mais abstratas.
- Evitar sequências de nomes de funções, campos, caminhos, versões e comandos
  no corpo do texto. Usar tabelas, notas de trabalho ou apêndices quando necessário.
- Tratar fontes de código e identificadores das campanhas como apoio à verificação.
  Sua presença no plano não exige reproduzi-los em todos os parágrafos finais.
- Apresentar apenas tabelas e figuras que ajudem a explicar ou comparar; não repetir
  em prosa todos os valores já apresentados nelas.
- Reduzir repetições entre capítulos e remeter a explicações anteriores.
- Manter precisão: clareza não autoriza omitir denominadores, condições de execução
  ou limitações que alterem o significado dos resultados.
- Não retirar termos fundamentais como RAG, SAST, worktrees, R/F/M e conjunto D;
  explicá-los em linguagem acessível e aprofundar apenas o necessário.
- Descrever ações realizadas no passado e definições no presente, conforme o contexto.

## Profundidade por capítulo

| Capítulo | O que o leitor deve compreender | Detalhes que podem ficar fora do corpo principal |
|---|---|---|
| 3 — Metodologia | Como o experimento foi organizado, quais escolhas foram feitas e como as correções foram avaliadas. | Identificadores completos, versões de arquivos de configuração, campos internos e etapas de algoritmos. |
| 4 — Implementação | Como as partes do sistema se conectam e tornam o método executável. | Explicação função por função, comandos extensos, estruturas completas de JSON, travas de processo e detalhes de bibliotecas. |
| 5 — Resultados | O que foi observado, como interpretar as diferenças e quais respostas são sustentadas. | Listagens completas de execuções e cálculos extensos que podem ser consultados em tabelas auxiliares ou apêndices. |

A explicação das worktrees deve abordar cópias separadas, distribuição das
tentativas e restauração do código. A apresentação do painel deve destacar sua
finalidade e o acompanhamento das execuções. A possibilidade de replicação com
Docker pode ser apresentada em um parágrafo breve, como decidido pelo autor.

## Exemplos da linguagem desejada

**Worktrees:** “Para evitar que uma tentativa interferisse nas demais, foram
utilizadas cópias de trabalho separadas do projeto. Após cada tentativa, o código
era restaurado à versão original, mantendo as mesmas condições para a seguinte.”

**Verificação funcional:** “As correções foram avaliadas por testes relacionados
aos arquivos modificados. Os resultados foram comparados com uma execução de
referência, permitindo distinguir falhas já existentes de problemas introduzidos
pela alteração.”

Esses exemplos orientam o estilo; a redação final deverá ser conferida com as
evidências da execução descrita.

## Revisão de cada seção

Conferir se o leitor consegue identificar o assunto, sua finalidade e sua relação
com o estudo. Encurtar explicações que apenas descrevem detalhes internos.
Preservar as distinções entre alerta e vulnerabilidade, ausência de medição e
falha, aceite individual e avaliação conjunta, resultado observado e generalização.
Os parágrafos dos planos são unidades de conteúdo: podem ser unidos ou divididos
para melhorar a fluidez, preservando a rastreabilidade das alterações.
