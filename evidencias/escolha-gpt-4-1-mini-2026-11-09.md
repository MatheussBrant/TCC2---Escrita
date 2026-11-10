# Ampliação da justificativa do GPT-4.1 mini — 09/11/2026

Solicitação do autor: desenvolver melhor a justificativa de uso do GPT-4.1 mini
na seção 3.4. Foram acrescentados dois parágrafos, preservando a justificativa
existente dos Luna e a decisão operacional de uso da API OpenAI.

## Argumentos e fontes

| Argumento | Fonte | Alcance |
|---|---|---|
| Viabilidade experimental e custo de múltiplas gerações | Texto de planejamento preservado no Markdown completo de referência, seção de contexto do experimento | Justificativa já expressa, recuperada sem mencionar entregas anteriores no texto acadêmico. Não foi alegado que o mini fosse o mais barato entre os três modelos finais. |
| Papel de referência já integrado e com registros exploratórios | `docs/historico/features/10-comparacao-modelos-openai/README.md`, decisão de 02/11/2026, seções 1 e 3; `docs/protocolo_experimental.md`, seção 9 | Fundamenta a manutenção do modelo, sem agregar resultados históricos aos finais nem usar a eficácia posterior como motivo inicial. |
| Contexto e saídas estruturadas | [Documentação oficial do GPT-4.1 mini](https://developers.openai.com/api/docs/models/gpt-4.1-mini), pesquisada e aberta em 09/11/2026 | A página informa contexto de 1.047.576 tokens e suporte a Structured Outputs. O texto utiliza a descrição qualitativa, sem afirmar que o experimento explorou toda a janela. |
| Relevância do JSON para a integração | `src/pipeline/etapas/e05_geracao_llm/esquema.py` e `cliente_openai.py` | O cliente solicita JSON Schema estrito e o esquema prevê campos descritivos e lista de edições. Isso facilita processamento, não comprova correção do conteúdo. |

O repositório experimental permanece no SHA
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`. Não foram executadas chamadas,
scans ou testes, nem alterados modelos, parâmetros, resultados ou preços.

## Limites da justificativa

- Critérios de escolha e requisitos técnicos foram separados dos resultados
  comparativos, que permanecem no capítulo 5.
- Não se atribuiu ao GPT-4.1 mini maior popularidade, superioridade em segurança
  ou menor custo que os Luna sem evidência correspondente.
- A documentação oficial atual foi usada para conferir os recursos técnicos;
  não foi apresentada como um snapshot da página no momento da decisão original.
- O status atual de disponibilidade do modelo não foi usado para reescrever a
  escolha histórica nem para recomendar uma seleção nova.
- A referência OpenAI (2026) já consta de `manuscrito/referencias.md`.

As alterações se limitam à justificativa na seção 3.4 e a esta nota. Os demais
trechos do manuscrito, inclusive as correções de triagem e de caracterização do
Juice Shop feitas anteriormente, foram preservados.

## Complemento — explicação dos parâmetros

A pedido do autor, os parágrafos de parâmetros da seção 3.4 foram ajustados:

- **Limite 4.096:** configuração comum para limitar saída e consumo, sem alegação
  de que esse teto foi demonstrado ótimo para as correções.
- **Semente 42:** valor mantido constante como controle; não foi atribuída
  vantagem específica ao número escolhido nem garantia de determinismo.
- **Esforço no GPT-4.1 mini:** omissão relacionada à descrição oficial do modelo
  como operando sem uma etapa separada de raciocínio. A página oficial foi
  novamente pesquisada e aberta em 09/11/2026. O código de `modelos.py` confirma
  que o parâmetro é enviado somente aos Luna, com valor `none`.
- A omissão no mini não foi apresentada como configuração interna equivalente
  ao `none` dos Luna, nem como incapacidade de seguir instruções de raciocínio
  guiado. O controle de geração foi distinguido do roteiro dos prompts.

Fonte técnica: [GPT-4.1 mini — documentação oficial da OpenAI](https://developers.openai.com/api/docs/models/gpt-4.1-mini).
Fonte da condição experimental: `src/pipeline/etapas/e05_geracao_llm/modelos.py`
e `docs/historico/features/10-comparacao-modelos-openai/README.md`, seção 4,
no SHA registrado acima. Não foram alteradas configurações ou executadas chamadas.
