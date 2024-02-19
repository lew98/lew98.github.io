import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [7/6]
b_n = [1/3]
for j in range(2, 33):
    a_n.append(a_n[-1] + (1 / (3*j - 2) + 1 / (3*j - 1) - 1 / (3*j)))
    b_n.append(b_n[-1] + 1 / (3*j))

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x', label='$s_{3n}$')
ax.scatter(n, b_n, color='red', marker='s', label=r'$\frac{1}{3} \sum_{k=1}^n \frac{1}{k}$')

ax.legend(loc = 'lower right', fontsize=16, framealpha=1, edgecolor='black', fancybox=False)

ax.set_xlim(0, 31)
ax.set_ylim(-1.2, 3.2)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0, 1, 2, 3])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()