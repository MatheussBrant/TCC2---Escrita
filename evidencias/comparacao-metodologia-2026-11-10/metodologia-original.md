## 3 Metodologia

Este capítulo apresenta os procedimentos metodológicos propostos para avaliar a eficácia de um _pipeline_ automatizado de correção de vulnerabilidades em código-fonte com o apoio de Modelos de Linguagem de Grande Escala, ferramentas de Análise Estática de Segurança e estratégias de contextualização.

A pesquisa será conduzida sobre o OWASP Juice Shop, uma aplicação web _open source_ deliberadamente vulnerável e utilizada como referência em treinamentos, demonstrações de segurança e avaliação de ferramentas de segurança. Serão consideradas as vulnerabilidades de segurança efetivamente identificadas por uma ferramenta SAST no projeto selecionado. Essa decisão aproxima o experimento de um cenário prático de desenvolvimento, no qual possui regras de negócio, a arquitetura do sistema precisa ser compreendida e as correções devem respeitar as dependências, os testes e o funcionamento existente da aplicação.

A escolha por este projeto permite avaliar o _pipeline_ em uma aplicação de grande porte, composta por múltiplos módulos, dependências e suíte de testes, proporcionando um cenário mais representativo do que exemplos sintéticos ou casos isolados.

### 3.1 Plano Metodológico

Esta pesquisa é um estudo empírico de natureza aplicada, com abordagem predominantemente quantitativa. Em relação aos objetivos, tem caráter exploratório e avaliativo, pois busca investigar a eficácia de diferentes estratégias de _prompt_ na correção automatizada de vulnerabilidades de segurança. Em relação aos procedimentos, a pesquisa será conduzida como um estudo experimental sobre uma aplicação de referência, na qual um _pipeline_ automatizado será executado repetidas vezes para avaliar o desempenho das estratégias propostas, com base em métricas definidas previamente.

O estudo será conduzido a partir da implementação e avaliação de um _pipeline_ automatizado de correção de vulnerabilidades. Esse _pipeline_ receberá como entrada um projeto com vulnerabilidades identificadas por uma ferramenta SAST, coletará informações sobre as _issues_ encontradas, enriquecerá o contexto fornecido ao modelo de linguagem, solicitará uma correção à LLM, aplicará a modificação gerada e, em seguida, executará novamente a análise estática e os testes automatizados.

O fluxo metodológico geral será composto pelas seguintes etapas:

1. Preparação do ambiente de execução do projeto;

2. _Pipeline_

3. Consolidação dos resultados em um conjunto estruturado de dados;

4. Análise comparativa dos resultados obtidos.


![Figura 1](TCC1___Caio_Lamego_e_Matheus_Brant-11_assets/figura-1.png)

Figura 1 – Visão geral do fluxo metodológico adotado na pesquisa.

**Legenda:** A etapa _Pipeline automatizado de correção_ está detalhada na Figura 2.

A metodologia parte da premissa de que uma correção de vulnerabilidade não deve ser considerada bem-sucedida apenas porque a ferramenta SAST deixou de apontar uma issue. Uma alteração pode remover o alerta sem corrigir a causa real da falha, ou pode eliminar a vulnerabilidade comprometendo a funcionalidade esperada do sistema. Por esse motivo, a avaliação combinará três critérios principais: o desaparecimento da issue na reanálise estática, a aprovação dos testes automatizados após a aplicação da correção e a não introdução de novas issues de segurança.

Assim, uma correção será considerada bem-sucedida apenas quando atender simultaneamente aos critérios de segurança, funcionalidade e não regressão de segurança.

### 3.2 Contexto de aplicação do experimento

O experimento será conduzido sobre o OWASP Juice Shop, uma aplicação web _open source_ deliberadamente vulnerável e mantida no ecossistema da OWASP. A escolha do OWASP Juice Shop como objeto de estudo foi motivada por quatro fatores principais: sua disponibilidade como projeto _open source_, sua adoção pela comunidade de segurança, sua implementação em tecnologias amplamente utilizadas no desenvolvimento web moderno e sua concentração de vulnerabilidades documentadas e associadas ao OWASP Top 10 (OWASP Foundation, 2026a).

A prova de conceito inicial utilizou códigos vulneráveis pequenos e isolados para validar o funcionamento inicial do _pipeline_. No TCC 2, essa abordagem será ampliada para um projeto mais completo, contendo múltiplos arquivos, estrutura modular, testes automatizados e dependências externas. Essa ampliação permitirá avaliar se o _pipeline_ continua funcional em um cenário mais próximo de um projeto real.

Para a correção do código vulnerável será utilizado o modelo `gpt-4.1-mini`. A escolha do modelo `gpt-4.1-mini` foi definida a partir de critérios de viabilidade experimental, custo de execução e adequação ao fluxo automatizado proposto. Como o _pipeline_ realiza múltiplas chamadas à API para diferentes vulnerabilidades e estratégias de _prompt_, o consumo de tokens representa um fator relevante para a condução do estudo. Nesse sentido, a utilização de um modelo menor da família GPT-4.1 permite reduzir o custo das execuções, mantendo recursos importantes para o experimento, como ampla janela de contexto, suporte a saídas estruturadas e capacidade de seguir instruções em tarefas envolvendo código (OPENAI, 2026). Além disso, a implementação do _pipeline_ será parametrizada, permitindo substituir o modelo por versões anteriores ou posteriores em execuções futuras, o que facilita testes comparativos sem alterar a lógica central do experimento.

Além disso, a escolha por um modelo da OpenAI se justifica pela representatividade da família GPT no cenário atual de uso de LLMs. Como o objetivo do trabalho é avaliar um pipeline de reparo automático apoiado por um modelo comercial de uso amplo, optou-se por utilizar uma tecnologia já consolidada entre usuários, desenvolvedores e organizações, em vez de um modelo experimental ou de adoção restrita. Essa escolha aumenta a relevância prática do estudo, pois permite analisar o comportamento de um modelo pertencente à família de LLMs mais difundida no uso cotidiano e profissional. A popularidade do ChatGPT é evidenciada por dados de mercado que o colocam como o site mais acessado na categoria de ferramentas e chatbots de IA, além de relatórios que indicam grande volume de uso semanal e forte presença em ambientes profissionais. No contexto específico de desenvolvimento de software, a pesquisa _Stack Overflow Developer Survey 2025_ também aponta o ChatGPT como uma das ferramentas de IA mais utilizadas por desenvolvedores, sendo citado por 81,7% dos respondentes que utilizam agentes e assistentes de IA. (Similarweb, 2026; Stack Overflow, 2025).

### 3.3 Objeto de estudo: OWASP Juice Shop

O OWASP Juice Shop é implementado principalmente em JavaScript e TypeScript, utilizando Node.js, Express e Angular. Por esse motivo, a metodologia considerará ferramentas, regras SAST, testes e estratégias de correção compatíveis com essas linguagens.

Na versão utilizada nesta pesquisa (v20.1.1), o OWASP Juice Shop reúne 113 desafios distribuídos em 16 categorias de vulnerabilidades, abrangendo problemas como exposição de dados sensíveis, injeção, quebra de controle de acesso, validação imprópria de entrada e _Cross-Site Scripting_ (XSS). Essas categorias são derivadas de padrões amplamente reconhecidos pela comunidade, incluindo o OWASP Top 10, o OWASP ASVS, o OWASP API Security Top 10 e a Common Weakness Enumeration (CWE), tornando a aplicação uma base adequada para pesquisas em segurança de software.

Além dos desafios de exploração, o Juice Shop disponibiliza 33 Coding Challenges, nos quais o usuário localiza o trecho vulnerável do código e identifica a alternativa de correção mais adequada. Embora, nesta pesquisa, as correções sejam geradas automaticamente por um pipeline baseado em LLM, a existência desses desafios evidencia que a aplicação foi projetada para apoiar estudos sobre identificação e remediação de vulnerabilidades, oferecendo um ambiente reprodutível e amplamente documentado para avaliação da abordagem proposta.

### 3.4 Seleção das vulnerabilidades de segurança

A seleção das vulnerabilidades ocorrerá a partir dos alertas produzidos pela ferramenta SAST durante a análise inicial do OWASP Juice Shop. Como a aplicação é deliberadamente vulnerável, espera-se que parte dos alertas esteja relacionada a falhas conhecidas ou compatíveis com categorias do OWASP Top 10. Dessa forma, o conjunto de vulnerabilidades analisado será composto pelos alertas efetivamente identificados pela ferramenta SAST durante a execução inicial do _pipeline_.

Após a execução inicial da ferramenta SAST, as vulnerabilidades detectadas serão submetidas ao _pipeline_ de correção. Para cada _issue_ identificada, serão aplicadas as diferentes estratégias de _prompt_ propostas neste trabalho, permitindo avaliar o desempenho da LLM na remediação de diferentes tipos de vulnerabilidades presentes na aplicação.

Embora o OWASP Juice Shop contemple vulnerabilidades associadas ao OWASP Top 10, o experimento não partirá da seleção manual de categorias específicas. As tentativas de correção serão realizadas sobre todos os alertas produzidos pela ferramenta SAST. Sempre que a ferramenta fornecer mapeamentos para CWE, OWASP ou outras regras de segurança, essas informações serão registradas e utilizadas posteriormente na análise dos resultados.

As vulnerabilidades identificadas serão documentadas em um arquivo de metadados contendo:

1. identificador da _issue_;

2. ferramenta SAST responsável pela detecção;

3. regra acionada;

4. severidade;

5. arquivo e linha afetados;

6. mensagem da ferramenta;

7. CWE ou categoria OWASP associada, quando disponível;

8. trecho de código relacionado;

9. estratégia de validação utilizada após a correção.

### 3.5 Ferramenta de análise estática

A análise estática será utilizada para identificar vulnerabilidades antes e depois da aplicação das correções. A ferramenta SAST será responsável por produzir os diagnósticos iniciais que servirão como entrada para o _pipeline_, além de permitir a verificação posterior do desaparecimento das _issues_.

Na prova de conceito, verificou-se a necessidade de avaliar a adequação da ferramenta SAST ao contexto Python e aos tipos de vulnerabilidade analisados. Por isso, no TCC 2, a escolha da ferramenta considerará a capacidade real de detectar as vulnerabilidades. Será utilizada a ferramenta Semgrep como ferramenta SAST principal, por oferecer suporte a JavaScript e TypeScript, além de permitir a exportação dos resultados em formato JSON para integração com o _pipeline_.

Para cada execução da análise estática, serão coletados os seguintes dados:

1. Identificador da issue;

2. Ferramenta utilizada;

3. Regra acionada;

4. Severidade;

5. Arquivo e linha afetados;

6. Mensagem da ferramenta;

7. Categoria CWE ou OWASP, quando disponível;

8. Trecho de código relacionado;

9. Data e identificador da execução.

A análise estática inicial será executada antes da chamada à LLM. Em seguida, após a aplicação da correção gerada, a ferramenta será executada novamente para verificar se a _issue_ original deixou de ser detectada e se novas _issues_ foram introduzidas.

### 3.6 Estratégias de prompt

O experimento avaliará diferentes estratégias de _prompt_ para verificar como a formulação da instrução influencia a qualidade das correções geradas. A comparação entre _prompts_ é essencial para observar se estratégias mais estruturadas, com contexto adicional e raciocínio guiado, produzem correções melhores do que instruções simples. Serão avaliadas, inicialmente, quatro estratégias.

A primeira será o **_prompt_ simples**, no qual o modelo recebe o trecho de código do OWASP Juice Shop associado ao alerta SAST e uma instrução direta para identificar e corrigir a vulnerabilidade.

A segunda será o **_prompt_ com raciocínio guiado**, inspirado na ideia de _Chainof-Thought_ discutida no referencial teórico. Neste trabalho, essa estratégia não será utilizada como forma de acessar ou validar o raciocínio interno do modelo, mas como uma maneira de estruturar a tarefa em etapas explícitas. Assim, o modelo será orientado a identificar a vulnerabilidade, explicar sua causa, descrever o impacto, propor uma correção, justificar a alteração e indicar possíveis cuidados adicionais.

A terceira será o **_prompt_ com RAG simplificado**, no qual o modelo recebe, além do código e do alerta SAST, um documento de contexto recuperado automaticamente a partir da categoria da vulnerabilidade identificada.

A quarta será o **_prompt_ com RAG simplificado e raciocínio guiado**, combinando o contexto técnico recuperado com uma estrutura de resposta em etapas.

Para permitir integração automática com o pipeline, as respostas da LLM serão solicitadas em formato estruturado JSON. O formato esperado deverá conter campos:

1. Vulnerabilidade identificada;

2. Causa da vulnerabilidade;

3. Estratégia de correção;

4. Código corrigido ou _patch_;

5. Justificativa técnica;

6. Observações sobre possíveis limitações da correção.

A padronização da saída é necessária para que o _pipeline_ consiga extrair automaticamente o código corrigido, aplicar a alteração e registrar os dados da execução.

### 3.7 Estratégia de RAG simplificado

Neste trabalho, o RAG será implementado de forma simplificada, por meio da recuperação automática de documentos de contexto associados à categoria da vulnerabilidade identificada pela ferramenta SAST. Diferentemente de arquiteturas RAG completas baseadas em _embeddings_, bancos vetoriais e mecanismos de ranqueamento semântico, a abordagem proposta utilizará uma base documental controlada e indexada por categorias de vulnerabilidade.

Essa decisão metodológica foi adotada por questões de viabilidade e alinhamento com o escopo do trabalho. O objetivo da pesquisa não é desenvolver uma arquitetura de RAG sofisticada, mas avaliar se a inclusão de contexto técnico adicional no _prompt_ contribui para melhorar a qualidade das correções geradas pela LLM. Assim, a recuperação será baseada em um mapeamento direto entre o tipo de vulnerabilidade identificado e o documento de apoio correspondente.

A base de conhecimento será composta por arquivos em formato _Markdown_, organizados em uma pasta específica do projeto. Cada arquivo conterá informações técnicas sobre uma categoria de vulnerabilidade, incluindo descrição da falha, classificação OWASP, CWE relacionada, formas comuns de exploração, recomendações de mitigação e exemplos de código vulnerável e corrigido.

A estrutura inicial da base poderá seguir o seguinte formato, podendo ser ajustada:

```
contextos_rag/
  injection.md
  broken_access_control.md
  cryptographic_failures.md
  authentication_failures.md
  security_misconfiguration.md
  cross_site_scripting.md
  vulnerable_components.md
```

Cada documento de contexto poderá conter os seguintes elementos:

1. Nome da vulnerabilidade;

2. Categoria OWASP relacionada;

3. CWE associada, quando aplicável;

4. Descrição da vulnerabilidade;

5. Causa comum da falha;

6. Impacto de segurança;

7. Recomendações de correção;

8. Cuidados específicos em JavaScript, TypeScript, Node.js, Express ou Angular, quando aplicável;

9. Exemplo de código vulnerável;

10. Exemplo de código corrigido.

Durante a execução do _pipeline_, a ferramenta SAST identificará uma _issue_ de segurança. Em seguida, o _pipeline_ fará a associação dessa _issue_ com uma categoria conhecida de vulnerabilidade. A partir dessa associação, será selecionado automaticamente o documento de contexto correspondente.

Por exemplo, caso a _issue_ esteja relacionada a _SQL Injection_, o _pipeline_ recuperará o arquivo `sql_injection.md`. Esse conteúdo será então incorporado ao prompt enviado à LLM, juntamente com o código vulnerável e o alerta produzido pela ferramenta SAST.

O fluxo do RAG simplificado será composto pelas seguintes etapas:

1. Identificação da _issue_ pela ferramenta SAST;

2. Classificação da _issue_ em uma categoria de vulnerabilidade;

3. Seleção automática do arquivo de contexto correspondente;

4. Leitura do conteúdo do arquivo Markdown;

5. Inclusão do contexto recuperado no prompt;

6. Envio do prompt enriquecido para a LLM;

7. Geração da correção.

Essa estratégia permite comparar a correção gerada sem contexto adicional com a correção gerada a partir de um _prompt_ enriquecido. Dessa forma, será possível avaliar se a presença de um contexto técnico direcionado melhora a capacidade da LLM de identificar a causa da vulnerabilidade, propor uma correção adequada e preservar a funcionalidade original do sistema.

Embora essa abordagem não implemente todos os elementos de uma arquitetura RAG completa, ela mantém o princípio central da técnica: recuperar conhecimento externo relevante antes da geração da resposta. Por isso, neste trabalho, a estratégia será denominada RAG simplificado ou contextualização baseada em recuperação por categoria.

### 3.8 Pipeline

O _pipeline_ será implementado por meio de scripts responsáveis por orquestrar todas as etapas do experimento. A execução automatizada terá como objetivo reduzir intervenção manual, padronizar a coleta de dados e permitir a repetição dos experimentos.

O fluxo do pipeline será composto pelas seguintes etapas:

1. Executar a análise SAST inicial no projeto;

2. Filtrar vulnerabilidades de segurança relevantes para o experimento;

3. Coletar o trecho de código associado à vulnerabilidades;

4. Classificar a vulnerabilidades de acordo com a categoria de vulnerabilidade;

5. Recuperar o contexto correspondente, quando a estratégia testada utilizar RAG simplificado;

6. Montar o prompt de acordo com a estratégia experimental selecionada;

7. Enviar a requisição à API da LLM;

8. Receber e validar a resposta estruturada;

9. Aplicar a correção proposta em uma cópia isolada do projeto;

10. Executar novamente a análise SAST;

11. Executar a suíte de testes automatizados;

12. Registrar os resultados da tentativa de correção;

13. Restaurar o estado do projeto para a próxima execução.

![Figura 2](TCC1___Caio_Lamego_e_Matheus_Brant-11_assets/figura-2.png)

Figura 2 – Fluxo de correção de uma única vulnerabilidade, executado em paralelo para diferentes vulnerabilidades e com tentativas progressivas por estratégias de prompt. **Legenda:** P1 = prompt simples; P2 = prompt com raciocínio guiado; P3 = prompt com RAG simplificado; P4 = prompt com RAG simplificado combinado ao raciocínio guiado.

A Figura 2 representa o processamento de uma única vulnerabilidade por instância do pipeline. Após a análise SAST inicial identificar as vulnerabilidades elegíveis no projeto, uma instância independente desse fluxo é criada para cada uma delas. Essas instâncias são executadas em paralelo sobre cópias isoladas do projeto, evitando que as alterações realizadas durante a correção de uma vulnerabilidade interfiram nas demais.

Em cada instância, o pipeline seleciona uma estratégia de prompt, seguindo a ordem P1, P2, P3 e P4. Para cada tentativa, o prompt é montado, enviado à LLM e a correção gerada é aplicada ao código. Após essa etapa, são executados os testes automatizados e uma nova análise SAST. A correção é considerada válida apenas quando a vulnerabilidade deixa de ser detectada, os testes continuam passando e nenhuma nova issue de segurança é introduzida. Caso esses critérios não sejam atendidos, o pipeline avança para a próxima estratégia de prompt; se todas as estratégias forem esgotadas, a tentativa é registrada como falha.

Para reduzir o tempo total de execução, as chamadas à API da LLM associadas a vulnerabilidades distintas poderão ser realizadas em paralelo. Essa paralelização será aplicada de forma controlada, respeitando os limites de taxa da API e garantindo que cada instância opere em uma cópia isolada do projeto ou em um ambiente temporário independente. Dentro de uma mesma instância, entretanto, as estratégias de prompt permanecerão sequenciais, pois a próxima estratégia somente será utilizada quando a anterior não produzir uma correção válida.

### 3.9 Métricas de avaliação

As métricas foram definidas para avaliar as tentativas de correção sob três perspectivas: remoção do alerta de segurança, preservação funcional e não introdução de novas vulnerabilidades. Como o estudo será conduzido sobre uma aplicação deliberadamente vulnerável, haverá referências conhecidas sobre parte das falhas existentes. Entretanto, a avaliação do _pipeline_ será baseada nos alertas efetivamente identificados pela ferramenta SAST, na reanálise após a correção, nos testes automatizados e, quando necessário, na inspeção manual.

Para cada tentativa de correção submetida ao _pipeline_, serão definidas três variáveis binárias:

- _𝑅𝑗_: resultado da reanálise estática. Assume valor 1 se a vulnerabilidade original deixou de ser detectada após a correção, e 0 caso contrário.

- _𝐹𝑗_: resultado dos testes automatizados. Assume valor 1 se os testes do projeto passaram após a correção, e 0 caso contrário.

- _𝑀𝑗_: introdução de novas vulnerabilidades. Assume valor 1 se nenhuma nova _issue_ de segurança foi introduzida após a correção, e 0 caso contrário.

A métrica principal será a Taxa de Remediação Validada (TRV), calculada da seguinte forma:


$$
\mathrm{TRV} = \frac{\sum_{j=1}^{m}(R_j \times F_j \times M_j)}{m}
$$

Nessa fórmula, _𝑚_ representa o número total de tentativas de correção realizadas no projeto. O uso da multiplicação garante que uma tentativa só seja considerada uma remediação validada quando os três critérios forem satisfeitos simultaneamente: a vulnerabilidade original deixou de ser detectada, os testes continuaram passando e nenhuma nova vulnerabilidade de segurança foi introduzida.

Também serão calculadas métricas complementares. A Taxa de Remoção de _Issues_ (TRI) indicará a proporção de tentativas em que a _issue_ original deixou de ser detectada:

$$
\mathrm{TRI} = \frac{\sum_{j=1}^{m} R_j}{m}
$$

A Taxa de Preservação Funcional (TPF) indicará a proporção de tentativas em que os testes automatizados passaram após a correção:


$$
\mathrm{TPF} = \frac{\sum_{j=1}^{m} F_j}{m}
$$

A Taxa de Não Introdução de Novas _Issues_ (TNINI) indicará a proporção de tentativas em que nenhuma nova _issue_ de segurança foi introduzida:


$$
\mathrm{TNINI} = \frac{\sum_{j=1}^{m} M_j}{m}
$$

A Taxa de Falha Funcional (TFF) indicará a proporção de tentativas em que a correção comprometeu os testes automatizados:


$$
\mathrm{TFF} = 1 - \mathrm{TPF}
$$

Além dessas métricas por tentativa, será calculada a Redução Relativa de _Issues_ de Segurança (RRIS), considerando apenas as correções aceitas como válidas:


$$
\mathrm{RRIS} = \frac{I_{\text{antes}} - I_{\text{depois}}}{I_{\text{antes}}}
$$

Nessa fórmula, _𝐼_ antes representa o número de _issues_ de segurança detectadas antes da aplicação das correções aceitas, enquanto _𝐼_ depois representa o número de _issues_ de segurança detectadas após essas correções. Essa métrica indica a redução percentual de alertas de segurança no projeto.

A RRIS será interpretada com cautela, pois a redução de _issues_ na ferramenta SAST não garante, isoladamente, que todas as vulnerabilidades foram corretamente corrigidas. Por esse motivo, ela será analisada em conjunto com a execução dos testes automatizados e, quando necessário, com inspeção manual de uma amostra das correções geradas.

Essas métricas permitirão comparar o desempenho das diferentes estratégias de _prompt_ no projeto. Dessa forma, será possível observar se prompts com raciocínio guiado, prompts com RAG simplificado e prompts com RAG simplificado combinado ao raciocínio guiado apresentam maior taxa de remediação validada em comparação com prompts simples.

### 3.10 Armazenamento e organização dos dados

Todos os resultados serão armazenados em uma estrutura padronizada de diretórios e arquivos. Cada execução do pipeline produzirá um registro contendo os dados da vulnerabilidade, o prompt utilizado, a resposta da LLM, o código corrigido, os resultados da reanálise SAST e os resultados dos testes automatizados.

A estrutura de armazenamento seguirá o modelo:

```
outputs/
sast_antes/
  sast_depois/
prompts/
respostas_llm/
  codigos_corrigidos/
testes/
metricas/
resultados_consolidados/
```

Cada tentativa de correção receberá um identificador único, utilizado para nomear os artefatos gerados durante a execução do _pipeline_. Esse identificador foi definido de forma padronizada para facilitar a rastreabilidade dos resultados, permitindo identificar, a partir do próprio nome do arquivo, o caso analisado, a categoria do OWASP Top 10, o tipo de vulnerabilidade, a estratégia de _prompt_, o número da execução e o tipo de artefato produzido.


![Figura 3](TCC1___Caio_Lamego_e_Matheus_Brant-11_assets/figura-3.png)

Figura 3 – Estrutura do identificador utilizado na nomenclatura dos artefatos gerados pelo _pipeline_.

Esse identificador permitirá rastrear cada resultado desde o alerta inicial até a correção final. Também permitirá comparar tentativas diferentes para a mesma vulnerabilidade, realizadas com estratégias de _prompt_ distintas.

Os resultados consolidados serão armazenados em formato CSV, contendo os campos:

1. identificador da execução;

2. projeto analisado;

3. vulnerabilidade;

4. categoria OWASP;

5. CWE;

6. ferramenta SAST;

7. estratégia de prompt;

8. uso de RAG simplificado;

9. modelo utilizado;

10. _issue_ detectada antes da correção;

11. _issue_ detectada depois da correção;

12. resultado dos testes;

13. novas _issues_ introduzidas;

14. tempo de execução;

15. classificação final da tentativa.

Essa organização garante rastreabilidade e facilita a posterior geração de tabelas, gráficos e análises comparativas.

### 3.11 Análise dos dados

A análise dos dados será realizada a partir da comparação entre as estratégias de prompt e os tipos de vulnerabilidade. Inicialmente, será calculada a Taxa de Remediação Validada para cada estratégia de _prompt_ utilizada.

A análise buscará responder às perguntas de pesquisa definidas no Capítulo 1, observando principalmente:

1. Se o _pipeline_ consegue corrigir vulnerabilidades reais identificadas por SAST sem quebrar os testes;

2. Se prompts com raciocínio guiado apresentam melhor desempenho do que prompts simples;

3. Se o uso de RAG simplificado melhora a taxa de remediação validada;

4. Se a combinação entre RAG simplificado e raciocínio guiado apresenta melhor desempenho que as estratégias isoladas;

5. Quais tipos de vulnerabilidades ou regras SAST apresentam maior dificuldade de correção;

6. Quais limitações práticas surgem ao aplicar o _pipeline_ em um projeto _open source_.

### 3.12 Limitações do estudo

Apesar do cuidado metodológico, este estudo apresenta limitações. A primeira delas diz respeito à ferramenta SAST. Ferramentas de análise estática podem gerar falsos positivos e falsos negativos. Nesta pesquisa, não será realizada uma etapa prévia para identificar ou eliminar possíveis falsos positivos. Assim, todas as _issues_ detectadas pela ferramenta serão submetidas ao _pipeline_ de correção. Consequentemente, o desaparecimento de uma _issue_ após a execução do _pipeline_ não garante, de forma absoluta, que uma vulnerabilidade real tenha sido corrigida, pois o alerta original pode não corresponder a uma falha efetiva. Por esse motivo, os resultados serão analisados em conjunto com a reanálise SAST, a execução dos testes automatizados e, quando necessário, por meio de inspeção manual.

A segunda limitação está relacionada ao comportamento não determinístico das LLMs. Mesmo utilizando o mesmo prompt, o modelo pode gerar respostas diferentes dependendo dos parâmetros da chamada, da versão do modelo e das condições da API. Para reduzir essa variabilidade, os parâmetros de execução serão registrados e, sempre que possível, mantidos constantes.

A terceira limitação está relacionada ao próprio RAG simplificado. Como a recuperação será feita por categoria de vulnerabilidade, e não por similaridade semântica em uma base vetorial, o método pode recuperar documentos menos específicos em alguns casos. Entretanto, essa escolha é adequada ao escopo do trabalho, pois permite avaliar de forma controlada o efeito do contexto técnico adicional sem transformar a implementação do RAG no foco principal da pesquisa.Ma

A quarta limitação refere-se à utilização de uma única aplicação como objeto de estudo. Embora o OWASP Juice Shop seja uma aplicação amplamente utilizada em pesquisas e treinamentos de segurança, os resultados obtidos refletem o comportamento do _pipeline_ nesse contexto específico. Projetos desenvolvidos com outras linguagens, arquiteturas, frameworks ou práticas de desenvolvimento podem apresentar características distintas, influenciando tanto a detecção das _issues_ quanto a qualidade das correções geradas pela LLM. Dessa forma, os resultados deste trabalho não devem ser generalizados para todos os projetos de software, mas interpretados como uma avaliação da abordagem proposta em um cenário representativo.

### 3.13 Declaração de Uso de Inteligência Artificial

Durante a elaboração deste trabalho, foram utilizadas ferramentas de inteligência artificial generativa como apoio em etapas do processo de escrita e organização do conteúdo. Essas ferramentas auxiliaram, principalmente, na revisão de trechos do texto, na melhoria da clareza de determinadas explicações, na estruturação de ideias, na elaboração de exemplos de código e na organização de diagramas e tabelas.

O uso dessas ferramentas não substituiu o trabalho dos autores. As decisões sobre o tema, a metodologia, os experimentos, as interpretações e a versão final do texto foram realizadas pelos autores. Todo conteúdo gerado com auxílio de inteligência artificial foi revisado, ajustado e validado antes de ser incorporado ao trabalho.

Dessa forma, a inteligência artificial foi utilizada apenas como ferramenta de apoio, enquanto a responsabilidade pelo conteúdo final, pelas escolhas metodológicas e pelas conclusões apresentadas são de responsabilidade integral dos autores.

### 3.14 Cronograma

As principais atividades previstas para o desenvolvimento do TCC 2 são apresentadas na Tabela 1. O cronograma contempla desde a preparação do ambiente experimental utilizando o OWASP Juice Shop até a análise dos resultados e a redação final do trabalho.

**Tabela 1 – Cronograma previsto para o desenvolvimento do TCC 2**

|**Atividade**|**Período previsto**|
|---|---|
|Preparação do ambiente experimental com o OWASP<br>Juice Shop|Agosto de 2026|
|Estudo do código-fonte e identificação das<br>vulnerabilidades elegíveis|Agosto de 2026|
|Execução inicial do SAST e catalogação das _issues_|Agosto – Setembro de<br>2026|
|Implementação e ajustes do _pipeline_ automatizado|Setembro de 2026|
|Implementação do RAG simplificado|Setembro de 2026|
|Paralelização das chamadas à API da LLM|Setembro – Outubro de<br>2026|
|Definição e refinamento das estratégias de _prompt_|Outubro de 2026|
|Execução do _pipeline_ sobre as vulnerabilidades<br>selecionadas|Outubro – Novembro de<br>2026|
|Coleta e consolidação das métricas experimentais|Novembro de 2026|
|Análise dos resultados e discussão dos achados|Novembro – Dezembro de<br>2026|
|Escrita, revisão e preparação da versão final do TCC|Dezembro de 2026|

