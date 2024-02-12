import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.1, 0.17)

ax.axhline(y=0, linewidth=1.2, color='black')

for x in [-0.9, -0.5, -0.3, 0, 0.3, 0.5, 0.9]:
    ax.add_patch(plt.Circle(
        xy=(x, 0),
        radius=0.01,
        facecolor='white',
        edgecolor='black',
        zorder=3
    ))

ax.annotate(
    text=r'$\sqrt{2}$',
    fontsize=20,
    xy=(0, 0.07),
    ha='center',
    va='center'
)

for x in [-0.17, 0.17]:
    ax.annotate(
        text=r'$\cdots$',
        fontsize=20,
        xy=(x, 0.07),
        ha='center',
        va='center'
    )

for x, label in zip([0.4, 0.7, 1.05], ['$E_3$', '$E_2$', '$E_1$']):
    ax.annotate(
        text=label,
        fontsize=20,
        xy=(x, 0.07),
        ha='center',
        va='center'
    )
    ax.annotate(
        text=label,
        fontsize=20,
        xy=(-x, 0.07),
        ha='center',
        va='center'
    )

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)