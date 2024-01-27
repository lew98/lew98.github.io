import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot()

def f(n):
    return (np.sin(n**2)) / (np.cbrt(n))

n = np.arange(1, 33)
a_n = f(n)

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')

ax.set_xlim(0, 31)
ax.set_ylim(-0.7, 0.7)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()