# Triagem e revisão humana dos falsos positivos — 09/11/2026

## Fonte da informação sobre a revisão humana

Em resposta à pergunta sobre revisão efetiva das classificações, o usuário
confirmou nesta conversa que todos os casos apontados pela LLM como falsos
positivos foram revisados e confirmados. Em seguida, esclareceu que a revisão
foi realizada por ambos os autores, com exame do código, do contexto do alerta
e da regra do Semgrep.

A declaração foi registrada em 09/11/2026. Essa é a data da confirmação nesta
conversa, não uma data atribuída à execução da revisão.

O relato sustenta a descrição de revisão manual dos 21 falsos positivos pelos
dois autores, Matheus de Siqueira Brant e Caio Magalhães Lamego. Não foi inferido
que as revisões ocorreram de forma independente, às cegas ou mediante dois
pareceres individuais. Também não foram declarados execução adicional de testes,
validação dinâmica, cálculo de concordância ou revisão de todos os 78 rótulos.

A fonte dessa informação é a confirmação do usuário. Os arquivos de triagem
sustentam os rótulos e as justificativas, mas não foram apresentados como prova
autossuficiente de autoria ou realização da revisão humana. Autoria de commit
e nome de arquivo não foram utilizados para atribuir essa revisão.

## Origem e transferência dos rótulos no repositório

Fonte experimental: `../../tcc2-llm-sast-juiceshop`, SHA
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`.

- `scripts/auditoria/classificar_scan_combinado.py`: transfere rótulos de
  `outputs/auditoria_sast/rodada12/matriz_desafios.json` mediante correspondência
  exata de regra normalizada, arquivo e intervalo, na revisão fixada.
- Aceita uma revisão explícita em JSON para ocorrências identificadas exatamente;
  o arquivo usado no scan combinado trata de uma associação em userProfile.ts.
- `outputs/auditoria_sast/combinado-hZGD7r/triagem-final/alertas_classificados.json`:
  preserva rótulos e motivos. São 55 confirmados, 21 falsos positivos, dois
  inconclusivos e 46 fora do escopo do catálogo.
- `outputs/catalogos/ampliado_v1/catalogo_issues.json`: conserva os 78 casos,
  incluindo os mesmos 21 rótulos de falso positivo.

A reaplicação automatizada da classificação não corresponde à realização de
uma nova revisão humana a cada scan. O procedimento de associação dos registros
foi distinguido do exame manual confirmado pelo usuário.

## Critérios e exemplos usados na redação

A revisão informada pelo usuário examinou conjuntamente:

1. O trecho de código identificado.
2. O contexto de uso e a origem dos dados envolvidos no alerta.
3. A condição de insegurança descrita pela regra do Semgrep.

A explicação do critério no manuscrito é uma síntese desses elementos com as
justificativas arquivadas. Não foi atribuída a existência de um protocolo formal
prévio ou de verificações que o usuário não informou.

Exemplos recuperados das justificativas:

- JWTs sintéticos em testes: os valores serviam a cenários de teste, sem serem
  credenciais da aplicação naquele contexto.
- `routes/captcha.ts`: a expressão avaliada era formada por números aleatórios
  e operadores definidos internamente, sem entrada controlada pelo usuário.
- `Gruntfile.js`: MD5 era usado como checksum de artefatos, e não para armazenar
  senhas, que era a condição investigada pela regra local.

Essas classificações se referem ao alerta e ao contexto específicos. Elas não
comprovam que o arquivo ou a aplicação estejam livres de outras vulnerabilidades.

## Ajustes aplicados

- Seção 3.3: descrição da revisão dos falsos positivos, dos responsáveis e dos
  elementos examinados; exemplos breves das justificativas.
- Seção 5.1: atualização da caracterização da triagem para reconhecer a revisão
  manual confirmada, sem estendê-la aos demais rótulos.
- Plano do capítulo 3 e pendências das notas dos capítulos 3 e 5: atualização
  parcial do estado da triagem.
- Conteúdo das métricas e dados experimentais preservados.

## Pontos ainda não confirmados

- A origem e o procedimento documentado dos 55 confirmados e dois inconclusivos
  foram esclarecidos posteriormente por rastreamento no código. Isso não
  comprovou revisão humana nominal desses grupos. Ver
  [rastreio de origem](triagem-origem-2026-11-09/LEITURA.md).
- Identificação da LLM utilizada na classificação inicial e registros específicos
  dessa geração, caso sejam necessários para detalhar a rastreabilidade.
- Momento da revisão em relação às campanhas, sem atribuição cronológica por
  suposição.

A exclusão dos falsos positivos do recorte das métricas é um ajuste distinto da
confirmação dos rótulos. Os consolidados atuais permanecem baseados nos 78 casos;
a declaração de revisão humana não altera automaticamente esses denominadores.
Não foram recalculadas métricas nem executados novos experimentos nesta tarefa.

## Relação com as notas anteriores

Os registros de 07/11/2026 que indicavam ausência de confirmação humana descrevem
o estado de informação daquela redação. A confirmação do usuário em 09/11/2026
resolve a pendência especificamente para os falsos positivos. Ela não é usada
para transformar a inspeção automatizada de patches descrita no capítulo 5 em
uma auditoria humana das correções geradas.
