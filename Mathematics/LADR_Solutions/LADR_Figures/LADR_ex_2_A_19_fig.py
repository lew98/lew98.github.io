import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 32
rcParams['font.family'] = 'Computer Modern'
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.set_aspect('equal')
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)

ax.plot([0, 1/3, 0.5, 1], [1, 1, 0, 0], linewidth=2, color='black')

ax.grid(color='black', alpha=0.3, linewidth=1.5, linestyle=':')
ax.set_xticks([0, 1/3, 0.5, 1], labels=['$0$', r'$\frac{1}{j}$', r'$\frac{1}{j-1}$', '$1$'])
ax.set_yticks([0, 1])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.svg'), format="svg", bbox_inches="tight", pad_inches=0)