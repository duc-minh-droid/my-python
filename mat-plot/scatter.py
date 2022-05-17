import matplotlib.pyplot as plt
import numpy as np

# requires two arrays of the same length
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y, color='b')

# second scatter
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors,s=sizes, alpha=0.5, cmap='nipy_spectral')
# cmap='viridis' a color array with the same length is also required
# s=sizes a size array with same length
# alpha = 0->1 transparency

# plt.colorbar() => show viridis color map
plt.xlabel('car age')
plt.ylabel('car speed')
plt.title('Car Data')
plt.show()


















