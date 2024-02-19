import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
from matplotlib import rcParams
from pathlib import Path

rcParams['text.usetex'] = True
rcParams['font.family'] = 'Computer Modern'

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()
ax.set_aspect('equal')
ax.axis('off')

for x in range(6):
    for y in range(6):
        ax.annotate(
            text=f'$a_{{ {6-y}{x+1} }}$',
            xy=(x + 0.5, y + 0.5),
            fontsize=50,
            ha='center',
            va='center'
        )

ax.plot([3, 3], [6, 3], linewidth=2, color='black')
ax.axhline(y=3, linewidth=2, color='black')

ax.add_patch(plt.Rectangle(
    xy=(3, 3),
    width=3,
    height=3,
    facecolor=(1, 0, 0, 0.2)
))

ax.add_patch(plt.Rectangle(
    xy=(0, 0),
    width=36,
    height=3,
    facecolor=(0, 0, 1, 0.2)
))

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)