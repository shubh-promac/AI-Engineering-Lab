import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
#Grid Axis
# You can define if you want only a specific axis
# using plt.grid(axis = 'x') or plt.grid(axis = 'y') or plt.grid() uses both axis
plt.grid(color='gray', linestyle='--', linewidth=2) # you can define the grid with plt.grid(color='color', linestyle='linestyle', linewidth=width)
plt.show()

