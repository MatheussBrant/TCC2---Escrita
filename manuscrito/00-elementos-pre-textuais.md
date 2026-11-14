# Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado

## Capa

**Universidade de Brasília – UnB Faculdade de Ciências e Tecnologias em Engenharia – FCTE Engenharia de Software**

**Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado**

**Autor: Matheus de Siqueira Brant e Caio Magalhães Lamego Orientador: Profa. Dra. Elaine Venson**

**Brasília, DF 2026**

## Folha de rosto

Matheus de Siqueira Brant e Caio Magalhães Lamego

**Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado**

Monografia submetida ao curso de graduação em Engenharia de Software da Universidade de Brasília, como requisito parcial para obtenção do Título de Bacharel em Engenharia de Software.

Universidade de Brasília – UnB

Faculdade de Ciências e Tecnologias em Engenharia – FCTE

Orientador: Profa. Dra. Elaine Venson

Brasília, DF

2026

## Ficha catalográfica

Matheus de Siqueira Brant e Caio Magalhães Lamego

Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado/ Matheus de Siqueira Brant e Caio Magalhães Lamego. – Brasília, DF, 2026-

[PENDENTE: atualizar a paginação e os dados da ficha catalográfica após a diagramação final.]

Orientador: Profa. Dra. Elaine Venson

Trabalho de Conclusão de Curso – Universidade de Brasília – UnB Faculdade de Ciências e Tecnologias em Engenharia – FCTE , 2026.

1. segurança de software. 2. engenharia de software. I. Profa. Dra. Elaine Venson. II. Universidade de Brasília. III. Faculdade de Ciências e Tecnologias em Engenharia. IV. Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado

CDU 02:141:005.6

## Folha de aprovação

Matheus de Siqueira Brant e Caio Magalhães Lamego

**Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado**

Monografia submetida ao curso de graduação em Engenharia de Software da Universidade de Brasília, como requisito parcial para obtenção do Título de Bacharel em Engenharia de Software.

[PENDENTE: preencher a data de aprovação e a composição da banca referentes a esta monografia.]

**Profa. Dra. Elaine Venson** Orientador

Brasília, DF 2026

## Resumo

Este trabalho avaliou um pipeline automatizado que integra Modelos de Linguagem de Grande Escala (LLMs), Análise Estática de Segurança (SAST), testes automatizados e estratégias de contextualização para apoiar a correção de alertas de segurança em código-fonte. O experimento foi conduzido no OWASP Juice Shop, com Semgrep, quatro estratégias de prompt e três modelos: GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna. Cada campanha utilizou o mesmo catálogo de 78 casos. As propostas foram aplicadas em cópias isoladas e avaliadas quanto à remoção do alerta original, à preservação funcional e à ausência de novos alertas. Na definição funcional principal, os modelos obtiveram pelo menos um aceite em 38, 51 e 49 casos, respectivamente. O GPT-5.6 Luna apresentou o maior número de casos aceitos, enquanto o GPT-6 Luna teve o menor custo registrado e a menor duração da campanha. A avaliação conjunta dos patches reduziu os alertas estáticos, mas nenhum dos conjuntos recebeu aprovação funcional. Os resultados indicam a possibilidade de obter aceites individuais sob critérios explícitos e evidenciam a importância dos testes, da definição de preservação funcional e da avaliação da integração das alterações. As conclusões se limitam ao alvo, às campanhas e ao alcance das verificações utilizadas.

**Palavras-chave**: modelos de linguagem de grande escala; análise estática de segurança; correção de vulnerabilidades; engenharia de prompt; RAG; _pipeline_.

## Abstract

This work evaluated an automated pipeline integrating Large Language Models (LLMs), Static Application Security Testing (SAST), automated tests, and contextualization strategies to support the repair of security findings in source code. The experiment used OWASP Juice Shop, Semgrep, four prompting strategies, and three models: GPT-4.1 mini, GPT-5.6 Luna, and GPT-6 Luna. Each campaign used the same catalog of 78 cases. Proposed edits were applied in isolated working copies and assessed for removal of the original finding, functional preservation, and absence of new findings. Under the primary definition of functional preservation, the models achieved at least one accepted attempt in 38, 51, and 49 cases, respectively. GPT-5.6 Luna achieved the highest number of accepted cases, while GPT-6 Luna had the lowest recorded cost and shortest campaign duration. Joint patch evaluation reduced static findings, but none of the integrated sets passed functional validation. The results demonstrate the possibility of obtaining individually accepted attempts under explicit criteria and highlight the importance of tests, the definition of functional preservation, and evaluation of integrated changes. Conclusions are limited to the target, campaigns, and scope of the checks used.

**Keywords**: large language models; static application security testing; vulnerability repair; prompt engineering; RAG; pipeline.

## Lista de ilustrações

- Capítulo 3 — Figura 1 — Visão geral do fluxo metodológico adotado na pesquisa
- Capítulo 3 — Figura 2 — Procedimento de avaliação de um caso
- Capítulo 3 — Figura 3 — Estrutura do identificador utilizado na nomenclatura dos artefatos gerados pelo pipeline
- Capítulo 4 — Figura 1 — Principais etapas e conexões do pipeline
- Capítulo 4 — Figura 2 — Cópias de trabalho utilizadas pelo pipeline
- Capítulo 5 — Figura 1 — Distribuição dos casos pelo primeiro aceite e pela ausência de aceite

[PENDENTE: unificar a numeração e inserir as páginas após a integração do documento.]

## Lista de tabelas

- Capítulo 3 — Tabela 1 — Condições de referência do experimento
- Capítulo 3 — Tabela 2 — Constituição do catálogo ampliado
- Capítulo 3 — Tabela 3 — Informações fornecidas em cada estratégia
- Capítulo 3 — Tabela 4 — Tratamento das falhas nos testes para calcular F
- Capítulo 3 — Tabela 5 — Cronograma previsto para o desenvolvimento da pesquisa
- Capítulo 4 — Tabela 1 — Tecnologias e responsabilidades na solução
- Capítulo 4 — Tabela 2 — Organização principal do repositório
- Capítulo 4 — Tabela 3 — Informações preservadas por execução
- Capítulo 5 — Tabela 1 — Registros das campanhas finais e população de análise
- Capítulo 5 — Tabela 2 — Aceites por caso e por tentativa
- Capítulo 5 — Tabela 3 — Critérios de avaliação e medições ausentes
- Capítulo 5 — Tabela 4 — Sensibilidade da TRV à definição de F
- Capítulo 5 — Tabela 5 — Primeiros aceites e tentativas por estratégia
- Capítulo 5 — Tabela 6 — Sobreposição dos casos aceitos
- Capítulo 5 — Tabela 7 — Consumo e custos registrados das campanhas
- Capítulo 5 — Tabela 8 — Latência de geração e duração das campanhas
- Capítulo 5 — Tabela 9 — Casos aceitos por tipo de alerta catalogado
- Capítulo 5 — Tabela 10 — Casos aceitos segundo a categoria OWASP registrada
- Capítulo 5 — Tabela 11 — Evidências dos exemplos selecionados
- Capítulo 5 — Tabela 12 — Aplicação conjunta dos patches e redução dos alertas

[PENDENTE: unificar a numeração e inserir as páginas após a integração do documento.]

## Lista de abreviaturas e siglas

|ABNT|Associação Brasileira de Normas Técnicas|
|---|---|
|API|Application Programming Interface|
|CoT|Chain-of-Thought|
|CVE|Common Vulnerabilities and Exposures|
|CVSS|Common Vulnerability Scoring System|
|CWE|Common Weakness Enumeration|
|IA|Inteligência Artificial|
|IDOR|Insecure Direct Object Reference|
|LLM|Large Language Model|
|NVD|National Vulnerability Database|
|OWASP|Open Worldwide Application Security Project|
|PoC|Proof of Concept|
|RAG|Retrieval-Augmented Generation|
|SAST|Static Application Security Testing|
|SSRF|Server-Side Request Forgery|
|XSS|Cross-Site Scripting|

## Lista de símbolos

| Símbolo | Descrição |
|---|---|
| $\sum$ | Operador de somatório |
| $R_j$ | Resultado da remoção da issue real $j$ após a correção |
| $F_j$ | Resultado da preservação funcional da correção aplicada à issue real $j$ |
| $M_j$ | Indicador de não introdução de novas issues após a correção da issue real $j$ |
| $m$ | Número total de tentativas de correção realizadas no projeto real |
| $I_{\text{antes}}$ | Número de issues de segurança detectadas antes da aplicação das correções aceitas |
| $I_{\text{depois}}$ | Número de issues de segurança detectadas após a aplicação das correções aceitas |

## Sumário

- 1 Introdução
  - 1.1 Contexto
  - 1.2 Problema
  - 1.3 Objetivos
    - 1.3.1 Objetivo Geral
    - 1.3.2 Objetivos Específicos
  - 1.4 Metodologia
  - 1.5 Organização do Trabalho
- 2 Referencial Teórico
  - 2.1 Modelos de Linguagem de Grande Escala (LLMs)
  - 2.2 Engenharia de Prompt
  - 2.3 Vulnerabilidades de Software e OWASP 10
  - 2.4 Ferramentas de Análise Estática de Segurança (SAST)
  - 2.5 Trabalhos Relacionados
- 3 Metodologia
  - 3.1 Plano Metodológico
  - 3.2 Contexto de aplicação do experimento
  - 3.3 Objeto de estudo: OWASP Juice Shop
  - 3.4 Ferramenta de análise estática
  - 3.5 Seleção das vulnerabilidades de segurança
  - 3.6 Modelos de linguagem e condições de geração
  - 3.7 Estratégias de prompt
  - 3.8 Estratégia de RAG simplificado
  - 3.9 Pipeline
  - 3.10 Validação das correções
  - 3.11 Métricas de avaliação
  - 3.12 Armazenamento, organização e análise dos dados
  - 3.13 Limitações do estudo
  - 3.14 Declaração de Uso de Inteligência Artificial
  - 3.15 Cronograma
- 4 Desenvolvimento e implementação do pipeline
  - 4.1 Visão geral da solução
  - 4.2 Tecnologias e organização do projeto
  - 4.3 Detecção e preparação dos casos
  - 4.4 Construção dos prompts e recuperação de contexto
  - 4.5 Integração com os modelos de linguagem
  - 4.6 Aplicação das correções e isolamento
    - 4.6.1 Isolamento com Git worktrees
    - 4.6.2 Gerenciamento das worktrees
    - 4.6.3 Aplicação das edições
  - 4.7 Implementação da validação
  - 4.8 Orquestração e execução das campanhas
  - 4.9 Registro, métricas e reprodução
- 5 Resultados e discussão
  - 5.1 Caracterização das campanhas e dos casos
  - 5.2 Resultados gerais do pipeline
  - 5.3 Comparação das estratégias de prompt
  - 5.4 Comparação entre modelos de linguagem
  - 5.5 Resultados por tipo de vulnerabilidade e categoria
  - 5.6 Análise de correções e falhas representativas
  - 5.7 Redução conjunta de alertas e RRIS
  - 5.8 Respostas às perguntas de pesquisa
  - 5.9 Discussão com a literatura e implicações
  - 5.10 Alcance dos resultados e possibilidades de continuidade
- 6 Conclusão e trabalhos futuros [PENDENTE: redigir]
- Referências

[PENDENTE: inserir a paginação após a diagramação final.]
