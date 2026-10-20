---
id: F09
tipo: complemento
capitulo: null
saida: manuscrito/09-reproducao
inicio: imediato
fechamento_depende_de: [F04, F05, F06]
---

# F09 — Reprodução, apêndices e declaração de IA

## Objetivo e escopo

Produzir os materiais complementares que permitem localizar as evidências,
entender os procedimentos de reprodução e conhecer o uso efetivo de IA.
Vínculos: Q4, C14; apoio a C10/C11/C15. Ler o [contrato](../CONTRATO.md)
e a [base comum](../BASE_COMUM.md).

## O que escrever

1. Acesso às fontes: revisões do experimento, PDF, catálogo, contratos, registros
   e manifestos. Explicar o clone experimental dentro da escrita e sua configuração.
2. Ambiente de execução: versões, dependências, Docker e arquivos de configuração;
   distinguir preparação, geração, validação e análise offline dos resultados.
3. Procedimentos documentados de reprodução, com pré-requisitos, entradas,
   comandos, saídas esperadas e limites de disponibilidade. Sinalizar comandos
   que alteram arquivos, chamam APIs pagas ou executam experimentos.
4. Apêndices úteis à leitura: dicionário de dados, convenções de identificação
   e mapa de artefatos. Selecionar material de apoio, sem despejar logs brutos.
5. Declaração de uso de IA baseada no trabalho efetivamente registrado, com
   atividades, ferramentas e responsabilidade autoral; não presumir revisão humana.

Criar um inventário com procedimento → fonte → evidência de execução → alcance.
Distinguir “documentado”, “executado localmente” e “reproduzido independentemente”.
Documentação de comandos, por si só, não demonstra reprodução. Esta feature não
executa o pipeline nem publica imagens para preencher lacunas da escrita.

## Fontes para começar sem outras entregas

- No experimento fixado: `README.md`, `docs/docker.md`,
  `docs/validacao_baseline_docker.md`, `docker/referencia.json`,
  `docker/referencia.py`, `Makefile` e scripts efetivamente disponíveis.
- Manifestos e registros da campanha; hashes e inventários da coleta comum.
- Nesta escrita: `AGENTS.md`, `README.md`, `revisoes/configuracao-inicial.md`
  e registros reais das tarefas realizadas. Conferir a declaração prevista no PDF.
- PoC opcional apenas quando necessária para uma afirmação sobre aquele estágio.

## Entregáveis e paralelismo

Criar, em `manuscrito/09-reproducao/`, `apendices.md`, `declaracao-ia.md`,
`inventario-reproducao.md`, `evidencias.md` e `entrega.md`; referências quando usadas.
A posição final da declaração depende do template e será resolvida na F11.
Começa pelas fontes originais; fecha após reconciliar ambiente, identidades e
limites com F04–F06. Os apêndices complementam os capítulos, sem duplicá-los.

## Critérios específicos de aceitação

Além de G01–G06:

- [ ] **F09-AC01:** fontes e artefatos têm identidade e instruções de localização
  portáveis; a reprodução não depende de caminhos absolutos desta máquina.
- [ ] **F09-AC02:** comandos citados existem na revisão usada, com pré-requisitos
  e efeitos descritos; análise offline é separada de novas execuções experimentais.
- [ ] **F09-AC03:** cada alegação de execução/reprodução tem evidência; o inventário
  distingue procedimento documentado de reprodução efetivamente observada.
- [ ] **F09-AC04:** o inventário informa disponibilidade, versões e limitações dos
  artefatos, incluindo fontes opcionais ausentes, sem expor credenciais.
- [ ] **F09-AC05:** a declaração descreve o uso real de IA e os limites do registro;
  revisão ou aprovação humana não comprovada não é afirmada como realizada.
- [ ] **F09-AC06:** os apêndices são referenciáveis e úteis ao argumento, sem
  substituir a descrição do método nem repetir extensamente os capítulos.
- [ ] **F09-AC07:** os materiais concordam com as versões de F04–F06 registradas
  na entrega; reprodução independente e RRIS não são presumidos.

## Pedido de execução

Use `tcc2-redigir`, apoiada por `tcc2-historico` quando necessário, para produzir
os materiais complementares e conferir os procedimentos por leitura das fontes.
