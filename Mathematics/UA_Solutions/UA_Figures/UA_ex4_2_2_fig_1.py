import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot()
ax.set_aspect('equal')

ax.add_patch(plt.Rectangle(
    xy=(0, 1),
    width=8,
    height=2,
    facecolor=(0, 1, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(0, 0),
    width=8,
    height=1,
    facecolor=(1, 0, 0, 0.1)
))
ax.add_patch(plt.Rectangle(
    xy=(0, 3),
    width=8,
    height=0.2,
    facecolor=(1, 0, 0, 0.1)
))

for x, y in zip([1, 7], [1, 3]):
    ax.axvline(x=x, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
    ax.axhline(y=y, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

ax.axvline(x=4, linewidth=1, color=(0, 0, 0, 0.5))
ax.axhline(y=2, linewidth=1, color=(0, 0, 0, 0.5))

x = np.linspace(0, 8, 1000)
y = np.sqrt(x)

ax.plot(x, y, linewidth=3, color='black')

ax.annotate(
    xy=(4.6, 2.5),
    text=r'$y = \sqrt{x}$',
    fontsize=24,
    ha='center',
    va='center'
)

ax.set_xlim(0, 8)
ax.set_ylim(0, 3.2)
ax.set_xticks(ticks=[0, 1, 4, 7])
ax.set_yticks(ticks=[0, 1, 2, 3])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)