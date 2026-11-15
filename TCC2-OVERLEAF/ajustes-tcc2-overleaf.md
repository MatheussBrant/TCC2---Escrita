# Ajustes TCC2 Overleaf

Cada seção mostra a diferença entre o arquivo original, anterior às correções, e sua versão atual. Linhas com `-` foram excluídas e linhas com `+` foram adicionadas; linhas sem esses sinais fornecem contexto.

**Regra de atualização:** manter uma única seção por arquivo e atualizar seu diff quando houver nova alteração. Não acrescentar seções com versões intermediárias.

## [editaveis/introducao.tex](editaveis/introducao.tex)

```diff
--- original/editaveis/introducao.tex
+++ atual/editaveis/introducao.tex
@@ -35,4 +35,5 @@
 \item Q3: O desempenho do \textit{pipeline} varia de acordo com o tipo de vulnerabilidade ou categoria associada ao OWASP Top 10?
  \item Q4: Quais limitações práticas surgem ao aplicar um \textit{pipeline} automatizado de correção de vulnerabilidades em uma base de código real, com dependências, arquitetura própria e suíte de testes existente?
+ \item Q5: Como diferentes modelos de linguagem se comparam na geração de correções válidas pelo \textit{pipeline}, considerando eficácia, custo e tempo de execução?
 \end{itemize}
 
@@ -53,33 +54,20 @@
 \item Analisar os resultados obtidos no projeto, considerando a taxa de remediação validada, os tipos de \textit{issues} detectadas, as falhas de correção e as limitações práticas do \textit{pipeline}.
 
+\item Comparar diferentes modelos de linguagem na geração de correções válidas pelo \textit{pipeline}, considerando a eficácia, o custo e o tempo de execução nas condições avaliadas.
+
 \end{itemize}
 
 
 \section{Metodologia}
-Este trabalho propõe uma investigação empírica e experimental sobre a eficácia de um fluxo iterativo que integra Modelos de Linguagem de Grande Escala (LLMs) e ferramentas de Análise Estática de Segurança (SAST) na correção automatizada de vulnerabilidades. A pesquisa parte da ideia de que, embora LLMs possam auxiliar na identificação e no reparo de falhas, seu desempenho tende a melhorar quando elas recebem contexto adicional e operam em conjunto com ferramentas externas de apoio.
+Este trabalho realizou uma investigação empírica sobre a eficácia de um \textit{pipeline} que integra Modelos de Linguagem de Grande Escala (LLMs), Análise Estática de Segurança (SAST) e testes automatizados para apoiar a correção de alertas de segurança em código-fonte. A avaliação examinou diferentes estratégias de \textit{prompt} e modelos de linguagem, considerando a remoção dos alertas, a preservação funcional e a ausência de novos alertas nas condições definidas para o estudo.
 
-No TCC 1, essa proposta é inicialmente validada por meio de uma prova de conceito em ambiente controlado, composta por casos vulneráveis representativos, testes automatizados e execução integrada do \textit{pipeline}. Essa etapa tem como finalidade verificar a viabilidade técnica do fluxo proposto antes de sua aplicação em uma base de código real. No TCC 2, pretende-se evoluir essa abordagem para um projeto público, considerando as vulnerabilidades efetivamente identificadas pela ferramenta SAST selecionada.
+O experimento foi conduzido no OWASP Juice Shop, uma aplicação web de código aberto e deliberadamente vulnerável. A análise estática com Semgrep forneceu os alertas utilizados para constituir um catálogo de 78 casos. O projeto foi executado em ambiente preparado com Docker, mantendo uma revisão fixada do código e as condições de avaliação registradas nas campanhas.
 
+Foram avaliados os modelos GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna sobre os mesmos casos. Para cada caso, as estratégias seguiram a ordem P1, P2, P3 e P4: instrução direta, raciocínio guiado, diagnóstico SAST com documentação recuperada por RAG simplificado e combinação do diagnóstico e da documentação com o raciocínio guiado. Como as estratégias posteriores receberam os casos que não atenderam à regra de parada, as diferenças foram interpretadas considerando essa seleção.
 
-Inicialmente, será selecionado um projeto público que possa ser instalado e executado em ambiente local, possua estrutura modular e apresente \textit{issues} de segurança detectáveis por uma ferramenta SAST compatível com a linguagem. As vulnerabilidades analisadas serão determinadas a partir dos alertas emitidos pela ferramenta SAST sobre o código-fonte do projeto, respeitando critérios de elegibilidade relacionados à possibilidade de reprodução, correção e validação automatizada.
+As propostas foram aplicadas em cópias de trabalho isoladas e avaliadas por reanálise estática e testes relacionados aos arquivos modificados. Na análise principal, o aceite exigiu a remoção do alerta original, a aprovação funcional na interpretação por critérios e a ausência de novos alertas, conforme as definições do Capítulo~\ref{cap:metodologia}. Essa interpretação distinguiu testes de comportamento legítimo daqueles que dependiam das vulnerabilidades intencionais da aplicação. A aplicação conjunta dos \textit{patches} selecionados também foi examinada, permitindo avaliar sua integração no projeto.
 
-Em seguida, os alertas gerados pela análise estática serão utilizados como entrada para o \textit{pipeline}. Para cada \textit{issue}, serão aplicadas diferentes estratégias de \textit{prompt}, incluindo instrução simples, raciocínio guiado, RAG simplificado e a combinação entre RAG simplificado e raciocínio guiado. O objetivo é verificar se o aumento de contexto e estruturação da tarefa melhora a qualidade das correções propostas pela LLM.
-
-Após a geração das correções, as modificações serão aplicadas em cópias isoladas do projeto e avaliadas por meio de nova execução da ferramenta SAST e da suíte de testes automatizados disponível. Uma correção será considerada válida apenas quando a \textit{issue} original deixar de ser detectada, os testes continuarem passando e nenhuma nova \textit{issue} de segurança for introduzida. Os resultados serão consolidados em arquivos estruturados para permitir a comparação entre estratégias de \textit{prompt}, tipos de \textit{issues} detectadas e limitações observadas durante a aplicação em um projeto.
-
-Dessa forma, a metodologia pretende medir quantitativamente o desempenho da arquitetura proposta, como também compreender em quais condições a combinação entre análise estática, contexto adicional e raciocínio orientado por LLMs se mostra mais eficaz para apoiar tarefas de segurança de software.
+\textit{Prompts}, respostas, \textit{patches}, análises e testes foram registrados em arquivos estruturados. Esses dados sustentaram a comparação entre estratégias, modelos e tipos de alerta, incluindo custos calculados e tempos observados. As medições ausentes foram identificadas na análise, e o aceite foi interpretado como atendimento às verificações adotadas, sem constituir comprovação de segurança completa.
 
 \section{Organização do Trabalho}
-% Este trabalho está organizado em seis capítulos, sendo eles:
-% \begin{itemize}
-%  \item Introdução;
-%  \item Referencial teórico;
-%  \item Metodologia;
-%  \item Prova de Conceito
-%  \item Considerações Finais
-%  \item Declaração do uso de Inteligência Artificial
-% \end{itemize}
-
-O restante deste trabalho está organizado da seguinte forma: o Capítulo 2 apresenta o referencial teórico que fundamenta a pesquisa; o Capítulo 3 descreve a metodologia proposta para a continuidade do estudo, incluindo o planejamento da coleta e análise dos dados no TCC 2; o Capítulo 4 apresenta a prova de conceito desenvolvida no TCC 1, destacando sua estrutura, execução, métricas e resultados obtidos; por fim, o Capítulo 5 apresenta as considerações finais desta etapa do trabalho.
-
-
+O restante deste trabalho está organizado da seguinte forma: o Capítulo 2 apresenta o referencial teórico e os trabalhos relacionados; o Capítulo~\ref{cap:metodologia} descreve a metodologia e os critérios de avaliação; o Capítulo~\ref{cap:implementacao} apresenta o desenvolvimento e a implementação do \textit{pipeline}; o Capítulo~\ref{cap:resultados} expõe os resultados, sua discussão e as respostas às perguntas de pesquisa; e o Capítulo~\ref{cap:consideracoes-finais} reúne as considerações finais e as propostas de trabalhos futuros.
```

## [editaveis/resumo.tex](editaveis/resumo.tex)

```diff
--- original/editaveis/resumo.tex
+++ atual/editaveis/resumo.tex
@@ -1,4 +1,4 @@
 \begin{resumo}
-Modelos de Linguagem de Grande Escala (LLMs) têm sido cada vez mais utilizados no desenvolvimento de software, inclusive em tarefas de geração, explicação e correção de código. No entanto, seu uso em segurança ainda exige cautela, pois correções geradas automaticamente podem ser incompletas, inseguras ou comprometer o funcionamento original da aplicação. Este trabalho investiga a integração entre LLMs, ferramentas de Análise Estática de Segurança (SAST), testes automatizados e estratégias de contextualização para apoiar a correção de \textit{issues} de segurança em código-fonte. A metodologia proposta prevê a aplicação de um \textit{pipeline} automatizado em um projeto \textit{open source}, utilizando as vulnerabilidades efetivamente detectadas pela ferramenta SAST. Como etapa inicial, foi desenvolvida uma prova de conceito para validar o fluxo de identificação, geração de correções, reanálise estática, execução de testes e consolidação de métricas. O trabalho estabelece, assim, as bases técnicas e metodológicas para avaliar a eficácia do \textit{pipeline} no TCC 2.
+Modelos de Linguagem de Grande Escala (LLMs) têm sido utilizados no desenvolvimento de software, inclusive em atividades de geração e correção de código. Entretanto, seu uso em segurança exige validação, pois as alterações propostas podem ser incompletas ou comprometer o funcionamento da aplicação. Este trabalho investigou a integração entre LLMs, ferramentas de Análise Estática de Segurança (SAST), testes automatizados e estratégias de contextualização para apoiar a correção de alertas de segurança em código-fonte. Para isso, foi implementado e avaliado um \textit{pipeline} automatizado no OWASP Juice Shop, utilizando o Semgrep para identificar e reanalisar os alertas. A avaliação comparou modelos de linguagem e estratégias de \textit{prompt}, incluindo raciocínio guiado e RAG simplificado, considerando a remoção dos alertas, a preservação funcional e a ausência de novos alertas. Os resultados mostraram a possibilidade de obter propostas aceitas individualmente pelas verificações adotadas, mas também dificuldades na integração das alterações, cujos conjuntos não receberam aprovação funcional. O estudo contribui para compreender as possibilidades e as limitações da combinação entre geração de código e validação automatizada no apoio à correção de vulnerabilidades.
 
 \textbf{Palavras-chave}: modelos de linguagem de grande escala; análise estática de segurança; correção de vulnerabilidades; engenharia de prompt; RAG; \textit{pipeline}.
```

## [editaveis/abstract.tex](editaveis/abstract.tex)

```diff
--- original/editaveis/abstract.tex
+++ atual/editaveis/abstract.tex
@@ -1,5 +1,5 @@
 \begin{resumo}[Abstract]
 \begin{otherlanguage*}{english}
-Large Language Models (LLMs) have been increasingly used in software development, including tasks such as code generation, explanation, and correction. However, their use in software security still requires caution, since automatically generated fixes may be incomplete, insecure, or may compromise the original behavior of the application. This work investigates the integration of LLMs, Static Application Security Testing (SAST) tools, automated tests, and contextualization strategies to support the correction of security issues in source code. The proposed methodology applies an automated pipeline to an open source project, using the vulnerabilities effectively detected by the SAST tool. As an initial step, a proof of concept was developed to validate the workflow for issue identification, fix generation, static reanalysis, test execution, and metric consolidation. Thus, this work establishes the technical and methodological foundations to evaluate the effectiveness of the pipeline in TCC 2.
+Large Language Models (LLMs) have been used in software development, including code generation and correction. However, their use in security requires validation, as proposed changes may be incomplete or compromise application behavior. This study investigated the integration of LLMs, Static Application Security Testing (SAST) tools, automated tests, and contextualization strategies to support the correction of security alerts in source code. An automated pipeline was implemented and evaluated on OWASP Juice Shop, using Semgrep to identify and reassess alerts. The evaluation compared language models and prompting strategies, including guided reasoning and simplified RAG, considering alert removal, functional preservation, and the absence of new alerts. The results showed that individual proposals could be accepted under the adopted checks, while also revealing difficulties in integrating the changes, as none of the combined versions received functional approval. The study contributes to understanding the possibilities and limitations of combining code generation and automated validation to support vulnerability repair.
 
 \textbf{Keywords}: large language models; static application security testing; vulnerability repair; prompt engineering; RAG; pipeline.
```

## [editaveis/simbolos.tex](editaveis/simbolos.tex)

```diff
--- original/editaveis/simbolos.tex
+++ atual/editaveis/simbolos.tex
@@ -1,9 +1,21 @@
 \begin{simbolos}
   \item[$\sum$] Operador de somatório
-  \item[$R_j$] Resultado da remoção da \textit{issue} real $j$ após a correção
-  \item[$F_j$] Resultado da preservação funcional da correção aplicada à \textit{issue} real $j$
-  \item[$M_j$] Indicador de não introdução de novas \textit{issues} após a correção da \textit{issue} real $j$
-  \item[$m$] Número total de tentativas de correção realizadas no projeto real
-  \item[$I_{\text{antes}}$] Número de \textit{issues} de segurança detectadas antes da aplicação das correções aceitas
-  \item[$I_{\text{depois}}$] Número de \textit{issues} de segurança detectadas após a aplicação das correções aceitas
-\end{simbolos}+  \item[$j$] Índice de uma tentativa de geração e avaliação de uma proposta de correção
+  \item[$R_j$] Indicador de remoção do alerta original na tentativa $j$, quando há medição conclusiva
+  \item[$F_j$] Indicador de aprovação funcional da tentativa $j$, na interpretação de F adotada e quando há medição conclusiva
+  \item[$M_j$] Indicador de ausência de novos alertas na tentativa $j$, quando há medição conclusiva
+  \item[$m$] Número total de tentativas da população analisada, incluindo as não aplicadas e as indeterminadas
+  \item[$J_V$] Conjunto dos índices das tentativas aplicadas com R, F e M medidos
+  \item[$J_R$] Conjunto dos índices das tentativas com R medido
+  \item[$J_F$] Conjunto dos índices das tentativas com F medido
+  \item[$J_M$] Conjunto dos índices das tentativas com M medido
+  \item[$n_R$] Número de tentativas com R medido, correspondente a $|J_R|$
+  \item[$n_F$] Número de tentativas com F medido, correspondente a $|J_F|$
+  \item[$n_M$] Número de tentativas com M medido, correspondente a $|J_M|$
+  \item[$|J|$] Cardinalidade de um conjunto $J$, isto é, sua quantidade de elementos
+  \item[$D$] Conjunto de testes cujas asserções dependem das vulnerabilidades intencionais, conforme os critérios documentados
+  \item[$c_{\text{aceitos}}$] Número de casos distintos com pelo menos uma tentativa aceita
+  \item[$c_{\text{solicitados}}$] Número total de casos solicitados na campanha
+  \item[$I_{\text{antes}}$] Número de alertas no scan global comparável anterior à aplicação conjunta dos \textit{patches} selecionados
+  \item[$I_{\text{depois}}$] Número de alertas no scan global comparável posterior à aplicação conjunta dos \textit{patches} selecionados
+\end{simbolos}
```

## Verificação e envio

Conferidas as remissões e a disponibilidade das chaves citadas. Resumo e abstract refletem a versão escolhida pelo autor. Não foi realizada compilação local; a paginação deve ser conferida no Overleaf.

Para aplicar as correções no Overleaf, substituir os quatro arquivos vinculados acima. As versões originais usadas nesta comparação estão preservadas em [evidências](../evidencias/ajustes-tcc2-overleaf-2026-11-15/antes/).
