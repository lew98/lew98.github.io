import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()
#ax.axis('off')
ax.set_aspect('equal')
ax.grid()
ax.set_axisbelow(True)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks([0, 1/3, 2/3, 1], labels=['$0$', r'$\frac{1}{3}$', r'$\frac{2}{3}$', '$1$'], fontsize=32)
ax.set_yticks([0, 1/3, 2/3, 1], labels=['$0$', r'$\frac{1}{3}$', r'$\frac{2}{3}$', '$1$'], fontsize=32)

for (x, y) in [(x, y) for x in [0, 2/3] for y in [0, 2/3]]:
    ax.add_patch(plt.Rectangle(
        xy=(x, y),
        width=1/3,
        height=1/3,
        facecolor=(1, 0, 0, 0.4)
    ))

for s in np.linspace(0, 2, 14):
    ax.axline(xy1=(0, s), slope=-1, linewidth=1, color=(0, 0, 1))

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)