import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y, color = "darkblue", marker = "X")

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = "aquamarine", marker = "x")

plt.show()

# You can use specific colors for each point by passing an array with the same length as the x and y arrays, and specifying the color for each point:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()


# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='hsv')
plt.colorbar(label='Color Scale') # add a colorbar to the plot, for reference. I have specified the location.
plt.show()


x = np.array([5,7,8,7,2,8,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,67,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, c =colors, cmap = "hsv", alpha=0.5) # alpha is used to set the transparency of the points.
#The value ranges from 0 to 1, where 0 is completely transparent and 1 is completely opaque.
plt.show()
# You can use a clolormap to get the best visual effects, with transparency