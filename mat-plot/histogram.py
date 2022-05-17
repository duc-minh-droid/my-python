import matplotlib.pyplot as plt
import numpy as np

y = np.array([15,25,25,35])
my_label = ['A','B','C','D']
my_explode = [0,0,0.1,0]
my_colors = ['black','b','hotpink','#4CAF50']

# colors = my_colors
# startangle reference to the trigonometry
plt.pie(y, labels = my_label, startangle=90, explode=my_explode, shadow=True)

plt.legend(title='Four Pies:') # for description
plt.show()

