# Capítulo 4 — plano por parágrafo

**Título proposto:** Desenvolvimento e implementação do pipeline.

**Estado:** plano solicitado pelo autor a partir da estrutura discutida na conversa.
A organização inclui nove seções principais e o detalhamento das worktrees em
4.6.1–4.6.3. Os parágrafos são orientações para redação; não são texto final,
resultado experimental ou aprovação da orientadora. Títulos e extensão podem
ser ajustados durante a revisão.

## Decisões de organização

- Explicar a implementação pelo funcionamento do pipeline, com diretórios e
  componentes como apoio à arquitetura.
- Capítulo 3: decisões metodológicas, desenho, critérios e procedimento de análise.
- Capítulo 4: tecnologias, organização, funcionamento dos componentes e realização do método.
- Capítulo 5: resultados, interpretação e respostas a Q1–Q5, incluindo modelos.
- Explicar worktrees antes da aplicação dos patches, com isolamento, preparação,
  distribuição das tentativas, restauração e relação com a execução em paralelo.
- Dar destaque a aplicação das correções, validação e orquestração.
- Apresentar dificuldades técnicas junto das soluções correspondentes: problema,
  implementação e limite, sem transformar a exposição em histórico de commits.
- Acompanhar um caso ilustrativo com artefatos reais, cuja seleção está pendente.
- Separar justificativa dos modelos, tratada no capítulo 3, da integração técnica
  dos três modelos e da comparação dos resultados, tratada no capítulo 5.
- Tratar a possibilidade de replicação brevemente: um parágrafo sobre exportar
  e carregar a imagem Docker, junto da revisão do repositório e das configurações.
  Não criar subseção extensa nem detalhar comandos de distribuição. Essa
  possibilidade não equivale a uma replicação independente já demonstrada.

## Fontes e relação com o TCC1

Este capítulo terá conteúdo novo sobre o pipeline Juice Shop. O atual
[04-prova-de-conceito.md](../manuscrito/04-prova-de-conceito.md) ainda contém o
capítulo 4 original do TCC1 e permanece preservado. Não trocar a PoC Python/Bandit
pela implementação Juice Shop sem explicitar a mudança de objeto e de etapa.
O destino da apresentação detalhada da PoC será definido com os autores.

Planos relacionados:

- [Capítulo 3](plano-paragrafos-capitulo-3.md).
- [Diretrizes de escrita](diretrizes-escrita.md).
- [Comparação da metodologia TCC1/TCC2](comparacao-capitulo-3-tcc1-tcc2.md).

Experimento consultado: `../../tcc2-llm-sast-juiceshop`, revisão
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações rastreadas na consulta.
Os caminhos de fontes de cada seção são relativos à raiz desse repositório.
Foram consultados mapa de arquitetura, código selecionado e documentos já
examinados nesta conversa; não foi realizada revisão integral do código.
Conferir código e contratos da campanha antes de afirmar o comportamento executado:
há trechos desatualizados no mapa de arquitetura, como referências ao comparador
anterior e à ausência de evidência conjunta de RRIS.

## Linguagem e profundidade adotadas

Seguir os [critérios de escrita](criterios-escrita.md), definidos pelo autor:
linguagem acadêmica, objetiva e explicativa, próxima à do TCC1. Desenvolver uma
ideia central por parágrafo, explicar termos na primeira ocorrência e conectar
cada explicação à finalidade do estudo. As fontes e os detalhes internos deste
plano servem à conferência do redator; não precisam ser transcritos no texto.

Explicar a finalidade e o funcionamento das partes do sistema, sem descrever
função por função. Worktrees, comparação de alertas e painel devem ser apresentados
com exemplos breves e linguagem acessível. Detalhes internos, comandos extensos
e estruturas completas de dados podem ficar em apêndice.

## Roteiro dos parágrafos

### Abertura do capítulo

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P01 | Apresentar o sistema desenvolvido para executar o método e situar o capítulo em relação à metodologia e aos resultados. |
| C4-P02 | Indicar o percurso da explicação: organização, etapas, modelos, isolamento, validação, painel e registros. |

### 4.1 Visão geral da solução

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P03 | Apresentar a finalidade da solução: transformar alertas em propostas de correção que possam ser aplicadas e avaliadas automaticamente. |
| C4-P04 | Explicar a organização em etapas conectadas, chamada dutos e filtros, mostrando a responsabilidade de cada parte. |
| C4-P05 | Apresentar as principais entradas e saídas e introduzir um caso real para ilustrar o funcionamento ao longo do capítulo. |

**Fontes de implementação:**
- `src/pipeline/README.md`
- `src/pipeline/orquestracao/campanha.py`

**Apoio visual e limite:** Diagrama simples das principais etapas e suas conexões. O caso ilustrativo ainda será selecionado.

### 4.2 Tecnologias e organização do projeto

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P06 | Apresentar as tecnologias e a função de cada uma, com apoio de uma tabela resumida. |
| C4-P07 | Mostrar os diretórios principais e explicar como separam código, configurações, testes e resultados. |
| C4-P08 | Explicar como as partes do código acompanham as etapas do pipeline, sem descrever arquivo por arquivo. |
| C4-P09 | Explicar brevemente como o Docker reúne as dependências e mantém o ambiente preparado. Comandos de instalação ficam em material de apoio. |

**Fontes de implementação:**
- `README.md`
- `src/pipeline/README.md`
- `Dockerfile`
- `compose.yaml`
- `Makefile`
- `docker/referencia.json`
- `config/README.md`

**Apoio visual e limite:** Árvore curta de diretórios e tabela tecnologia/responsabilidade. Evitar inventário de todos os arquivos ou repetição da justificativa metodológica do Docker.

### 4.3 Detecção e preparação dos casos

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P10 | Explicar como o pipeline executa o Semgrep e transforma sua saída em informações utilizáveis nas etapas seguintes. |
| C4-P11 | Apresentar a organização das regras locais e um exemplo simples do padrão que procuram identificar. |
| C4-P12 | Explicar como o catálogo é formado a partir dos alertas e da triagem registrada, distinguindo a organização dos dados de sua classificação. |
| C4-P13 | Explicar como cada caso recebe um identificador e fica associado à localização do alerta e à versão analisada do projeto. |
| C4-P14 | Acompanhar um exemplo do alerta até sua entrada no catálogo, mostrando as verificações necessárias para utilizá-lo. |

**Fontes de implementação:**
- `src/pipeline/etapas/e01_analise_sast/semgrep.py`
- `src/pipeline/etapas/e01_analise_sast/perfil.py`
- `src/pipeline/etapas/e02_catalogo/catalogo.py`
- `scripts/experimento/gerar_catalogo_ampliado.py`
- `scripts/auditoria/classificar_scan_combinado.py`

**Apoio visual e limite:** Exemplo breve de alerta e de seu registro no catálogo. Não exigir código da regra no corpo do texto se uma explicação simples for suficiente.

### 4.4 Construção dos prompts e recuperação de contexto

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P15 | Explicar como o prompt reúne a instrução, o código e as restrições, selecionando um trecho adequado do arquivo. |
| C4-P16 | Mostrar, com uma tabela, quais informações são acrescentadas em P1–P4 e como os prompts são montados. |
| C4-P17 | Explicar como o pipeline encontra e incorpora o documento de contexto adequado, recorrendo a um texto genérico quando necessário. |
| C4-P18 | Apresentar um exemplo curto de prompt e explicar o registro da origem do contexto utilizado. |

**Fontes de implementação:**
- `src/pipeline/etapas/e04_prompt/montagem.py`
- `src/pipeline/etapas/e03_contexto_rag/recuperacao.py`
- `config/prompts/roteiro_raciocinio_guiado.md`
- `knowledge_base/_index.yaml`
- `knowledge_base/manifesto.json`

**Apoio visual e limite:** Tabela de blocos de P1–P4 e esquema de composição; prompts extensos podem ser apresentados em apêndice.

### 4.5 Integração com os modelos de linguagem

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P19 | Explicar como a mesma estrutura do pipeline permite selecionar e utilizar os três modelos comparados. |
| C4-P20 | Explicar como as configurações são ajustadas para cada modelo e registradas para identificar as condições da chamada. |
| C4-P21 | Apresentar o formato padronizado da resposta, com um exemplo curto dos trechos original e corrigido. |
| C4-P22 | Explicar como as respostas são salvas e como são tratados erros, novas tentativas de comunicação e consumo registrado. |

**Fontes de implementação:**
- `src/pipeline/etapas/e05_geracao_llm/provedor.py`
- `src/pipeline/etapas/e05_geracao_llm/modelos.py`
- `src/pipeline/etapas/e05_geracao_llm/cliente_openai.py`
- `src/pipeline/etapas/e05_geracao_llm/esquema.py`

**Apoio visual e limite:** Exemplo de resposta JSON e tabela de responsabilidades da integração. A justificativa da escolha dos modelos e a comparação de eficácia ficam nos capítulos 3 e 5.

### 4.6 Aplicação das correções e isolamento

As três subseções seguintes descrevem worktrees, gerenciamento e aplicação de edições.

#### 4.6.1 Isolamento com Git worktrees

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P23 | Apresentar worktrees como cópias de trabalho separadas ligadas ao mesmo repositório, usadas para isolar as alterações de cada tentativa. |
| C4-P24 | Explicar a preparação das cópias a partir da mesma versão do Juice Shop, com as dependências necessárias para executar os testes. |
| C4-P25 | Explicar o alcance desse isolamento: as alterações ficam separadas, mas recursos como portas e serviços ainda precisam ser coordenados. |

**Fontes de implementação:**
- `scripts/preparacao/preparar_alvo.sh`
- `src/pipeline/etapas/e06_aplicacao/worktrees.py`

**Apoio visual e limite:** Diagrama do repositório Git e de wt-1…wt-4. Conferir os comandos de preparação no script antes de incluí-los.

#### 4.6.2 Gerenciamento das worktrees

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P26 | Explicar como o sistema mantém um conjunto de worktrees disponíveis e reserva uma delas para cada trabalho em andamento. |
| C4-P27 | Descrever o uso e a devolução de uma worktree, incluindo a restauração do código antes e depois da tentativa, mesmo quando ocorre erro. |
| C4-P28 | Explicar como se evita o uso simultâneo da mesma cópia e como a limpeza preserva as dependências necessárias. |

**Fontes de implementação:**
- `src/pipeline/etapas/e06_aplicacao/worktrees.py`

**Apoio visual e limite:** Esquema simples mostrando distribuição da tentativa, uso de uma cópia e restauração. Relacionar com a execução em paralelo explicada em 4.8.

#### 4.6.3 Aplicação das edições

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P29 | Explicar as verificações que impedem alterações em arquivos não permitidos e confirmam os trechos que serão substituídos. |
| C4-P30 | Descrever a localização do trecho original, o tratamento de ambiguidades e os ajustes limitados de indentação, usando um exemplo breve. |
| C4-P31 | Mostrar a alteração antes e depois e o registro das diferenças. Esclarecer que aplicar a edição não basta para considerá-la válida. |

**Fontes de implementação:**
- `src/pipeline/etapas/e06_aplicacao/aplicador.py`
- `src/pipeline/etapas/e06_aplicacao/indentacao.py`
- `src/pipeline/orquestracao/campanha.py`

**Apoio visual e limite:** Trecho antes/depois e diff reduzido, acompanhado do status do aplicador. A inspeção do exemplo deve evitar atribuir validade de segurança apenas ao sucesso de aplicação.

### 4.7 Implementação da validação

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P32 | Explicar como a reanálise de segurança e os testes são reunidos para produzir R, F e M. |
| C4-P33 | Explicar, em alto nível, como o comparador acompanha alertas após mudanças no código e quais situações permanecem inconclusivas. |
| C4-P34 | Explicar como a referência de testes e a relação entre arquivos e grupos de testes orientam a verificação de cada correção. |
| C4-P35 | Descrever a execução das verificações, incluindo limites de tempo e tratamento de falhas, sem detalhar comandos internos. |
| C4-P36 | Explicar como as falhas dos testes são separadas conforme o conjunto D e como são registradas as interpretações de F. |
| C4-P37 | Apresentar um teste adicional como exemplo e explicar sua integração à validação e os limites do que ele verifica. |

**Fontes de implementação:**
- `src/pipeline/etapas/e07_validacao/medicao.py`
- `src/pipeline/etapas/e07_validacao/cobertura.py`
- `src/pipeline/etapas/e07_validacao/execucao_cobertura.py`
- `src/pipeline/etapas/e07_validacao/conjunto_d.py`
- `src/pipeline/etapas/e01_analise_sast/comparacao.py`
- `tests/functional/juice_shop/`

**Apoio visual e limite:** Esquema da validação ou uma tabela com as verificações realizadas. Estruturas completas dos registros ficam em material de apoio.

### 4.8 Orquestração e execução das campanhas

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P38 | Explicar como o coordenador conecta as etapas e verifica as condições necessárias antes de iniciar as tentativas. |
| C4-P39 | Explicar como os casos são distribuídos entre as cópias disponíveis e por que as estratégias de um mesmo caso seguem em sequência. |
| C4-P40 | Descrever a decisão de continuar ou encerrar as estratégias e como os registros permitem retomar uma execução interrompida. |
| C4-P41 | Apresentar a execução por terminal e distinguir verificação inicial, simulação e execução real, sem listar todas as opções disponíveis. |
| C4-P42 | Apresentar o painel: escolha do modelo, início e parada, acompanhamento das tentativas, logs e tempos. Usar uma ou duas capturas reais. |

**Fontes de implementação:**
- `src/pipeline/orquestracao/campanha.py`
- `src/pipeline/orquestracao/preflight.py`
- `executar.py`
- `painel.py`
- `src/pipeline/painel/controle.py`
- `src/pipeline/painel/servidor.py`

**Apoio visual e limite:** Uma ou duas capturas reais do painel, com legendas objetivas. Retomar o diagrama geral quando suficiente, evitando outra figura para o mesmo fluxo.

### 4.9 Registro, métricas e reprodução

| Parágrafo | Conteúdo a desenvolver |
|---|---|
| C4-P43 | Mostrar como os arquivos de cada execução permitem acompanhar o caminho do alerta até a avaliação da correção. |
| C4-P44 | Explicar como configurações e verificações de integridade identificam a execução e evitam retomadas com condições incompatíveis. |
| C4-P45 | Explicar como os registros são reunidos em tabelas e métricas, incluindo resultados ausentes e registros fora da análise principal. |
| C4-P46 | Descrever a avaliação de correções aplicadas em conjunto, incluindo alterações incompatíveis e testes. A interpretação dos resultados fica no capítulo 5. |
| C4-P47 | Destacar, em um parágrafo breve, a possibilidade de replicação mediante a imagem Docker, o repositório e as configurações correspondentes, sem aprofundar comandos nem prometer respostas idênticas. |

**Fontes de implementação:**
- `src/pipeline/etapas/e08_registro/registro.py`
- `src/pipeline/etapas/e09_metricas/calculo.py`
- `src/pipeline/etapas/e09_metricas/rris.py`
- `scripts/relatorios/consolidar_metricas.py`
- `scripts/experimento/avaliacao_conjunta_rris.py`
- `outputs/README.md`

**Apoio visual e limite:** Usar uma estrutura resumida dos resultados ou uma tabela etapa → saída, escolhendo a opção mais clara. Manter a replicação em um parágrafo breve.

## Pendências antes da redação final

1. Escolher o caso ilustrativo com código, resposta, patch, scans e testes completos; registrar a campanha e a revisão de origem.
2. Escolher uma regra local, uma edição e um teste adicional representativos, verificando suas evidências.
3. Conferir bibliografia para conceitos técnicos que precisem de fundamentação, incluindo Git worktrees e dutos e filtros.
4. Produzir os diagramas a partir do fluxo real e as capturas a partir da interface existente; não usar telas simuladas como evidência.
5. Conferir a configuração e o comportamento de cada etapa nos contratos das campanhas descritas.
6. Selecionar somente dificuldades técnicas documentadas e identificar o que foi implementado, testado e observado.
7. Definir a posição final da PoC do TCC1 e renomear o manuscrito do capítulo 4 quando começar sua adaptação.

## Orientação para redigir e revisar

Para cada parágrafo, explicar a responsabilidade do componente, seu funcionamento
e sua ligação com a próxima etapa. Usar trechos curtos de código quando eles
ajudarem a compreender uma decisão; reservar listagens extensas para apêndices.
Vincular afirmações de implementação à revisão e ao caminho da fonte e afirmações
de execução à campanha e ao artefato. IDs C4-Pxx identificam o plano e não precisam
aparecer no texto final.

Não confundir suporte a uma função com uso nas campanhas, resultado de teste
do pipeline com prova de segurança de um patch, nem sucesso isolado com validação
conjunta. O plano do capítulo 3 estabelece o significado dos critérios; este
capítulo demonstra sua realização técnica.
