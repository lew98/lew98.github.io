import numpy as np, matplotlib.pyplot as plt, matplotlib.transforms as transforms
from matplotlib import rcParams
from pathlib import Path

rcParams['font.family'] = 'Computer Modern'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-8, 8)
ax.set_ylim(-6, 6)

fig.patch.set_facecolor((0.8, 0.8, 0.8))

def u(x):
    return np.where(x <= 0, np.sqrt(16 - (x - 2)**2), np.sqrt(16 - (x + 2)**2))
    
x = np.linspace(-2, 2, 1000)
y = u(x)

ax.fill_between(x, y + 1, -y + 1, edgecolor='None', facecolor='white')

ax.add_patch(plt.Circle(
    xy=(-2, 1),
    radius=4,
    facecolor='None',
    edgecolor='black',
    linewidth=2
))
ax.add_patch(plt.Circle(
    xy=(2, 1),
    radius=4,
    facecolor='None',
    edgecolor='black',
    linewidth=2
))

ax.annotate(
    xy=(0, 1),
    text=r'$A \cap B$',
    fontsize=40,
    va='center',
    ha='center'
)

ax.annotate(
    xy=(-4, 1),
    text='$A$',
    fontsize=40,
    va='center',
    ha='center'
)

ax.annotate(
    xy=(4, 1),
    text='$B$',
    fontsize=40,
    va='center',
    ha='center'
)

ax.annotate(
    xy=(0, -4.5),
    text=r'$(A \cap B)^{\mathsf{c}}$',
    fontsize=40,
    va='center',
    ha='center'
)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.svg'), format="svg", bbox_inches="tight", pad_inches=0)