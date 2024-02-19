import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 38
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.2, 4.2)
ax.set_ylim(-0.2, 4.2)

ax.plot([-0.2, 0], [0, 0], linewidth=2, color='black')

x = np.linspace(0, 4.2, 1000)
for a, color in zip([0.25, 1, 3], ['red', 'orange', 'black']):
    ax.plot(x, x**a, linewidth=2, color=color)

for (x, y), label, color in zip(
    [(3.2, 1), (3.1, 2.5), (2.1, 3.3)],
    [r'$a = \frac{1}{4}$', '$a=1$', '$a=3$'],
    ['red', 'orange', 'black']):
    ax.annotate(
        xy=(x, y),
        text=label,
        color=color,
        fontsize=38,
        va='center',
        ha='center'
    )

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.set_xticks(ticks=[0, 1, 2, 3, 4])
ax.set_yticks(ticks=[0, 1, 2, 3, 4])

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)