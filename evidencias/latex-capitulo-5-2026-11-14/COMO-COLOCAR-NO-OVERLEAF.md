# Arquivos necessários para o capítulo 5

Copie da pasta `TCC2___Caio_Lamego_e_Matheus_Brant/` para os mesmos caminhos no Overleaf:

1. `editaveis/resultado-discussoes.tex` — substitui o capítulo provisório.
2. `figuras/resultados-aceites-por-estrategia.png` — figura usada pelo capítulo.

No preâmbulo de `tcc.tex`, antes de `\begin{document}`, acrescente:

```latex
\usepackage{listings}
```

Esse pacote já foi acrescentado na cópia local. Os demais pacotes necessários
já estão no modelo enviado (`tabularx`, `booktabs`, `array`, `float` e `graphicx`).
O `tcc.tex` original também já inclui o capítulo no lugar correto:

```latex
\input{editaveis/resultado-discussoes}
```

As tabelas estão dentro do `.tex`; não precisam ser enviadas separadamente.
As duas referências bibliográficas usadas já estão no `bibliografia.bib` do modelo.
A figura é fornecida em PNG; nenhum PDF compilado precisa ser enviado.
