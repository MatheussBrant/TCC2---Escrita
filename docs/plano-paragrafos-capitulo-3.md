# Capítulo 3 — plano consolidado por parágrafo

**Unidade da redação — 09/11/2026:** apresentar o método como parte de uma única
pesquisa completa, sem referências a TCC1/TCC2 no texto acadêmico. As indicações
de origem abaixo servem apenas ao controle editorial. Seguir a seção “Unidade
do trabalho” dos [critérios de escrita](criterios-escrita.md).

**Estado:** conteúdo e diretrizes consolidados a partir das decisões do autor
nesta conversa. Em 11/11/2026, o autor determinou preservar os 14 tópicos do
TCC1 separados, admitindo tópicos adicionais próprios. Por solicitação posterior,
a ferramenta passa a anteceder a seleção dos casos nas seções 3.4 e 3.5.
Este é um plano, não uma aprovação da orientadora.

**Atualização:** incorpora a comparação entre modelos e os acréscimos metodológicos
desenvolvidos no TCC2. Substitui o roteiro inicial de 45 parágrafos; os IDs foram
renumerados para acomodar os novos conteúdos.

## Decisões registradas até agora

1. Apresentar diretamente o estudo realizado, com Q1–Q5 e método completos; manter o histórico de adaptação somente nos arquivos de controle.
2. Descrever ações realizadas no passado; manter definições no presente quando adequado.
3. Usar o capítulo 3 para desenho, escolhas, execução, validação, métricas e procedimento de análise.
4. Destinar arquitetura, módulos, diretórios e realização técnica ao capítulo 4.
5. Destinar apresentação dos resultados, interpretação e respostas às perguntas ao capítulo 5.
6. Preservar Q1–Q4 e incluir a Q5 aceita pelo autor, com objetivo específico correspondente.
7. Criar uma seção própria de modelos e condições de geração e uma seção de comparação no capítulo 5.
8. Criar uma seção própria de validação das correções, antes das métricas.
9. Incluir regras locais e perfil congelado, catálogo por ocorrência, Docker e contratos,
   preflight, baseline e testes relacionados, testes adicionais e cobertura, conjunto D,
   comparação antes/depois, denominadores e avaliação conjunta da RRIS.
10. Atualizar a descrição do RAG e explicitar a diferença entre parada operacional
    e classificação adotada na análise.
11. Manter a ligação com as seções originais para controlar o que foi adaptado,
    corrigido ou acrescentado. O primeiro rascunho completo está no manuscrito;
    as fontes e pendências estão nas [notas de evidência](../evidencias/capitulo-3-notas.md).

> **Q5:** Como diferentes modelos de linguagem se comparam na geração de
> correções válidas pelo pipeline, considerando eficácia, custo e tempo de execução?

**Objetivo específico acrescentado:** comparar diferentes modelos de linguagem
na geração de correções válidas pelo pipeline, considerando eficácia, custo e
tempo de execução nas condições avaliadas.

As alterações de Q5 e do objetivo já estão na
[introdução de trabalho](../manuscrito/01-introducao.md).

## Fontes e limites do planejamento

- [Capítulo 3 em redação](../manuscrito/03-metodologia.md) e texto de partida no
  [Markdown completo do TCC1](../TCC1___Caio_Lamego_e_Matheus_Brant-11.md).
- [Comparação seção a seção com o TCC1](comparacao-capitulo-3-tcc1-tcc2.md).
- [Diretrizes de escrita](diretrizes-escrita.md).
- Experimento irmão: `../../tcc2-llm-sast-juiceshop`, revisão
  `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas nesta consulta.
- Referência de campanhas: 06/11/2026, 78 casos por modelo, identificadas nos
  contratos citados ao final. Histórico e pilotos têm seus próprios ambientes e recortes.

O planejamento se apoia na documentação, no código e nos artefatos selecionados
consultados nesta conversa. Não constitui revisão integral dos patches nem nova
execução experimental. Itens que exigem manifestação dos autores estão listados
como pendências ao final.

## Linguagem e profundidade adotadas

Seguir os [critérios de escrita](criterios-escrita.md), definidos pelo autor:
linguagem acadêmica, objetiva e explicativa, próxima à do TCC1. Desenvolver uma
ideia central por parágrafo, explicar termos na primeira ocorrência e conectar
cada explicação à finalidade do estudo. As fontes e os detalhes internos deste
plano servem à conferência do redator; não precisam ser transcritos no texto.

Priorizar escolhas, procedimentos e critérios de avaliação. Usar tabelas para
parâmetros e versões; remeter algoritmos e comandos ao capítulo 4 ou a apêndices.
Preservar as distinções necessárias para interpretar as métricas.

## Roteiro consolidado

**Diretriz estrutural de 11/11/2026:** os títulos abaixo correspondem ao manuscrito
reorganizado. Os IDs P01–P54 foram preservados para rastrear o planejamento anterior;
sua ordem nesta lista pode mudar quando um conteúdo foi separado. O mapa entre os
14 tópicos originais e os 16 atuais está em
[comparacao-topicos-metodologia.md](comparacao-topicos-metodologia.md).

### Abertura do capítulo

**Origem no TCC1:** Abertura do capítulo 3 do TCC1.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P01 | Adaptar | Apresentar a finalidade do capítulo: explicar como o experimento foi conduzido e como as correções foram avaliadas. |
| P02 | Ampliar | Apresentar a sequência do método e indicar o que será desenvolvido nos capítulos de implementação e resultados. |

### 3.1 Plano Metodológico

**Origem no TCC1:** seção 3.1.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P03 | Adaptar | Caracterizar a pesquisa e explicar, brevemente, sua natureza aplicada e sua abordagem de avaliação. |
| P04 | Ampliar | Relacionar o experimento aos objetivos e a Q1–Q5, incluindo a comparação entre modelos. |
| P05 | Acrescentar | Explicar o significado de caso, tentativa e campanha. Esclarecer que um alerta não comprova, sozinho, uma vulnerabilidade. |

### 3.2 Contexto de aplicação do experimento

**Origem no TCC1:** seção 3.2.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P08 | Adaptar | Explicar o papel das execuções exploratórias e dos pilotos na preparação do experimento, mantendo seus registros separados das campanhas finais. |
| P09 | Acrescentar | Explicar como o Docker ajudou a manter o mesmo ambiente e a mesma referência de testes nas campanhas. |

Separar as condições de execução da caracterização do objeto. Manter aqui a tabela do ambiente, os pilotos e a padronização Docker.

### 3.3 Objeto de estudo: OWASP Juice Shop

**Origem no TCC1:** seção 3.3.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P06 | Adaptar | Apresentar o Juice Shop e justificar sua escolha como aplicação de estudo, reconhecendo sua finalidade didática. |
| P07 | Precisar | Identificar a versão do projeto e suas tecnologias principais. Registrar a revisão exata em tabela ou nota de apoio. |

**Atualização de 11/11/2026:** preservar a apresentação mais detalhada da seção
original: tecnologias, 113 desafios em 16 categorias e 33 Coding Challenges na
versão utilizada. As contagens foram conferidas no código fixado. Explicar a
finalidade dos desafios de código e sua relação com o objeto de estudo, sem
equiparar desafios pedagógicos aos 78 casos do catálogo. Manter o link para o
fork e deixar os identificadores completos nas notas de evidência.

### 3.4 Ferramenta de análise estática

**Origem no TCC1:** seção 3.5.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P10 | Adaptar | Apresentar o Semgrep e justificar seu uso para identificar alertas antes e depois das correções. |
| P11 | Acrescentar | Explicar por que foram combinadas regras disponíveis na ferramenta e regras elaboradas para o estudo. |
| P12 | Acrescentar | Explicar como o conjunto de regras e as exclusões foram mantidos fixos para permitir comparações consistentes. |

### 3.5 Seleção das vulnerabilidades de segurança

**Origem no TCC1:** seção 3.4.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P13 | Atualizar | Apresentar a seleção dos 78 casos a partir de 124 alertas, com 46 exclusões. Explicar o que representa cada ocorrência. |
| P14 | Acrescentar | Explicar a ampliação do conjunto anteriormente preparado de 52 para 78 casos, sem misturar os resultados dessas campanhas. |
| P15 | Corrigir | Apresentar as informações por caso e os rótulos da triagem. Explicar a origem dos confirmados e inconclusivos nos registros versionados e a consolidação por regra, arquivo e intervalo, com revisão explícita de divergências. Registrar a confirmação do autor em 09/11/2026: os 21 falsos positivos apontados pela LLM foram revisados pelos dois autores com exame do código, contexto do alerta e regra do Semgrep. Não atribuir essa revisão humana aos outros grupos nem exploração dinâmica a todos os casos. |

Manter a constituição do catálogo, os critérios de seleção e as justificativas de triagem nesta seção. A ferramenta e o perfil de regras ficam na seção 3.4.

### 3.6 Modelos de linguagem e condições de geração

**Origem no TCC1:** seção 3.2.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P16 | Acrescentar | Apresentar os três modelos e a justificativa de sua escolha como parte do mesmo desenho de pesquisa, sem narrar uma ampliação entre entregas acadêmicas. |
| P17 | Acrescentar | Explicar as condições de geração de cada modelo. Reunir os parâmetros e suas diferenças em uma tabela breve. |
| P18 | Acrescentar | Explicar como os modelos foram avaliados sobre os mesmos casos e estratégias, indicando as condições comuns e as diferenças relevantes. |
| P19 | Acrescentar | Descrever brevemente o controle de chamadas, falhas e consumo. Esclarecer que as campanhas finais não reutilizaram respostas armazenadas. |

Seção adicional independente. O conteúdo sobre modelos foi separado do contexto de aplicação para explicitar a comparação e os parâmetros de geração.

### 3.7 Estratégias de prompt

**Origem no TCC1:** seção 3.6.

**Diretriz do autor em 11/11/2026:** aproximar a organização e a redação do
original: abertura sobre a comparação, apresentação da primeira à quarta
estratégia com seus nomes completos e lista dos seis campos da resposta JSON.
Manter a descrição do experimento realizado, as diferenças de conteúdo entre
P1–P4 e a lista de edições efetivamente adotada.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P20 | Adaptar | Apresentar as quatro estratégias e os elementos comuns dos prompts, incluindo a seleção do trecho de código. |
| P21 | Precisar | Descrever P1 como instrução direta acompanhada de código, sem diagnóstico SAST explícito ou documento recuperado. |
| P22 | Precisar | Descrever P2 e explicar como o roteiro orienta a análise em etapas, sem representar acesso ao raciocínio interno do modelo. |
| P23 | Precisar | Descrever P3, que acrescenta o diagnóstico da ferramenta e um documento de contexto ao código fornecido. |
| P24 | Precisar | Descrever P4, que combina contexto e roteiro, e explicar as restrições comuns às alterações propostas. |
| P25 | Atualizar | Explicar que as respostas seguiram um formato padronizado com os trechos originais e corrigidos, permitindo a aplicação automática. |

### 3.8 Estratégia de RAG simplificado

**Origem no TCC1:** seção 3.7.

**Diretriz do autor em 11/11/2026:** aproximar a exposição do original, mantendo
justificativa, composição dos documentos, exemplo e fluxo em etapas. Adaptar à
base 2.1 com 14 documentos, às sete seções obrigatórias e à recuperação por
primeira CWE mapeada, categoria do catálogo e documento genérico. O exemplo
CWE-89 usa `injection.md`. Conferência dos 382 prompts P3/P4 confirmou os corpos
e hashes recuperados; os 78 casos têm correspondência por CWE. Distinguir os
caminhos de contingência implementados daqueles efetivamente usados.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P26 | Atualizar | Apresentar a base de 14 documentos e seu propósito. Identificar sua versão em nota ou tabela de apoio. |
| P27 | Precisar | Explicar como o documento é selecionado pelo tipo de fraqueza e como se utiliza um texto genérico quando não há correspondência. |
| P28 | Ampliar | Justificar a recuperação simplificada e explicar como a base foi mantida identificável, sem incorporar soluções do alvo ou correções anteriores. |

### 3.9 Pipeline

**Origem no TCC1:** seção 3.8.

**Diretriz de continuidade em 11/11/2026:** recuperar a abertura sobre automação,
a lista de 13 etapas e a explicação do fluxo por caso, da sequência P1–P4 e do
paralelismo. Adaptar a seleção ao catálogo efetivo e a validação aos testes
selecionados. Distinguir a preparação da campanha do ciclo de cada tentativa e
preservar a diferença entre parada operacional e aceite na análise principal.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P29 | Adaptar | Apresentar o percurso de uma tentativa, da seleção do caso ao registro dos resultados, com apoio de um diagrama simples. |
| P30 | Acrescentar | Explicar a verificação inicial que confirma se projeto, regras, prompts e referência de testes correspondem às condições definidas. |
| P31 | Ampliar | Explicar o isolamento das tentativas e a restauração do código original, evitando interferência entre as correções. |
| P32 | Precisar | Explicar a sequência P1–P4 e qual critério interrompe a execução. Distinguir essa regra da classificação principal usada na análise. |
| P33 | Acrescentar | Explicar o tratamento de respostas inválidas, correções não aplicáveis e interrupções, distinguindo ausência de medição de falha comprovada. |
| P34 | Atualizar | Descrever a execução de até quatro casos em paralelo e a retomada das campanhas. Identificar as execuções finais separadamente dos pilotos. |

### 3.10 Validação das correções

**Origem no TCC1:** seção 3.5, 3.8 e 3.9.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P35 | Acrescentar | Explicar como se verifica se o alerta original permaneceu após a alteração, mesmo quando o código mudou de posição. |
| P36 | Acrescentar | Explicar a busca por novos alertas e as situações em que a ferramenta não permite uma conclusão segura. |
| P37 | Acrescentar | Apresentar o baseline como referência dos testes antes das correções, permitindo identificar problemas já existentes. |
| P38 | Acrescentar | Explicar a escolha de testes relacionados aos arquivos alterados e delimitar o que essa verificação permite afirmar sobre o funcionamento. |
| P39 | Acrescentar | Explicar por que foram acrescentados testes e como se verificou se eles eram capazes de revelar alterações no comportamento esperado. |
| P40 | Acrescentar | Apresentar o conjunto D e explicar por que determinados testes deixam de passar quando a vulnerabilidade é corrigida. |
| P41 | Acrescentar | Explicar as diferentes formas de interpretar F e o tratamento de falhas intermitentes ou resultados inconclusivos, com uma tabela de apoio. |

Seção adicional independente para desenvolver os procedimentos de validação, mantendo as fórmulas e métricas na seção 3.11.

### 3.11 Métricas de avaliação

**Origem no TCC1:** seção 3.9.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P42 | Adaptar | Apresentar a TRV e explicar seus três critérios. Informar que tentativas sem aplicação ou conclusão também entram no total considerado. |
| P43 | Corrigir | Apresentar as métricas complementares e explicar que seus totais consideram as medições disponíveis; distinguir ausência de resultado de falha. |
| P44 | Acrescentar | Distinguir sucesso por tentativa de sucesso por caso e explicar o tratamento dos registros posteriores ao primeiro aceite. |
| P45 | Acrescentar | Definir como serão comparados custo, tokens e tempo, distinguindo tempo de resposta do modelo de duração total da campanha. |
| P46 | Ampliar | Explicar a RRIS e a avaliação das correções aplicadas em conjunto, distinguindo redução de alertas de preservação funcional do conjunto. |

### 3.12 Armazenamento e organização dos dados

**Origem no TCC1:** seção 3.10.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P47 | Atualizar | Explicar como cada caso é ligado ao prompt, à resposta, à alteração e aos resultados dos testes, permitindo acompanhar sua origem. |

Tratar aqui da identificação e do armazenamento dos registros. A delimitação da população e as comparações ficam na seção 3.13.

### 3.13 Análise dos dados

**Origem no TCC1:** seção 3.11.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P48 | Ampliar | Explicar quais registros entram na análise principal e como são separados pilotos, simulações e tentativas posteriores ao primeiro aceite. |
| P49 | Ampliar | Apresentar as comparações por estratégia e tipo de vulnerabilidade, considerando o tamanho dos grupos e as informações ausentes. |
| P50 | Acrescentar | Apresentar a comparação dos três modelos para Q5, considerando eficácia, funcionamento, novos alertas, custo e tempo nas condições observadas. |
| P51 | Precisar | Explicar os limites da sequência de estratégias e da inclusão conjunta de diagnóstico e documentos. Descrever a análise de exemplos somente se realizada. |

Incluir a classificação OWASP complementar documentada em 11/11/2026. O conteúdo de P51 sobre limitações da sequência foi realocado para a seção 3.14; a análise de exemplos permanece nesta seção.

### 3.14 Limitações do estudo

**Origem no TCC1:** seção 3.12.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P52 | Atualizar | Apresentar os limites do alvo, do detector, dos testes e das classificações dos alertas, sem antecipar a discussão dos resultados. |
| P53 | Ampliar | Explicar como a sequência de estratégias, a variação das respostas e as configurações dos modelos limitam as comparações. |

Incluir aqui o parágrafo detalhado sobre a limitação da execução sequencial, anteriormente inserido na análise dos dados. Manter a declaração de IA separada.

### 3.15 Declaração de Uso de Inteligência Artificial

**Origem no TCC1:** seção 3.13.

| Parágrafo | Tratamento | Conteúdo a desenvolver |
|---|---|---|
| P54 | Atualizar | Declarar o uso efetivo de IA e a responsabilidade dos autores, descrevendo apenas a revisão humana que puder ser confirmada. |

### 3.16 Cronograma

**Origem no TCC1:** seção 3.14.

Recuperar a tabela de planejamento da seção 3.14 original. Identificar os períodos como previstos; não convertê-los em datas efetivas nem afirmar a conclusão de atividades futuras sem evidência.

## Decisões e evidências ainda pendentes

A origem e o procedimento documentado dos 55 confirmados e dois inconclusivos
foram rastreados no código em 09/11/2026, resolvendo a pendência textual. A revisão
humana confirmada pelo autor abrange os 21 falsos positivos; não presumir o mesmo
para os demais grupos. Ver o [rastreio de origem](../evidencias/triagem-origem-2026-11-09/LEITURA.md).

- Justificativa dos autores para a seleção dos três modelos, especialmente os dois acrescentados.
- Resolvido em 10/11/2026: o autor informou que não houve inspeção manual dos patches; a avaliação utilizou as métricas e verificações automatizadas. Descrever os exemplos do Capítulo 5 como análise documental com apoio automatizado, sem atribuir validação humana das correções.
- Confirmação do uso real de IA e das revisões humanas que serão declaradas.
- Alinhamento da ampliação Q5 com a orientadora; não afirmar aprovação sem registro.
- Resolvido em 11/11/2026: os tópicos originais foram separados, a declaração de IA recebeu seção própria e os tópicos de modelos e validação foram mantidos como acréscimos. O destino da PoC detalhada permanece fora desta reorganização.
- Resolvido em 11/11/2026: por determinação do autor de manter todos os tópicos, o cronograma foi recuperado como planejamento, com períodos explicitamente previstos.

## Fontes do experimento para a redação

Os caminhos seguintes são relativos à raiz do experimento na revisão registrada:

- `docs/protocolo_experimental.md` e `config/execucao_docker_78.yaml`.
- `outputs/catalogos/ampliado_v1/catalogo_issues.json` e metadados do catálogo.
- `src/pipeline/etapas/e04_prompt/montagem.py` e `src/pipeline/etapas/e05_geracao_llm/esquema.py`.
- `knowledge_base/_index.yaml`, `knowledge_base/manifesto.json` e documentos da base.
- `src/pipeline/orquestracao/campanha.py` e `src/pipeline/orquestracao/preflight.py`.
- `src/pipeline/etapas/e01_analise_sast/comparacao.py` e `src/pipeline/etapas/e07_validacao/`.
- `config/cobertura_funcional_v8.yaml`, `config/mapa_testes_relacionados_v9.yaml` e baseline referenciado no contrato.
- `src/pipeline/etapas/e09_metricas/calculo.py` e métricas das campanhas.
- `outputs/campanha_docker/AMP_REAL_20261106T105533Z_aa697342/contrato_execucao.json` — GPT-6 Luna.
- `outputs/campanha_docker/AMP_REAL_20261106T125801Z_0eb68fe4/contrato_execucao.json` — GPT-5.6 Luna.
- `outputs/campanha_docker/AMP_REAL_20261106T151004Z_f49ac0d2/contrato_execucao.json` — GPT-4.1 mini.
- `outputs/rris/<EXECUCAO>_METRICAS/metricas.json` e evidências conjuntas correspondentes.

Para descrever condições executadas, conferir contratos e registros específicos;
o protocolo contém trechos históricos que não descrevem automaticamente as campanhas finais.

## Como executar a redação deste plano

Para cada parágrafo, reunir a evidência, definir a mensagem e redigir o texto.
Indicar no material de trabalho a revisão, o caminho e a execução que sustentam
as afirmações empíricas. Uma classificação automática ou arquivada não equivale
a validação humana. Proposta, implementação e execução observada devem permanecer
distintas. Equações, tabelas e diagramas podem ser inseridos entre parágrafos.

Comparar a redação com o [Markdown completo do TCC1](../TCC1___Caio_Lamego_e_Matheus_Brant-11.md)
para acompanhar a evolução. O primeiro rascunho já foi redigido conforme este
plano e aguarda revisão dos autores, especialmente nos pontos marcados como
pendentes. A existência do rascunho não encerra essas decisões.
