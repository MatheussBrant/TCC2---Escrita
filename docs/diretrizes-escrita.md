# Diretrizes para iniciar a escrita do TCC2

Registro das ideias dos autores e de uma proposta de organização, elaborado em
07/11/2026. Este arquivo orienta a redação; não constitui um capítulo nem comprova
resultados experimentais.

## Diretrizes informadas pelo autor

- O TCC2 será construído a partir do TCC1, preservando a continuidade do trabalho.
- O capítulo 3 deverá descrever o que foi efetivamente realizado, usando o passado
  para os procedimentos executados e explicando as escolhas e suas justificativas.
- A descrição deverá abranger a construção do pipeline, as tecnologias utilizadas
  e o percurso até a obtenção dos resultados finais.
- Um capítulo 4 deverá apresentar a implementação com maior detalhe técnico,
  incluindo a organização dos diretórios e a função dos componentes.
- O capítulo 5 deverá apresentar e interpretar os resultados e responder às
  perguntas de pesquisa definidas no TCC1.

## Linguagem definida para todos os planos

O autor definiu que a escrita deve ser acadêmica, objetiva e explicativa,
próxima à linguagem do TCC1. As explicações devem desenvolver as ideias com
clareza, apresentando os termos necessários sem aprofundamento técnico excessivo.

Essa orientação também delimita o capítulo 4: o maior detalhe da implementação
consiste em explicar como as partes funcionam e se conectam. Classes, funções,
comandos e formatos completos de dados só entram quando ajudam a compreender
uma decisão; detalhes extensos podem ser consultados em apêndices.

Os [critérios de escrita](criterios-escrita.md) orientam os três planos:

- [Capítulo 3 — Metodologia](plano-paragrafos-capitulo-3.md).
- [Capítulo 4 — Implementação](plano-paragrafos-capitulo-4.md).
- [Capítulo 5 — Resultados e discussão](plano-paragrafos-capitulo-5.md).

As orientações de todos os parágrafos foram simplificadas, mantendo seus IDs e
os assuntos previstos. A quantidade é uma referência de organização, não uma
exigência de extensão: parágrafos podem ser unidos ou divididos para melhorar
a leitura. As evidências permanecem como apoio de trabalho para sustentar a
redação, sem exigir sua descrição integral no corpo da monografia.

Essa orientação substitui a proposta anterior de agrupar metodologia e
desenvolvimento em um único capítulo e resultados e discussão no capítulo 4.
Os arquivos de organização anteriores estão ausentes na árvore de trabalho
consultada; não foram restaurados.

## Ampliação aceita: comparação entre modelos

O autor aceitou acrescentar a comparação entre modelos como eixo do TCC2,
preservando Q1–Q4 e incluindo a seguinte pergunta:

> **Q5:** Como diferentes modelos de linguagem se comparam na geração de
> correções válidas pelo pipeline, considerando eficácia, custo e tempo de execução?

Objetivo específico correspondente: comparar diferentes modelos de linguagem na
geração de correções válidas pelo pipeline, considerando eficácia, custo e tempo
de execução nas condições avaliadas.

Modelos das campanhas finais consultadas: GPT-4.1 mini, GPT-5.6 Luna e GPT-6 Luna.
O capítulo 3 terá uma seção própria de modelos e parâmetros de geração e explicará
o procedimento de comparação. O capítulo 5 terá uma seção de comparação dos
modelos e responderá explicitamente a Q5, além de Q1–Q4.

Comparar taxas por tentativa e aceites por caso, preservação funcional, novos
alertas, custos conhecidos e tempos. Declarar as condições compartilhadas e as
diferenças de parâmetros, distinguir latência de geração de tempo total e
considerar a seleção sequencial das estratégias. Não tratar a comparação como
avaliação de superioridade geral dos modelos.

A decisão foi aceita pelo autor na conversa. O alinhamento com a orientadora
permanece a realizar; não há registro de aprovação acadêmica nesta decisão.

## Proposta de sumário para desenvolver com os autores

Os capítulos 3–5 abaixo seguem a divisão solicitada. A manutenção dos capítulos
1–2 e o capítulo 6 de conclusão são propostas de organização a confirmar durante
o refinamento do sumário.

### 1. Introdução

Partir da introdução do TCC1. Preservar problema, objetivo geral, objetivos
específicos e perguntas Q1–Q4, acrescentando Q5 e o objetivo de comparar modelos,
conforme a ampliação aceita. Conferir a coerência com o estudo realizado.
Atualizar a apresentação da contribuição e a organização do documento.

### 2. Referencial teórico e trabalhos relacionados

Aproveitar a fundamentação do TCC1, revisar as referências e acrescentar conceitos
necessários à compreensão do experimento. Ainda será definida a posição da PoC
Python/Bandit: síntese como etapa preliminar ou apresentação em apêndice, conforme
a orientação acadêmica recebida.

### 3. Metodologia

Explicar o desenho do estudo e o procedimento experimental, incluindo as decisões
que determinam o significado dos resultados.

Possíveis seções:

1. Caracterização da pesquisa, perguntas e visão geral do experimento.
2. Objeto de estudo: Juice Shop, versão, commit e delimitação do escopo.
3. Ferramenta SAST, regras utilizadas e constituição do catálogo de alertas.
4. Modelos, parâmetros e estratégias P1–P4, incluindo o RAG simplificado.
5. Procedimento por caso, isolamento, sequência de estratégias e regra de parada.
6. Validação: R, F, M, baseline, conjunto D e tratamento de indeterminações.
7. Campanhas selecionadas, métricas, denominadores e plano de análise.
8. Limitações metodológicas e declaração do uso de IA.

A troca de tempo verbal exige conferência factual: propostas não executadas
devem ser identificadas; mudanças em relação ao TCC1 devem ser explicadas.
Definições e propriedades atuais podem permanecer no presente.

### 4. Desenvolvimento e implementação do pipeline

Explicar como o método foi concretizado em software e como os componentes se
conectam. A organização de diretórios serve de apoio à explicação da arquitetura.

Possíveis seções:

1. Requisitos do pipeline e decisões de arquitetura.
2. Visão geral em dutos e filtros e fluxo dos artefatos.
3. Tecnologias, dependências, ambiente Docker e configuração.
4. Organização do repositório e responsabilidades dos diretórios principais.
5. Etapas: SAST, catálogo, recuperação, prompts, geração e aplicação de patches.
6. Implementação da validação e consolidação das métricas.
7. Orquestração, worktrees, execução concorrente, interface e retomada.
8. Rastreabilidade e dificuldades técnicas relevantes, com suas soluções.

Não é necessário descrever cada arquivo. Selecionar componentes que expliquem o
funcionamento, as decisões e a reprodução do experimento. Conferir comportamento
e caminhos no código utilizado pelas campanhas descritas.

### 5. Resultados e discussão

Apresentar os resultados das campanhas selecionadas e interpretar o que eles
permitem concluir em relação às perguntas de pesquisa.

Possíveis seções:

1. Caracterização dos casos, campanhas e tentativas analisadas.
2. Resultados gerais: aceites por caso e métricas por tentativa.
3. Comparação descritiva das estratégias de prompt.
4. Comparação dos modelos nas condições observadas.
5. Resultados por tipo de vulnerabilidade, regra e categoria OWASP.
6. Exemplos de correções aceitas e falhas, com análise do código.
7. RRIS e limitações da aplicação conjunta dos patches.
8. Respostas explícitas a Q1–Q5, ameaças à validade e discussão com a literatura.

Cuidados para a análise:

- Separar alertas de vulnerabilidades demonstradas. As classificações da triagem
  arquivada não devem ser apresentadas como revisão humana comprovada sem fonte.
- Declarar a definição de F e os denominadores de cada métrica.
- Considerar a seleção sequencial: P2–P4 recebem os casos sem aceite anterior.
- P3/P4 adicionam diagnóstico SAST e documentos; não atribuir toda diferença ao
  efeito isolado do RAG.
- Distinguir validação individual de patches e validação de sua aplicação conjunta.
- Resultados de execuções diferentes exigem identificação de ambiente e contrato.

### 6. Conclusão e trabalhos futuros — sugestão

Retomar o objetivo, sintetizar as respostas sustentadas, explicitar contribuições
e limitações e propor trabalhos futuros. A discussão detalhada fica no capítulo 5.

## Próximo passo

O primeiro rascunho completo do [capítulo 3](../manuscrito/03-metodologia.md)
foi elaborado seguindo o plano por parágrafos e os critérios de linguagem.
As [notas de evidência](../evidencias/capitulo-3-notas.md) registram fontes,
mudanças em relação ao TCC1 e pendências para os autores. O próximo passo é
revisar esse texto e esclarecer as pendências, antes de fechar a metodologia.
O [capítulo 4](../manuscrito/04-implementacao.md) também recebeu um primeiro
rascunho completo, com [notas de evidência](../evidencias/capitulo-4-notas.md).
Sua revisão inclui a inserção de capturas reais do painel e a integração das
figuras ao documento final. Os resultados permanecem com seu plano de redação.

Ainda precisam ser definidos: destino da PoC, título final dos capítulos,
template, prazo, eventual limite de páginas e recorte experimental final.
