import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 32
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsfonts} \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}'

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.22, 0.22)
ax.set_ylim(-0.0025, 0.0025)

x = np.linspace(-0.2, 0.2, 10000)
y = x**3 * np.sin(1 / x)

ax.plot(x, x**3, linewidth=1, color='red', linestyle='--')
ax.plot(x, -x**3, linewidth=1, color='red', linestyle='--')

ax.plot(x, y, linewidth=1.5, color='black')

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.annotate(
    xy=(0, -0.001),
    text='$g_3$',
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks([-0.2, 0, 0.2], labels=[r'$\shortminus 1/5$', '$0$', '$1/5$'])
ax.set_yticks([-0.002, 0, 0.002], labels=[r'$\shortminus \frac{1}{500}$', '$0$', r'$\frac{1}{500}$'])

for tick in ax.get_xticklabels()[::2]:
    tick.set_fontsize(28)

for tick in ax.get_yticklabels()[::2]:
    tick.set_fontsize(36)

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)