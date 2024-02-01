import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot()

n = np.arange(1, 33)

partials = {
    -1 : [1],
    0 : [1],
    0.5 : [1],
    1 : [1],
    1.25 : [1],
    2 : [1]
}

for j in range(2, 33):
    for p in [-1, 0, 0.5, 1, 1.25, 2]:
        partials[p].append(partials[p][-1] + 1 / j**p)


ax.grid()
ax.set_axisbelow(True)

x = np.linspace(1, 33)
ax.fill_between(x, np.log(x) + 0.57721 + 1/(2*x), 33, color='red', alpha=0.1)
ax.fill_between(x, 1, np.log(x) + 0.57721 + 1/(2*x), color='green', alpha=0.1)

ax.plot(n, partials[-1], color='red', linewidth=0.5, marker='^', label='$p=-1$')
ax.plot(n, partials[0], color='red', linewidth=0.5, marker='s', label='$p=0$')
ax.plot(n, partials[0.5], color='red', linewidth=0.5, marker='P', label='$p=1/2$')
ax.plot(n, partials[1], color='red', linewidth=0.5, linestyle=(0, (4, 4)), marker='o', label='$p=1$')
ax.plot(n[:21], partials[1.25][:21], color='green', linewidth=0.5, marker='X', label='$p=5/4$')
ax.plot(n[29:], partials[1.25][29:], color='green', linewidth=0.5, marker='X')
ax.plot(n, partials[2], color='green', linewidth=0.5, marker='x', label='$p=2$')

ax.text(x=22, y=4.5, s=r'$p \leq 1, \mathrm{divergent}$', color='red', fontsize=20)
ax.text(x=21.8, y=2.65, s=r'$p > 1, \mathrm{convergent}$', color='green', fontsize=20)

ax.legend(loc = 'upper right', fontsize=18, framealpha=1, edgecolor='black', fancybox=False)

ax.set_xlim(1, 31)
ax.set_ylim(1, 11)
ax.set_xticks(ticks=[1, 5, 10, 15, 20, 25, 30])
ax.set_yticks(ticks=[1, 5, 10])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight")
#plt.show()