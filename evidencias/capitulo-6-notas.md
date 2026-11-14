# Capítulo 6 — notas de evidência

Primeira redação produzida em 14/11/2026, a pedido do autor, para concluir o estudo
atual. Não constitui revisão ou aprovação da orientadora. Linguagem e organização
seguem `docs/diretrizes-escrita.md` e `docs/criterios-escrita.md`.

## Arquivos

- Texto: `manuscrito/06-consideracoes-finais.md`.
- LaTeX: `../TCC2___Caio_Lamego_e_Matheus_Brant/editaveis/elementosdopostexto.tex`
  (caminho a partir da raiz da escrita). O `tcc.tex` já inclui esse arquivo depois
  de `resultado-discussoes.tex`, portanto o capítulo ocupa a posição 6.
- O LaTeX anterior foi preservado em
  `capitulo-6-2026-11-14/elementosdopostexto-antes.tex`.
- Índice e sumário Markdown atualizados para registrar a redação e as três seções.
- A conclusão histórica `manuscrito/05-consideracoes-finais.md` não foi alterada.

## Base utilizada

O texto retoma o objetivo geral e os cinco objetivos específicos da Seção 1.3,
os critérios de aceite das Seções 3.10–3.11, a implementação descrita no capítulo 4
e os resultados do capítulo 5, especialmente suas Seções 5.2–5.8 e 5.10.
A introdução Markdown foi utilizada como referência atual do estudo.

SHA experimental confirmado: `2e8f9a9285c8bf521ee3ddc33d8d20a62495ca59`, igual ao
registrado nas últimas conferências dos resultados. Não houve novo experimento,
consulta bibliográfica ou inferência de dados não medidos. Os hashes dos textos
consultados estão em `capitulo-6-2026-11-14/fontes-sha256.json`.

## Correspondência entre conclusões e evidências

| Conteúdo da conclusão | Base e limite preservado |
|---|---|
| Desenvolvimento e avaliação do fluxo | Objetivos da introdução; implementação do capítulo 4. Atingir o objetivo de investigar não foi apresentado como corrigir todas as ocorrências ou integrar todas as propostas com sucesso. |
| Aceites no catálogo completo | Tabela 2 do capítulo 5: 38/78, 51/78 e 49/78, com F por critérios. Os denominadores incluem os 21 falsos positivos e os dois inconclusivos. |
| Aceites nos confirmados | Tabela 2 e conferência dos CSVs: 32/55, 39/55 e 36/55. Confirmado conserva o sentido da triagem documentada. |
| Escolha dos modelos | Seções 5.2 e 5.4: GPT-5.6 Luna em quantidade de aceites/TRV principal; GPT-6 Luna em custo calculado de geração, custo por caso, duração de campanha e TPF; GPT-4.1 mini em latência média de geração. Sem generalização universal. |
| Ganho acumulado das estratégias | Tabelas 5 e 5a: todas as etapas acrescentaram aceites nos três modelos; P3 teve maior contribuição adicional após P1. Mantida a premissa do desenho sobre casos aceitos antes, sem atribuir sua verificação ao experimento. |
| Categorias OWASP | Tabela 10a, recorte confirmado: A05 com 15/16 em cada Luna; A01 favorece GPT-5.6 Luna; A06 empata mini/Luna 5.6; A07 empata os três; A08 sem aceite. Não se reproduziu no fechamento uma indicação baseada em todos os alertas sem identificar o recorte. |
| Aplicação conjunta | Seção 5.7 e Tabela 12: maior RRIS 70,51% no GPT-5.6 Luna; nenhum conjunto aprovado funcionalmente. Distinguidos patches aprovados individualmente sobre o código original da versão resultante da integração. |
| Contribuições | Pipeline, registros, isolamento, Docker e painel implementados; indicadores individuais e avaliação conjunta mantidos distintos. Repetibilidade apoiada pelos artefatos, sem afirmar replicação independente realizada. |
| Trabalhos futuros | Continuidade das propostas de 5.10: integração incremental, repetição e outros projetos, estratégias independentes e avaliação adicional de segurança. Acrescentada a proposta de contabilizar infraestrutura, revisão e resolução de conflitos, sem atribuir esses custos aos dados atuais. |

## Conferência de texto e LaTeX

`capitulo-6-2026-11-14/converter_e_conferir.py` produziu um capítulo, três seções
e 15 parágrafos. O script confere os blocos correspondentes, as razões e os
percentuais contra o capítulo 5, a inclusão existente no `tcc.tex` e a unicidade
dos labels. Os totais por modelo e os numeradores no recorte confirmado foram
também conferidos contra `revisao-capitulo-5-2026-11-13/conferencia.json`.

O relatório é `capitulo-6-2026-11-14/conferencia.json`. O texto não acrescenta
referências bibliográficas, figuras, tabelas ou dependências de pacotes. Não foi
gerado PDF, conforme a preferência do autor pela inclusão manual no Overleaf.
`git diff --check` sem erros.

## Pendência concreta de coerência do projeto LaTeX

`TCC2___Caio_Lamego_e_Matheus_Brant/editaveis/introducao.tex` ainda descreve
TCC 1/TCC 2 como entregas separadas, a execução como futura, o capítulo 4 como
prova de conceito e o capítulo 5 como considerações finais. Isso difere da
introdução Markdown atual e dos capítulos 3–6 do modelo. Essa introdução precisa
ser alinhada em tarefa própria; não foi reescrita durante a redação do capítulo 6.
As conclusões agora escritas se baseiam no estudo efetivamente apresentado nos
capítulos revisados, sem reproduzir a organização histórica.

## Versão concisa em cinco parágrafos — 14/11/2026

O autor solicitou no máximo quatro ou cinco parágrafos. A redação foi reduzida
para cinco parágrafos, sem subseções: objetivo/contribuição, modelos, estratégias
e OWASP, aplicação conjunta e trabalhos futuros. A versão longa permanece em
`capitulo-6-2026-11-14/capitulo-6-antes-sintese.md`, com seu LaTeX correspondente.
O sumário e o índice foram ajustados para a nova estrutura.

Preservados os 51/78, 49/78 e 38/78 aceites no catálogo completo, os 39/55 do
GPT-5.6 Luna no recorte confirmado e os 15/16 de cada Luna em A05 entre os
confirmados. Identificados o catálogo com falsos positivos/inconclusivos,
F por critérios e a reprovação funcional conjunta. A premissa das estratégias
permanece no método e no capítulo 5, sem ser reapresentada como resultado medido.

O conversor foi ajustado para exigir exatamente cinco parágrafos e nenhuma
subseção. Markdown e LaTeX conferidos, com atualização do manifesto de hashes;
`git diff --check` sem erros. Nenhum PDF foi gerado.
