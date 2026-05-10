import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Font of the Labels
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'ariel','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()

#Location of the labels
# you can also define the location of the labels using the loc parameter in the title, xlabel and ylabel functions. The possible values for loc are 'left', 'center' and 'right' for the title, and 'top', 'center' and 'bottom' for the x and y labels.        
#labelpad is used to adjust the distance of the label from the axis. The default value is 4.0
plt.title("Sports Watch Data", loc = 'left') # supported values are left, right, center.
plt.xlabel("Average Pulse", loc = 'right') # supported values are left, right, center.
plt.ylabel("Calorie Burnage", loc = 'top', labelpad=-40) # supported values are top, bottom, center.
plt.plot(x, y)
plt.show()