"""Confere conteúdo, números e vínculos sem regravar o projeto LaTeX."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
WRITING = HERE.parents[1]
PROJECT = WRITING.parent / 'TCC2___Caio_Lamego_e_Matheus_Brant'
m = json.loads((HERE / 'conversao.json').read_text())
source = WRITING / m['fonte']
target = PROJECT / m['destino']
tex = target.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest() == m['fonte_sha256']
assert hashlib.sha256(target.read_bytes()).hexdigest() == m['destino_sha256']
assert len(m['tabelas']) == tex.count(r'\begin{table}') == 14
assert tex.count(r'\begin{figure}') == 1
assert tex.count(r'\section{') == 10
assert tex.count(r'\subsection{') == 6
for table in m['tabelas']:
    block = next(b for b in re.findall(r'\\begin\{table\}.*?\\end\{table\}', tex, re.S)
                 if r'\label{' + table['label'] + '}' in b)
    body = block.split(r'\toprule', 1)[1].split(r'\bottomrule', 1)[0]
    rows = [r for r in body.splitlines() if r.endswith(r'\\') and not r.startswith(r'\textbf')]
    assert len(rows) == len(table['linhas'])
    for markdown_row, latex_row in zip(table['linhas'], rows):
        numbers = lambda s: re.findall(r'\d+(?:[,.]\d+)?', s)
        assert numbers(' & '.join(markdown_row)) == numbers(latex_row), table['label']
    assert r'\fonte{' in block
for paragraph in m['paragrafos']:
    assert paragraph['latex'] in tex
for code in m['excertos']:
    assert code['codigo'] in tex
assert len(re.findall(r'\\textbf\{Q[1-5] ', tex)) == 5
all_tex = '\n'.join(p.read_text() for p in PROJECT.rglob('*.tex'))
labels = re.findall(r'\\label\{([^}]+)\}', all_tex)
for ref in re.findall(r'\\ref\{([^}]+)\}', tex):
    assert labels.count(ref) == 1, ref
bib = (PROJECT / 'bibliografia.bib').read_text()
for cite in re.findall(r'\\citeonline\{([^}]+)\}', tex):
    assert re.search(r'@\w+\{' + re.escape(cite) + ',', bib), cite
figure = PROJECT / 'figuras/resultados-aceites-por-estrategia.png'
assert hashlib.sha256(figure.read_bytes()).hexdigest() == m['figura_sha256']
print('OK: fonte e destino, 14 tabelas e seus números/fontes, 76 parágrafos, 2 excertos, 1 figura, 5 perguntas, labels e citações.')
