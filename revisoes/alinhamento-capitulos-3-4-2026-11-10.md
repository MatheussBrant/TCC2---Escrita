# Alinhamento dos capítulos 3 e 4 — 10/11/2026

Revisão avulsa de continuidade, conforme a skill `tcc2-revisar`. Foram lidos
integralmente o Capítulo 4 e a versão atual do Capítulo 3 no contexto desta
revisão, além das notas do Capítulo 4. Foram conferidos pontualmente o aceite
em `src/pipeline/orquestracao/campanha.py` e a produção das interpretações de F
em `src/pipeline/etapas/e07_validacao/execucao_cobertura.py`, no experimento
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`.
Não foram executadas campanhas, testes ou nova auditoria de todos os módulos.
Nenhum manuscrito foi alterado.

## Parecer

O Capítulo 4 está alinhado às escolhas centrais da metodologia revisada.
Não foram identificadas contradições materiais nos assuntos conferidos.
A divisão pretendida funciona: o Capítulo 3 define o desenho e os critérios;
o Capítulo 4 explica os componentes que os tornam executáveis.
A revisão não equivale à validação integral da implementação.

| Assunto | Metodologia | Implementação e acréscimo |
|---|---|---|
| Alvo e ambiente | 3.2: projeto, revisão e ambiente fixados | 4.2: ferramentas, organização do repositório e montagem do pipeline no contêiner |
| SAST e catálogo | 3.3: escopo, seleção e triagem | 4.3: leitura JSON, regras locais, correspondência das ocorrências e construção dos identificadores |
| Modelos e geração | 3.4: seleção e parâmetros | 4.5: integração por API, adaptação dos parâmetros, resposta estruturada, erros e cache opcional |
| Prompts e RAG | 3.5–3.6: condições P1–P4 e recuperação | 4.4: montagem dos blocos, leitura do código e consulta ao índice, com excerto real do prompt |
| Execução e isolamento | 3.7: sequência, contrato e restauração | 4.6: reserva e devolução das worktrees, proteção de arquivos, âncoras e gravação das edições |
| Validação | 3.8: significado de R/F/M, referência e conjunto D | 4.7: comparador, seleção dos grupos, compilação, reexecução e classificação automática das falhas |
| Parada | 3.7: regra operacional distinta da análise | 4.8: decisão do coordenador pelo aceite sem separação, mantendo classificação principal por critérios |
| Métricas e registros | 3.9–3.10: fórmulas, denominadores e populações | 4.9: leitura dos registros, separação dos posteriores ao aceite, JSON/CSV e rotina conjunta de RRIS |
| Controle e reprodução | Condições metodológicas distribuídas no Capítulo 3 | 4.8–4.9: lançador, painel web, modos de execução e exportação/importação da imagem Docker |

## O que diferencia o Capítulo 4

O capítulo descreve a solução construída, não uma segunda metodologia. O exemplo
real de `routes/trackOrder.ts` conecta catálogo, prompt, JSON de resposta e diff.
O tratamento de âncoras, a proteção dos testes, o gerenciamento de cópias e a
coordenação de recursos compartilhados explicam dificuldades de implementação
que não precisam ocupar o capítulo metodológico. O painel e os arquivos de
saída mostram como o experimento é operado e acompanhado.

Os resultados de eficácia e a comparação de modelos permanecem reservados ao
Capítulo 5. O exemplo serve para explicar o percurso e não acrescenta validação
manual dos patches. O suporte a provedor adicional e a cache é distinguido das
condições usadas nas campanhas finais. A possibilidade de repetição por Docker
não é apresentada como comprovação de reprodução independente já realizada.

## Ajustes recomendados

1. **Clareza, 4.7–4.8:** as expressões “avaliação mais estrita” e “aceite sem
   separação das falhas do conjunto D” continuam corretas por remissão ao
   Capítulo 3, mas podem ser simplificadas para a linguagem recém-adotada:
   falhas novas persistentes nos testes, inclusive em D, impedem a parada por
   aceite. Basta uma explicação breve e remissão à Seção 3.8.
2. **Repetição, 4.6–4.7:** há explicações reiteradas sobre isolamento,
   restauração e limites dos testes. Uma revisão de fluidez pode encurtá-las
   sem retirar o funcionamento da reserva, aplicação e devolução das cópias.
   A ressalva sobre cobertura completa do exemplo de CAPTCHA permanece em 4.7;
   o autor retirou uma ressalva semelhante de 3.8. Isso é questão editorial,
   não contradição metodológica, e pode ser reavaliado na revisão de estilo.
3. **Pendência existente, 4.8:** faltam as capturas reais do painel prometidas
   pelo marcador. O texto não afirma que as três campanhas finais foram
   iniciadas por ele; não acrescentar essa afirmação sem evidência.
4. **Controle documental:** as notas antigas do Capítulo 4 ainda registram
   autoria da triagem e uso de IA como pendências. Os esclarecimentos posteriores
   estão nas notas do Capítulo 3 e nos registros de confirmação. Uma atualização
   deve distinguir essas resoluções do que permanece sem comprovação humana;
   não é necessário repetir toda a triagem e a declaração de IA no Capítulo 4.

A suposição sobre sucesso de uma estratégia posterior é uma limitação do desenho
já descrita em 3.10; não precisa ser reproduzida no capítulo de implementação.
Da mesma forma, não é necessário repetir as fórmulas ou os valores dos parâmetros.
As remissões atuais são adequadas.

## Pendência que afeta a integração futura

Os resultados atuais ainda incluem os 21 falsos positivos. O Capítulo 4 não
alega que o consolidador os excluiu, portanto não há contradição nesse ponto.
Quando o recorte analítico for corrigido, será necessário documentar o filtro
adotado e conferir a continuidade com a consolidação descrita em 4.9, preservando
os dados originais. Esta revisão não realiza esse recálculo.
