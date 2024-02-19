import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n_odd = np.arange(1, 33, 2)
x_n_odd = -1 + 2 / n_odd

n_even = np.arange(2, 33, 2)
x_n_even = 1 + 2 / n_even

ax.grid()
ax.set_axisbelow(True)
ax.plot(n_even, x_n_even, color='red', linewidth=1, marker='o', label='$x_{2n}$')
ax.plot(n_odd, x_n_odd, color='black', linewidth=1, marker='s', label='$x_{2n-1}$')

ax.legend(loc='upper right', fontsize=16, framealpha=1, edgecolor='black', fancybox=False)

ax.set_xlim(0, 31)
ax.set_ylim(-1.5, 4)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[-1, 1, 2])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()