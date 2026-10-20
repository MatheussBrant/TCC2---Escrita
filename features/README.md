# Features de escrita do TCC2

Esta é a divisão de trabalho da redação. São **cinco capítulos**, distribuídos
em oito features de conteúdo, duas entregas complementares e uma integração.
Novas evoluções entram como features adicionais, conforme o [fluxo de evoluções](EVOLUCOES.md).
As especificações estão
prontas para execução; os capítulos ainda não foram redigidos por esta entrega.

Cada README de feature é uma tarefa para uma LLM: define o que escrever, fontes,
limites, entregáveis, dependências de fechamento e critérios de aceitação.
Leia-o junto do [contrato de trabalho](CONTRATO.md) e da [base comum](BASE_COMUM.md).
Os caminhos de saída são relativos à raiz de escrita, independentemente do cliente.
Os textos Markdown vão para [manuscrito/](../manuscrito/README.md), em pastas
separadas por feature. O [README principal](../README.md#planejar-e-depois-escrever)
traz o fluxo de planejar uma tarefa, executar sua redação e revisar os critérios.

## Features e destino no texto

**Uma feature é uma unidade de trabalho; um capítulo pode reunir várias features.**
Os números dos diretórios e os IDs F01–F11 identificam tarefas, não a numeração
final dos capítulos. As pastas existentes foram mantidas para preservar os IDs.

| Feature | Capítulo ou entrega | Pasta exclusiva de saída | Início | Conferências para fechar |
|---|---|---|---|---|
| [F01](01-introducao/README.md) | 1. Introdução | `manuscrito/01-introducao/` | Imediato | Recorte com F04/F06 |
| [F02](02-fundamentacao/README.md) | 2. Referencial teórico — conceitos | `manuscrito/02-fundamentacao/` | Imediato | Fontes primárias verificadas |
| [F03](03-trabalhos-relacionados/README.md) | 2. Referencial teórico — trabalhos relacionados | `manuscrito/03-trabalhos-relacionados/` | Imediato | Comparação sustentada pelas fontes |
| [F04](04-metodologia/README.md) | 3. Metodologia e desenvolvimento — desenho e avaliação | `manuscrito/04-metodologia/` | Imediato | Contratos e operacionalização conferidos |
| [F05](05-implementacao/README.md) | 3. Metodologia e desenvolvimento — implementação e evolução | `manuscrito/05-implementacao/` | Imediato | Coerência com F04 |
| [F06](06-resultados/README.md) | 4. Resultados e discussão — resultados | `manuscrito/06-resultados/` | Imediato | Reconciliação numérica e políticas de F04 |
| [F07](07-discussao/README.md) | 4. Resultados e discussão — interpretação e validade | `manuscrito/07-discussao/` | Imediato | Confronto com F03–F06 |
| [F08](08-conclusao/README.md) | 5. Conclusão e trabalhos futuros | `manuscrito/08-conclusao/` | Imediato | Respostas compatíveis com F06/F07 |
| [F09](09-reproducao/README.md) | Apêndices, reprodução e declaração de IA | `manuscrito/09-reproducao/` | Imediato | Identidades e limites de F04–F06 |
| [F10](10-resumos/README.md) | Resumo, abstract e palavras-chave | `manuscrito/10-resumos/` | Imediato | Síntese compatível com F06–F08 |
| [F11](11-integracao/README.md) | Integração editorial e conferência final | `manuscrito/11-integracao/` | Após entregas revisadas | F01–F10 reconciliadas |

**Paralelismo significa independência para produzir o rascunho.** F01–F10
podem trabalhar simultaneamente a partir das fontes originais, sem esperar outro
agente criar um arquivo. Dependências acima condicionam o fechamento, não o início.
Discussão, conclusão e resumos podem ter trechos condicionais durante a redação;
nenhuma pendência material que sustente uma conclusão pode permanecer no aceite.
A integração final tem ordem obrigatória, porque depende dos textos produzidos.

Não é necessário iniciar dez processos se o cliente tiver menos vagas. Distribua
as features em lotes respeitando a capacidade disponível; a divisão não impõe
edição simultânea nem depende de um provedor específico.

## Como executar uma feature

Exemplo no Codex:

```text
$tcc2-redigir Execute a feature features/04-metodologia/README.md.
Leia o contrato e a base comum. Trabalhe somente na pasta de saída da feature,
entregue o capítulo, as evidências e a autoavaliação de cada critério.
```

No Claude Code, use `/tcc2-redigir` no mesmo pedido. Para distribuir várias:

```text
$tcc2-coordenar Execute F01–F10 de features/README.md em paralelo, dentro das
vagas disponíveis, com um responsável por feature. Use a mesma base de fontes,
respeite as pastas exclusivas e agende revisão por critérios. Integre com F11
somente depois de reconciliar as entregas; registre pendências sem inventar dados.
```

Para revisão: `$tcc2-revisar Revise a entrega F04 contra seus critérios e o
contrato comum; registre o parecer em revisoes/F04/parecer.md.` No Claude, troque
o prefixo `$` por `/`.

## Controle de trabalho sem conflitos

Os estados correntes ficam em `manuscrito/<pasta>/entrega.md`, um por feature,
conforme o [modelo de entrega](MODELO_ENTREGA.md). Não há quadro central que
todos os agentes precisem editar. O coordenador pode resumir esses estados em
sua mensagem, mas não atribuir a mesma pasta a dois redatores.

Uma feature concluída documentalmente pode ainda aguardar revisão ou reconciliação.
Os checklists dos READMEs são especificações, não progresso: permanecem desmarcados.
O agente registra evidências e autoavaliação na entrega; o revisor registra seu
parecer separado. Nenhuma marcação de checklist substitui a verificação das fontes.

As especificações não constituem aprovação da orientadora nem escolha do template
institucional. A conversão para o template efetivamente adotado pertence à F11.

## Adições futuras ao experimento

Use `tcc2-evoluir` para examinar novos commits e criar tarefas `E001`, `E002` etc.
Essas features indicam quais partes de F01–F10 precisam ser acrescentadas ou
substituídas. Têm pasta própria, base de fontes, evidências e critérios de aceitação.
Sua especificação usa o [modelo de evolução](MODELO_EVOLUCAO.md); seu registro fica
no [índice de evoluções](EVOLUCOES.md). Não é necessário criar outro capítulo por adição.

F11 incorpora também as evoluções selecionadas, revisadas e reconciliadas para
aquela versão da monografia. O conjunto incluído deve ser declarado, sem presumir
que as onze features iniciais esgotam o escopo final.
