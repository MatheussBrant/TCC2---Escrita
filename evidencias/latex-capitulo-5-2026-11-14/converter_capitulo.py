"""Converte o capítulo revisado para o template abnTeX2 do projeto dos autores."""
from pathlib import Path
import hashlib
import json
import re
import shutil

HERE = Path(__file__).resolve().parent
WRITING = HERE.parents[1]
PROJECT = WRITING.parent / 'TCC2___Caio_Lamego_e_Matheus_Brant'
SOURCE = WRITING / 'manuscrito/05-resultados-discussao.md'
DESTINATION = PROJECT / 'editaveis/resultado-discussoes.tex'
TABLES = dict(zip(['1','2','3','4','5','5a','6','7','8','9','10','10a','11','12'],
 ['populacao','aceites','criterios','sensibilidade-f','estrategias','ganho-sequencia',
  'sobreposicao','custos','tempos','tipos','owasp','owasp-confirmados','exemplos','rris']))
SECTIONS = {'3.5':'met-selecao','3.9':'met-pipeline','3.10':'met-validacao',
 '3.11':'met-metricas','3.13':'met-limitacoes',
 '5.1':'res-campanhas','5.2':'res-gerais','5.2.1':'res-aceites-trv',
 '5.2.2':'res-criterios','5.2.3':'res-sensibilidade','5.3':'res-estrategias',
 '5.4':'res-modelos','5.4.1':'res-eficacia','5.4.2':'res-custo','5.4.3':'res-tempo',
 '5.5':'res-categorias','5.6':'res-exemplos','5.7':'res-rris','5.8':'res-perguntas',
 '5.9':'res-literatura','5.10':'res-continuidade'}
refs = set()
manifest = {'fonte':str(SOURCE.relative_to(WRITING)),
            'fonte_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'tabelas':[], 'paragrafos':[], 'excertos':[]}
ENGLISH = r'\b(pipelines?|prompts?|patch(?:es)?|baselines?|scans?|worktrees?|tokens?|hash(?:es)?|feedback)\b'


def escape(s, auto_italic=True):
    chars = {'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$',
             '&':r'\&','#':r'\#','_':r'\_','%':r'\%','^':r'\textasciicircum{}',
             '~':r'\textasciitilde{}','→':r'\ensuremath{\rightarrow}',
             '×':r'\ensuremath{\times}','−':r'\ensuremath{-}',
             '—':'---','–':'--','“':'``','”':"''"}
    text=''.join(chars.get(c,c) for c in s)
    return re.sub(ENGLISH,lambda m:r'\textit{'+m[0]+'}',text) if auto_italic else text


def label(kind, number):
    if kind.startswith('Tabela'):
        return 'tab:res-'+TABLES[number]
    if kind.startswith('Seç'):
        return 'sec:'+SECTIONS[number]
    if kind=='Figura':
        assert number=='1'
        return 'fig:res-aceites-estrategia'
    return {'3':'cap:metodologia','4':'cap:implementacao','5':'cap:resultados'}[number]


def plain(s):
    pattern=r'(Seções|Seção|Tabelas|Tabela|Figura|Capítulo) (\d+(?:\.\d+)*[a-z]?(?:, \d+(?:\.\d+)*[a-z]?)*(?: e \d+(?:\.\d+)*[a-z]?)?)'
    result=[]; end=0
    for match in re.finditer(pattern,s):
        result.append(escape(s[end:match.start()]))
        kind, numbers=match.groups()
        parts=re.split(r'(, | e )',numbers)
        result.append(kind+'~')
        for part in parts:
            if part in (', ',' e '):
                result.append(', ' if part==', ' else ' e~')
            else:
                ref=label(kind,part);refs.add(ref)
                result.append(r'\ref{'+ref+'}')
        end=match.end()
    result.append(escape(s[end:]))
    return ''.join(result)


def inline(s):
    if s.startswith('Os achados dialogam com a discussão do referencial'):
        s=re.sub(r' \[Khan, Liu e Gao \(2025\)\].*$', '', s)
        # Citações usam as entradas já existentes na bibliografia do projeto.
        s=s.replace('Khan, Liu e Gao (2025)', '`CITACAOKHAN`').replace('Sriram et al. (2026)', '`CITACAOSRIRAM`')
    result=[];end=0
    pattern=r'(`[^`]+`|\*\*.+?\*\*|_[^_]+_|\[[^\]]+\]\([^)]+\))'
    for m in re.finditer(pattern,s):
        result.append(plain(s[end:m.start()])); token=m[0]
        if token=='`CITACAOKHAN`':result.append(r'\citeonline{khan_code_2025}')
        elif token=='`CITACAOSRIRAM`':result.append(r'\citeonline{sriram_improving_2026}')
        elif token.startswith('`'):result.append(r'\texttt{'+escape(token[1:-1],False)+'}')
        elif token.startswith('**'):result.append(r'\textbf{'+inline(token[2:-2])+'}')
        elif token.startswith('_'):result.append(r'\textit{'+escape(token[1:-1],False)+'}')
        else:
            name,url=re.fullmatch(r'\[([^\]]+)\]\(([^)]+)\)',token).groups()
            result.append(r'\href{'+url+'}{'+plain(name)+'}')
        end=m.end()
    result.append(plain(s[end:]))
    return ''.join(result)


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def tabular(key, caption, headers, data, source):
    count=len(headers)
    first={'1':'.19','2':'.17','3':'.16','4':'.18','5':'.18','5a':'.19',
           '6':'.39','7':'.19','8':'.18','9':'.43','10':'.14','10a':'.28',
           '11':'.37','12':'.17'}[key]
    spec=r'>{\raggedright\arraybackslash}p{'+first+r'\textwidth}'
    for col in range(1,count):
        aligned='raggedright' if (key=='6' and col==1) or (key in ('10','10a') and col==4) else 'centering'
        spec+='>{\\'+aligned+r'\arraybackslash}X'
    if key=='11':
        spec=(r'>{\raggedright\arraybackslash}p{.32\textwidth}'
              r'>{\centering\arraybackslash}p{.04\textwidth}'
              r'>{\centering\arraybackslash}p{.13\textwidth}'
              r'>{\centering\arraybackslash}p{.13\textwidth}'
              r'>{\centering\arraybackslash}p{.04\textwidth}'
              r'>{\centering\arraybackslash}X')
    if key=='12':
        spec=(r'>{\raggedright\arraybackslash}p{.14\textwidth}'
              r'>{\centering\arraybackslash}p{.16\textwidth}'
              r'>{\centering\arraybackslash}p{.12\textwidth}'
              r'>{\centering\arraybackslash}p{.11\textwidth}'
              r'>{\centering\arraybackslash}p{.12\textwidth}'
              r'>{\centering\arraybackslash}p{.12\textwidth}'
              r'>{\centering\arraybackslash}X')
    rendered_headers=[inline(h) for h in headers]
    out=[r'\begin{table}[H]',r'\centering',r'\begin{SingleSpace}',r'\small',
         r'\setlength{\tabcolsep}{'+('2' if key=='12' else '4')+'pt}',r'\renewcommand{\arraystretch}{1.3}',
         r'\caption{'+inline(caption)+'}',r'\label{tab:res-'+TABLES[key]+'}',
         r'\begin{tabularx}{\textwidth}{'+spec+'}',r'\toprule',
         ' & '.join(r'\textbf{'+h+'}' for h in rendered_headers)+r' \\',r'\midrule']
    for row in data:
        assert len(row)==count
        rendered=[]
        for cell in row:
            text=inline(cell)
            if re.fullmatch(r'\d+/\d+ \([\d,]+%\)',cell):
                text=text.replace(' (',r'\newline (')
            rendered.append(text)
        out.append(' & '.join(rendered)+r' \\')
    out += [r'\bottomrule',r'\end{tabularx}',r'\fonte{'+inline(source)+'}',
            r'\end{SingleSpace}',r'\end{table}']
    manifest['tabelas'].append({'numero_markdown':key,'label':'tab:res-'+TABLES[key],
                                'titulo':caption,'cabecalhos':headers,'linhas':data,'fonte':source})
    return '\n'.join(out)


raw=SOURCE.read_text()
raw=re.sub(r'<!--.*?-->','',raw,flags=re.S)
lines=raw.splitlines();out=[];i=0
while i<len(lines):
    line=lines[i]
    if not line.strip():i+=1;continue
    heading=re.match(r'^(#{2,4}) ([\d.]+) (.+)$',line)
    if heading:
        marks,num,title=heading.groups();command={2:'chapter',3:'section',4:'subsection'}[len(marks)]
        out.append('\\'+command+'{'+inline(title)+'}')
        out.append(r'\label{'+('cap:resultados' if command=='chapter' else 'sec:'+SECTIONS[num])+'}')
        i+=1;continue
    cap=re.fullmatch(r'\*\*Tabela (\d+[a-z]?) — (.+)\*\*',line)
    if cap:
        key,caption=cap.groups();i+=1
        while not lines[i].strip():i+=1
        headers=cells(lines[i]);i+=2;data=[]
        while i<len(lines) and lines[i].startswith('|'):
            data.append(cells(lines[i]));i+=1
        while not lines[i].strip():i+=1
        assert lines[i].startswith('Fonte: ')
        source=lines[i][7:];i+=1
        out.append(tabular(key,caption,headers,data,source));continue
    if line.startswith('!['):
        i+=1
        while not lines[i].strip():i+=1
        fig=re.fullmatch(r'\*\*Figura 1 — (.+?)\*\* (.+)',lines[i]);assert fig
        caption,legend=fig.groups();i+=1
        while not lines[i].strip():i+=1
        assert lines[i].startswith('Fonte: ')
        source=lines[i][7:];i+=1
        out.append('\n'.join([r'\begin{figure}[H]',r'\centering',r'\caption{'+inline(caption.rstrip('.'))+'}',
          r'\label{fig:res-aceites-estrategia}',
          r'\includegraphics[width=\textwidth]{figuras/resultados-aceites-por-estrategia.png}',
          r'\legend{'+inline(legend)+'}',r'\fonte{'+inline(source)+'}',r'\end{figure}']))
        continue
    if line.startswith('```'):
        language=line[3:];i+=1;code=[]
        while lines[i]!='```':code.append(lines[i]);i+=1
        i+=1
        text='\n'.join(code)
        out.append(r'\begin{lstlisting}[basicstyle=\ttfamily\footnotesize,breaklines=true,columns=fullflexible,keepspaces=true,showstringspaces=false]'+'\n'+text+'\n'+r'\end{lstlisting}')
        manifest['excertos'].append({'linguagem':language,'codigo':text});continue
    text=line;i+=1
    while i<len(lines) and lines[i].strip():
        assert not lines[i].startswith(('#','|','```','![')), lines[i]
        text+=' '+lines[i];i+=1
    rendered=inline(text)
    if text.startswith('Fonte: '):
        rendered=r'{\footnotesize\noindent '+rendered+r'\par}'
    elif text.startswith('**Q'):
        rendered+=r'\nopagebreak[4]'
    out.append(rendered)
    manifest['paragrafos'].append({'markdown':text,'latex':rendered})

assert len(manifest['tabelas'])==14
assert len(manifest['excertos'])==2
prefix='% Capítulo convertido de manuscrito/05-resultados-discussao.md.\n% SHA-256 da fonte: '+manifest['fonte_sha256']+'\n% Numeração de tabelas, figura e seções automática; fontes preservadas do manuscrito.\n\n'
DESTINATION.write_text(prefix+'\n\n'.join(out)+'\n')
asset=WRITING/'manuscrito/assets/capitulo-5/aceites-por-estrategia.png'
shutil.copy2(asset,PROJECT/'figuras/resultados-aceites-por-estrategia.png')
manifest['destino']=str(DESTINATION.relative_to(PROJECT))
manifest['destino_sha256']=hashlib.sha256(DESTINATION.read_bytes()).hexdigest()
manifest['figura_sha256']=hashlib.sha256(asset.read_bytes()).hexdigest()
manifest['referencias_cruzadas']=sorted(refs)
(HERE/'conversao.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Convertidos:',len(manifest['tabelas']),'tabelas, 1 figura,',len(manifest['excertos']),'excertos e',len(manifest['paragrafos']),'parágrafos.')
