import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.size'] = 24
rcParams['text.usetex'] = True
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot()
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')

# for x, y in zip([9, 11], [4/45, 1/9]):
#     ax.axvline(x=x, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
#     ax.axhline(y=y, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

ax.axvline(x=0, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))
ax.axhline(y=0, linewidth=1, linestyle=':', color=(0, 0, 0, 0.3))

x = np.linspace(-1, 1, 10000)
y = x * np.sin(1 / x)

ax.plot(x, y, linewidth=1, color='black')

ax.annotate(
    xy=(0.6, -0.3),
    text=r'$y = \begin{cases} x \sin \left( \frac{1}{x} \right) & \text{if } x \neq 0, \\ 0 & \text{if } x = 0. \end{cases}$',
    fontsize=24,
    ha='center',
    va='center'
)

ax.set_xticks(ticks=[0])
ax.set_yticks(ticks=[0])

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)