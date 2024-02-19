import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 40
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

ax.axvline(x=0, linewidth=2, linestyle=':', color=(0, 0, 0, 0.3))

ax.plot([-1.2, 0, 1.2], [0, 0, 1.2], linewidth=2, color='black')

ax.annotate(
    xy=(0, -0.3),
    text=r'$y = \max \{ 0, x \}$',
    fontsize=40,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[0])
ax.set_yticks(ticks=[0])

ax.xaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(width=2)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)