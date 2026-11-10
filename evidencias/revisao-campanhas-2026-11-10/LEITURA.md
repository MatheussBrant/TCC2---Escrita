# Revisão documental das campanhas de 6 de novembro de 2026

Conferência em 10/11/2026, pela leitura dos arquivos experimentais no commit
`062a203516fd7f55ce86d9c19dc0f23f6e92ed61`, sem alterações locais na fonte.
Skill utilizada: `.claude/skills/tcc2-resultados/SKILL.md`.
Não foram executados LLMs, SAST, testes ou novas campanhas. Esta conferência
não é revisão humana das correções nem nova validação de segurança.

## Campanhas conferidas

Horários das sessões convertidos para America/Sao_Paulo (UTC−3); os nomes das
pastas usam UTC e antecedem ligeiramente o início da sessão de tentativas.

| Modelo | Execução | Início–fim, Brasília | Casos observados | Tentativas totais | Principal / posteriores ao aceite |
|---|---|---|---:|---:|---:|
| GPT-6 Luna | `AMP_REAL_20261106T105533Z_aa697342` | 07:56:29–09:57:49 | 78 | 274 | 221 / 53 |
| GPT-5.6 Luna | `AMP_REAL_20261106T125801Z_0eb68fe4` | 09:59:05–12:09:52 | 78 | 277 | 223 / 54 |
| GPT-4.1 mini | `AMP_REAL_20261106T151004Z_f49ac0d2` | 12:11:11–14:20:26 | 78 | 283 | 241 / 42 |

São três execuções reais, sem reutilização local de respostas. Os diretórios
com sufixo `_METRICAS` são saídas derivadas, não outras campanhas.
Cada campanha possui uma sessão com término, sem interrupção por orçamento ou
usuário e com lista de erros da sessão vazia. Isso não significa ausência de
falhas nas tentativas: há propostas não aplicadas, reprovações e indeterminações,
registradas em `conferencia.json`.

Todos os casos começaram em P1 e seguiram uma sequência sem lacunas até o aceite
sem separação ou P4. Nenhuma tentativa ocorreu depois de um aceite sem separação
na cadeia do respectivo caso. Encerramentos na campanha completa:

| Modelo | Aceite sem separação | P4 sem aceite sem separação | Total |
|---|---:|---:|---:|
| GPT-6 Luna | 25 | 53 | 78 |
| GPT-5.6 Luna | 23 | 55 | 78 |
| GPT-4.1 mini | 17 | 61 | 78 |

Esses valores usam a campanha completa; não devem ser confundidos com a
sensibilidade de F calculada apenas na população principal, que é delimitada
pelo primeiro aceite por critérios. A população principal mantém 49, 51 e 38
casos aceitos, respectivamente, conforme o consolidado existente.

## Comparabilidade e integridade

Todos os campos dos contratos, exceto `execucao` e `inferencia`, são iguais:
mesmo commit alvo, 78 casos, catálogo, perfil Semgrep 1.177.0, comparador,
P1–P4, prompts, base RAG, referência funcional e condições de validação.
As sessões registram quatro casos em paralelo e nenhum caso pulado por alerta
ausente. Os relatórios iniciais registram a reprodução dos 78 alertas.
As campanhas ocorreram sucessivamente, não simultaneamente.

As diferenças de inferência são explícitas: modelo, tarifas e geração.
Temperatura 0 e limite 4096 são comuns; mini envia seed 42, sem effort;
os Luna enviam effort `none`, sem seed. O mini solicitado como `gpt-4.1-mini`
retornou `gpt-4.1-mini-2025-04-14` nas 283 tentativas; os Luna retornaram os
mesmos identificadores solicitados. Não interpretar isso como divergência de
campanha nem presumir equivalência interna entre os modelos.

Foram conferidas 5.623 referências de hashes de artefatos das 834 tentativas
(1.833 / 1.894 / 1.896, na ordem da tabela), sem divergências. Também foram
conferidos o hash do contrato em cada tentativa, a identidade do modelo
solicitado, a unicidade dos IDs e a correspondência dos IDs com os CSVs
normalizados já existentes. O script não repete toda a consolidação de métricas
nem inspeciona semanticamente todos os patches.

## Limites e pendências

- Cada relatório SAST inicial contém oito diagnósticos de análise. A reprodução
  do catálogo não demonstra cobertura integral de todos os arquivos do projeto.
- Término registrado significa conclusão operacional; não significa que todos
  os casos receberam correção aceita ou que o conjunto passou nos testes.
- As populações consolidadas atuais ainda incluem os 21 falsos positivos e os
  dois inconclusivos. A exclusão dos falsos positivos solicitada pelo autor ainda
  requer novo recorte analítico, sem alterar os resultados experimentais originais.
  As contagens desta nota descrevem as campanhas arquivadas; não resolvem essa
  pendência nem substituem as tabelas após eventual filtragem.
- P1–P4 são sequenciais; a comparação de estratégias é condicionada aos casos
  que chegaram a cada etapa. As condições comuns apoiam uma comparação
  descritiva entre modelos, sem demonstrar superioridade causal geral.

## Reprodução da conferência

Executar `python3 evidencias/revisao-campanhas-2026-11-10/conferir.py` na raiz da
escrita. O script somente lê a fonte e os consolidados existentes e grava
`conferencia.json` nesta pasta. Esse JSON registra resultados detalhados e
hashes dos contratos, sessões, JSONL e relatórios de reprodução consultados.
