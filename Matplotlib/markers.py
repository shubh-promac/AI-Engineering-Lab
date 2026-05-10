import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
#Markers
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
plt.plot(ypoints, marker = '+', color = 'cornsilk', linewidth = 2, markersize = 30)
plt.show()

'''
Format Strings(fmt) 
They make life easier as you can set 3 parameters in one go, instead of setting them separately.
You can also use the shortcut string notation parameter to specify the marker.
This parameter is also called fmt, and is written with this syntax:
marker|line|color
markers:x,o,d,h,s,*,p,h,v,^,<,>,8,+
line: -, --, -., :
color: r g b c m y k w

You can use this in the form of fmt:
string = 'marker|line|color'
plt.plot(xpoints, ypoints, 'o:r') # this will plot the points with circle markers(o), dotted line(:) and red color(r)

You can aslo define marker size using the markersize(ms) parameter, and marker color using the markerfacecolor(mfc) parameter.
You can also use the markeredgecolor(mec) parameter to specify the color of the marker's edge, and markeredgewidth(mew) to specify the width of the marker's edge.
'''
plt.plot(ypoints, marker = '3', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()

plt.plot(ypoints, "X-.r",mfc= 'hotpink',mec= 'chartreuse', lw = 2, ms = 30) # i have set the format string to "X-r" which means I want to use X as marker, - as line and r as color. I can overide the color red with the "color = aqua" parameter
# I have set different colors, for marker, marker edge and line using the parameters
plt.show()