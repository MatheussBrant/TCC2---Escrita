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

## [editaveis/aspectosgerais.tex](editaveis/aspectosgerais.tex)

```diff
--- original/editaveis/aspectosgerais.tex
+++ atual/editaveis/aspectosgerais.tex
@@ -59 +59 @@
-Contudo, a Cadeia de Pensamento não deve ser interpretada como uma representação necessariamente fiel do processo interno utilizado pelo modelo. A sequência textual pode constituir uma justificativa plausível produzida após a escolha da resposta, sem refletir exatamente os fatores que determinaram a geração. Portanto, o CoT deve ser utilizado como uma estratégia para estruturar a tarefa e produzir etapas verificáveis, e não como uma garantia de transparência ou correção do raciocínio \cite{lester_power_2021}. No contexto deste trabalho, as etapas apresentadas pela LLM deverão ser confrontadas com os diagnósticos da ferramenta SAST, com testes e com a reanálise do código corrigido.
+Contudo, a Cadeia de Pensamento não deve ser interpretada como uma representação necessariamente fiel do processo interno utilizado pelo modelo. A sequência textual pode constituir uma justificativa plausível produzida após a escolha da resposta, sem refletir exatamente os fatores que determinaram a geração. Portanto, o CoT deve ser utilizado como uma estratégia para estruturar a tarefa e produzir etapas verificáveis, e não como uma garantia de transparência ou correção do raciocínio \cite{lester_power_2021}. Neste trabalho, as propostas de alteração foram avaliadas por reanálise estática e testes automatizados, sem validar o raciocínio interno do modelo.
@@ -69 +69 @@
-As três etapas centrais desse processo são a recuperação, o enriquecimento e a geração. Na recuperação, são localizados os documentos considerados mais relevantes para a consulta. No enriquecimento, os documentos selecionados são organizados e anexados à instrução. Na geração, a LLM produz a resposta utilizando o contexto ampliado \cite{klesel_retrieval-augmented_2025}. No domínio deste trabalho, a consulta pode ser formada a partir da linguagem de programação, da regra emitida pelo SAST, da categoria CWE, das funções utilizadas e do tipo de vulnerabilidade detectada.
+As três etapas centrais desse processo são a recuperação, o enriquecimento e a geração. Na recuperação, são localizados os documentos considerados mais relevantes para a consulta. No enriquecimento, os documentos selecionados são organizados e anexados à instrução. Na geração, a LLM produz a resposta utilizando o contexto ampliado \cite{klesel_retrieval-augmented_2025}. Neste trabalho, a recuperação utilizou um mapeamento entre CWEs e documentos de apoio, com alternativas por categoria e documento genérico, conforme descrito na metodologia.
@@ -77 +77 @@
-Neste trabalho, a engenharia de prompt será utilizada para organizar essas diferentes fontes de informação. O prompt poderá ser composto pela descrição da tarefa, pelo código vulnerável, pelos dados do alerta SAST, pela regra violada, pela categoria CWE, pelo contexto recuperado por meio do RAG e pelas restrições de preservação da funcionalidade. Exemplos \textit{few-shot} poderão orientar o formato da resposta e demonstrar correções previamente validadas, enquanto uma estratégia de decomposição conduzirá a LLM pelas etapas de triagem, análise da causa, geração do reparo e revisão da modificação.
+Neste trabalho, a engenharia de prompt organizou a instrução, o código e as restrições de alteração. Conforme a estratégia, foram acrescentados um roteiro de raciocínio guiado, o diagnóstico SAST e um documento recuperado pelo RAG simplificado. Essas combinações constituíram as estratégias P1--P4, descritas na metodologia.
@@ -79 +79 @@
-A resposta do modelo deverá ser estruturada para permitir sua utilização automática pelo pipeline. Além do código corrigido, poderão ser solicitados a decisão sobre a validade do alerta, o tipo de modificação realizada e as suposições necessárias para a solução. Entretanto, nenhuma justificativa produzida pela LLM será considerada suficiente para validar o reparo. O código será novamente submetido à ferramenta SAST e aos mecanismos de verificação funcional definidos no experimento.
+As respostas foram solicitadas em formato JSON, contendo as edições propostas, suas justificativas e limitações. As propostas aplicadas foram avaliadas por compilação, testes automatizados e reanálise estática. As justificativas produzidas pela LLM não foram utilizadas como evidência suficiente de validade da correção.
@@ -81 +81 @@
-Assim, o enriquecimento do prompt, o RAG e a decomposição orientada não substituem a validação externa. Essas técnicas buscam aumentar a quantidade e a qualidade das informações disponíveis durante a geração. A confiabilidade final será obtida pela combinação entre contexto técnico, geração orientada e feedback de ferramentas externas. Nesse fluxo, o alerta do SAST deixa de ser apenas uma mensagem textual e passa a integrar um processo iterativo no qual o diagnóstico, o conhecimento recuperado, a correção gerada e os resultados da reanálise são utilizados conjuntamente para produzir e validar o reparo.
+O enriquecimento de contexto e o raciocínio guiado apoiaram a geração das propostas, enquanto a análise estática e os testes determinaram sua avaliação e a continuidade da sequência. Cada tentativa partiu do código original, sem incorporar ao prompt as respostas ou os erros das tentativas anteriores. A iteração consistiu, portanto, na execução de estratégias sucessivas até atender à regra de parada ou esgotar P1--P4.
@@ -146,3 +146 @@
-No pipeline proposto, uma primeira execução da SAST será utilizada para estabelecer o estado inicial do código. Para cada issue relacionado à segurança, poderão ser coletados dados como o identificador e a descrição da regra, o arquivo e a linha afetados, a mensagem apresentada, a severidade, as classificações CWE e OWASP, as localizações secundárias e os fluxos entre fontes e destinos. Esses dados formarão o contexto técnico fornecido à LLM.
-
-Após a geração do reparo, o projeto será analisado novamente pela SAST. Essa nova execução permitirá verificar se o issue original deixou de ser identificado e se a alteração introduziu novos alertas. Entretanto, o desaparecimento do alerta não será considerado, isoladamente, prova suficiente de que o reparo foi bem-sucedido. A ferramenta pode deixar de detectar uma vulnerabilidade mesmo que ela permaneça no código, e a LLM pode eliminar o alerta comprometendo a funcionalidade da aplicação. Dessa forma, a validação deverá combinar a reanálise estática com compilação, testes funcionais e comparação do comportamento esperado.
+No pipeline implementado, a análise inicial com Semgrep estabeleceu os alertas de referência e forneceu os dados utilizados na constituição do catálogo. Nas estratégias P3 e P4, o diagnóstico do alerta também integrou o contexto enviado à LLM. Após a aplicação de cada proposta, a reanálise verificou a permanência do alerta original e o aparecimento de novos alertas. Essa avaliação foi combinada com compilação e testes automatizados, pois o desaparecimento de um alerta não comprova, isoladamente, uma correção segura e funcional.
@@ -163 +161 @@
-Diante das lacunas e dos resultados apresentados por ests trabalhos, esta pesquisa fundamenta-se na integração dessas tecnologias. Ao combinar o diagnóstico de uma ferramenta SAST com modelos de linguagem comerciais utilizando técnicas de RAG e Cadeia de Pensamento (CoT), o estudo propõe um fluxo iterativo capaz de interpretar os alertas gerados e sugerir correções mais precisas para vulnerabilidades associadas ao OWASP Top 10. Com isso, busca-se alcançar um método que contribua para a correção das falhas sem comprometer negativamente o código.
+Com base nesses trabalhos, esta pesquisa implementou e avaliou um pipeline que combina LLMs, análise estática, testes automatizados e diferentes estratégias de contextualização e raciocínio guiado. A avaliação examinou o aceite das propostas individuais e o comportamento do projeto após a aplicação conjunta das alterações.
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

## [editaveis/consideracoes.tex](editaveis/consideracoes.tex)

```diff
--- original/editaveis/consideracoes.tex
+++ atual/editaveis/consideracoes.tex
@@ -28,0 +29,2 @@
+    \caption{Visão geral do fluxo metodológico adotado na pesquisa.}
+    \label{fig:plano}
@@ -35,3 +36,0 @@
-    \caption{Visão geral do fluxo metodológico adotado na pesquisa.}
-    \label{fig:plano}
-
@@ -40,0 +40 @@
+        Fonte: elaboração própria.\par
@@ -71,3 +71,7 @@
-Plataforma Docker & \texttt{linux/amd64} \\
-\hline
-Node.js e npm do \textit{baseline} final & 24.14.0 e 11.9.0 \\
+Plataforma Docker & \texttt{linux/amd64}; imagem \texttt{81fe6403f07a} \\
+\hline
+Node.js (execução e testes) e npm & 24.14.0 e 11.9.0 \\
+\hline
+Execução do \textit{pipeline} & Python 3.11.2 \\
+\hline
+Integração com os modelos & OpenAI 3.14.1 (biblioteca Python) \\
@@ -75,0 +80,10 @@
+\hline
+Compilação TypeScript & 6.0.3 no servidor e 5.9.3 no frontend \\
+\hline
+Interface e ferramentas Angular & Angular 21.2.25; CLI e ferramenta de compilação 21.2.27 \\
+\hline
+Servidor web & Express 4.22.3 \\
+\hline
+Requisições nos testes de API & Supertest 7.3.1 \\
+\hline
+Testes da interface & Vitest 4.1.12 e jsdom 29.1.1 \\
@@ -86 +100 @@
-    Fonte: configurações, \textit{baseline} funcional e contratos das campanhas do experimento.
+    Fonte: protocolo, \textit{baseline} funcional, referência da imagem Docker e arquivos de dependências fixadas do experimento. As versões do Docker Engine e do Git não foram recuperadas nos registros das campanhas consultados.
@@ -127 +141 @@
-Os critérios de escopo limitaram a avaliação ao código das funcionalidades da aplicação, que podia ser examinado pela análise estática e pelos testes do Juice Shop. Foram excluídos os alertas nos exemplos dos \textit{Coding Challenges}, localizados em \texttt{data/static/codefixes/}, nos arquivos de automação do GitHub, em \texttt{.github/workflows/}, e nos arquivos de configuração do npm, \texttt{.npmrc}. Os exemplos dos \textit{Coding Challenges} contêm alternativas de correção dos exercícios pedagógicos, e sua exclusão evitou fornecê-las aos modelos como soluções. Os outros dois tipos de arquivo tratam de integração contínua e gerenciamento de dependências, aspectos cuja segurança não era avaliada pela suíte de testes da aplicação. A exclusão expressou uma decisão sobre o recorte do experimento, sem determinar se cada alerta correspondia a uma falha real ou a um falso positivo. A Tabela~\ref{tab:catalogo} apresenta a distribuição das exclusões.
+Os critérios de escopo limitaram a avaliação ao código das funcionalidades da aplicação, que podia ser examinado pela análise estática e pelos testes do Juice Shop. Foram excluídos os alertas nos exemplos dos \textit{Coding Challenges}, localizados em \texttt{data/\allowbreak static/\allowbreak codefixes/\allowbreak }, nos arquivos de automação do GitHub, em \texttt{.\allowbreak github/\allowbreak workflows/\allowbreak }, e nos arquivos de configuração do npm, \texttt{.\allowbreak npmrc}. Os exemplos dos \textit{Coding Challenges} contêm alternativas de correção dos exercícios pedagógicos, e sua exclusão evitou fornecê-las aos modelos como soluções. Os outros dois tipos de arquivo tratam de integração contínua e gerenciamento de dependências, aspectos cuja segurança não era avaliada pela suíte de testes da aplicação. A exclusão expressou uma decisão sobre o recorte do experimento, sem determinar se cada alerta correspondia a uma falha real ou a um falso positivo. A Tabela~\ref{tab:catalogo} apresenta a distribuição das exclusões.
@@ -163 +177,3 @@
-Para cada caso, foram registrados identificador, regra, arquivo e localização, mensagem, severidade, trecho de código e associações a CWE e OWASP quando disponíveis. O catálogo também preservou a triagem de 55 casos classificados como confirmados, 21 como falsos positivos e dois como inconclusivos.
+Para cada caso, foram registrados identificador, regra, arquivo e localização, mensagem, severidade, trecho de código e associações a CWE e OWASP quando disponíveis. O catálogo também preservou a triagem de 55 casos classificados como confirmados, 21 como falsos positivos e dois como inconclusivos. Os falsos positivos foram mantidos para observar o comportamento do \textit{pipeline} diante dos alertas do SAST, sem interpretar seu eventual aceite como correção de uma vulnerabilidade real.
+
+O catálogo incluiu três alertas em arquivos de teste do frontend, relacionados a tokens JWT utilizados como exemplos e classificados como falsos positivos na triagem.
@@ -307,0 +324,2 @@
+    \caption{Fluxo de correção de um caso, com tentativas progressivas por estratégia de \textit{prompt}.}
+    \label{fig:pipeline}
@@ -314,3 +331,0 @@
-    \caption{Fluxo de correção de um caso, com tentativas progressivas por estratégia de \textit{prompt}.}
-    \label{fig:pipeline}
-
@@ -319,0 +335 @@
+        Fonte: elaboração própria.\par
@@ -447 +463 @@
-Cada tentativa de correção recebeu um identificador único, utilizado para nomear os artefatos e relacioná-los aos registros do experimento. A composição desse identificador reuniu o caso analisado, a categoria OWASP, a sigla do tipo de vulnerabilidade, a estratégia de \textit{prompt} e a execução correspondente, separados por sublinhados. A identificação do artefato foi complementada pelo diretório, pelo sufixo ou pela extensão do arquivo. A Figura~\ref{fig:nomenclatura_artefatos} ilustra os componentes dessa nomenclatura com um exemplo abreviado.
+A Figura~\ref{fig:modelo-dados} sintetiza os principais campos e vínculos entre os registros. Cada tentativa referencia um caso e uma campanha e registra os caminhos e \textit{hashes} de seus artefatos. As tentativas alimentam a consolidação das métricas, enquanto os \textit{patches} selecionados passam por avaliação conjunta para obter a RRIS e o resultado funcional da integração.
@@ -450,0 +467,17 @@
+    \caption{Modelo lógico dos dados e artefatos do experimento.}
+    \label{fig:modelo-dados}
+    \includegraphics[width=\textwidth]{figuras/modelo-dados.pdf}
+    \vspace{0.2cm}
+    \begin{minipage}{\textwidth}
+        \footnotesize
+        Fonte: elaboração própria, a partir dos registros do experimento.\par
+        Setas contínuas indicam vínculos entre registros e arquivos; setas tracejadas indicam seleção, processamento ou consolidação dos dados. A notação 0..N indica nenhum ou vários registros. Os campos apresentados são uma seleção dos dados armazenados.
+    \end{minipage}
+\end{figure}
+
+Cada tentativa de correção recebeu um identificador único, utilizado para nomear os artefatos e relacioná-los aos registros do experimento. A composição desse identificador reuniu o caso analisado, a categoria OWASP, a sigla do tipo de vulnerabilidade, a estratégia de \textit{prompt} e a execução correspondente, separados por sublinhados. A identificação do artefato foi complementada pelo diretório, pelo sufixo ou pela extensão do arquivo. A Figura~\ref{fig:nomenclatura_artefatos} ilustra os componentes dessa nomenclatura com um exemplo abreviado.
+
+\begin{figure}[H]
+    \centering
+    \caption{Estrutura do identificador utilizado na nomenclatura dos artefatos gerados pelo \textit{pipeline}.}
+    \label{fig:nomenclatura_artefatos}
@@ -457,3 +489,0 @@
-    \caption{Estrutura do identificador utilizado na nomenclatura dos artefatos gerados pelo \textit{pipeline}.}
-    \label{fig:nomenclatura_artefatos}
-
@@ -462,0 +493 @@
+        Fonte: elaboração própria.\par
```

## [editaveis/elementosdotexto.tex](editaveis/elementosdotexto.tex)

```diff
--- original/editaveis/elementosdotexto.tex
+++ atual/editaveis/elementosdotexto.tex
@@ -20,0 +21,2 @@
+    \caption{Etapas principais do \textit{pipeline} e suas conexões.}
+    \label{fig:impl-etapas}
@@ -29,3 +30,0 @@
-    \caption{Etapas principais do \textit{pipeline} e suas conexões.}
-    \label{fig:impl-etapas}
-
@@ -34,0 +34 @@
+        Fonte: elaboração própria.\par
@@ -60,0 +61,2 @@
+    \caption{Cópias de trabalho do Juice Shop utilizadas pelo \textit{pipeline}.}
+    \label{fig:impl-worktrees}
@@ -69,3 +70,0 @@
-    \caption{Cópias de trabalho do Juice Shop utilizadas pelo \textit{pipeline}.}
-    \label{fig:impl-worktrees}
-
@@ -74,0 +74 @@
+        Fonte: elaboração própria.\par
@@ -95 +95 @@
-No caso utilizado como exemplo, o Semgrep apontou a linha 14 do arquivo \texttt{routes/keyServer.ts} com a regra \texttt{express-res-sendfile}, do conjunto público, associada à CWE-73. O código não garante que o caminho final permaneça dentro da pasta prevista, o que caracteriza uma vulnerabilidade de \textit{path traversal}, na qual um atacante manipula o caminho para ler arquivos fora do local permitido. O caso recebeu o identificador \texttt{AMP95adf572d3c6677f}. O trecho apontado é apresentado a seguir.
+No caso utilizado como exemplo, o Semgrep apontou a linha 14 do arquivo \texttt{routes/\allowbreak keyServer.\allowbreak ts} com a regra \texttt{express-res-sendfile}, do conjunto público, associada à CWE-73. A regra sinalizou uma possibilidade de \textit{path traversal}. Entretanto, a triagem classificou o caso como confirmado pela exposição de arquivos de chaves em uma rota pública, sem comprovar a exploração por travessia de diretórios. O caso recebeu o identificador \texttt{AMP95adf572d3c6677f}. O trecho apontado é apresentado a seguir.
@@ -195 +195 @@
-A implementação está disponível em repositório público no GitHub, em \href{https://github.com/caiolamego/tcc2-llm-sast-juiceshop}{caiolamego/tcc2-llm-sast-juiceshop}. A estrutura principal do projeto foi organizada da seguinte forma:
+A implementação está disponível no \href{https://github.com/caiolamego/tcc2-llm-sast-juiceshop}{repositório público do projeto no GitHub}. A estrutura principal do projeto foi organizada da seguinte forma:
@@ -277 +277 @@
-O arquivo \texttt{contrato\_execucao.json} registra as condições da execução, como os modelos e parâmetros utilizados, a versão do Juice Shop, as estratégias, a lista de casos e os \textit{hashes} do catálogo, do perfil de regras, da base de conhecimento, dos testes e do próprio código do \textit{pipeline}. As pastas \texttt{sast\_antes/} e \texttt{sast\_depois/} guardam os relatórios do Semgrep antes e depois das correções. As pastas \texttt{prompts/} e \texttt{respostas\_llm/} guardam o conteúdo enviado e recebido em cada tentativa. As pastas \texttt{patches/} e \texttt{codigos\_corrigidos/} guardam as alterações aplicadas, \texttt{testes/} guarda os resultados da validação funcional e \texttt{comparacoes/} guarda o resultado da comparação dos alertas. A pasta \texttt{resultados\_consolidados/} contém o arquivo consolidado com uma linha por tentativa. A versão final dos artefatos foi reunida na pasta \texttt{outputs/resultados\_finais/}, que contém uma cópia dessa estrutura para cada campanha e os mapas de correspondência citados na Seção~\ref{sec:met-dados}. As métricas calculadas a partir desses registros são gravadas em uma pasta separada, descrita na Seção~\ref{sec:impl-metricas}.
+O arquivo \texttt{contrato\_\allowbreak execucao.\allowbreak json} registra as condições da execução, como os modelos e parâmetros utilizados, a versão do Juice Shop, as estratégias, a lista de casos e os \textit{hashes} do catálogo, do perfil de regras, da base de conhecimento, dos testes e do próprio código do \textit{pipeline}. As pastas \texttt{sast\_\allowbreak antes/\allowbreak } e \texttt{sast\_\allowbreak depois/\allowbreak } guardam os relatórios do Semgrep antes e depois das correções. As pastas \texttt{prompts/\allowbreak } e \texttt{respostas\_\allowbreak llm/\allowbreak } guardam o conteúdo enviado e recebido em cada tentativa. As pastas \texttt{patches/\allowbreak } e \texttt{codigos\_\allowbreak corrigidos/\allowbreak } guardam as alterações aplicadas, \texttt{testes/\allowbreak } guarda os resultados da validação funcional e \texttt{comparacoes/\allowbreak } guarda o resultado da comparação dos alertas. A pasta \texttt{resultados\_\allowbreak consolidados/\allowbreak } contém o arquivo consolidado com uma linha por tentativa. A versão final dos artefatos foi reunida na pasta \texttt{outputs/\allowbreak resultados\_\allowbreak finais/\allowbreak }, que contém uma cópia dessa estrutura para cada campanha e os mapas de correspondência citados na Seção~\ref{sec:met-dados}. As métricas calculadas a partir desses registros são gravadas em uma pasta separada, descrita na Seção~\ref{sec:impl-metricas}.
@@ -290 +290 @@
-O código alterado foi compilado e aprovado nos testes do grupo de entrega de arquivos. Na nova análise, o alerta original deixou de ser apontado e nenhum alerta novo apareceu. Com R, F e M iguais a 1, a correção atendeu à regra de parada e o caso foi encerrado, sem a execução da estratégia P4. Os arquivos dessa tentativa receberam o identificador \texttt{AMP95adf572d3c6677f\_\allowbreak A06\_\allowbreak PATHTRAV\_\allowbreak P3\_\allowbreak AMP\_\allowbreak REAL\_\allowbreak 20261106T151004Z\_\allowbreak f49ac0d2}, que segue a estrutura apresentada na Figura~\ref{fig:nomenclatura_artefatos}.
+O código alterado foi compilado e aprovado nos testes do grupo de entrega de arquivos. Na nova análise, o alerta original deixou de ser apontado e nenhum alerta novo apareceu. Com R, F e M iguais a 1, a correção atendeu à regra de parada e o caso foi encerrado, sem a execução da estratégia P4. Esse aceite corresponde às verificações realizadas e não comprova a eliminação da exposição de chaves identificada na triagem. Os arquivos dessa tentativa receberam o identificador \texttt{AMP95adf572d3c6677f\_\allowbreak A06\_\allowbreak PATHTRAV\_\allowbreak P3\_\allowbreak AMP\_\allowbreak REAL\_\allowbreak 20261106T151004Z\_\allowbreak f49ac0d2}, que segue a estrutura apresentada na Figura~\ref{fig:nomenclatura_artefatos}.
```

## [editaveis/resultado-discussoes.tex](editaveis/resultado-discussoes.tex)

```diff
--- original/editaveis/resultado-discussoes.tex
+++ atual/editaveis/resultado-discussoes.tex
@@ -189,0 +190,2 @@
+    \caption{Distribuição dos casos pelo primeiro aceite e pela ausência de aceite.}
+    \label{fig:res-aceites-estrategia}
@@ -195,3 +196,0 @@
-
-    \caption{Distribuição dos casos pelo primeiro aceite e pela ausência de aceite.}
-    \label{fig:res-aceites-estrategia}
@@ -536,2 +535,9 @@
-      ? calculate(firstTerm, firstOperator, calculate(secondTerm, secondOperator, thirdTerm))
-      : calculate(calculate(firstTerm, firstOperator, secondTerm), secondOperator, thirdTerm)).toString()
+      ? calculate(
+          firstTerm, firstOperator,
+          calculate(secondTerm, secondOperator, thirdTerm)
+        )
+      : calculate(
+          calculate(firstTerm, firstOperator, secondTerm),
+          secondOperator, thirdTerm
+        )
+    ).toString()
@@ -541 +547 @@
-{\footnotesize Fonte: trecho literal do \textit{patch} arquivado. A função auxiliar \texttt{calculate} realiza as operações aritméticas explícitas.\par}
+{\footnotesize Fonte: trecho do \textit{patch} arquivado, com quebras de linha ajustadas para apresentação. A função auxiliar \texttt{calculate} realiza as operações aritméticas explícitas.\par}
```

## [figuras/modelo-dados.pdf](figuras/modelo-dados.pdf)

Figura nova, em PDF vetorial, inserida na seção de armazenamento e organização dos dados. Organizada em três níveis: casos e campanhas; tentativas; artefatos, avaliação conjunta dos patches e resultados consolidados. Apresenta formatos, campos, identificadores, caminhos, hashes e cardinalidades. Setas contínuas representam vínculos; tracejadas representam seleção, processamento ou consolidação. A RRIS utiliza os scans da avaliação conjunta, com resultado funcional separado. Fonte editável: [figuras/modelo-dados.tex](figuras/modelo-dados.tex), compilada separadamente; o documento principal utiliza apenas o PDF. O bloco de inserção, o título, a fonte e a explicação estão no diff de `consideracoes.tex` acima.

## Verificação e envio

Conferidas as remissões e a disponibilidade das chaves citadas. As sete substituições do capítulo 2 preservam as citações e a estrutura LaTeX; suas fontes estão nas [notas do capítulo 2](../evidencias/capitulo-2-notas.md). Resumo e abstract refletem a versão escolhida pelo autor. As dez figuras dos capítulos 3–5 foram conferidas no fonte: todas têm título antes da imagem e indicação de fonte. Os quatro parágrafos com caminhos longos foram compilados em um documento de teste: quatro avisos de estouro de margem antes e nenhum após o ajuste. O excerto P2 do CAPTCHA também foi compilado isoladamente, sem estouro horizontal. A tabela de condições foi completada com versões conferidas no protocolo e nos arquivos vinculados à imagem e ao baseline; sua compilação isolada não apresentou estouros de margem. O propósito de manter falsos positivos foi explicitado no parágrafo da triagem. O modelo de dados foi compilado em PDF vetorial e inspecionado visualmente; sua inserção com título e fonte foi conferida em documento isolado. A compilação integral permanece indisponível por ausência de `abntex2.cls`; a paginação deve ser conferida no Overleaf.

Para aplicar as correções no Overleaf, substituir os oito arquivos de capítulos e pré-textuais vinculados acima e adicionar `figuras/modelo-dados.pdf`. O fonte `figuras/modelo-dados.tex` é opcional para edição da figura e não deve substituir `tcc.tex` como documento principal. As versões originais dos quatro ajustes anteriores estão preservadas em [evidências](../evidencias/ajustes-tcc2-overleaf-2026-11-15/antes/).
