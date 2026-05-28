import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y,color="lightcoral", width = 0.5)# this plots a vertical bar chart
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, color="#4CAF50", height = 0.01)# this plots a horizontal bar chart
# the height argument does the same job as the width argument in the vertical bar chart
plt.show()

