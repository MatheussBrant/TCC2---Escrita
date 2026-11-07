#!/usr/bin/env python3
"""Figura descritiva de primeiros aceites, sem novas execuções do pipeline."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
DEST = HERE.parents[1] / 'manuscrito/assets/capitulo-5'
DEST.mkdir(parents=True, exist_ok=True)
with (HERE / 'estrategias.csv').open() as stream:
    rows = list(csv.DictReader(stream))
models = ['GPT-4.1 mini', 'GPT-5.6 Luna', 'GPT-6 Luna']
strategies = ['P1', 'P2', 'P3', 'P4']
colors = ['#24476b', '#437ca0', '#36897e', '#95b96c', '#e1e4e8']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, ax = plt.subplots(figsize=(9.4, 3.8), layout='constrained')
left = [0, 0, 0]
for i, strategy in enumerate(strategies + ['Sem aceite']):
    values = [next(int(r['numerador']) for r in rows if r['modelo'] == model and r['estrategia'] == strategy)
              if strategy in strategies else 78-left[j] for j, model in enumerate(models)]
    bars = ax.barh(models, values, left=left, height=.53, color=colors[i], label=strategy,
                   edgecolor='white', linewidth=1)
    for j, (bar, val) in enumerate(zip(bars, values)):
        ax.text(left[j]+val/2, bar.get_y()+bar.get_height()/2, str(val), ha='center', va='center',
                color='white' if i < 3 else '#26323e', fontsize=10)
    left = [a+b for a,b in zip(left, values)]
assert left == [78, 78, 78]
ax.invert_yaxis()
ax.set_xlim(0, 78)
ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 78])
ax.set_xlabel('Casos (78 por modelo)')
ax.set_title('Primeiro aceite por estratégia na definição principal de F', loc='left', pad=45, fontsize=12)
ax.legend(ncol=5, loc='lower left', bbox_to_anchor=(0, 1.01), frameon=False, fontsize=9)
ax.spines[['top', 'right', 'left']].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.set_axisbelow(True)
ax.grid(axis='x', alpha=.15)
for extension in ('png', 'pdf', 'svg'):
    fig.savefig(DEST / ('aceites-por-estrategia.' + extension), dpi=220)
plt.close(fig)
print('Figura exportada em PNG, PDF e SVG:', DEST)
