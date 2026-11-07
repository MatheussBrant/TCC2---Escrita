# Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado

> Transcrição em Markdown do arquivo [TCC1___Caio_Lamego_e_Matheus_Brant-11.pdf](../TCC1___Caio_Lamego_e_Matheus_Brant-11.pdf). Foram adaptadas a diagramação, a hierarquia de títulos, as tabelas e as fórmulas; as cinco figuras foram preservadas como imagens. O conteúdo, os números e as eventuais inconsistências do original foram mantidos. As páginas indicadas no sumário e nas listas correspondem à numeração impressa no PDF.

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

71 p. : il. ; 30 cm.

Orientador: Profa. Dra. Elaine Venson

Trabalho de Conclusão de Curso – Universidade de Brasília – UnB Faculdade de Ciências e Tecnologias em Engenharia – FCTE , 2026.

1. segurança de software. 2. engenharia de software. I. Profa. Dra. Elaine Venson. II. Universidade de Brasília. III. Faculdade de Ciências e Tecnologias em Engenharia. IV. Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado

CDU 02:141:005.6

## Folha de aprovação

Matheus de Siqueira Brant e Caio Magalhães Lamego

**Correção de vulnerabilidades em código com LLMs: uma avaliação da integração com ferramentas SAST, testes automatizados, estratégias de contextualização e raciocínio guiado**

Monografia submetida ao curso de graduação em Engenharia de Software da Universidade de Brasília, como requisito parcial para obtenção do Título de Bacharel em Engenharia de Software.

Trabalho aprovado. Brasília, DF, 16 de julho de 2026:

**Profa. Dra. Elaine Venson** Orientador

**Dra. Cristiane Soares Ramos** Convidado 1

**Indiana Medeiros** Convidado 2

Brasília, DF 2026

## Resumo

Modelos de Linguagem de Grande Escala (LLMs) têm sido cada vez mais utilizados no desenvolvimento de software, inclusive em tarefas de geração, explicação e correção de código. No entanto, seu uso em segurança ainda exige cautela, pois correções geradas automaticamente podem ser incompletas, inseguras ou comprometer o funcionamento original da aplicação. Este trabalho investiga a integração entre LLMs, ferramentas de Análise Estática de Segurança (SAST), testes automatizados e estratégias de contextualização para apoiar a correção de _issues_ de segurança em código-fonte. A metodologia proposta prevê a aplicação de um _pipeline_ automatizado em um projeto _open source_, utilizando as vulnerabilidades efetivamente detectadas pela ferramenta SAST. Como etapa inicial, foi desenvolvida uma prova de conceito para validar o fluxo de identificação, geração de correções, reanálise estática, execução de testes e consolidação de métricas. O trabalho estabelece, assim, as bases técnicas e metodológicas para avaliar a eficácia do _pipeline_ no TCC 2.

**Palavras-chave**: modelos de linguagem de grande escala; análise estática de segurança; correção de vulnerabilidades; engenharia de prompt; RAG; _pipeline_.

## Abstract

Large Language Models (LLMs) have been increasingly used in software development, including tasks such as code generation, explanation, and correction. However, their use in software security still requires caution, since automatically generated fixes may be incomplete, insecure, or may compromise the original behavior of the application. This work investigates the integration of LLMs, Static Application Security Testing (SAST) tools, automated tests, and contextualization strategies to support the correction of security issues in source code. The proposed methodology applies an automated pipeline to an open source project, using the vulnerabilities effectively detected by the SAST tool. As an initial step, a proof of concept was developed to validate the workflow for issue identification, fix generation, static reanalysis, test execution, and metric consolidation. Thus, this work establishes the technical and methodological foundations to evaluate the effectiveness of the pipeline in TCC 2.

**Keywords**: large language models; static application security testing; vulnerability repair; prompt engineering; RAG; pipeline.

## Lista de ilustrações

- Figura 1 – Visão geral do fluxo metodológico adotado na pesquisa — p. 34
- Figura 2 – Fluxo de correção de uma única vulnerabilidade, executado em para- lelo para diferentes vulnerabilidades e com tentativas progressivas por estratégias de prompt — p. 42
- Figura 3 – Estrutura do identificador utilizado na nomenclatura dos artefatos ge- rados pelo pipeline — p. 45
- Figura 4 – Primeira parte da execução completa do pipeline da PoC — p. 62
- Figura 5 – Segunda parte da execução completa do pipeline da PoC — p. 63

## Lista de tabelas

- Tabela 1 – Cronograma previsto para o desenvolvimento do TCC 2 — p. 49
- Tabela 2 – Resultados operacionais das execuções da PoC — p. 64
- Tabela 3 – Métricas e classificação final das correções — p. 64
- Tabela 4 – Métricas gerais obtidas na execução da PoC — p. 64
- Tabela 5 – Métricas consolidadas por estratégia de prompt — p. 65
- Tabela 6 – Métricas consolidadas por caso vulnerável — p. 65

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

- 1 INTRODUÇÃO — p. 12
  - 1.1 Contexto — p. 12
  - 1.2 Problema — p. 13
  - 1.3 Objetivos — p. 15
    - 1.3.1 Objetivo Geral — p. 15
    - 1.3.2 Objetivos Específicos — p. 15
  - 1.4 Metodologia — p. 15
  - 1.5 Organização do Trabalho — p. 16
- 2 REFERENCIAL TEÓRICO — p. 17
  - 2.1 Modelos de Linguagem de Grande Escala (LLMs) — p. 17
  - 2.2 Engenharia de Prompt — p. 20
  - 2.3 Vulnerabilidades de Software e OWASP 10 — p. 25
  - 2.4 Ferramentas de Análise Estática de Segurança (SAST) — p. 28
  - 2.5 Trabalhos Relacionados — p. 31
- 3 METODOLOGIA — p. 33
  - 3.1 Plano Metodológico — p. 33
  - 3.2 Contexto de aplicação do experimento — p. 34
  - 3.3 Objeto de estudo: OWASP Juice Shop — p. 35
  - 3.4 Seleção das vulnerabilidades de segurança — p. 36
  - 3.5 Ferramenta de análise estática — p. 37
  - 3.6 Estratégias de prompt — p. 38
  - 3.7 Estratégia de RAG simplificado — p. 39
  - 3.8 Pipeline — p. 41
  - 3.9 Métricas de avaliação — p. 43
  - 3.10 Armazenamento e organização dos dados — p. 44
  - 3.11 Análise dos dados — p. 46
  - 3.12 Limitações do estudo — p. 47
  - 3.13 Declaração de Uso de Inteligência Artificial — p. 48
  - 3.14 Cronograma — p. 48
- 4 PROVA DE CONCEITO — p. 50
  - 4.1 Visão geral — p. 50
  - 4.2 Elaboração da PoC — p. 50
    - 4.2.1 Escolha e fundamentação das vulnerabilidades — p. 51
    - 4.2.2 Criação dos códigos vulneráveis — p. 52
    - 4.2.3 Elaboração dos testes automatizados — p. 53
    - 4.2.4 Elaboração das estratégias de prompt — p. 54
    - 4.2.5 Definição do fluxo experimental — p. 55
  - 4.3 Estrutura do projeto — p. 56
  - 4.4 Fluxo de execução e armazenamento dos resultados — p. 58
  - 4.5 Métricas de avaliação — p. 60
  - 4.6 Execução da PoC — p. 61
  - 4.7 Interpretação dos resultados — p. 61
  - 4.8 Contribuição da PoC — p. 66
- 5 CONSIDERAÇÕES FINAIS — p. 67
- REFERÊNCIAS — p. 68

