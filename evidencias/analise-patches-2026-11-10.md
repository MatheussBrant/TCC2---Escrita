# Delimitação da análise dos patches — 10/11/2026

## Declaração do autor

Ao ser perguntado se, além da revisão dos falsos positivos, houve exame manual
das correções, o autor respondeu: “MANUEALMENTE NÃO LEVAMOS EM CONSIDERAÇÃO AS MAETRICAS DEFINIDAS”.
No contexto da pergunta, a resposta foi interpretada como ausência de inspeção
manual dos patches e utilização das métricas definidas para avaliar as correções.
Não foram atribuídos revisores, casos ou procedimentos de revisão manual inexistentes.

A revisão humana dos 21 falsos positivos, anteriormente confirmada, é uma
atividade distinta: examina a pertinência dos alertas originais, não valida
manualmente os patches gerados. Essa declaração anterior permanece preservada.

## O que está documentado

A Seção 5.6 já contém leitura documental, com apoio automatizado, de quatro
tentativas em dois casos: `AMP20721d202c8b96d6` (`routes/trackOrder.ts`,
GPT-4.1 mini/P1) e `AMP869de4721b99fc7c` (`routes/captcha.ts`, GPT-4.1 mini/P1,
GPT-6 Luna/P1 e P2).

A seleção foi ilustrativa, pela disponibilidade de artefatos, clareza das
alterações e contraste entre resultados. Foram relacionadas as alterações,
a remoção do alerta (R), o resultado funcional (F) e os novos alertas (M),
com atenção ao tratamento do conjunto D. Não foi uma amostra representativa
nem um novo critério de aceite. O caso CAPTCHA tem classificação de falso
positivo: ilustra os efeitos da alteração, sem demonstrar correção de uma
vulnerabilidade confirmada. A pendência de excluir falsos positivos das métricas
não é resolvida por esta declaração.

Fontes: `capitulo-5-notas.md`, seção dos exemplos;
`capitulo-5-apoio/conferir_exemplos.py`; `capitulo-5-apoio/exemplos/indice.json`
e patches copiados. A integridade dos 28 artefatos foi novamente conferida
por leitura e SHA-256 nesta tarefa. Nenhum teste ou campanha foi executado.
Fonte experimental mantida no commit `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`.

## Resolução editorial

Removida a pendência na Seção 3.10. A metodologia e a Seção 5.6 passaram a
explicitar que a avaliação não incluiu inspeção manual dos patches pelos autores.
A análise documental dos exemplos foi descrita como apoio à discussão.
Pendências PE03 do Capítulo 3 e PE5-03 do Capítulo 5 resolvidas quanto à natureza
e ao alcance do procedimento, sem inventar validação humana ou aprovação dos exemplos.
