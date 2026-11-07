## 1 Introdução

### 1.1 Contexto

Nos últimos anos, especialmente a partir de 2022, os Modelos de Linguagem de Grande Escala, do inglês _Large Language Models_ (LLMs), passaram a integrar de forma cada vez mais significativa o processo de desenvolvimento de software. Essas ferramentas têm sido utilizadas em diversas atividades, como geração de código, explicação de trechos, sugestão de correções e apoio à análise de programas. Com isso, os LLMs passaram a ocupar um papel relevante no cotidiano de desenvolvedores e equipes de engenharia de software, ainda que continuem apresentando limitações em tarefas que demandam maior precisão e compreensão da lógica do código (ZHOU et al., 2024).

Com esse crescimento, também emergiram novas formas de desenvolvimento de software apoiadas por IA. Uma delas é o chamado _vibe coding_, no qual o desenvolvedor descreve, em linguagem natural, o que deseja construir e realiza ajustes sobre o código gerado pelo modelo. Paralelamente, ganhou destaque uma abordagem mais controlada, conhecida como _AI-assisted engineering_, na qual a IA atua como suporte dentro de um processo supervisionado, enquanto o desenvolvedor permanece responsável por revisar, validar e decidir o que deve ser incorporado ao sistema (OSMANI, 2025). Essa distinção é relevante, pois evidencia que o impacto da IA no desenvolvimento de software não depende apenas das capacidades do modelo, mas também da forma como ele é integrado ao processo de desenvolvimento.

Apesar dos ganhos de produtividade proporcionados por essas ferramentas, o uso de LLMs em tarefas relacionadas à segurança de software tem gerado preocupações. Estudos indicam que assistentes de programação baseados em IA podem produzir código inseguro em uma parcela significativa dos casos. Em uma pesquisa sobre o GitHub Copilot, por exemplo, cerca de 40% dos programas gerados nos cenários analisados apresentavam vulnerabilidades, evidenciando que essas ferramentas podem acelerar o desenvolvimento, mas não devem ser utilizadas sem validação, especialmente em contextos críticos (PEARCE et al., 2021).

Outro fator relevante é que o desempenho desses modelos depende fortemente do contexto fornecido. Em tarefas de detecção de vulnerabilidades, pesquisas mostram que a inclusão de informações adicionais pode melhorar a capacidade da IA de diferenciar falhas reais de situações apenas aparentemente suspeitas (IRANMANESH et al., 2025).

Diante disso, trabalhos recentes passaram a explorar abordagens em que a LLM não atua de forma isolada, mas em conjunto com ferramentas externas de apoio. Entre essas ferramentas, destacam-se as soluções de _Static Application Security Testing_ (SAST), que analisam o código-fonte sem executá-lo e apontam possíveis vulnerabilidades com base em padrões e regras conhecidas. Embora sejam úteis por ampliarem a cobertura da análise, essas ferramentas indicam condições potencialmente vulneráveis que ainda precisam ser interpretadas e validadas. Assim, seus alertas não devem ser tratados isoladamente como correções ou comprovações definitivas de vulnerabilidade, mas como evidências técnicas que podem orientar etapas posteriores de análise e remediação (IRANMANESH et al., 2025).

Nesse contexto, a integração entre LLMs e ferramentas SAST apresenta-se como uma alternativa promissora para tornar a correção de vulnerabilidades mais eficiente e adequada ao contexto do código analisado. Enquanto as ferramentas SAST contribuem para a identificação de possíveis problemas no código-fonte, os LLMs podem apoiar uma análise mais contextualizada, auxiliando na compreensão e na correção das vulnerabilidades detectadas. Estudos recentes indicam que abordagens iterativas, baseadas no uso de contexto adicional e no feedback de ferramentas externas, tendem a produzir resultados mais confiáveis do que interações isoladas fundamentadas em um único prompt (SRIRAM et al., 2026). É a partir dessa possibilidade de combinação entre essas tecnologias que se estabelece a motivação deste trabalho.

### 1.2 Problema

Embora a integração entre ferramentas de segurança e inteligência artificial se mostre promissora, sua aplicação prática ainda apresenta diversos desafios. Um dos principais está relacionado ao fato de que os modelos de linguagem, quando utilizados de forma isolada para corrigir vulnerabilidades, ainda não produzem resultados suficientemente confiáveis. Estudos recentes indicam que esses modelos conseguem identificar a existência de falhas com desempenho razoável, mas ainda apresentam grande dificuldade para gerar correções efetivas. Em um desses trabalhos, por exemplo, o modelo alcançou 76% de acerto na detecção de vulnerabilidades, mas apenas 15% de sucesso no reparo quando não recebeu contexto adicional sobre o problema (KHAN; LIU; GAO, 2025).

Além da baixa taxa de sucesso no reparo, outro problema relevante é que, em muitos casos, a tentativa de corrigir a vulnerabilidade pode comprometer o funcionamento original do software. Em vez de produzir uma solução segura e funcional, o modelo pode remover partes importantes da lógica da aplicação ou gerar um código que, embora elimine a falha de segurança, prejudique a utilidade do sistema. Esse comportamento evidencia que corrigir uma vulnerabilidade não consiste apenas em remover o erro, mas também em preservar o comportamento esperado do programa (DAI; XU; TAO, 2025).

Por outro lado, depender exclusivamente de ferramentas tradicionais de análise estática também não resolve o problema. Embora essas ferramentas sejam importantes para localizar possíveis falhas no código, seus alertas ainda precisam ser interpretados, priorizados e validados por desenvolvedores. Além disso, a identificação de uma _issue_ não implica, por si só, a existência de uma correção segura e funcional. Dessa forma, o SAST contribui para apontar evidências técnicas sobre possíveis vulnerabilidades, mas não substitui etapas posteriores de análise, remediação e validação (IRANMANESH et al., 2025).

Pesquisas recentes indicam que o desempenho das LLMs em tarefas de segurança pode melhorar quando o modelo recebe mais contexto e quando seu processo de resposta é conduzido de forma mais estruturada (TAO et al., 2025). Nesse cenário, estratégias como _Retrieval-Augmented Generation_ (RAG), que permite recuperar informações relevantes antes da geração da resposta, e _Chain-of-Thought_ (CoT), que incentiva um raciocínio em etapas, surgem como alternativas promissoras para apoiar tanto a interpretação dos alertas quanto o reparo das vulnerabilidades. Ainda assim, não está claro até que ponto essas estratégias realmente aumentam a eficácia da LLM quando ela atua em conjunto com ferramentas SAST (SRIRAM et al., 2026).

Assim, o problema central desta pesquisa surge justamente das limitações dessas abordagens quando utilizadas de forma isolada. De um lado, as LLMs ainda apresentam dificuldade para reparar vulnerabilidades de maneira confiável e sem comprometer a funcionalidade do software. De outro, ferramentas SAST são capazes de apontar possíveis falhas no código, mas não produzem, por si só, uma correção segura e funcional. Essa situação evidencia uma lacuna importante na engenharia de software atual: compreender até que ponto essas tecnologias podem atuar de forma complementar, com o SAST auxiliando na localização e descrição dos problemas, e a LLM contribuindo para gerar correções que possam ser posteriormente validadas por reanálise estática e testes automatizados.

Com base nisso, esta pesquisa busca responder às seguintes questões:

- Q1: É possível gerar correções válidas para vulnerabilidades por meio de um _pipeline_ automatizado que integra LLMs, ferramentas SAST e testes automatizados, considerando a remoção dos alertas, a preservação dos testes automatizados e a não introdução de novas _issues_ de segurança?

- Q2: Como diferentes estratégias de prompt, incluindo prompt simples, raciocínio guiado e enriquecimento de contexto por RAG simplificado, influenciam a taxa de correções válidas geradas pelo modelo de linguagem?

- Q3: O desempenho do _pipeline_ varia de acordo com o tipo de vulnerabilidade ou categoria associada ao OWASP Top 10?

- Q4: Quais limitações práticas surgem ao aplicar um _pipeline_ automatizado de correção de vulnerabilidades em uma base de código real, com dependências, arquitetura própria e suíte de testes existente?

### 1.3 Objetivos

#### 1.3.1 Objetivo Geral

Investigar a eficácia de um fluxo iterativo que integra Modelos de Linguagem de Grande Escala (LLMs), ferramentas de Análise Estática de Segurança (SAST) e testes automatizados na correção de vulnerabilidades em código-fonte, considerando a remoção dos alertas de segurança, a preservação da funcionalidade original e a não introdução de novas _issues_.

#### 1.3.2 Objetivos Específicos

- Desenvolver um _pipeline_ automatizado que integre uma ferramenta de análise estática de segurança, um modelo de linguagem e testes automatizados para apoiar a correção de _issues_ de segurança em código-fonte.

- Definir e aplicar diferentes estratégias de _prompt_, incluindo _prompt_ simples, raciocínio guiado e enriquecimento de contexto por RAG simplificado, a fim de comparar seu impacto na geração de correções válidas.

- Avaliar as correções geradas a partir da reanálise SAST, da execução dos testes automatizados e da verificação de que novas _issues_ de segurança não foram introduzidas.

- Analisar os resultados obtidos no projeto, considerando a taxa de remediação validada, os tipos de _issues_ detectadas, as falhas de correção e as limitações práticas do _pipeline_.

### 1.4 Metodologia

Este trabalho propõe uma investigação empírica e experimental sobre a eficácia de um fluxo iterativo que integra Modelos de Linguagem de Grande Escala (LLMs) e ferramentas de Análise Estática de Segurança (SAST) na correção automatizada de vulnerabilidades. A pesquisa parte da ideia de que, embora LLMs possam auxiliar na identificação e no reparo de falhas, seu desempenho tende a melhorar quando elas recebem contexto adicional e operam em conjunto com ferramentas externas de apoio.

No TCC 1, essa proposta é inicialmente validada por meio de uma prova de conceito em ambiente controlado, composta por casos vulneráveis representativos, testes automatizados e execução integrada do _pipeline_. Essa etapa tem como finalidade verificar a viabilidade técnica do fluxo proposto antes de sua aplicação em uma base de código real. No TCC 2, pretende-se evoluir essa abordagem para um projeto público, considerando as vulnerabilidades efetivamente identificadas pela ferramenta SAST selecionada.

Inicialmente, será selecionado um projeto público que possa ser instalado e executado em ambiente local, possua estrutura modular e apresente _issues_ de segurança detectáveis por uma ferramenta SAST compatível com a linguagem. As vulnerabilidades analisadas serão determinadas a partir dos alertas emitidos pela ferramenta SAST sobre o código-fonte do projeto, respeitando critérios de elegibilidade relacionados à possibilidade de reprodução, correção e validação automatizada.

Em seguida, os alertas gerados pela análise estática serão utilizados como entrada para o _pipeline_. Para cada _issue_, serão aplicadas diferentes estratégias de _prompt_, incluindo instrução simples, raciocínio guiado, RAG simplificado e a combinação entre RAG simplificado e raciocínio guiado. O objetivo é verificar se o aumento de contexto e estruturação da tarefa melhora a qualidade das correções propostas pela LLM.

Após a geração das correções, as modificações serão aplicadas em cópias isoladas do projeto e avaliadas por meio de nova execução da ferramenta SAST e da suíte de testes automatizados disponível. Uma correção será considerada válida apenas quando a _issue_ original deixar de ser detectada, os testes continuarem passando e nenhuma nova _issue_ de segurança for introduzida. Os resultados serão consolidados em arquivos estruturados para permitir a comparação entre estratégias de _prompt_, tipos de _issues_ detectadas e limitações observadas durante a aplicação em um projeto.

Dessa forma, a metodologia pretende medir quantitativamente o desempenho da arquitetura proposta, como também compreender em quais condições a combinação entre análise estática, contexto adicional e raciocínio orientado por LLMs se mostra mais eficaz para apoiar tarefas de segurança de software.

### 1.5 Organização do Trabalho

O restante deste trabalho está organizado da seguinte forma: o Capítulo 2 apresenta o referencial teórico que fundamenta a pesquisa; o Capítulo 3 descreve a metodologia proposta para a continuidade do estudo, incluindo o planejamento da coleta e análise dos dados no TCC 2; o Capítulo 4 apresenta a prova de conceito desenvolvida no TCC 1, destacando sua estrutura, execução, métricas e resultados obtidos; por fim, o Capítulo 5 apresenta as considerações finais desta etapa do trabalho.

