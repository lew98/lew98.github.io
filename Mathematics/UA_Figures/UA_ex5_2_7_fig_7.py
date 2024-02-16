import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 40
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsfonts} \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}'

fig = plt.figure(figsize=(13, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.32, 0.32)
ax.set_ylim(-1.7, 1.7)

x = np.linspace(-0.32, 0.32, 100000)
y = (12 * x**2 - 1) * np.sin(1 / x) - 6 * x * np.cos(1 / x)

ax.plot(x, y, linewidth=1.5, color='black')

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.annotate(
    xy=(0, -1.35),
    text="$g_4''$",
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks([-0.2, 0, 0.2], labels=[r'$\shortminus 1/5$', '$0$', '$1/5$'])
ax.set_yticks([-1, 0, 1], labels=[r'$\shortminus 1$', '$0$', '$1$'])

for tick in ax.get_xticklabels()[::2]:
    tick.set_fontsize(38)

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)