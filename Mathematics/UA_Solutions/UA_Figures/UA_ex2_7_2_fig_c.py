import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [1]
for j in range(2, 33):
    a_n.append(a_n[-1] + ((j + 1) / (2*j) if j % 2 == 1 else -(j + 1) / (2*j)))

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')

ax.set_xlim(0, 31)
ax.set_ylim(-0.2, 1.2)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0, 0.5, 1], labels=[r'$0$', r'$\frac{1}{2}$', r'$1$'])

ax.get_yticklabels()[1].set_fontsize(32)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()