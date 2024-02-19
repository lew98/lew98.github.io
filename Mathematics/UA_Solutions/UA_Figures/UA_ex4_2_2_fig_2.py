import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(10,4.5))
ax = fig.add_subplot()

ax.add_patch(plt.Rectangle(
    xy=(1.8, 2),
    width=3.4,
    height=2,
    facecolor=(0, 1, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(1.8, 1.8),
    width=3.4,
    height=0.2,
    facecolor=(1, 0, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(1.8, 4),
    width=3.4,
    height=0.2,
    facecolor=(1, 0, 0, 0.1)
))

for x, y in zip([3, 2*np.pi - 3], [2, 4]):
    ax.axvline(x=x, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
    ax.axhline(y=y, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

ax.axvline(x=np.pi, linewidth=1, color=(0, 0, 0, 0.5))
ax.axhline(y=3, linewidth=1, color=(0, 0, 0, 0.5))

for x in [2, 3, 4]:
    ax.plot([x, x+1], [x, x], linewidth=3, color='black')
    ax.add_patch(plt.Circle(
        xy=(0, 0),
        radius=0.05,
        facecolor='white',
        edgecolor='black',
        zorder=3,
        transform=(fig.dpi_scale_trans + transforms.ScaledTranslation(x+1, x, ax.transData))
    ))

ax.annotate(
    xy=(3.6, 3.6),
    text=r'$y = [[x]]$',
    fontsize=24,
    ha='center',
    va='center'
)

ax.set_xlim(1.8, 5.2)
ax.set_ylim(1.8, 4.2)
ax.set_xticks(ticks=[2, 3, np.pi, 4, 5], labels=['$2$', '$3$', r'$\pi$', '$4$', '$5$'])
ax.set_yticks(ticks=[2, 3, 4])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)