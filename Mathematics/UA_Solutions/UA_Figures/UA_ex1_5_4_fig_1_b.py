import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 48
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()

ax.grid()
ax.set_axisbelow(True)
ax.plot([-0.9, 0.8975], [-0.5, 0.4975], color='black', linewidth=3)

ax.add_patch(plt.Circle((-0.9, -0.5), 0.02, facecolor='white', edgecolor='black', linewidth=1, zorder=2))
ax.add_patch(plt.Circle((0.9, 0.5), 0.02, facecolor='white', edgecolor='black', linewidth=1, zorder=2))

ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-1.05, 1.05)
ax.set_xticks(ticks=[-0.9, 0, 0.9], labels=['$a$', r'$\frac{a + b}{2}$', '$b$'])
ax.set_yticks(ticks=[-0.5, 0, 0.5], labels=['$-1$', '$0$', '$1$'])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()