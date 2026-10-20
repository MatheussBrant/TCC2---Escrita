---
name: tcc2-bibliografia
description: Verifica e organiza referências científicas do TCC2, conecta fontes às afirmações e prepara citações ou BibTeX com metadados conferidos.
---

# Verificar bibliografia e afirmações teóricas

Leia [contexto](../../../docs/contexto.md). Para reaproveitar o TCC1, consulte
as referências nas páginas impressas 68–71 (PDF 69–72) e os trechos onde são
citadas. Uma entrada no TCC1 é candidata a fonte; não comprova automaticamente
que título, autoria, ano, link e interpretação estão corretos.

O PDF fica por padrão na raiz da escrita. Use a configuração efetiva descrita
no `AGENTS.md` para encontrá-lo; caminhos de manifestos históricos podem apontar
para outro layout. A ausência do clone opcional da PoC não impede verificar
referências no PDF e nas fontes primárias.

Localize o texto primário: artigo, proceedings, preprint identificado ou
documentação oficial. Quando houver acesso à web, abra a fonte e confira o que
ela sustenta. Metadados de buscador, resumos secundários e DOI plausível não bastam.
Se faltar acesso, registre `não verificada` e continue com as fontes disponíveis;
não gere uma referência fictícia para completar o parágrafo.

Registre chave, título, autores, ano/versão, URL/DOI conferido, data real de acesso,
seção/página de apoio, afirmação sustentada e limitações. Diferencie preprint de
publicação revisada e versão consultada de versão mais recente. Para ferramentas
e modelos usados em 2026, cite a versão histórica do experimento; a documentação
atual não comprova automaticamente capacidades ou custos daquela execução.

Ao atuar em uma feature, mantenha a verificação em `evidencias.md` ou arquivo de
apoio dentro da pasta `saida`, e as entradas no seu `referencias.bib`, com prefixo
da feature conforme o [contrato](../../../features/CONTRATO.md). Não edite um
arquivo global em paralelo; a F11 unifica duplicatas e chaves na integração.
Em tarefas avulsas, crie ou atualize `referencias/verificacao.md` quando necessário
e o `.bib` adotado pelo manuscrito. Preserve chaves existentes e evite duplicatas.
Não afirme conformidade ABNT só porque o BibTeX é sintaticamente válido; siga o
template institucional disponível. Use paráfrases próprias e citações textuais
curtas, conferindo localização e atribuição.

Entregue referências verificadas separadas de pendências, com a relação explícita
entre cada fonte e o argumento do capítulo. Não use documentação de Codex/Claude
como evidência de eficácia do pipeline experimental.
