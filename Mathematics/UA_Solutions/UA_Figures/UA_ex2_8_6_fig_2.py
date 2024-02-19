import numpy as np, matplotlib.pyplot as plt, matplotlib.patches as patches
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()
ax.set_aspect('equal')

ek = patches.Polygon(
    xy=[[0, 6], [5, 6], [5, 5], [4, 5], [4, 4], [3, 4], [3, 3], [2, 3], [2, 2], [1, 2], [1, 1], [0, 1], [0, 6]],
    facecolor=(1, 0, 0, 0.1)
)

tNN = patches.Rectangle(
    xy=(0.032, 3.023),
    width=2.945,
    height=2.945,
    facecolor='none',
    edgecolor=(0, 0, 1, 0.8),
    linewidth=4
)

ax.add_patch(ek)
ax.add_patch(tNN)

for t in range(1, 6):
    ax.axhline(y=t, color='black', linewidth=0.7)
    ax.axvline(x=t, color='black', linewidth=0.7)

for i in range(1, 7):
    for j in range(1, 7):
        ax.annotate(
            text=f'$| a_{{ {i}{j} }} |$',
            xy=(j-0.5, 6.5-i),
            fontsize=36,
            ha='center',
            va='center'
        )

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