# Modelo para entrega de uma feature

Copie e preencha na pasta exclusiva da feature como `entrega.md`; este arquivo
compartilhado permanece como modelo. Os campos abaixo não são resultados já obtidos.

## Identificação

- Feature: ID — título (por exemplo, F04 ou E001).
- Versão da entrega: ID-v1; incrementar após alterações no conteúdo já revisado.
- Estado: em_redacao / rascunho / pronta_para_revisao / revisada / integrada.
- Responsável e data: identificar quem produziu esta versão, sem inventar revisão humana.
- Versão da base: ID realmente usado; SHA do experimento, hash do PDF e coleta.
- Arquivos entregues: caminhos relativos à raiz de escrita.

## Fontes e decisões

Informe fontes realmente consultadas e a localização da matriz `evidencias.md`.
Registre diferenças entre HEAD local, base fixada e conteúdo lido. Identifique
decisões D01–D08 pertinentes, sua verificação e eventuais divergências.

## Critérios de aceitação

Crie uma linha para cada G01–G06 e cada Fxx-ACnn da especificação.
Para evoluções, use os IDs E001-ACnn e registre também a base anterior/destino
e a localização de `impacto.md`.

| Critério | Autoavaliação | Evidência verificável | Pendência |
|---|---|---|---|
| ID do critério | atendido / parcial / não atendido | arquivo, seção, tabela, comando ou fonte consultada | descrição concreta ou nenhuma |

## Dependências de fechamento

Liste as features exigidas pela especificação, a versão consultada e a conferência
feita. Se a outra entrega ainda não existir, indique o trecho que permanece
provisório e qual fonte bruta foi usada para avançar.

## Limitações e questões em aberto

Diferencie informação comprovadamente indisponível de análise ainda pendente.
Registre impacto no texto, quem pode resolver e próxima ação. Não esconda lacunas
apenas para declarar a feature concluída.

## Revisão

Informe o caminho e a autoria real do parecer, fontes verificadas e correções
aplicadas. Enquanto não houver parecer, escreva “ainda não revisada”. A passagem
para `integrada` inclui o registro de incorporação produzido pela F11.
