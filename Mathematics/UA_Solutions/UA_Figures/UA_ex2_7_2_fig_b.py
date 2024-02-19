import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [np.sin(1)]
for j in range(2, 33):
    a_n.append(a_n[-1] + np.sin(j) / j**2)

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')

ax.set_xlim(0, 31)
ax.set_ylim(0.8, 1.2)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0.9, 1, 1.1])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()