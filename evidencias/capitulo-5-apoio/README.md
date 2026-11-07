# Apoio ao capítulo 5

As [notas de evidência](../capitulo-5-notas.md) descrevem o recorte, as fontes,
os cálculos e os limites desta análise. Esta pasta contém dados derivados;
os resultados originais continuam no repositório experimental irmão.

- `consolidados/`: saídas novas do consolidador offline existente. Os 45 arquivos
  foram comparados aos originais e coincidiram byte a byte.
- `analisar_dados.py`: confere essas saídas e deriva métricas, grupos,
  sobreposição dos casos, custos e tempos.
- `dados-conferidos.json`: resultados da conferência e informações de contexto.
- `metricas-conferidas.csv`: numeradores e denominadores por definição de F.
- `estrategias.csv`: primeiros aceites e casos alcançados por etapa.
- `grupos-casos.csv`: aceites por tipo, regra, OWASP e classificação arquivada.
- `casos-modelos.csv`: casos aceitos e primeira estratégia de aceite.
- `tentativas-resumo.csv`: versão compacta dos registros, preservando pós-aceite.
- `conferir_exemplos.py` e `exemplos/`: quatro tentativas, patches e conferência
  de 28 hashes de artefatos; leitura documental com apoio automatizado.
- `gerar_grafico.py`: figura descritiva com os dados de `estrategias.csv`.
- `requisitos-graficos.txt`: versões utilizadas para gerar a figura.
- `fontes-sha256.json`: identificação das fontes consultadas diretamente.
- `preservacao-inicial.json`: hashes dos manuscritos de partida e do TCC1 completo.
- `mapa-paragrafos.json`: correspondência das 40 unidades de conteúdo do plano.

Os scripts leem os arquivos originais e escrevem apenas na escrita. Não chamam
modelos, Semgrep ou testes do alvo. `analisar_dados.py` e `conferir_exemplos.py`
usam a biblioteca padrão do Python. Para o gráfico, instalar as dependências
em ambiente separado com `pip install -r requisitos-graficos.txt`.

A partir da raiz de escrita:

```sh
python3 evidencias/capitulo-5-apoio/analisar_dados.py
python3 evidencias/capitulo-5-apoio/conferir_exemplos.py
python3 evidencias/capitulo-5-apoio/gerar_grafico.py
```

As versões PNG, PDF e SVG da figura estão em
[`manuscrito/assets/capitulo-5/`](../../manuscrito/assets/capitulo-5/).
Não são capturas do painel nem resultados de novas campanhas.
