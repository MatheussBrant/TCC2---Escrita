# Origem dos rótulos confirmados e inconclusivos

Consulta realizada em 09/11/2026 no experimento
`tcc2-llm-sast-juiceshop`, SHA `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`,
sem alterações rastreadas na fonte. O objetivo foi resolver a pendência de
descrever a origem e o procedimento documentado da triagem, sem executar novos
scans, testes, modelos ou classificações.

## Resultado do rastreamento

Foram rastreados os **55 confirmados e dois inconclusivos** do catálogo final:

- 56 ocorrências por referências históricas explícitas na classificação final;
- uma ocorrência por revisão explícita, confrontada com a identidade exata no
  histórico. Trata-se de `routes/userProfile.ts:61`, cuja associação a SSTI
  possuía divergência entre registros anteriores.

Todos os 57 casos possuem entradas correspondentes nos arquivos de triagem
versionados, sem ocorrência sem origem identificada. Os hashes da matriz
histórica e da revisão explícita coincidem com os informados no resumo final.
As classificações também coincidem com as entradas do catálogo de 78 casos.

Os 109 alertas da matriz histórica agregam perfis e scans diferentes. Não são
109 casos independentes do catálogo final. Uma ocorrência final pode ter mais
de uma referência histórica; por isso, contagens de referências não equivalem
às contagens dos 57 casos rastreados.

## Caminho da classificação no código

1. `config/auditoria_desafios.yaml` e arquivos adicionais das rodadas 2–12
   registram regra, arquivo, linha, status, motivo e eventuais desafios associados.
   Os rótulos são decisões de triagem armazenadas, não valores deduzidos apenas
   da execução do Semgrep.
2. `scripts/auditoria/gerar_matriz_desafios.py`, função `aplicar_triagem`, aplica
   essas entradas por regra, arquivo, linha e, quando indicado, scan. Verifica
   status e referências e rejeita entradas sem alerta correspondente.
3. Para associações a desafios, o gerador confronta os registros com os blocos
   e marcadores extraídos do alvo. Uma associação sem marcador exige declaração
   explícita e justificativa no registro; não basta proximidade de linhas.
4. `scripts/auditoria/revisar_associacoes.py` aplica revisões aditivas por ID,
   confere o estado anterior e registra a alteração e o motivo. O exemplo de
   userProfile.ts conserva uma revisão estática da associação, sem alegar
   execução de payload nessa revisão.
5. A matriz resultante foi arquivada em
   `outputs/auditoria_sast/rodada12/matriz_desafios.json`.
6. `scripts/auditoria/classificar_scan_combinado.py` transfere a classificação
   para o scan combinado por regra normalizada, arquivo e intervalo completo,
   conferindo a revisão do alvo e preservando condições históricas. Usa revisão
   explícita quando fornecida. Sem decisão conclusiva, mantém inconclusivo.
7. `scripts/experimento/gerar_catalogo_ampliado.py` consome a classificação final
   e conserva rótulo e justificativa no catálogo, sem realizar nova validação
   humana ou inferir exploração de cada ocorrência.

## Significado e limites dos rótulos

**Confirmado:** as justificativas arquivadas relacionam o alerta a uma condição
de insegurança no contexto do código, por exemplo entrada da requisição usada em
SQL não parametrizado ou exposição de informações por uma rota pública. Parte
contém condições e limites explícitos, como desafios habilitados e requisitos
de origem nas verificações de JSONP. O rótulo não equivale a uma prova de
exploração dinâmica de todos os 55 casos, a uma correção aceita ou à segurança
integral da aplicação.

**Inconclusivo:** a justificativa não confirma nem descarta a falha com a evidência
registrada. Os dois casos finais são:

| Caso | Local | Motivo arquivado |
|---|---|---|
| `AMPba6a42f81dbc573f` | routes/basketItems.ts:68 | Consulta intermediária de estoque; a escrita ocorre depois em API gerada, sem demonstração completa de manipulação da cesta nesse alerta. |
| `AMPa4fbc80b66819196` | routes/quarantineServer.ts:14 | Serviço de arquivos de quarentena sem demonstração de acesso fora do diretório ou impacto de um arquivo específico. |

O arquivo `rastreio.json` preserva os motivos integrais, IDs históricos e entradas
de configuração. Os nomes e os motivos dessa tabela descrevem o estado arquivado;
não houve nova decisão sobre explorabilidade nesta tarefa.

## Revisão humana: o que pode ser afirmado

O código e os registros sustentam a origem e o processamento das classificações.
Não permitem atribuir nominalmente a revisão dos 55 confirmados e dois
inconclusivos a uma pessoa, nem demonstrar revisão independente por dois autores.
O comentário “revisão manual exploratória” e o campo
`confirmacao_manual_sem_marcador` indicam a forma declarada do registro; não são
prova autossuficiente de quem realizou a análise.

A revisão humana dos **21 falsos positivos**, por ambos os autores, foi confirmada
pelo usuário em outra etapa desta conversa. Esse relato foi preservado e não
estendido aos demais rótulos. Não foi inferida autoria humana a partir do nome
de um commit ou da existência de um arquivo com “revisão” no nome.

Com essa delimitação, a pendência textual foi resolvida pela descrição do
procedimento efetivamente documentado, sem inventar uma revisão humana adicional.
Caso uma revisão humana desses outros grupos venha a ser declarada, deverá ser
identificada com seu próprio alcance e procedimento.

## Histórico consultado

- `git log --follow` dos arquivos de geração e configuração identificou a
  configuração no commit `4df147d` (10/10/2026) e reorganizações posteriores,
  incluindo `0a5a63c` (27/10/2026).
- Foi consultado o conteúdo da configuração no objeto `4df147d`; a mensagem do
  commit não foi usada para comprovar qualidade ou autoria da revisão.
- A cadeia de origem foi reconstruída nos arquivos do SHA fixado e nos hashes
  registrados nos artefatos. Não foi realizada revisão integral de todos os
  diffs do histórico ou dos testes exploratórios de todas as rodadas.

## Arquivos e reprodução

- `rastrear_rotulos.py`: leitura e conferência de identidade, status e origem.
- `rastreio.json`: 57 casos com justificativas e referências completas.
- `rastreio.csv`: versão resumida para consulta.
- `fontes-sha256.json`: identificação dos arquivos utilizados.

O script requer Python e PyYAML e pode ser executado da raiz da escrita:

```sh
python3 evidencias/triagem-origem-2026-11-09/rastrear_rotulos.py
```

Ele escreve somente nesta pasta de evidências, sem alterar o experimento.
Os resultados numéricos, denominadores e campanhas não foram modificados.
