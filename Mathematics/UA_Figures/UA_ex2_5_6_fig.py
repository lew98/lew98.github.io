import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot()

n = np.arange(1, 33)

ax.grid()
ax.set_axisbelow(True)

ax.scatter(n, np.power(2, 1/n), color='red', marker='^', label='$b=2$')
ax.scatter(n, np.ones(32), color='maroon', marker='.', label='$b=1$')
ax.scatter(n, np.power(0.5, 1/n), color='orange', marker='o', label='$b=1/2$')
ax.scatter(n, np.zeros(32), color='black', marker='x', label='$b=0$')

ax.legend(loc = 'upper right', fontsize=18, framealpha=1, edgecolor='black', fancybox=False)

ax.set_xlim(0, 31)
ax.set_ylim(-0.1, 2.1)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0, 1, 2])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()