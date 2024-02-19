import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [0.5]
for j in range(2, 33):
    a_n.append(a_n[-1] * (1.0 - 1.0 / (2.0 * j)))

ax.grid()
ax.set_axisbelow(True)
ax.plot(n, a_n, color='black', linewidth=1, marker='s')

ax.set_xlim(0, 31)
ax.set_ylim(-0.1, 0.6)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[0, 0.5], labels=['$0$', r'$\frac{1}{2}$'])

ax.get_yticklabels()[1].set_fontsize(30)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()