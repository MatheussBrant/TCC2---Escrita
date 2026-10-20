# Contrato comum das features de escrita

Aplica-se às F01–F11 e às features de evolução E001 em diante. É complementar
ao `AGENTS.md` e às skills; os requisitos específicos estão no README de cada
feature. Esta versão define trabalho em
Markdown, com fontes e escolhas da [base comum](BASE_COMUM.md).

## Entradas e versões

Cada agente lê `AGENTS.md`, sua feature, este contrato e a base comum. Resolve
as fontes pela configuração efetiva, sem copiar os caminhos históricos de uma
coleta para outra máquina. O PDF e o clone experimental são insumos de leitura.

Use o SHA e os hashes da base desta rodada, registrando-os na entrega. Se o HEAD
local avançar, consulte a revisão fixada com `git show` ou uma cópia de leitura;
não mude o recorte silenciosamente nem faça checkout/reset no clone compartilhado.
Avise sobre a evolução encontrada. Alterar o recorte é uma decisão coordenada,
registrada antes de produzir uma nova versão das entregas afetadas.

Uma entrega existente conserva sua base registrada. Para uma tarefa nova, use
a base explicitamente definida para ela ou, na ausência, a selecionada pelo
coordenador a partir de `BASE_COMUM.md`, registrando-a antes de começar. Esse índice
seleciona a base para novas tarefas; seus arquivos em `bases/` são preservados.
Uma feature já iniciada não muda de base quando o índice avança. Adições futuras
seguem o [fluxo de evoluções](EVOLUCOES.md), com impacto e revisão explícitos.

Uma fonte faltante deve ser registrada com a afirmação afetada. Uma feature pode
avançar com o material independente disponível. Nem ausência de dados nem
ausência da PoC opcional autorizam fabricação de evidências.

## Propriedade dos arquivos

- Cada redator escreve **somente** em `saida` indicada no frontmatter da feature.
  Pode criar subpastas `figuras/`, `tabelas/` e `scripts/` dentro dela quando usadas.
- Os READMEs de features, a base, o contrato, as skills e as fontes experimentais
  são entradas compartilhadas de leitura durante a rodada.
- Referências usadas por uma feature ficam no seu `referencias.bib`; não há `.bib`
  global editado em paralelo. F11 deduplica e integra depois.
- O revisor escreve em `revisoes/<ID>/parecer.md` (F04 ou E001, por exemplo); ele não edita simultaneamente o
  texto do redator. Correções retornam ao responsável da feature.
- F11 gera uma versão integrada em sua própria pasta. Não sobrescreve capítulos
  ainda sendo editados; pede correções de conteúdo aos respectivos responsáveis.
- Uma evolução escreve sua contribuição na própria pasta, com o mapa de trechos
  a acrescentar/substituir. Não altera diretamente as pastas F01–F10 em paralelo.

Essas pastas são separadas do diretório `features/` do clone experimental, que
descreve entregas de software. As features daqui são tarefas de escrita.

## Entregáveis mínimos

Cada feature entrega seu texto principal, `evidencias.md` e `entrega.md` na pasta
exclusiva. Referências, figuras, tabelas e scripts são adicionados quando utilizados.
Não crie arquivos vazios para simular completude. A [F11](11-integracao/README.md)
tem uma saída principal de integração; as demais descrevem a sua explicitamente.

`evidencias.md` liga afirmações a fontes, com uma linha por afirmação relevante:

| ID | Afirmação/trecho | Natureza | Fonte e localização | Versão | Limite |
|---|---|---|---|---|---|
| `Fxx-E01` | Texto verificável | proposta / implementação / observação / interpretação | Repositório+caminho+execução+campo/linha/página ou fonte primária | SHA/hash, versão e data de acesso quando aplicável | O que a fonte não demonstra |

Para cada número experimental, acrescente população, unidade de análise, definição
de F quando pertinente, numerador, denominador, política e tratamento de ausentes.
Para contagens ou tempos, informe o universo, unidade e método de obtenção em vez
de inventar uma razão. Cite a seção da fonte científica, não apenas seu título.
Uma mesma evidência pode sustentar vários trechos se a relação estiver explícita.

`entrega.md` segue o [modelo](MODELO_ENTREGA.md): estado, arquivos, fontes, critérios,
dependências, decisões e pendências. Critérios específicos usam `<ID>-ACnn`;
os comuns abaixo usam `Gnn`. O ID acompanha a prova de atendimento.

## Convenções editoriais para integração

Escreva português acadêmico claro, usando as Qs e objetivos originais. Capítulos
inteiros usam título de nível 1. Features `tipo: secao` entregam fragmentos com
títulos de nível 2 e subseções de nível 3; o frontmatter informa capítulo/destino.
F11 gera os cinco títulos de capítulo, suas aberturas e transições. IDs e números
de pastas não são números de capítulo. Não numere figuras/tabelas manualmente.
F10 entrega também inglês no abstract.

Use chaves bibliográficas com prefixo da feature (`f02-autor2025-tema`) e citações
Markdown `[@f02-autor2025-tema]`. A chave só recebe uma entrada quando metadados
e fonte forem verificados. F11 unifica duplicatas por DOI/identidade e atualiza
as citações da cópia integrada, preservando a trilha das chaves originais.

Figuras e tabelas recebem identificadores estáveis, como `fig-f05-fluxo` e
`tab-f06-estrategias`. Mantenha arquivos e instruções para regenerar figuras de
dados; um diagrama conceitual deve corresponder ao método/código citado.

Remissões podem usar “Capítulo 3” e um comentário de trabalho
`<!-- remissao: F04; capitulo: 3; assunto: denominadores -->`. Não dependa de títulos/âncoras
que outro agente ainda não escreveu. F11 resolve e confere essas remissões.

Pendências de rascunho usam `[PENDENTE: Fxx — evidência ou decisão concreta]`.
Remova-as do texto aceito depois de resolver a questão ou delimitá-la de forma
justificada como resultado indisponível/limitação. Uma ausência comprovada de
RRIS, por exemplo, pode ser corretamente reportada; não exige novo experimento.

## Critérios de aceitação comuns

- [ ] **G01 — Escopo:** a entrega cobre os itens da feature e todos os arquivos
  produzidos estão na pasta autorizada; não altera fontes ou trabalho alheio.
- [ ] **G02 — Rastreabilidade:** afirmações relevantes têm fonte acessível e
  localização verificável; números têm universo/unidade/política e razões têm n/d.
- [ ] **G03 — Coerência científica:** distingue plano, implementação e execução;
  preserva ausências, limitações e populações; nenhuma conclusão excede a evidência.
- [ ] **G04 — Texto utilizável:** há prosa acadêmica completa, terminologia consistente
  e referências conferidas; não se entrega apenas um roteiro ou uma lista de commits.
- [ ] **G05 — Integração:** chaves, figuras, tabelas e remissões são identificáveis;
  conflitos com a base ou outras features foram registrados e resolvidos para fechar.
- [ ] **G06 — Verificação:** `entrega.md` relaciona todos os critérios à evidência;
  o parecer informa verificações reais, fontes indisponíveis e pendências materiais.

Um rascunho com lacunas pode ser entregue como `rascunho`, mas não satisfaz o aceite
final se as lacunas sustentarem conclusões. Informação comprovadamente indisponível,
corretamente delimitada, é diferente de uma verificação ainda não feita.

## Estados e fechamento

1. `em_redacao`: trabalho iniciado por um responsável.
2. `rascunho`: texto produzido, com pendências ou dependências declaradas.
3. `pronta_para_revisao`: autoavaliação dos critérios preenchida; o redator considera
   a entrega verificável. Isso ainda não significa revisão independente.
4. `revisada`: parecer efetivamente emitido e critérios atendidos; dependências
   de fechamento da feature foram reconciliadas, sem divergências materiais.
5. `integrada`: F11 incorporou essa versão e registrou o vínculo aos arquivos fonte.

O frontmatter de cada especificação descreve o estado inicial do planejamento;
o estado de execução vive em `entrega.md`. Não edite a especificação para atualizar
progresso. `revisada` é um estado de trabalho, não aprovação da banca ou dos autores.

Identifique cada entrega como `Fxx-vN`. O parecer registra essa versão e os hashes
dos arquivos de conteúdo conferidos. Alterações no conteúdo já revisado geram
nova versão e nova conferência; informe às features dependentes quais afirmações
mudaram. Um parecer anterior não aprova automaticamente a versão alterada.

As mesmas convenções valem para E001-v1, chaves `e001-...` e critérios E001-ACnn.
F11 lista todas as evoluções incluídas/excluídas e suas razões, e verifica os
efeitos transitivos sobre discussão, conclusão e resumos. Texto histórico pode
conservar uma base anterior se estiver identificado como histórico; a descrição
do estado atual deve refletir o recorte final escolhido e suas evidências.

As dependências de fechamento formam uma ordem de conferência. F04 estabelece a
descrição operacional; F06 a confronta com os registros. Se houver incompatibilidade,
registre a divergência, corrija a fonte textual responsável e reavalie as entregas
afetadas. Um agente não escolhe uma política diferente só para fechar seu capítulo.
