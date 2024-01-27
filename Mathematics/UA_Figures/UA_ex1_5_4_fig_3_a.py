import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 50.0
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()

ax.grid()
ax.plot([0, 1], [0, 1], color='black', linewidth=2)

ax.add_patch(plt.Circle((0, 0), 0.009, facecolor='white', edgecolor='black', linewidth=1, zorder=2))
ax.add_patch(plt.Circle((1, 1), 0.009, facecolor='white', edgecolor='black', linewidth=1, zorder=2))

def radius(j):
    if j <= 5:
        return 0.009
    else:
        return 0.009 / np.sqrt(j - 4)
n = 50
for j in range(2, n + 2):
    ax.add_patch(plt.Circle((1/j, 1/j), radius(j), facecolor='white', edgecolor='black', linewidth=1, zorder=2))
    ax.add_patch(plt.Circle((1/j, 1/(j-1)), radius(j), color='black', zorder=2))

ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks(ticks=[0, 1/5, 1/4, 1/3, 1/2, 1], labels=['$0$', r'$\frac{1}{5}$', r'$\frac{1}{4}$', r'$\frac{1}{3}$', r'$\frac{1}{2}$', '$1$'])
ax.set_yticks(ticks=[0, 1/5, 1/4, 1/3, 1/2, 1], labels=['$0$', '$1/5$', '$1/4$', '$1/3$', '$1/2$', '$1$'])

for tick in ax.get_xticklabels()[1:-1]:
    tick.set_fontsize(40)

y_ticksizes = [18, 23, 30, 30]
for tick, size in zip(ax.get_yticklabels()[1:-1], y_ticksizes):
    tick.set_fontsize(size)

fig.text(0.233, 0.1125, r'$\cdots$', fontsize=40)
fig.text(0.122, 0.28, r'$\cdot$', fontsize=40)
fig.text(0.122, 0.26, r'$\cdot$', fontsize=40)
fig.text(0.122, 0.24, r'$\cdot$', fontsize=40)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()