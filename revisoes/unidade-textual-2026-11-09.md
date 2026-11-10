# Revisão de unidade textual — 09/11/2026

Revisão editorial e correção solicitadas pelo autor: a monografia deve ser
um trabalho completo e autônomo, sem referências a TCC1/TCC2 como entregas
separadas. Não constitui revisão humana independente, nova validação do
experimento ou aprovação acadêmica.

## Achados e correções

| Prioridade | Local | Problema identificado | Correção aplicada |
|---|---|---|---|
| Alta | Introdução 1.4–1.5 | O experimento era apresentado como continuação futura, e a organização ainda remetia à prova de conceito e às considerações finais antigas. | Apresentação do estudo realizado e da estrutura atual: fundamentação, metodologia, implementação, resultados e conclusão. |
| Alta | Metodologia 3.1–3.5 e 3.9 | Perguntas, modelos, prompts e métricas eram descritos por comparação com uma entrega anterior. | Descrição direta das decisões e definições da mesma pesquisa, mantendo os critérios e denominadores. |
| Média | Referencial 2.2 e 2.4 | Trechos sobre o próprio experimento usavam futuro e apresentavam possibilidades que não correspondiam necessariamente ao desenho realizado, como exemplos few-shot. | Remissões ao método utilizado, sem afirmar execução de funcionalidades apenas hipotéticas. As referências bibliográficas foram preservadas e não foram revalidadas nesta tarefa. |
| Alta | Pré-textuais | Resumo e abstract apresentavam o trabalho como preparação para uma entrega futura; listas e sumário refletiam capítulos antigos. | Resumos do experimento e resultados já documentados; listas e sumário dos capítulos atuais, sem paginação inventada. |
| Alta | Folha de aprovação e ficha | Havia data de aprovação e paginação herdadas, sem evidência de que se aplicassem ao documento atual. | Campos de aprovação, banca e paginação ficaram pendentes, sem presumir novo aceite acadêmico. |
| Média | Índice do manuscrito | Arquivos históricos apareciam intercalados aos capítulos atuais. | Separação explícita entre texto em elaboração e fontes históricas que não devem integrar a monografia. |
| Média | Critérios e planos | Algumas orientações pediam narrar a ampliação ou mudanças em relação ao documento anterior. | Registro da diretriz de unidade textual nos critérios, nos três planos, nas diretrizes gerais e no AGENTS.md. |

## Escopo dos ajustes

- `manuscrito/00-elementos-pre-textuais.md`: resumos, listas, sumário e campos
  editoriais pendentes. Os dados de identificação foram preservados.
- `manuscrito/01-introducao.md`: síntese do método e organização do trabalho;
  retirada de comentário de histórico editorial. Q1–Q5 e objetivos foram mantidos.
- `manuscrito/02-referencial-teorico.md`: ajustes localizados nos parágrafos que
  descrevem a aplicação dos conceitos neste experimento.
- `manuscrito/03-metodologia.md`: retirada da comparação entre entregas e da
  narrativa de mudança de objeto. Pilotos são apresentados como preparação do
  mesmo estudo, com seus registros separados das campanhas finais.
- `manuscrito/README.md`: índice dos arquivos ativos e seção própria para fontes
  históricas. O capítulo de conclusão continua explicitamente não redigido.
- Critérios, diretrizes, planos 3–5 e AGENTS.md: regra permanente para a redação.

Os capítulos 4 e 5 não continham referências às entregas anteriores e foram
preservados integralmente. Também foram preservados o Markdown completo de
referência, `04-prova-de-conceito.md`, `05-consideracoes-finais.md`, as referências
bibliográficas e os resultados experimentais. As menções a documentos anteriores
nos planos e nas notas de evidência identificam a origem dos trechos e não fazem
parte do texto acadêmico.

## Fontes e verificações

- Leitura da introdução, metodologia, referencial, pré-textuais, índice e planos.
- Critérios de linguagem e skill local `tcc2-revisar`.
- Conferência da síntese do resumo com `evidencias/capitulo-5-apoio/dados-conferidos.json`
  e com os resultados do capítulo 5: 38, 51 e 49 casos aceitos, respectivamente,
  dentre 78 por modelo, na definição principal de F; nenhum conjunto integrado
  aprovado funcionalmente. Não foram alterados os números ou sua interpretação.
- Fonte experimental mantida no SHA `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`,
  sem alterações rastreadas na consulta. Não foram executados modelos, SAST ou testes.
- Busca de referências a TCC1/TCC2 nos arquivos acadêmicos ativos.
- Conferência de preservação das perguntas, objetivos, tabelas e equações da
  metodologia e dos arquivos históricos por comparação e hashes.
- Listas e sumário derivados dos títulos atuais; paginação e numeração global
  continuam pendentes da integração.

O [registro de hashes](../evidencias/unidade-textual-2026-11-09.json) identifica
os textos antes e depois da correção. Os hashes iniciais correspondem ao HEAD
da escrita, cujo estado estava limpo no início desta tarefa. As notas dos
capítulos 3–5 preservam a coleta de 07/11/2026; seus hashes de rascunho identificam
as versões anteriores a esta revisão editorial, sem substituição do histórico.

## Pendências mantidas

- Redigir o capítulo de conclusão; a atualização do sumário não significa que ele
  esteja concluído.
- Integrar a numeração e paginação e preencher os dados atuais de aprovação e ficha.
- Revisar a bibliografia e as pendências metodológicas já registradas.

Não foi presumida aprovação dos autores sobre cada alteração de redação ou
verificação integral das referências científicas.
