import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 40
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsfonts} \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}'

fig = plt.figure(figsize=(14, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.11, 0.11)
ax.set_ylim(-0.07, 0.07)

x = np.linspace(-0.11, 0.11, 100000)
y = x / 2 + x**2 * np.sin(1 / x)

ax.plot(x, y, linewidth=1.5, color='black')

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.annotate(
    xy=(0.01, -0.02),
    text="$f$",
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks([-0.1, 0, 0.1], labels=[r'$\shortminus 1/10$', '$0$', '$1/10$'])
ax.set_yticks([-0.05, 0, 0.05], labels=[r'$\shortminus \frac{1}{20}$', '$0$', r'$\frac{1}{20}$'])

for tick in ax.get_xticklabels()[::2]:
    tick.set_fontsize(32)

for tick in ax.get_yticklabels()[::2]:
    tick.set_fontsize(44)

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)