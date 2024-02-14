import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(10,4.5))
ax = fig.add_subplot()
ax.set_xlim(7.9, 11.1)
ax.set_ylim(0.07, 0.13)

ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], 2/25),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=1/25,
    facecolor=(0, 1, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], ax.get_ylim()[0]),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=0.01,
    facecolor=(1, 0, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], 0.12),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=0.01,
    facecolor=(1, 0, 0, 0.1)
))

for x, y in zip([9, 11], [0.08, 0.12]):
    ax.axvline(x=x, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
    ax.axhline(y=y, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

ax.axvline(x=8, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
ax.axvline(x=10, linewidth=1, color=(0, 0, 0, 0.5))
ax.axhline(y=0.1, linewidth=1, color=(0, 0, 0, 0.5))

for x in [8, 9, 10]:
    ax.plot([x, x+1], [1/x, 1/x], linewidth=2, color='black')
    ax.add_patch(plt.Circle(
        xy=(0, 0),
        radius=0.05,
        facecolor='white',
        edgecolor='black',
        zorder=3,
        transform=(fig.dpi_scale_trans + transforms.ScaledTranslation(x+1, 1/x, ax.transData))
    ))

ax.annotate(
    xy=(10.5, 0.11),
    text=r'$y = \frac{1}{[[x]]}$',
    fontsize=28,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[8, 9, 10, 11])
ax.set_yticks(ticks=[2/25, 1/10, 3/25], labels=[r'$\frac{2}{25}$', r'$\frac{1}{10}$', r'$\frac{3}{25}$'], fontsize=30)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)