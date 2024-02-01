import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

def f(n):
    if n % 2 == 1:
        return 1 - n
    else:
        return 3 - n

n = np.arange(1, 33, 2)
a_n = np.array([f(j) for j in n])

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')

n_even = np.arange(2, 32, 2)
a_n_even = np.array([f(j) for j in n_even])
ax.scatter(n_even, a_n_even, color='red', marker='s')

ax.set_xlim(0, 31)
ax.set_ylim(-32, 5)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()