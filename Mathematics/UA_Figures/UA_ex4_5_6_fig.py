import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-2.2, 2.2)

ax.plot([0, 0.2, 0.4, 0.6, 0.8, 1], [0, -2, 1, -1, 2, 0], linewidth=2, color='black')

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')

ax.set_xticks(ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], labels=['$0$', '$1/5$', '$2/5$', '$3/5$', '$4/5$', '$1$'])
ax.set_yticks(ticks=[-2, -1, 0, 1, 2])

ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)