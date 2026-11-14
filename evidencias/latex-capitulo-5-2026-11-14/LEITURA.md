# Capítulo 5 integrado ao projeto LaTeX — 14/11/2026

Fonte: `manuscrito/05-resultados-discussao.md`, SHA-256
`f1e8c8c19e737048a1a1718c7cebd8d45934d4f3de3f5e1605346189685e744d`.
Destino: `../TCC2___Caio_Lamego_e_Matheus_Brant/editaveis/resultado-discussoes.tex`
(a partir da raiz de escrita). O arquivo principal `tcc.tex` já incluía esse
capítulo depois da implementação e antes das considerações finais.

Foi utilizado o template institucional existente, baseado em `abntex2`, A4,
fonte de corpo de 12 pontos e margens/estilos configurados pelo próprio projeto.
Não se realizou auditoria integral de conformidade de todos os capítulos ou de
cada requisito das normas ABNT.

## Conversão

- Texto revisado preservado em 76 blocos de parágrafo, dez seções e seis subseções.
- 14 tabelas com títulos acima, fontes abaixo, corpo em espaçamento simples e
  colunas ajustadas à largura do texto. Usados `tabularx` e `booktabs`, já carregados.
- Numeração automática e remissões por `label`/`ref`; as tabelas locais 1–12,
  incluindo 5a e 10a, passaram aos números 6–19 do documento completo.
- Figura copiada em PDF vetorial para `figuras/resultados-aceites-por-estrategia.pdf`.
- Dois excertos de código preservados, com quebra visual de linhas por `listings`.
- Perguntas Q1–Q5 destacadas e unidas ao início das respostas.
- Termos estrangeiros em itálico e caracteres especiais escapados para LaTeX.
- Citações de Khan, Liu e Gao e Sriram convertidas para `citeonline`, usando as
  duas entradas já existentes no arquivo bibliográfico.
- Fontes textuais das tabelas mantidas. A inclusão dos links do GitHub foi adiada
  pelo autor e não integra esta tarefa.

## Ajustes de integração

- `tcc.tex`: inclusão do pacote `listings`.
- `editaveis/consideracoes.tex` e `editaveis/elementosdotexto.tex`: remissões ao
  capítulo 5 passaram a usar `ref{cap:resultados}`; conteúdo acadêmico preservado.
- `bibliografia.bib`: segunda entrada com chave duplicada
  `owasp_top10_2025_intro` recebeu a chave `owasp_top10_2025_intro_20260618`.
  Ambas as entradas e seus campos foram preservados; as citações existentes
  continuam apontando para a primeira, que já era a considerada pelo BibTeX.
- Capa EPS preservada e convertida também para `figuras/capa.pdf`; em
  `fixos/customizacoes.sty`, a referência sem extensão permite usar PDF em
  compilação direta e EPS no fluxo DVI. Isso resolve a restrição do Tectonic a EPS.
- Os arquivos anteriores às alterações estão preservados nesta pasta com
  sufixo `-antes`. O projeto LaTeX de destino não possui repositório Git nesta cópia.

## Verificação

```sh
python3 evidencias/latex-capitulo-5-2026-11-14/verificar_conversao.py
```

O script confere hashes do Markdown e do TeX, todos os valores das 14 tabelas,
os 76 blocos de texto, os dois excertos, as cinco perguntas, a figura e a existência
única dos labels e das entradas de citação usadas no capítulo. O manifesto é
`conversao.json`. O conversor utilizado é `converter_capitulo.py`.

O documento completo foi compilado com Tectonic 0.17.0 a partir de `tcc.tex`.
Não houve referência/citação indefinida ou aviso de estouro de margem no capítulo 5.
Foram inspecionadas visualmente as páginas de métricas, OWASP confirmado, RRIS
e figura/ganho das estratégias. As fontes e a largura das tabelas estão legíveis.

`validacao.json` registra o resultado e o mapeamento dos números das tabelas.
`tcc.log`, `tcc.blg` e `compilacao.txt` preservam a compilação. Permanecem avisos
anteriores de largura na ficha e em outros capítulos, aspas Unicode no capítulo 2
no motor utilizado e âncoras PDF duplicadas do template, sem impedir a geração.

## PDFs

No projeto LaTeX, `tcc.pdf` contém a compilação completa e `capitulo-5.pdf` contém
as 20 páginas físicas 70–89 extraídas, mantendo a numeração impressa 69–88.
A prévia isolada serve à leitura; os destinos de links para outros capítulos e
para a bibliografia estão disponíveis no PDF completo.

Os capítulos anteriores e as considerações finais não foram revisados quanto
a conteúdo nesta tarefa. A atualização desse conteúdo permanece independente
da inclusão do capítulo 5. Nenhum experimento ou métrica foi alterado.
