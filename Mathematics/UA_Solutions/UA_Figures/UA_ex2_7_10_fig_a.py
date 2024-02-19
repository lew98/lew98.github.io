import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(0, 33)
a_n = [2.0]
for j in range(1, 33):
    a_n.append(a_n[-1] * (1.0 + 2.0 ** (-j)))

ax.grid()
ax.set_axisbelow(True)
ax.plot(n, a_n, color='black', linewidth=1, marker='s')

ax.set_xlim(-1, 31)
ax.set_ylim(1.6, 5.4)
ax.set_xticks(ticks=[0, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[2, 3, 4, 5])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()