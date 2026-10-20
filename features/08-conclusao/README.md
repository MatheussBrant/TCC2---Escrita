---
id: F08
tipo: capitulo
capitulo: 5
destino: Conclusão e trabalhos futuros
saida: manuscrito/08-conclusao
inicio: imediato
fechamento_depende_de: [F06, F07]
---

# F08 — Conclusão e trabalhos futuros

## Objetivo e escopo

Escrever o Capítulo 5 encerrando o argumento da monografia com respostas delimitadas,
contribuições e continuidade. Vínculos: Q1–Q4/OE1–OE4; síntese de C01–C15.
Ler o [contrato](../CONTRATO.md) e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Retomada breve do objetivo e do método, sem repetir a introdução inteira.
2. Resposta explícita a cada Q, admitindo resposta parcial/inconclusiva quando cabível.
3. Contribuições efetivamente demonstradas e grau de atendimento dos objetivos.
4. Limitações centrais que restringem as conclusões.
5. Trabalhos futuros derivados de limitações concretas, distinguindo melhoria
   de implementação, nova avaliação e ampliação de validade externa.

Criar `respostas-qs.md` com Q → resposta proposta → evidência → limite →
conferência com F06/F07. O capítulo apresenta a síntese em prosa, não apenas a tabela.
Não introduzir resultados, referências ou experimentos novos na conclusão.

## Fontes para começar sem outras entregas

- Qs/objetivos/compromissos da matriz do TCC1 e considerações finais do PDF.
- Protocolo, caderno e artefatos da campanha fixada para um rascunho fundamentado.
- A base comum e o contexto para mapear limitações conhecidas sem depender de
  outro agente. Evite uma afirmação de eficácia quando a verificação estiver pendente.

## Entregáveis e paralelismo

Criar `manuscrito/08-conclusao/capitulo.md`, `respostas-qs.md`, `evidencias.md`
e `entrega.md`. Pode começar imediatamente pela estrutura e respostas provisórias
apoiadas nas fontes. O texto só fecha depois de confrontar cada resposta e eventual
número com F06/F07 revisadas; pendências materiais impedem o estado `revisada`.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F08-AC01:** responde separadamente Q1–Q4, com evidência e limite; não
  substitui respostas inconclusivas por afirmações genéricas de sucesso.
- [ ] **F08-AC02:** distingue objetivos cumpridos, parciais e não demonstrados,
  sem equiparar código implementado a eficácia experimental.
- [ ] **F08-AC03:** todas as contribuições declaradas são sustentadas no corpo
  da monografia; a conclusão não introduz fatos ou resultados novos.
- [ ] **F08-AC04:** trabalhos futuros derivam de limitações identificadas, sem
  narrar propostas como tarefas já realizadas.
- [ ] **F08-AC05:** respostas, valores e alcance concordam com F06/F07; a tabela
  `respostas-qs.md` identifica a versão dessas entregas usada na conferência.
- [ ] **F08-AC06:** a síntese mantém os limites do estudo e a distinção entre
  aceite operacional de um reparo e segurança absoluta da aplicação.

## Pedido de execução

Use `tcc2-redigir` para construir a conclusão e a tabela de respostas, mantendo
o estado de rascunho enquanto a reconciliação com F06/F07 estiver pendente.
