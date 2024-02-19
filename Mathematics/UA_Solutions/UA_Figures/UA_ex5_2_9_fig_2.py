import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 40
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsfonts} \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}'

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.11, 0.11)
ax.set_ylim(-1.25, 2.25)

x = np.linspace(-0.11, 0.11, 100000)
y = 0.5 + 2* x * np.sin(1 / x) - np.cos(1 / x)

ax.plot(x, y, linewidth=1.5, color='black')

n = np.arange(1, 151)
x_n = 1 / (2 * np.pi * n)

ax.scatter(x_n, [-0.5] * len(n), marker='.', s=100, color='red', zorder=3)
    
ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.annotate(
    xy=(0.03, 1.875),
    text="$f'$",
    fontsize=40,
    ha='center',
    va='center'
)

ax.annotate(
    xy=(0.03, -0.875),
    text="$f'(x_n)$",
    color='red',
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks([-0.1, 0, 0.1], labels=[r'$\shortminus 1/10$', '$0$', '$1/10$'])
ax.set_yticks([-0.5, 0.5, 1.5], labels=[r'$\shortminus \frac{1}{2}$', r'$\frac{1}{2}$', r'$\frac{3}{2}$'], fontsize=56)

for tick in ax.get_xticklabels()[::2]:
    tick.set_fontsize(32)

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)