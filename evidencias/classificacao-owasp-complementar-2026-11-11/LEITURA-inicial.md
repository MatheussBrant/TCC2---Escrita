# Classificação OWASP complementar dos 49 casos sem associação

Consulta em 11/11/2026. Esta tabela é uma análise derivada: não altera o catálogo, os registros das campanhas, os nomes dos artefatos ou as métricas publicadas. Não foram executados modelos ou testes.

Base experimental: HEAD `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`.
Fonte: `tcc2-llm-sast-juiceshop/outputs/catalogos/ampliado_v1/catalogo_issues.json`.
SHA-256 do catálogo: `08672899e712fbeef2070f01c58b5867e080e74f716ddc7d8fd10c6d58344aee`.

## Método e limites

Para cada ocorrência originalmente com `owasp_2025=null`, cruzou-se o CWE registrado com as listas oficiais “List of Mapped CWEs” das categorias OWASP Top 10:2025. As URLs estão em cada linha do CSV. O rótulo original e a classificação de triagem foram preservados.

45 ocorrências têm correspondência explícita CWE–OWASP nas listas consultadas. Para quatro ocorrências CWE-943, A05 é uma proposta por contexto da regra (NoSQL/entrada não confiável), pendente de revisão, e não uma correspondência explícita da lista oficial.

A classificação descreve o tipo de fraqueza sinalizado. Não constitui revisão independente do código nem prova de explorabilidade. Falsos positivos e inconclusivos permanecem com esses rótulos. CWEs amplos, em particular CWE-20, permitem agrupamento taxonômico mas não demonstram um mecanismo específico de exploração. A atribuição do CWE pela regra não foi revalidada nesta análise.

## Distribuição proposta apenas dos 49 casos anteriormente SEMOWASP

| Categoria | Ocorrências |
|---|---:|
| A01 | 19 |
| A02 | 1 |
| A04 | 2 |
| A05 | 18 |
| A06 | 5 |
| A07 | 2 |
| A08 | 2 |

## Uso na redação

Apresentar como classificação complementar posterior às campanhas. Manter o agrupamento original identificável; se usado para novos resultados por OWASP, produzir tabelas derivadas e explicar o método e os denominadores. A associação não exige repetir geração ou validação. Os resultados gerais por tentativa não são alterados por uma mudança de agrupamento.

Arquivo: [classificacao-complementar.csv](classificacao-complementar.csv).
