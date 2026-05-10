import matplotlib.pyplot as plt
import numpy as np

# linestyle(ls)
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashdot')#dotted, dashed, dashdot, solid
plt.show()
"""
dotted = :
dashed = --
dashdot = -.
solid = -
none = ''
"""
#linecolor(c)
# use the color arguement, you can also use the shortcut color codes or RGB hexadecimal color codes.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = 'green')#b, g, r, c, m, y, k, w
plt.show()

# Line Width(lw or linewidth)
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
# Multiple Lines
# To plot more than one graph on the same figure, simply call the plot() function multiple times before calling show().
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()