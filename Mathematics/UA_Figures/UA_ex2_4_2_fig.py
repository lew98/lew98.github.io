import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot()

n = np.arange(1, 33)
a_n = [1]
for _ in range(31):
    a_n.append(3 - 1 / a_n[-1])

ax.grid()
ax.set_axisbelow(True)
ax.scatter(n, a_n, color='black', marker='x')

ax.set_xlim(0, 31)
ax.set_ylim(0.8, 2.8)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[1.5 + 0.5 * np.sqrt(5)], labels=[r'$\frac{3}{2} + \frac{1}{2} \sqrt{5}$'])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()