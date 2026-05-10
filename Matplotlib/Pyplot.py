import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 67])
ypoints = np.array([0, 250])

# Linear graph
plt.plot(xpoints, ypoints, color='red', linewidth=3)
plt.title("Linear graph")
plt.show()

# Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

#Plotting without x-points:
# The x-points in the example above are [0, 1, 2, 3, 4, 5].
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()


# Sine Graph
# Data generation
x = np.linspace(0, 360, 10000) # 100 x values from 0 to 2pi, creates values to which the sine function will be applied to, basically creates the x values. The np.linspace function generates 100 evenly spaced values between 0 and 2π.
y = np.arcsin(x) # applies the arcsine function to each of the x values, creating the corresponding y values for the sine wave.

# Visualization
plt.plot(x, y, color='black', linewidth=2)
plt.title("Arc Sin Wave Graph")
plt.xlabel("Angle [rad]")
plt.ylabel("arcsin(x)")
plt.grid(True)
plt.show()