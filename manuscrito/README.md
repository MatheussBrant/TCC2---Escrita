# Textos do TCC2

Esta pasta recebe os arquivos Markdown produzidos durante a redação. As tarefas
e critérios estão em [features/](../features/README.md); a organização dos cinco
capítulos está no [plano de redação](../docs/plano-redacao.md).

## Organização das entregas

| Pasta criada ao executar a feature | Conteúdo principal | Destino final |
|---|---|---|
| `01-introducao/` | `capitulo.md` | Capítulo 1 |
| `02-fundamentacao/` | `texto.md` | Capítulo 2 — conceitos |
| `03-trabalhos-relacionados/` | `texto.md` | Capítulo 2 — relacionados |
| `04-metodologia/` | `texto.md` | Capítulo 3 — método |
| `05-implementacao/` | `texto.md` e diagrama | Capítulo 3 — desenvolvimento |
| `06-resultados/` | `texto.md` e tabelas | Capítulo 4 — resultados |
| `07-discussao/` | `texto.md` e matriz de ameaças | Capítulo 4 — discussão |
| `08-conclusao/` | `capitulo.md` | Capítulo 5 |
| `09-reproducao/` | Apêndices e declaração de IA | Complementos |
| `10-resumos/` | Resumo, abstract e palavras-chave | Elementos iniciais |
| `11-integracao/` | `tcc2.md` e referências integradas | Monografia reunida |
| `evolucoes/E001-assunto/` em diante | `texto.md` e `impacto.md` | Atualizações dos destinos definidos |

Cada pasta também recebe `evidencias.md` e `entrega.md`, além dos arquivos exigidos
pela sua especificação. Um plano de execução persistido fica em `plano.md` na
mesma pasta. As subpastas e textos são criados quando houver conteúdo; a tabela
descreve o destino esperado, não capítulos já escritos.

## Planejar, redigir e revisar

1. Pedir a `tcc2-planejar` um plano para a feature: fontes, argumento, etapas,
   arquivos e critérios a verificar. O pedido de planejamento pode se limitar
   à resposta no chat ou ao plano nativo da extensão. Quando solicitado salvar
   no repositório, usar `plano.md` da pasta exclusiva.
2. Pedir a `tcc2-redigir` para executar a especificação e o plano adotado,
   produzindo texto completo, evidências e autoavaliação dos critérios.
3. Pedir a `tcc2-revisar` um parecer em `revisoes/<ID>/parecer.md`; as correções
   retornam ao responsável pelo texto. F11 integra as versões reconciliadas.

F01–F10 podem produzir rascunhos em paralelo, cada responsável em sua pasta,
conforme as vagas reais do cliente. Discussão, conclusão e resumos precisam ser
conferidos com método e resultados antes do fechamento. Dois agentes não devem
editar a mesma pasta ao mesmo tempo, inclusive usando clientes diferentes.
