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
ax.set_ylim(-0.25, 0.16)

ax.axhline(y=0, linewidth=1.2, color='black')

ax.add_patch(plt.Circle(
    xy=(0, 0),
    radius=0.015,
    facecolor='black',
    zorder=3
))

ax.annotate(
    text='$x$',
    fontsize=24,
    xy=(0, 0.07),
    ha='center',
    va='center'
)

ax.plot([-1, 1], [0, 0], linewidth=3, color=(0, 0.8, 0))
for x in [-1, 1]:
    ax.add_patch(centred_rectangle(
        x=x,
        y=0,
        width=0.016,
        height=0.05,
        facecolor=(0, 0.8, 0),
        zorder=3
    ))

ax.plot([-0.1, 0.8], [0, 0], linewidth=3, color=(1, 0, 0))
for x in [-0.1, 0.8]:
    ax.add_patch(centred_rectangle(
        x=x,
        y=0,
        width=0.016,
        height=0.05,
        facecolor=(1, 0, 0),
        zorder=3
    ))

ax.annotate(
    xy=(0.35, -0.08),
    text=r'$I_N$',
    fontsize=20,
    color=(1, 0, 0),
    ha='center',
    va='center'
)

ax.annotate(
    xy=(0, -0.14),
    text=r'$V_{\epsilon}(x)$',
    fontsize=28,
    color=(0, 0.8, 0),
    ha='center',
    va='center'
)

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)