"""Compara os capítulos Markdown; não altera os manuscritos."""
import difflib
import hashlib
import json
import re
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
original=ROOT/'TCC1___Caio_Lamego_e_Matheus_Brant-11.md'
current=ROOT/'manuscrito/03-metodologia.md'
full=original.read_text().splitlines(keepends=True)
start=next(i for i,line in enumerate(full) if line.strip()=='## 3 Metodologia')
end=next(i for i in range(start+1,len(full)) if full[i].startswith('## 4 '))
a=full[start:end]
b=current.read_text().splitlines(keepends=True)
(HERE/'metodologia-original.md').write_text(''.join(a))
(HERE/'metodologia-atual.md').write_text(''.join(b))
(HERE/'comparacao.diff').write_text(''.join(difflib.unified_diff(a,b,fromfile='metodologia-original.md',tofile='metodologia-atual.md')))

def stats(lines,offset=0):
    text=''.join(lines)
    prose=re.sub(r'<!--.*?-->','',text,flags=re.S)
    prose=re.sub(r'^```.*?^```[^\n]*','',prose,flags=re.M|re.S)
    headings=[(i,line.strip()) for i,line in enumerate(lines) if line.startswith('### ')]
    sections=[]
    for pos,(idx,title) in enumerate(headings):
        finish=headings[pos+1][0] if pos+1<len(headings) else len(lines)
        sections.append(dict(titulo=title[4:],inicio=idx+1+offset,fim=finish+offset,linhas=finish-idx))
    return dict(linhas=len(lines),linhas_nao_vazias=sum(bool(l.strip()) for l in lines),
        palavras_por_espacos=len(text.split()),palavras_sem_blocos_codigo_e_comentarios=len(prose.split()),
        secoes=len(headings),tabelas=len(re.findall(r'^\*\*Tabela \d+',text,re.M)),
        figuras_raster=len(re.findall(r'^!\[',text,re.M)),diagramas_mermaid=text.count('```mermaid'),
        secoes_detalhadas=sections)

ops=difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes()
added=sum(j2-j1 for tag,i1,i2,j1,j2 in ops if tag in ('replace','insert'))
removed=sum(i2-i1 for tag,i1,i2,j1,j2 in ops if tag in ('replace','delete'))
equal=sum(i2-i1 for tag,i1,i2,j1,j2 in ops if tag=='equal')
result=dict(original=stats(a,start),atual=stats(b),
    origem=dict(arquivo=str(original.relative_to(ROOT)),linha_inicial=start+1,linha_final=end),
    diff_por_linha=dict(adicionadas=added,removidas=removed,inalteradas=equal,saldo=len(b)-len(a),
        metodo='difflib.SequenceMatcher, autojunk=False; linhas exatas, incluindo vazias'),
    fontes_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (original,current)})
assert len(a)-removed+added==len(b)
(HERE/'contagens.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
