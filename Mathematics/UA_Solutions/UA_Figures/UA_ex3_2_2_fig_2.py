import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()
ax.axis('off')
ax.set_aspect('equal')

ax.set_xlim(-1.6, 1.6)
ax.set_ylim(-0.3, 0.3)
ax.axhline(y=0, color='black', linewidth=1.2)

for x, s in zip([-1, 0.4, 1], ['-1', 'x', '1']):
    ax.add_patch(plt.Circle(
        xy=(x, 0),
        radius=0.02,
        facecolor='black',
        zorder=3
    ))
    ax.annotate(
        text=f'${s}$',
        fontsize=20,
        xy=(x, 0),
        xytext=(0, 16),
        textcoords='offset pixels',
        ha='center',
        va='center'
    )

for x in [-1.3, -0.7, 0.1, 0.7, 1.3]:
    ax.add_patch(plt.Circle(
        xy=(x, 0),
        radius=0.015,
        facecolor='white',
        edgecolor='black',
        zorder=3
    ))

for x in [-1.3, 0.7]:
    ax.plot([x, x + 0.6], [0, 0], linewidth=3, color=(0, 0.7, 0))

ax.plot([0.1, 0.7], [0, 0], linewidth=3, color=(1, 0, 0))

ax.add_patch(FancyArrowPatch(
    (0.4, 0.2),
    (1.0, 0.2),
    color='black',
    arrowstyle='<->',
    mutation_scale=10,
    shrinkA=0,
    shrinkB=0
))

ax.annotate(
    text=r'$\epsilon$',
    fontsize=20,
    xy=(0.7, 0.2),
    ha='center',
    va='center',
    bbox=dict(facecolor='white', edgecolor='none', pad=5)
)

ax.annotate(
    text=r'$V_{\epsilon/2}(x)$',
    fontsize=18,
    color=(1, 0, 0),
    xy=(0.4, -0.12),
    ha='center',
    va='center'
)

for x in [-1, 1]:
    ax.annotate(
        text=fr'$V_{{\epsilon/2}}({x})$',
        fontsize=18,
        color=(0, 0.7, 0),
        xy=(x, -0.12),
        ha='center',
        va='center'
    )

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()