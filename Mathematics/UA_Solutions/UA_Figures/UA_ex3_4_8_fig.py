import numpy as np, matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch
from pathlib import Path

rcParams['text.usetex'] = True

def centred_rectangle(x, y, width, height, **kwargs):
    return plt.Rectangle(
        xy=(x - 0.5*width, y - 0.5*height),
        width=width,
        height=height,
        **kwargs
    )

fig = plt.figure(figsize=(9,3))
ax = fig.add_subplot()
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.4, 0.05)

ax.plot([0, 1], [0, 0], linewidth=2, color='black')
ax.plot([0, 1/3], [-0.1, -0.1], linewidth=2, color='black')
ax.plot([2/3, 1], [-0.1, -0.1], linewidth=2, color='black')
ax.plot([0, 1/9], [-0.2, -0.2], linewidth=2, color='black')
ax.plot([2/9, 1/3], [-0.2, -0.2], linewidth=2, color='black')
ax.plot([2/3, 7/9], [-0.2, -0.2], linewidth=2, color='black')
ax.plot([8/9, 1], [-0.2, -0.2], linewidth=2, color='black')

for label, y in zip(['$C_0$', '$C_1$', '$C_2$'], [0, -0.1, -0.2]):
    ax.annotate(
        text=label,
        fontsize=20,
        xy=(1.1, y),
        ha='center',
        va='center'
    )

for x in [1/18, 5/18, 13/18, 17/18, 1.1]:
    ax.annotate(
        text=r'$\cdots$',
        fontsize=20,
        xy=(x, -0.3),
        ha='center',
        va='center',
        rotation=90
    )

for x, label in [(0, '$a$'), (1/3, '$b$')]:
    ax.add_patch(centred_rectangle(
        x=x,
        y=-0.1,
        width=0.004,
        height=0.02,
        color='black'
    ))
    ax.annotate(
        text=label,
        fontsize=16,
        xy=(x, -0.06),
        ha='center',
        va='center'
    )

for x, label in [(0.3, '$x$'), (0.7, '$y$'), (0.5, r'$t = b + \frac{1}{6}$')]:
    ax.add_patch(plt.Circle(
        xy=(x, -0.1),
        radius=0.004,
        color='black'
    ))
    ax.annotate(
        text=label,
        fontsize=16,
        xy=(x, -0.06),
        ha='center',
        va='center'
    )

ax.plot([1/3, 2/3], [-0.1, -0.1], linewidth=1, linestyle='--', color='black')
ax.annotate(
    text='(',
    fontsize=14,
    fontweight='heavy',
    xy=(1/3, -0.1),
    xytext=(2, 0),
    textcoords='offset pixels',
    ha='center',
    va='center'
)
ax.annotate(
    text=')',
    fontsize=14,
    fontweight='heavy',
    xy=(2/3, -0.1),
    xytext=(-3, 0),
    textcoords='offset pixels',
    ha='center',
    va='center'
)
ax.annotate(
    text=r'$\left( b, b + \frac{1}{3} \right)$',
    fontsize=16,
    xy=(0.5, -0.15),
    ha='center',
    va='center'
)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)