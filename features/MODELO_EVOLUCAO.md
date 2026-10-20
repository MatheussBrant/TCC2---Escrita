# Modelo de feature para uma evolução

Copiar para `features/evolucoes/E001-assunto/README.md`, usando o próximo ID livre.
Este documento é um modelo; os campos e critérios devem ser concretizados para
a adição real. Consulte o [fluxo](EVOLUCOES.md) e o [contrato](CONTRATO.md).

```yaml
---
id: E001
tipo: evolucao
capitulo: null
destinos: [F04, F05]
saida: manuscrito/evolucoes/E001-assunto
estado_planejamento: planejada
base_anterior: R1
base_destino: null
inicio: apos_base_definida
fechamento_depende_de: []
---
```

Preencher `capitulo` quando houver um único destino; usar `destinos` para indicar
todas as features afetadas. Quando houver fontes verificáveis, informar o ID real
em `base_destino`, usar `estado_planejamento: pronta` e `inicio: imediato` se não
houver impedimento real. Dependências referem-se a entregas necessárias para
fechar; destinos não são automaticamente dependências. Não criar ciclos.

## Objetivo e mudança a documentar

Descrever a adição, por que importa para Q/OE/C e o que deve ser escrito.
Distinguir intenção, implementação e execução observada. Informar se afeta método,
implementação, resultados, validade ou apenas contexto histórico.

## Fontes e comparação

Informar bases anterior/destino, SHAs, commits relevantes, arquivos e campos de
artefatos, com hashes/identidades. Para uma adição planejada, listar quais fontes
ainda precisam existir. Identificar mudanças nas políticas D01–D08 pertinentes,
novas decisões e compatibilidade entre campanhas; não copiar números antigos
para uma execução nova.

## O que escrever e onde incorporar

| Destino Fxx / capítulo | Trecho ou assunto | Operação | Evidência necessária | Efeito em outras partes |
|---|---|---|---|---|
| Preencher | Identificar seção existente ou assunto novo | acrescentar / substituir / contextualizar | Fonte concreta | tabelas, discussão, conclusão, resumos ou nenhum, com justificativa |

Delimitar a profundidade e o que permanece fora do recorte. Indicar a ordem de
aplicação se outra evolução alterar o mesmo trecho. Ao substituir, explicar qual
afirmação antiga deixa de valer e em qual base; preservar a descrição histórica.

## Entregáveis e paralelismo

Na pasta `saida`, produzir `texto.md`, `impacto.md`, `evidencias.md`, `entrega.md`
e referências/tabelas/figuras/scripts quando utilizados. `impacto.md` identifica
operações e trechos suficientes para F11 aplicar a atualização sem adivinhação.
Seguir o modelo de entrega comum; parecer em `revisoes/E001/parecer.md`.
Não editar diretamente as pastas dos capítulos. Declarar fontes independentes
para começar e conferências necessárias para fechar.

## Critérios de aceitação a concretizar

Além de G01–G06, substituir estes itens por verificações específicas da adição:

- [ ] **E001-AC01:** o comportamento novo descrito é sustentado pelos commits,
  código e artefatos identificados, distinguindo o que foi executado do que foi planejado.
- [ ] **E001-AC02:** a comparação anterior/depois delimita o que mudou e seu
  impacto científico, sem inferir eficácia apenas pela existência de código.
- [ ] **E001-AC03:** cada trecho tem destino e operação definidos; consequências
  para método, tabelas, discussão, conclusão e resumo foram avaliadas.
- [ ] **E001-AC04:** novos números, quando houver, têm população, política,
  ausentes e proveniência; compatibilidade ou separação das campanhas está justificada.
- [ ] **E001-AC05:** o texto não conserva afirmações conflitantes como atuais;
  sobreposições com outras evoluções têm resolução e ordem de incorporação explícitas.
- [ ] **E001-AC06:** a entrega identifica base, versão e fontes, e contém todas
  as provas necessárias à revisão e incorporação por F11.

Adicionar critérios próprios do tópico: arquivos/campos exigidos, comportamento
do mecanismo, fórmula alterada ou verificação do artefato pertinente. Antes de
marcar a especificação como pronta, remover campos genéricos e tornar cada
critério aplicável à adição concreta. Este modelo não é uma entrega aceita.
