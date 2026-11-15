"""Converte manuscrito/05-resultados-discussao.md para o padrão LaTeX de overleaf/oficial."""
import re
import sys

ORIGEM, DESTINO = sys.argv[1], sys.argv[2]

SECOES = {
    '5.1': 'sec:res-campanhas', '5.2': 'sec:res-gerais', '5.2.1': 'sec:res-aceites',
    '5.2.2': 'sec:res-criterios', '5.2.3': 'sec:res-tratamento-testes', '5.3': 'sec:res-estrategias',
    '5.4': 'sec:res-modelos', '5.4.1': 'sec:res-eficacia', '5.4.2': 'sec:res-custo',
    '5.4.3': 'sec:res-tempo', '5.5': 'sec:res-tipos', '5.6': 'sec:res-exemplos',
    '5.7': 'sec:res-rris', '5.8': 'sec:res-perguntas', '5.9': 'sec:res-literatura',
    '5.10': 'sec:res-alcance',
}
CAP3 = {'3.5': 'sec:met-selecao', '3.9': 'sec:met-pipeline', '3.10': 'sec:met-validacao',
        '3.11': 'sec:met-metricas', '3.13': 'sec:met-limitacoes'}
TABELAS = {
    '1': 'tab:res-populacao', '2': 'tab:res-aceites', '3': 'tab:res-criterios',
    '4': 'tab:res-sensibilidade-f', '5': 'tab:res-estrategias', '5a': 'tab:res-ganho-sequencia',
    '6': 'tab:res-sobreposicao', '7': 'tab:res-custos', '8': 'tab:res-tempos', '9': 'tab:res-tipos',
    '10': 'tab:res-owasp', '10a': 'tab:res-owasp-confirmados', '11': 'tab:res-exemplos',
    '12': 'tab:res-rris',
}
FIGURA = 'fig:res-aceites-estrategia'

C = r'>{\centering\arraybackslash}'
L = r'>{\raggedright\arraybackslash}'
X = 'X'
ESPEC = {  # (tamanho da fonte, especificação das colunas)
    '1': ('', f'|{L}p{{0.20\\textwidth}}|{C}X|{C}X|{C}X|'),
    '2': ('', f'|{L}p{{0.20\\textwidth}}|{C}X|{C}X|{C}X|'),
    '3': (r'\footnotesize', f'|{L}p{{0.13\\textwidth}}|{C}X|{C}X|{C}X|{C}X|{C}p{{0.09\\textwidth}}|{C}p{{0.09\\textwidth}}|'),
    '4': ('', f'|{L}p{{0.20\\textwidth}}|{C}X|{C}X|{C}X|'),
    '5': (r'\small', f'|{L}p{{0.16\\textwidth}}|{C}X|{C}X|{C}X|{C}X|'),
    '5a': (r'\small', f'|{L}p{{0.16\\textwidth}}|{C}X|{C}X|{C}X|{C}X|'),
    '6': ('', f'|{L}X|{L}X|{C}p{{0.15\\textwidth}}|'),
    '7': (r'\small', f'|{L}p{{0.16\\textwidth}}|{C}X|{C}X|{C}X|{C}X|'),
    '8': (r'\small', f'|{L}p{{0.16\\textwidth}}|{C}X|{C}X|{C}X|{C}X|'),
    '9': ('', f'|{L}X|{C}p{{0.14\\textwidth}}|{C}p{{0.14\\textwidth}}|{C}p{{0.14\\textwidth}}|'),
    '10': (r'\small', f'|{L}p{{0.13\\textwidth}}|{C}p{{0.12\\textwidth}}|{C}p{{0.12\\textwidth}}|{C}p{{0.12\\textwidth}}|{L}X|'),
    '10a': (r'\small', f'|{L}X|{C}p{{0.10\\textwidth}}|{C}p{{0.10\\textwidth}}|{C}p{{0.10\\textwidth}}|{L}p{{0.20\\textwidth}}|'),
    '11': (r'\small', f'|{L}X|{C}p{{0.04\\textwidth}}|{C}p{{0.10\\textwidth}}|{C}p{{0.11\\textwidth}}|{C}p{{0.04\\textwidth}}|{C}p{{0.14\\textwidth}}|'),
    '12': (r'\footnotesize', f'|{L}p{{0.13\\textwidth}}|{C}X|{C}X|{C}X|{C}p{{0.13\\textwidth}}|{C}p{{0.13\\textwidth}}|{C}p{{0.13\\textwidth}}|'),
}

INGLES = ['pipelines', 'pipeline', 'prompts', 'prompt', 'patches', 'patch', 'scans', 'scan',
          'tokens', 'token', 'Issues', 'issues', 'feedback', 'login', 'software', 'baseline', 'script', 'buffer']


def escapar_codigo(s):
    return s.replace('\\', r'\textbackslash{}').replace('$', r'\$').replace('_', r'\_').replace('%', r'\%').replace('&', r'\&').replace('#', r'\#')


def remissoes(t):
    t = re.sub(r'Seções (3\.\d+) e (3\.\d+)', lambda m: f'Seções~\\ref{{{CAP3[m.group(1)]}}} e~\\ref{{{CAP3[m.group(2)]}}}', t)
    t = re.sub(r'Seção (3\.\d+)', lambda m: f'Seção~\\ref{{{CAP3[m.group(1)]}}}', t)
    t = re.sub(r'Seção (5\.\d+(?:\.\d+)?)', lambda m: f'Seção~\\ref{{{SECOES[m.group(1)]}}}', t)
    t = t.replace('Capítulo 3', r'Capítulo~\ref{cap:metodologia}')
    t = re.sub(r'Tabelas (\d+a?), (\d+a?) e (\d+a?)', lambda m: f'Tabelas~\\ref{{{TABELAS[m.group(1)]}}}, \\ref{{{TABELAS[m.group(2)]}}} e~\\ref{{{TABELAS[m.group(3)]}}}', t)
    t = re.sub(r'Tabelas (\d+a?) e (\d+a?)', lambda m: f'Tabelas~\\ref{{{TABELAS[m.group(1)]}}} e~\\ref{{{TABELAS[m.group(2)]}}}', t)
    t = re.sub(r'Tabela (\d+a?)\b', lambda m: f'Tabela~\\ref{{{TABELAS[m.group(1)]}}}', t)
    t = t.replace('Figura 1', f'Figura~\\ref{{{FIGURA}}}')
    t = t.replace('Khan, Liu e Gao (2025)', r'\citeonline{khan_code_2025}')
    t = t.replace('Sriram et al. (2026)', r'\citeonline{sriram_improving_2026}')
    return t


def inline(t, refs=True):
    guard = []

    def guardar(s):
        guard.append(s)
        return f'\x00{len(guard) - 1}\x00'

    t = re.sub(r'`([^`]+)`', lambda m: guardar(r'\texttt{' + escapar_codigo(m.group(1)) + '}'), t)
    t = t.replace('%', r'\%').replace('$', r'\$').replace('&', r'\&').replace('#', r'\#')
    t = t.replace('—', '---').replace('–', '--').replace('−', '$-$').replace('×', r'$\times$')
    t = t.replace('→', r'$\rightarrow$').replace('“', '``').replace('”', "''")
    t = re.sub(r'(?<![A-Za-z0-9])_([^_]+)_(?![A-Za-z0-9])', lambda m: guardar(r'\textit{' + m.group(1) + '}'), t)
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t)
    for w in INGLES:
        t = re.sub(r'(?<![\w\\{])' + w + r'(?![\w])', lambda m: guardar(r'\textit{' + m.group(0) + '}'), t, flags=re.I)
    if refs:
        t = remissoes(t)
    for _ in range(3):
        t = re.sub(r'\x00(\d+)\x00', lambda m: guard[int(m.group(1))], t)
    return t


def fonte(texto, largura=r'\textwidth'):
    return ('\n\\vspace{0.2cm}\n\\begin{minipage}{' + largura + '}\n    \\footnotesize\n    '
            + texto + '\n\\end{minipage}\n')


def tabela(num, titulo, linhas, texto_fonte):
    tam, espec = ESPEC[num]
    cab = [c.strip() for c in linhas[0].strip().strip('|').split('|')]
    corpo = [[c.strip() for c in l.strip().strip('|').split('|')] for l in linhas[2:]]
    assert all(len(r) == len(cab) for r in corpo), (num, cab)
    out = ['\\begin{table}[H]', '\\centering', '\\caption{' + inline(titulo, refs=False) + '}',
           '\\label{' + TABELAS[num] + '}', '\\renewcommand{\\arraystretch}{1.35}']
    if tam:
        out.append(tam)
    out += ['\\begin{tabularx}{\\textwidth}{' + espec + '}', '\\hline',
            ' & '.join('\\textbf{' + inline(c, refs=False) + '}' for c in cab) + ' \\\\', '\\hline']
    for r in corpo:
        out += [' & '.join(inline(c, refs=False) for c in r) + ' \\\\', '\\hline']
    out.append('\\end{tabularx}')
    out.append(fonte(inline(texto_fonte)).rstrip('\n'))
    out.append('\\end{table}')
    return '\n'.join(out)


md = open(ORIGEM).read()
md = re.sub(r'<!--.*?-->\n*', '', md, flags=re.S)
blocos = []
for parte in re.split(r'(```\w*\n.*?```)', md, flags=re.S):
    if parte.startswith('```'):
        blocos.append(parte)
    else:
        blocos += [b.strip('\n') for b in re.split(r'\n\s*\n', parte) if b.strip()]

saida = []
i = 0
while i < len(blocos):
    b = blocos[i]
    if b.startswith('```'):
        corpo = re.match(r'```\w*\n(.*?)```', b, re.S).group(1).rstrip('\n')
        maior = max(len(l) for l in corpo.splitlines())
        tam = r'\footnotesize' if maior <= 86 else r'\scriptsize'
        saida.append('{' + tam + '\n\\begin{verbatim}\n' + corpo + '\n\\end{verbatim}\n}')
    elif b.startswith('## '):
        saida.append('\\chapter[Resultados e discussão]{Resultados e discussão}\n\\label{cap:resultados}')
    elif b.startswith('### ') or b.startswith('#### '):
        m = re.match(r'(#+) (\d+(?:\.\d+)+) (.+)', b)
        cmd = 'section' if m.group(1) == '###' else 'subsection'
        saida.append(f'\\{cmd}{{{inline(m.group(3), refs=False)}}}\n\\label{{{SECOES[m.group(2)]}}}')
    elif re.match(r'\*\*Tabela (\d+a?) — ', b):
        m = re.match(r'\*\*Tabela (\d+a?) — (.+)\*\*$', b)
        linhas = blocos[i + 1].splitlines()
        assert blocos[i + 2].startswith('Fonte:'), blocos[i + 2][:40]
        saida.append(tabela(m.group(1), m.group(2), linhas, blocos[i + 2]))
        i += 3
        continue
    elif b.startswith('!['):
        caminho = 'figuras/resultados-aceites-por-estrategia.png'
        cap = re.match(r'\*\*Figura 1 — (.+?)\*\* (.+)$', blocos[i + 1])
        assert blocos[i + 2].startswith('Fonte:')
        saida.append('\n'.join([
            '\\begin{figure}[H]', '    \\centering', '    \\includegraphics[', '        width=0.95\\textwidth,',
            '        height=0.55\\textheight,', '        keepaspectratio', '    ]{' + caminho + '}', '',
            '    \\caption{' + inline(cap.group(1), refs=False) + '}', '    \\label{' + FIGURA + '}', '',
            '    \\vspace{0.2cm}', '    \\begin{minipage}{0.95\\textwidth}', '        \\footnotesize',
            '        \\textbf{Legenda:} ' + inline(cap.group(2)), '',
            '        ' + inline(blocos[i + 2]), '    \\end{minipage}', '\\end{figure}']))
        i += 3
        continue
    elif b.startswith('Fonte:'):
        saida.append('{\\footnotesize ' + inline(b) + '\\par}')
    else:
        saida.append(inline(b))
    i += 1

open(DESTINO, 'w').write('\n\n'.join(saida) + '\n')
print('blocos:', len(blocos), 'saída:', len(saida))
