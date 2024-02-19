import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()
ax.set_aspect('equal')

dk = patches.Polygon(
    xy=[[0, 6], [5, 6], [5, 5], [4, 5], [4, 4], [3, 4], [3, 3], [2, 3], [2, 2], [1, 2], [1, 1], [0, 1], [0, 6]],
    facecolor=(1, 0, 0, 0.1)
)

remainder = patches.Polygon(
    xy=[[0, 0], [0, 1], [1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4], [4, 4], [4, 5], [5, 5], [5, 6], [6, 6], [6, 0], [0, 0]],
    facecolor=(0, 0, 1, 0.1)
)

ax.add_patch(dk)
ax.add_patch(remainder)

for t in range(1, 6):
    ax.axhline(y=t, color='black', linewidth=0.7)
    ax.axvline(x=t, color='black', linewidth=0.7)

for i in range(1, 7):
    for j in range(1, 7):
        ax.text(
            x=j-0.5,
            y=6.5-i,
            s=f'$a_{{ {i}{j} }}$',
            fontsize=44,
            ha='center',
            va='center')

ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.tick_params(
    axis='both',
    which='both',
    bottom=False,
    top=False,
    left=False,
    right=False,
    labelbottom=False,
    labeltop=False,
    labelleft=False,
    labelright=False)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()