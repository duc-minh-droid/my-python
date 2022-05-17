
import numpy as np

# Create a numpy array
array = np.array([1,2,3,4])

# Count dimension in an array
dcount = array.ndim

# use keyword argument 'ndmin' to specify the dimension
multiDarray = np.array([1,2,3,4], ndmin=5)

# find the data type of the array
# print(multiDarray.dtype)

'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

'''

# Specify the data type using 'dtype'
arr = np.array([1,2,3,4], dtype='S')
arr2 = np.array([1,2,3,4], dtype='i4')

# Change the data type of every item
arr3 = np.array([1.1,2.1,3.1])
newArr = arr3.astype('i')

# view a ndarray, changes in view affect the original array, DOES NOT own the data
x = arr.view()

# copy a ndarray, changes in view DOES NOT affect the original array, own the data
y = arr.copy()

# base returns None if array owns the data, otherwise return the original array
print(x.base)
print(y.base)

# shape returns a tuple with each element being the element amount in the nested dimension
z = np.array([1, 2, 3, 4], ndmin=2)
print('shape of array :', z.shape)

# reshaping ~ reconstruct an array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# 4 nested arrays with 3 elements each
newarr = arr.reshape(4, 3)
# This is a view not a copy

# pass in -1 when dimension count is unknown, python will calculate the rest
newarr = arr.reshape(2, 2, -1)

# FLATTENING AN ARRAY
newarr = arr.reshape(-1)

# Looping through dimensional arrays
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Remember to pass the array to the iter function
# nditer() similar to iter() without next()
# change data type: flags=['buffered'], op_dtypes=['']
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Different Step
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)

# ndenumerate() looping while printing the index of each element
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
      # idx is the index
  print(idx, x)

# Array concatenation 
arrX = np.array([1, 2, 3])
arrY = np.array([4, 5, 6])
arrZ = np.concatenate((arrX, arrY))

# stack() concatenating array value with one another, along with the axis?
arrM = np.stack((arrX, arrY), axis=1)

arr = np.array([1, 2, 3, 4, 5, 6])
# array_split() split the original array into 4 smaller arrays
newarr = np.array_split(arr, 4, axis=0)
# print(newarr) ==> [array([1, 2]), array([3, 4]), array([5]), array([6])]

# where() ~ return a list containing the indexes of value where the condition is satisfied
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # BOOLEAN
# print(x) => (array([3, 5, 6],)

# searchsorted() ~ The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 12, side='left') # output: 1
# The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])

# Create an array from the elements on index 0 and 2:
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

# Using an array as index ?
print(arr[[0,1,3,2]])
# Python will iterate the given array and use its elements as indexes for accessing the new array




