import numpy as np


# Create a ufunc
def my_add(x, y):
    return x+y
# pass to frompyfunc()
my_add = np.frompyfunc(my_add,2,1)
print(my_add([0,1],[2,3]))

# check if a func is ufunc
if type(np.add) == np.ufunc:
    print('OMG')


