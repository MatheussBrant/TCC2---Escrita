"""Gera somente o LaTeX do capítulo 6 e confere sua correspondência textual."""
from pathlib import Path
import hashlib
import json
import re

HERE=Path(__file__).resolve().parent
WRITING=HERE.parents[1]
PROJECT=WRITING.parent/'TCC2___Caio_Lamego_e_Matheus_Brant'
SOURCE=WRITING/'manuscrito/06-consideracoes-finais.md'
TARGET=PROJECT/'editaveis/elementosdopostexto.tex'
raw=SOURCE.read_text()
labels={'6.1':'sec:cf-resultados','6.2':'sec:cf-contribuicoes','6.3':'sec:cf-trabalhos-futuros'}


def inline(text):
    special={'\\':r'\textbackslash{}','%':r'\%','&':r'\&','$':r'\$',
             '#':r'\#','_':r'\_','{':r'\{','}':r'\}',
             '–':'--','—':'---'}
    rendered=''.join(special.get(c,c) for c in text)
    rendered=re.sub(r'\b(pipelines?|prompts?|patch(?:es)?|worktrees?|baselines?|tokens?|scans?)\b',
                    lambda m:r'\textit{'+m[0]+'}',rendered)
    return rendered.replace('Capítulo 5',r'Capítulo~\ref{cap:resultados}')


out=['% Fonte: manuscrito/06-consideracoes-finais.md.',
     '% SHA-256: '+hashlib.sha256(SOURCE.read_bytes()).hexdigest()]
paragraphs=[]
for block in raw.strip().split('\n\n'):
    heading=re.fullmatch(r'(#{2,3}) ([\d.]+) (.+)',block)
    if heading:
        level,num,title=heading.groups()
        if len(level)==2:
            assert num=='6'
            out.extend([r'\chapter{'+inline(title)+'}',r'\label{cap:consideracoes-finais}'])
        else:
            out.extend([r'\section{'+inline(title)+'}',r'\label{'+labels[num]+'}'])
    else:
        rendered=inline(block)
        out.append(rendered)
        paragraphs.append({'markdown':block,'latex':rendered})
tex='\n\n'.join(out)+'\n'
TARGET.write_text(tex)
assert all(p['latex'] in tex for p in paragraphs)
assert tex.count(r'\chapter{')==1 and tex.count(r'\section{')==0
assert len(paragraphs)==5
assert not re.search(r'TCC\s*[12]|PoC|prova de conceito',tex)
assert re.search(r'\\input\{editaveis/elementosdopostexto\}',(PROJECT/'tcc.tex').read_text())
project_tex='\n'.join(p.read_text() for p in PROJECT.rglob('*.tex'))
for label in re.findall(r'\\label\{([^}]+)\}',tex):
    assert project_tex.count(r'\label{'+label+'}')==1,label
assert r'\label{cap:resultados}' in project_tex
results=(WRITING/'manuscrito/05-resultados-discussao.md').read_text()
for ratio in re.findall(r'\d+/\d+',raw):
    assert ratio in results,ratio
for percentage in re.findall(r'\d+,\d+%',raw):
    assert percentage in results,percentage
report={'data':'2026-11-14','fonte':str(SOURCE.relative_to(WRITING)),
        'fonte_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'destino':str(TARGET.relative_to(PROJECT)),
        'destino_sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
        'paragrafos':paragraphs,'capitulos':1,'secoes':0,
        'numeros':'Razões e percentuais presentes no capítulo 5; conferência por modelo nas notas.',
        'pdf_gerado':False}
(HERE/'conferencia.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'Capítulo 6: {len(paragraphs)} parágrafos, sem subseções, Markdown e LaTeX correspondentes; nenhum PDF gerado.')
