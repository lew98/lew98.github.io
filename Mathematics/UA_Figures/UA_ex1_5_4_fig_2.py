import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 48
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()

x = np.linspace(1, 55, 1000)
y = 1 / x

ax.grid()
ax.set_axisbelow(True)
ax.plot(x, y, color='black', linewidth=3)

ax.add_patch(plt.Circle((0.038, 0.953), 0.01, transform=ax.transAxes, facecolor='white', edgecolor='black', linewidth=1, zorder=2))

ax.set_xlim(-1, 52)
ax.set_ylim(-0.05, 1.05)
ax.set_xticks(ticks=[1], labels=['$a$'])
ax.set_yticks(ticks=[0, 1])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()