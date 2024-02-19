import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 48
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot()

def f(x):
    return x / (x**2 - 1)

x = np.linspace(-0.999, 0.999, 1000)
y = f(x)

ax.grid()
ax.set_axisbelow(True)
ax.plot(x, y, color='black', linewidth=3)

ax.set_xlim(-1.05, 1.05)
ax.set_ylim(-10, 10)
ax.set_xticks(ticks=[-1, 0, 1])
ax.set_yticks(ticks=[0])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()