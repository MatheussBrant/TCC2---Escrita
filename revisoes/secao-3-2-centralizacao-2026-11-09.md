# Seção 3.2 — centralização da caracterização do Juice Shop

Revisão solicitada em 09/11/2026. Escopo: verificar a concentração da descrição
do objeto de estudo e do ambiente experimental na seção 3.2, considerando os
capítulos ativos 1–5. Não foram alterados manuscritos ou planos nesta verificação.

## Parecer

A caracterização principal já está concentrada na seção 3.2, mas a apresentação
pode ficar mais completa com uma explicação funcional breve da aplicação e a
identificação do fork utilizado. As referências ao Juice Shop em outras seções
cumprem, em geral, funções distintas: síntese, recorte, validação, implementação
e interpretação. Sua presença fora de 3.2 não caracteriza, por si só, dispersão
indevida do objeto de estudo.

## Mapa do conteúdo

| Informação | Local atual | Avaliação |
|---|---|---|
| Aplicação web aberta e deliberadamente vulnerável | 3.2, primeiro parágrafo | Centralizado; sua menção breve na introdução é adequada. |
| Finalidade didática e motivação da escolha | 3.2, primeiro parágrafo | Centralizado. |
| O que a aplicação simula e funcionalidades que o leitor reconhece | Não explicado diretamente em 3.2; pedidos, feedback e outros fluxos aparecem nos exemplos | Complementar 3.2 com uma descrição breve de loja virtual, sem catalogar todas as funcionalidades. |
| Versão 20.1.1, linguagens e tecnologias principais | 3.2, segundo parágrafo e Tabela 1 | Centralizado. |
| Revisão exata do código | Tabela 1 de 3.2 | Centralizado; sem necessidade de repetir o SHA no corpo de outros capítulos. |
| Origem da revisão no fork utilizado | Protocolo experimental e Dockerfile; ausente em 3.2 | Acrescentar a identificação do repositório à caracterização da versão. Não afirmar equivalência a uma distribuição oficial inalterada sem comparar as revisões. |
| Docker, plataforma, Node.js, npm e UTC | 3.2, Tabela 1 e último parágrafo | Centralizado quanto às condições. O capítulo 4 explica como o ambiente foi preparado e utilizado. |
| Dependências preparadas e desafios habilitados em contêiner | Último parágrafo de 3.2 | Centralizado; sustentado pelo Dockerfile. |
| Papel das execuções exploratórias e dos pilotos | Terceiro parágrafo de 3.2; também 3.3, 3.7 e 3.10 | É delimitação do procedimento e da população, não caracterização da aplicação. Pode ser sintetizado em 3.7/3.10 se a intenção for tornar 3.2 mais focada. |
| Escopo dos alertas e exclusão das soluções pedagógicas | 3.3 | Local adequado à seleção dos casos. Uma remissão a 3.3 basta em 3.2. |
| Particularidade dos testes que esperam comportamento vulnerável | 3.8 | Desenvolvimento adequado junto ao conjunto D. Uma frase de ligação em 3.2 pode antecipar essa consequência da finalidade didática. |
| Worktrees, cópia de dependências, restauração e imagem exportável | 3.7 e capítulo 4 | Locais adequados ao procedimento e à implementação; não transferir integralmente para 3.2. |
| Limite de generalização por utilizar uma aplicação didática | 3.11 e 5.10 | Locais adequados para metodologia e discussão. Não é necessário remover essas retomadas. |

## Achados e sugestões

### 1. Complemento de caracterização — prioridade média

O texto apresenta a finalidade de segurança, mas ainda não explica de forma
simples o que o usuário faz na aplicação. Recomenda-se acrescentar ao primeiro
parágrafo uma frase sobre a simulação de uma loja virtual, com exemplos breves
como consulta de produtos, carrinho e pedidos. Isso fornece contexto para os
exemplos dos capítulos 4 e 5 sem exigir conhecimento prévio do projeto.

É um complemento de apresentação, não evidência de falha metodológica. Não é
necessário acrescentar números de desafios ou listar todas as vulnerabilidades.

### 2. Identificação do fork — prioridade média

A versão e o commit estão informados, mas a origem do código pode ficar mais
explícita. O protocolo identifica `https://github.com/caiolamego/juice-shop-tcc`
como fork utilizado, e o Dockerfile o configura como origem da revisão fixada.
Recomenda-se registrar essa informação no segundo parágrafo ou na Tabela 1.
A ausência não torna o SHA incorreto; reduz a clareza da localização da fonte.
Não foram examinadas todas as diferenças entre o fork e o projeto original.

### 3. Foco do parágrafo sobre pilotos — sugestão editorial

O terceiro parágrafo de 3.2 trata da separação de pilotos e campanhas finais.
Seu conteúdo já é retomado nas seções que definem o procedimento e a análise.
Caso se reorganize a seção, recomenda-se concentrar essa delimitação em 3.7/3.10,
preservando a informação de que os resultados exploratórios não foram agregados.
A mudança não deve eliminar a distinção entre condições experimentais.

### 4. Retomadas em outras seções — sem erro de localização demonstrado

A natureza deliberadamente vulnerável tem efeitos na avaliação dos testes e na
generalização. Por isso, 3.8, 3.11 e 5.10 devem continuar tratando desses efeitos.
O capítulo 4 deve manter a explicação técnica da preparação e do isolamento.
Centralizar a caracterização em 3.2 não significa retirar o nome da aplicação
ou toda referência a seu comportamento das demais seções.

## Organização recomendada para 3.2

1. O que é o Juice Shop, o que a aplicação simula e por que foi selecionado.
2. Versão, fork, revisão fixada e tecnologias principais.
3. Condições do ambiente e tabela de referência.
4. Desafios habilitados e consequência de utilizar uma aplicação didática,
   com remissões à seleção dos casos e à validação.

Essa organização pode aproveitar os parágrafos existentes. Não exige ampliar
substancialmente a extensão nem antecipar a explicação detalhada do pipeline.

## Fontes conferidas

- `manuscrito/03-metodologia.md`, seções 3.2, 3.3, 3.7, 3.8, 3.10 e 3.11.
- Introdução 1.4; implementação 4.2 e 4.6; resultados 5.1 e 5.10.
- Plano do capítulo 3, unidades P06–P09.
- Repositório experimental no SHA `062a203516fd7f55ce86d9c19dc0f23f6e92ed61`,
  sem alterações rastreadas na consulta: `docs/protocolo_experimental.md`,
  quadro do alvo; `Dockerfile`, origem da revisão e configuração de desafios;
  contrato da campanha `AMP_REAL_20261106T105533Z_aa697342`.
- Alvo local `workspace/catalogo-alvo` no SHA
  `f915bddd82790d0f3018902d36ae9b4241a5f51f`: README, package.json e config/default.yml
  lidos nessa revisão, sem alterar a cópia de trabalho.

Não foram realizadas novas execuções, consulta integral ao histórico do fork,
verificação bibliográfica externa ou alteração dos resultados.

## Ajustes aplicados após solicitação do autor

Em 09/11/2026, o autor solicitou a inclusão dos dois complementos de
caracterização. A seção 3.2 recebeu:

- Descrição breve da loja virtual, com produtos, carrinho e pedidos.
- Identificação do fork caiolamego/juice-shop-tcc, explicação breve do termo
  e link para o repositório na Tabela 1.

As funcionalidades foram conferidas nos arquivos do alvo e a origem do
repositório no protocolo experimental. A versão, o commit e as demais condições
da tabela foram preservados. Nenhuma outra seção do manuscrito foi alterada
nessa aplicação dos complementos; o deslocamento do parágrafo sobre pilotos
permanece apenas como sugestão da revisão.
