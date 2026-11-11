---
name: tcc2-redigir
description: Redige ou revisa seções da monografia em manuscrito/, seguindo os planos e critérios de escrita, com fontes verificadas, notas de evidência e lacunas explícitas.
---

# Redigir uma seção sustentada por evidências

Leia os [critérios de escrita](../../../docs/criterios-escrita.md), as
[diretrizes](../../../docs/diretrizes-escrita.md), o plano de parágrafos do capítulo
(`docs/plano-paragrafos-capitulo-N.md`, quando existir) e as notas de evidência do
capítulo (`evidencias/capitulo-N-notas.md`). Confira no
[índice do manuscrito](../../../manuscrito/README.md) qual arquivo é o capítulo atual;
os arquivos históricos ali listados não recebem texto novo.

O texto apresenta uma única pesquisa: não mencione TCC1 ou TCC2. Use a proposta
original apenas como referência de linguagem e de compromissos. Descreva no passado
o que foi executado e no presente as definições.

Defina a seção, seu argumento e as perguntas (Q1–Q5) que ela atende. Reúna as fontes
antes de escrever afirmações factuais: a proposta original para o que foi prometido,
o código na revisão citada para a implementação, o protocolo e o caderno de
laboratório do experimento para o método executado, e os dados auditados para os
resultados. Localize o experimento conforme o `AGENTS.md`. Use as skills de
histórico, resultados ou bibliografia só quando a evidência ainda não estiver nas notas.

Escreva em português acadêmico claro: problema, decisão, funcionamento, evidência
e implicação, conforme a seção, sem transformar o capítulo em um changelog.
Preserve a terminologia: issue/alerta SAST, ocorrência, caso, tentativa, execução e
desafio não são sinônimos. Raciocínio guiado é uma estrutura pedida na resposta, não
observação do raciocínio interno do modelo.

Para cada afirmação empírica importante, deixe uma nota de trabalho como
`<!-- Evidência: experimento@SHA; caminho; execução; Q1 -->` e registre a fonte nas
notas do capítulo. Tabelas de taxas exigem numerador e denominador, população,
definição de F e política. Use `[PENDENTE: fonte ou decisão específica]` quando
faltar evidência, sem preencher com dados plausíveis. Não generalize resultados do
Juice Shop para software em geral. Referências acadêmicas exigem metadados
conferidos; um hash Git não substitui literatura científica.

Ao terminar, atualize as notas de evidência do capítulo e, se o estado mudar, a
tabela do índice do manuscrito. Com LaTeX, preserve estrutura, labels e chaves
bibliográficas; não invente normas ABNT nem estilos da UnB a partir do PDF.

Entregue o texto, a trilha de fontes e as pendências precisas. Não marque
"revisado pelos autores" nem "aprovado pela orientadora" sem evidência. A declaração
de uso de IA deve refletir o trabalho efetivo e a responsabilidade dos autores.
