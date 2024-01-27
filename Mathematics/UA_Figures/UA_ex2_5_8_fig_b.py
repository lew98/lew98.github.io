import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

def f(n):
    if n == 1:
        return 3
    elif n == 2:
        return 2
    else:
        return (n - 3)/(n - 2)

n = np.arange(3, 33)
a_n = np.array([f(j) for j in n])

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')
ax.scatter([1, 2], [3, 2], color='red', marker='o')

ax.set_xlim(0, 31)
ax.set_ylim(-0.2, 3.2)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0, 1, 2, 3])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()