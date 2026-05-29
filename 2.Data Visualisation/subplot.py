import matplotlib.pyplot as plt
import numpy as np

# With the subplot() function you can draw multiple plots in one figure: 
#plt.subplot(x, y, z) the figure has x row, y columns, and this plot is the zth plot.

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES") # add a title to the first plot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME") # add a title to the second plot

plt.suptitle("MY SHOP") # add a title to the entire figure
plt.show()


# this is the same graph plotted horizontally:
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()


# Plotting 6 graphs in one figure with plt.subplot:
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x1,y1)

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x2,y2)

x3 = np.array([0, 1, 2, 3])
y3 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x3,y3)

x4 = np.array([0, 1, 2, 3])
y4 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x4,y4)

x5 = np.array([0, 1, 2, 3])
y5 = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x5,y5)

x6 = np.array([0, 1, 2, 3])
y6 = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x6,y6)

plt.show()

# This process is really slow
# There is another method we could use called plt.subplots

fig, axes = plt.subplots(nrows=2, ncols=3) # specifiying number of 

axes[0, 0].plot(x1, y1)
axes[0, 0].set_title("Plot 1") # you can also set the title for each singualr graph
axes[0, 1].plot(x2, y2)
axes[0, 1].set_title("Plot 2")
axes[0, 2].plot(x3, y3)
axes[0, 2].set_title("Plot 3")
axes[1, 0].plot(x4, y4)
axes[1, 0].set_title("Plot 4")
axes[1, 1].plot(x5, y5)
axes[1, 1].set_title("Plot 5")
axes[1, 2].plot(x6, y6)
axes[1, 2].set_title("Plot 6")
plt.show()