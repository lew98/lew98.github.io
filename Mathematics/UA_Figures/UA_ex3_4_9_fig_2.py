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
ax.set_ylim(-0.15, 0.12)

ax.axhline(y=0, linewidth=1.2, color='black')

for x, label in zip([0.1, 0.9], ['$a$', '$b$']):
    ax.add_patch(plt.Circle(
        xy=(x, 0),
        radius=0.01,
        facecolor='black',
        zorder=3
    ))
    ax.annotate(
        text=label,
        fontsize=20,
        xy=(x, 0.05),
        va='center',
        ha='center'
    )

for x in [0, 0.35, 0.7, 1]:
    ax.add_patch(centred_rectangle(
        x=x,
        y=0,
        width=0.01,
        height=0.03,
        facecolor='black'
    ))

ax.plot([0, 0.35], [0, 0], linewidth=2, color='black')
ax.plot([0.7, 1], [0, 0], linewidth=2, color='black')

for x, label in zip([0.35, 0.7], [r'$r_m + \epsilon_m$', r'$r_n + \epsilon_n$']):
    ax.annotate(
        text=label,
        fontsize=16,
        xy=(x, 0.05),
        va='center',
        ha='center'
    )

for x, label in zip([0.175, 0.85], [r'$V_{\epsilon_m}(r_m)$', r'$V_{\epsilon_n}(r_n)$']):
    ax.annotate(
        text=label,
        fontsize=20,
        xy=(x, -0.075),
        va='center',
        ha='center'
    )

plt.tight_layout()

plt.savefig(Path(__file__).with_suffix('.pdf'), format="pdf", bbox_inches="tight", pad_inches=0)