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
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-0.1, 0.2)

ax.axhline(y=0, linewidth=1.2, color='black')

ax.add_patch(plt.Circle(
    xy=(0, 0),
    radius=0.015,
    facecolor='black'
))

ax.annotate(
    text='$x_1$',
    fontsize=24,
    xy=(0, 0.1),
    ha='center',
    va='center'
)

for x, label_1, label_2 in zip([-0.9, 0.9], ['(', ')'], [r'$x_1 - \epsilon_1$', r'$x_1 + \epsilon_1$']):
    ax.annotate(
        text=label_1,
        xy=(x, 0),
        fontsize=24,
        fontweight='bold',
        va='center',
        ha='center'
    )
    ax.annotate(
        text=label_2,
        xy=(x, 0.1),
        fontsize=24,
        va='center',
        ha='center'
    )

for x, label in zip([-0.45, 0.45], [r'$a_1 = x_1 - \frac{\epsilon_1}{2}$', r'$b_1 = x_1 + \frac{\epsilon_1}{2}$']):
    ax.add_patch(centred_rectangle(
        x=x,
        y=0,
        width=0.015,
        height=0.05,
        facecolor='black'
    ))
    ax.annotate(
        text=label,
        xy=(x, 0.1),
        fontsize=20,
        va='center',
        ha='center'
    )

ax.plot([-0.45, 0.45], [0, 0], linewidth=3, color='black')

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)