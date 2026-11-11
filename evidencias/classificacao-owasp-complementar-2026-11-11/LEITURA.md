# Classificação OWASP complementar — conferência de 11/11/2026

Os 78 casos têm categoria no agrupamento complementar: 29 associações originais
foram preservadas e 49 foram acrescentadas. A análise é posterior às campanhas.
Catálogo, prompts, respostas, nomes dos artefatos e resultados experimentais
originais não foram alterados. Não houve chamada a modelos, execução do pipeline,
SAST ou novos testes do alvo.

## Método

Foram arquivadas as dez páginas em inglês do repositório oficial `OWASP/Top10`,
no commit `3a31f35346c3f4e90f350395124382fa53af2afe`. As listas “List of Mapped
CWEs” foram extraídas dos arquivos e conferidas contra o manifesto de origem
em `fontes-owasp/manifesto.json`. Os documentos preservam a autoria da OWASP
e a licença CC BY 3.0 indicada no manifesto. A análise pode ser repetida offline.

Dos 49 casos, **41** receberam a categoria explicitamente associada ao CWE na
lista oficial e **oito** receberam associação contextual documentada.

Na proposta inicial eram 45 correspondências e quatro inferências pendentes.
Os quatro CWE-943 foram associados a A05 pela descrição de injeção NoSQL e pelo
contexto arquivado. O caso de `chat.ts` continua falso positivo: o código converte
a entrada em número; A05 identifica a família do alerta, sem confirmar exploração.

Também foram revistas quatro ocorrências CWE-20. A associação automática desse
CWE a A05 não descreve adequadamente seus mecanismos específicos:

| Mecanismo | Categoria da análise | Fundamentação |
|---|---|---|
| Nota sem intervalo em `models/feedback.ts` | A06 | Restrição de negócio ausente; sem evidência de injeção. |
| Primeiro BasketId validado e último persistido | A01 | Contorno da verificação de propriedade do carrinho. |
| Quantidade negativa em `routes/basketItems.ts` | A06 | Restrição de quantidade positiva ausente no fluxo de compra. |
| Validação de cadastro contornada em `server.ts` | A07 | Estabelecimento de credenciais vazias e confirmação de senha não exigida, conforme a triagem arquivada. |

As decisões são interpretativas, documentadas e passíveis de revisão. A coluna
`owasp_por_cwe` preserva a correspondência taxonômica, e `owasp_2025_analise`
contém a categoria adotada. Não se alteraram os CWEs originais.

O contexto foi confrontado com as descrições de
[A01](https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/),
[A05](https://top10.owasp.org/2025/A05_2025-Injection/),
[A06](https://top10.owasp.org/2025/A06_2025-Insecure_Design/) e
[A07](https://top10.owasp.org/2025/A07_2025-Authentication_Failures/).
Não se afirma que a OWASP classificou individualmente estes casos.

## Bases e verificações

- Experimento: `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`.
- Alvo: `f915bddd82790d0f3018902d36ae9b4241a5f51f`.
- Fonte: `outputs/catalogos/ampliado_v1/catalogo_issues.json`, SHA-256
  `08672899e712fbeef2070f01c58b5867e080e74f716ddc7d8fd10c6d58344aee`.
- Conferência por caso dos hashes dos arquivos no objeto Git fixado e da igualdade
  dos trechos arquivados com as linhas da fonte: **78/78**.
- Preservados 55 rótulos confirmados, 21 falsos positivos e dois inconclusivos.
  Entre os 49 complementares são 38, dez e um, respectivamente.
- Os CSVs originais `outputs/rris/<execução>_METRICAS/casos.csv` sustentam os
  234 pares caso/modelo. F=`criterio`, aceite por caso conforme o consolidador.
- Todos os 78 casos foram iniciados em cada campanha. Os totais de aceites
  permanecem **38**, **51** e **49**, para GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna.
  Os denominadores incluem falsos positivos e inconclusivos e contam casos,
  não tentativas. As oito decisões contextuais preservam esse mesmo universo.

## Distribuição

| Categoria | 49 complementares | Total dos 78 |
|---|---:|---:|
| A01 | 20 | 26 |
| A02 | 1 | 3 |
| A04 | 2 | 5 |
| A05 | 14 | 22 |
| A06 | 7 | 12 |
| A07 | 3 | 7 |
| A08 | 2 | 3 |
| Total | 49 | 78 |

A03, A09 e A10 não receberam casos nessa partição. Isso não demonstra ausência
dessas classes de falhas na aplicação, nem representatividade de todo o Top 10.

## Arquivos e reprodução

- `classificacao-complementar.csv`: os 49 casos, categorias original/por CWE/da
  análise, método, triagem, fonte e justificativa.
- `classificacao-78-casos.csv`: inclui os 29 rótulos preservados.
- `decisoes-contextuais.json`: decisões explícitas para os oito casos interpretados.
- `revisao-contextual.json`: trechos e justificativas arquivadas desses oito casos.
- `casos-modelos-classificados.csv`: 234 pares caso/modelo com aceite por critérios.
- `aceites-por-owasp-complementar.csv`: numeradores, denominadores e triagem por grupo.
- `tabela-owasp-complementar.md`: tabela incorporada como Tabela 10a do Capítulo 5.
- `fontes-owasp/`: documentos oficiais fixados e manifesto de origem.
- `manifesto-conferencia.json`: hashes, proveniência e contagens verificadas.
- `proposta-inicial.csv` e `LEITURA-inicial.md`: versão anterior preservada;
  seus números de 45 correspondências e quatro inferências foram superados.

A partir da raiz de escrita:

```sh
python3 evidencias/classificacao-owasp-complementar-2026-11-11/conferir_classificacao.py
```

O script lê as fontes e grava apenas derivados nesta pasta. Confere unicidade,
população, correspondências, triagem, hashes, trechos e totais de aceites. Os
caminhos usam o layout desta máquina, com escrita e experimento como irmãos.

## Integração e limites

A seção 3.10 descreve o procedimento posterior às campanhas. O Capítulo 5 mantém
a Tabela 10 original, acrescenta a Tabela 10a e distingue os recortes na resposta
à Q3. Não foram substituídos silenciosamente os resultados originais por OWASP.

Esta é uma revisão documental com apoio automatizado, sem revisão humana
independente, novo teste de exploração, revisão integral dos CWEs originais ou
validação adicional dos patches. As oito decisões contextuais têm justificativas
para avaliação acadêmica. Eventual revisão dessas decisões exige regenerar os
agrupamentos e atualizar a Tabela 10a, sem repetir a geração das correções.
