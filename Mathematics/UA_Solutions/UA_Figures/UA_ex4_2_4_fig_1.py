import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(10,4.5))
ax = fig.add_subplot()
ax.set_xlim(0.5, 18.5)
ax.set_ylim(-0.9, 1.1)

ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], -0.4),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=1,
    facecolor=(0, 1, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], -0.9),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=0.5,
    facecolor=(1, 0, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(ax.get_xlim()[0], 0.6),
    width=ax.get_xlim()[1] - ax.get_xlim()[0],
    height=0.5,
    facecolor=(1, 0, 0, 0.1)
))

for x, y in zip([2, 18], [-0.4, 0.6]):
    ax.axvline(x=x, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
    ax.axhline(y=y, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

ax.axvline(x=1, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
ax.axvline(x=10, linewidth=1, color=(0, 0, 0, 0.5))
ax.axhline(y=0.1, linewidth=1, color=(0, 0, 0, 0.5))

for x in range(1, 18):
    ax.plot([x, x+1], [1/x, 1/x], linewidth=2, color='black')
    ax.add_patch(plt.Circle(
        xy=(0, 0),
        radius=0.025,
        facecolor='white',
        edgecolor='black',
        zorder=3,
        transform=(fig.dpi_scale_trans + transforms.ScaledTranslation(x+1, 1/x, ax.transData))
    ))

ax.annotate(
    xy=(12, 0.35),
    text=r'$y = \frac{1}{[[x]]}$',
    fontsize=28,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[1, 2, 10, 18])
ax.set_yticks(ticks=[-0.4, 0.1, 0.6, 1], labels=[r'$-\frac{2}{5}$', r'$\frac{1}{10}$', r'$\frac{3}{5}$', '$1$'])

for label in ax.get_yticklabels()[:-1]:
    label.set_fontsize(30)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)