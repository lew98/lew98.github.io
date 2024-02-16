import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 32
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsfonts} \DeclareMathSymbol{\shortminus}{\mathbin}{AMSa}{"39}'

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-5.2, 5.2)

x = np.linspace(-1.2, 1.2, 100000)
y = (5 * x * np.sin(1 / x) - 3 * np.cos(1 / x)) / (3 * np.sign(x) * (np.abs(x) ** (1/3)))

ax.plot(x, y, linewidth=1.5, color='black')

n = np.arange(1, 23)
x_n = 1 / (np.pi * (1 + 2 * n))
g_n = np.cbrt(np.pi * (1 + 2 * n))

ax.scatter(x_n, g_n, marker='.', s=100, color='red', zorder=3)

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.annotate(
    xy=(0.6, -1),
    text="$g_{5/3}'$",
    fontsize=40,
    ha='center',
    va='center'
)

ax.annotate(
    xy=(0.4, 3.2),
    text="$g_{5/3}'(x_n)$",
    color='red',
    fontsize=32,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[-1, 0, 1], labels=[r'$\shortminus 1$', '$0$', '$1$'])
ax.set_yticks(ticks=[-4, -2, 0, 2, 4], labels=[r'$\shortminus 4$', r'$\shortminus 2$', '$0$', '$2$', '$4$'])

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)