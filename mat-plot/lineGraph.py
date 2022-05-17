import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 13, 16])
# If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.
ypoints = np.array([3, 10, 15, 18])

# fmt: 'marker|line|color'
# o*.,xX+sDpv | -:-- -. | rgbcmykw
# ms = 'marker size' number, mec = 'marker color', mfc for coloring entire marker, ls = 'linestyle', linewidth = '20', can use hexadecimal code
plt.plot(xpoints, ypoints)

# subplot() create 2 seprate plots and add subplot for each, can add title for each
# The subplot() function takes three arguments that describes the layout of the figure. The layout is organized in rows and columns, which are represented by the first and second argument. The third argument represents the index of the current plot.
# suptitle() the title for the entire figure

# multiple line 
# plt.plot(xpoints, color='b')
# plt.plot(ypoints, color='g')

# Or
# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
# plt.plot(x1, y1, x2, y2)

# font
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

# title
plt.title('Loser Data', fontdict = font1)
# loc = 'left|right|center'

# label the graph
plt.xlabel('effort', fontdict = font2)
plt.ylabel('chance to get her', fontdict = font2)

# add grid
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# axis = 'x|y|both'

plt.show()
















