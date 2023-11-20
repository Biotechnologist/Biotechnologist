# -*- coding: utf-8 -*-
import numpy as np
from scipy import integrate
#import scipy
#import matplotlib as mpl
#import pandas
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# def f1(x):
#    return x**2

# def f2(x):
#    return x**3

# x = np.array([1,3,4])
# y1 = f2(x)

# I1 = integrate.simpson(y1, x)
# print(I1)

def func(x):
    return (x - 3) * (x - 5) * (x - 9) + 85


a, b = 2, 9  # integral limits
x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)

# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)

fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])

plt.show()