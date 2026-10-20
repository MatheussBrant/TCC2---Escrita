# Histórico local — experimento

Todos os commits alcançáveis por refs locais, em ordem topológica reversa.
Mensagens são índices para investigação; os diffs não foram auditados integralmente.

| Commit | Data do autor | Evolução registrada |
|---|---|---|
| `dab4c1b046c463429ad9097efd0e7a7d2ae8ab12` | 2026-09-08T16:06:33-03:00 | Initial commit |
| `341eca39741da5d9a3d4469bce8008832aad048d` | 2026-09-08T16:16:55-03:00 | configuração inicial do repositório |
| `bdef8534564b96f66757c504b346c4bcc5fdc0b3` | 2026-09-08T16:20:50-03:00 | adiciona env.example |
| `ba41fcb0cdc029ae49efd5095d91805ab1d434f1` | 2026-09-08T16:40:03-03:00 | atualiza README.md com descrição do projeto e detalhes sobre a correção de vulnerabilidades |
| `b829c5453d640dd4eab32a3c5f3e15b4d5764900` | 2026-09-08T16:40:28-03:00 | remove TCC 1 and proof of concept links from README.md |
| `9d646b28b0bee35172c08a54110817e4889cbf5a` | 2026-09-08T16:54:15-03:00 | feat: implementa script bash para preparação do workspace |
| `7186b9ea6dfec53408ac2d9a29aa2c8a17cbe816` | 2026-09-17T17:35:11-03:00 | atualiza env.example |
| `6a07a95f78754f2ef678ccfe704781a112065ba1` | 2026-09-17T17:36:21-03:00 | altera de npm ci para npm install, pois package-lock.json é gitignorado no Juice Shop |
| `697f81647f4f2fb0076b6df85e580adb97e9e928` | 2026-09-17T17:41:21-03:00 | Implementa script de medição para rodar os tiers sobre os worktrees |
| `34a4a81cea3795eda31f7ec4e1103da0ba4fc8ab` | 2026-09-17T17:42:18-03:00 | 17/09/2026 - v1 custos de validação |
| `f3919d70b31c63557102f04336dacbd5a1a7c1d9` | 2026-09-22T18:27:35-03:00 | v1 caderno de laboratório |
| `27c705b7d5e4c3d2f5881db5d96cdd1cae056fb2` | 2026-09-23T16:11:00-03:00 | F3.1 - configuração do semgrepignore |
| `c50fd9b19d19a1423b13aa8c6c89e3151c9f51c1` | 2026-09-23T16:22:19-03:00 | F3.3 - Implementa funções de execução e normalização dos resultados do Semgrep |
| `1ebb3ab17bea15c2ba23f0ee89e6c67b290f626d` | 2026-09-23T16:23:30-03:00 | F3.4 - Atualiza mapeamento dos CWEs e implementa catálogo de issues |
| `10cf2c2cd1e3d783532db2d0d0f9fe482e3f6f9e` | 2026-09-23T16:27:58-03:00 | Adiciona protocolo exprimental |
| `cd93708793b7932b4cc3246b35d0b0ab22ba2f64` | 2026-09-23T16:32:11-03:00 | F3.5 - Implementa cruzamento com os marcadores |
| `2d23759d2ab5ff1e4c1f09dc191df5150dd4d9d8` | 2026-09-23T16:49:43-03:00 | F3.6 - Gera o relatorio do baseline SAST a partir do catalogo ja |
| `969356cb062640ce008d0b579b5369cc414fbd56` | 2026-09-23T16:50:50-03:00 | feat(f3): baseline SAST, catalogo de issues, marcadores e relatorio |
| `69bfb2a5d5509d4f611ce4e0f5b83794967bb023` | 2026-10-07T16:36:48-03:00 | F4 - Implementação de workspace e validação |
| `a6fcde57d3dd021cbaff4ca21eb31dccd214cae0` | 2026-10-07T17:25:59-03:00 | docs: registra decisoes de assinatura, linha de base de testes e commit do alvo |
| `eeb5f8df9847b2a7e85b2e1f8289c5950052eab1` | 2026-10-07T17:26:51-03:00 | feat(f5): camada LLM, aplicacao de patch por ancora e prompt P1 |
| `799e95650624ffa0fc0a6f23e456dc65eb6bd2c3` | 2026-10-07T17:27:56-03:00 | chore: catalogo com assinaturas distintas, linha de base e primeira tentativa real |
| `4df147d7a6cfb3917975c46fa9df623da8bd9eae` | 2026-10-10T18:14:12-03:00 | Add rules to Semgrep |
| `dbf5b88c55d12f04520624142b3063ac5aaa7782` | 2026-10-12T22:26:34-03:00 | Organiza regras iniciais em rodada1 |
| `3cd1f9115b3027f8680479f7fad0f893960bbd52` | 2026-10-08T17:14:04-03:00 | chore: remove outputs do dry run do versionamento |
| `92d3229a0c966e505ada468d4ebeb333ba12092c` | 2026-10-12T16:48:26-03:00 | docs(fd): criterios do conjunto D e lista a priori sobre a suite inteira |
| `6d4b6b3aa3bd363e316a13cebc498ff514880460` | 2026-10-12T16:53:53-03:00 | feat(f6): orquestrador, P2, P1L, reexecucao por timeout e separacao F/D em duas definicoes |
| `1a80a7e7ec521beaa43020926cf9866efdc88ba3` | 2026-10-12T16:56:29-03:00 | chore: regras de referencia do Semgrep, catalogo com faixas, sondagens A/B, EXP01/EXP02 |
| `3b7ef48158d2419fa12101e94662ce106de9e76b` | 2026-10-12T16:58:22-03:00 | data(e01): execucao preliminar, anterior a separacao F/D |
| `da10b26864b614055b0f74df79162a395eef709c` | 2026-10-12T16:59:22-03:00 | data(e02): execucao oficial do desenho com separacao F/D e diagnostico P1L |
| `0577032445ee8e9bb0e926da4331bbe19d6fadde` | 2026-10-12T22:27:37-03:00 | Merge remote-tracking branch 'origin/main' into semgrep-findings |
| `ffc6f427c11dc80fbca3f6703485948142e25646` | 2026-10-12T22:54:27-03:00 | reorganiza arquivos |
| `ccea1c95b32c07bd289ca1f64b112185d6040d59` | 2026-10-12T23:18:28-03:00 | catologo ampliado para  78 casos |
| `6d90f347bacd8ef571dcec5c2b03cbe1ea6d9148` | 2026-10-12T23:58:48-03:00 | implementa feature 02 |
| `133523731daa278e63adceb6f6e7fea2d3a4d89c` | 2026-10-13T00:37:13-03:00 | implementa feature 03 |
| `41eebfa8bb03aaee674fea8a1de38efe64c85244` | 2026-10-12T23:58:48-03:00 | implementa feature 02 |
| `1dc014708d8f7896267a4ca9488d91261bd50a9c` | 2026-10-13T00:37:13-03:00 | implementa feature 03 |
| `34e0b3dfb1b0ee6ec5201755ac7fb7a8042b6e9c` | 2026-10-13T01:30:16-03:00 | implementa feature 4 |
| `d645466efbff498f725c464fa7c15f982606e108` | 2026-10-13T15:09:23-03:00 | atualiza documentação da f6 |
| `112a4e43f8c1661521236ac03605aade0ce3df0d` | 2026-10-16T23:31:02-03:00 | feat: catalogo v2, saidas por execucao, quatro definicoes de F; artefatos E01/E02 recuperados |
| `fa7b644957a71c68264f3f15474c59337e7c64e2` | 2026-10-18T16:02:59-03:00 | data(e03): execucao sobre o catalogo v2 (22 casos, P1, P2 e P1L) e relatorio das execucoes |
| `fa044444abe4feb7b53dbf88859c99a45e089352` | 2026-10-13T01:30:16-03:00 | implementa feature 4 |
| `2727a836ccde9c22f0d83d1f6b4666810a7234b2` | 2026-10-16T01:40:03-03:00 | feat: adicionar painel local e execução simplificada do pipeline |
| `db70ab7446d22217fa64dac29b3fa58de7aafb3a` | 2026-10-16T02:47:01-03:00 | Adiciona Qwen2.5-Coder-14B |
| `c1e1f441c5ba16e9407bf96f1c9faaeed30aa118` | 2026-10-16T12:52:41-03:00 | feat: otimiza validação do pipeline com cache, triagem e benchmark K=2 |
| `f2179c6d7ba0ea94aca83db0c0e4075c872fe964` | 2026-10-17T00:20:31-03:00 | feat: valida funcionalidades com testes relacionados e habilita duas worktrees |
| `932bd44e242af7e5407df2c561fea1e92714a29a` | 2026-10-17T01:45:38-03:00 | feat(sast): adiciona comparador v2, auditoria de referências e motivos de indeterminação no painel |
| `f8a1f1205b01d3bc204c967a847a7908e63a2f3f` | 2026-10-17T03:25:24-03:00 | feat: adiciona auditoria de cobertura funcional e validação seletiva com Angular |
| `9d7286ef899acf28653b57fc5b9436e53a050726` | 2026-10-17T04:09:21-03:00 | feat: configura piloto de 10 issues com quatro worktrees e registra resultados preliminares |
| `8da402bd9bfb1b74c583891ac9b2d8d49755bf56` | 2026-10-17T04:43:58-03:00 | fix: corrige preparação das worktrees e classificação de falhas operacionais, com revalidação dos patches |
| `d03fe579d2302fd4a2c8d2450173db58562c457a` | 2026-10-18T00:43:02-03:00 | feat: integra Qwen no Colab ao pipeline e adiciona diagnósticos de geração e controle do servidor |
| `85ee214ab672303340c6f348eb1e7ec2bf5a9134` | 2026-10-18T00:43:33-03:00 | resultado resposta qwen p1 |
| `1cea0e7a63fb1397c607521155f995f573ca8c75` | 2026-10-18T19:29:15-03:00 | feat(docker): ambiente único com Juice Shop travado por lockfiles e safetyMode disabled |
| `48ff5bcd64fd2a3fd7e394a884a70ab7d2576870` | 2026-10-18T19:29:28-03:00 | feat(audit): compara baselines funcionais entre ambientes |
| `fd1e1d158188560d7d0243a0d359c7df0b18492f` | 2026-10-18T19:29:42-03:00 | data(revalidacoes): baselines funcionais no Docker (V1 com safetyMode auto, V2 corrigido e equivalente ao piloto) |
| `517385e3f4784fda06ff7e946d2add0c44f7cf5d` | 2026-10-18T19:30:27-03:00 | docs: registra a adoção do Docker no caderno e no protocolo |
| `94c74d778e60e80dccbf2cf0f09ad716d6f46d9f` | 2026-10-19T18:20:22-03:00 | feat: padroniza baseline Docker e corrige aplicação de patches por indentação |
