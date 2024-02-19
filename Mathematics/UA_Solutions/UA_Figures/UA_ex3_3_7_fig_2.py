import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-0.05, 3.05)
ax.set_ylim(-0.05, 1.05)

ax.add_patch(plt.Rectangle(
    xy=(0, 0),
    width=1,
    height=1,
    facecolor=(1, 0, 0, 0.4)
))

for (x, y) in [(x, y) for x in [2, 8/3] for y in [0, 2/3]]:
    ax.add_patch(plt.Rectangle(
        xy=(x, y),
        width=1/3,
        height=1/3,
        facecolor=(1, 0, 0, 0.4)
    ))

ax.plot([0.5, 1.05], [1.05, 0.5], linewidth=1, color=(0, 0, 1))
ax.plot([2.5, 3.05], [1.05, 0.5], linewidth=1, color=(0, 0, 1))

ax.annotate(
    text=r'$C_n \to C_{n+1}$',
    fontsize=24,
    xy=(1.5, 0.5),
    va='center',
    ha='center'
)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)