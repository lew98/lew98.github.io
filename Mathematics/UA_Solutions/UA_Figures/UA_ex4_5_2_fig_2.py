import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 40
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.8, 10)

for x in [0, 2]:
    ax.axvline(x=x, linewidth=2, linestyle=':', color=(0, 0, 0, 0.3))
ax.axhline(y=1, linewidth=2, linestyle=':', color=(0, 0, 0, 0.3))

x = np.linspace(0.01, 1.99, 1000)
y = 1 / (x * (2 - x))

ax.plot(x, y, linewidth=2, color='black')

ax.annotate(
    xy=(1, 3),
    text=r'$y = \frac{1}{x(2 - x)}$',
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[0, 2])
ax.set_yticks(ticks=[1])

ax.xaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(width=2)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)