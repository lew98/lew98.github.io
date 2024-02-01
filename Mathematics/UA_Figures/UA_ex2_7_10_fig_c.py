import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [4.0/3.0]
for j in range(2, 33):
    a_n.append(a_n[-1] * (1.0 + 1.0 / (4.0 * j**2 - 1.0)))

ax.grid()
ax.set_axisbelow(True)
ax.plot(n, a_n, color='black', linewidth=1, marker='s')

ax.set_xlim(0, 31)
ax.set_ylim(1.27, 1.62)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[4.0/3.0, np.pi/2.0], labels=[r'$\frac{4}{3}$', r'$\frac{\pi}{2}$'])

for tick in ax.get_yticklabels():
    tick.set_fontsize(30)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()