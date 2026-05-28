import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 154])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# You can also specifiy a custom label distance and a custom start angle:

plt.pie(y, labels = mylabels, labeldistance=1.1, startangle=90)
plt.show()


myexplode = [0.2, 0.5, 0, .67]
# using the explode function you can define the distance between the pie chart and the the selected pieces
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

# You calso add shadows to the pie pieces
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 

# You can also add colors to each pie section

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

# You can also add a legend
plt.title("Favourite Fruits")
plt.pie(y, labels = mylabels)
plt.legend(title = "People with favourite fruit as:",loc = "upper left")
plt.show() 