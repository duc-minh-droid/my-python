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

# add arrays vertically
arr1 = np.array([10, 11, 12, 13, 14, 20])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)

# subtract arrays vertically
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)

# multiply arrays vertically
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)

# divide arrays vertically
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)

# power()
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)

# remainder() same as mod()
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)

# divmod() returns 2 arrays: the division and the remainder
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)

# absolute()
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)

# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])
arr = np.fix([-3.9666, 3.6667])
print(arr)

# round off a number for ... decimals
arr = np.round(3.11223,2)
print(arr)

# floor() >< ceil()
arr = np.floor([3.9999, 4.123])
print(arr)

# pass in an array return the total sum of both arrays
newarr = np.sum([arr1, arr2], axis=1)
# pass in  the axis parameter to add horizontally or vertically
print(newarr)

# cumsum() partially adding the elements in array
arr = np.array([1, 2, 3])
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
newarr = np.cumsum(arr)

# prod() returns the total multiplication of every elements in array 
x = np.prod(arr)
# can specify the axis too
print(x)

# cumprod() works similarly to cumsum()

# A discrete difference means subtracting two successive elements.
arr = np.array([10, 15, 25, 5])
# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
newarr = np.diff(arr)

# We can perform this operation repeatedly by giving parameter n.

# E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]


num1 = 4
num2 = 6
# find the lowest common number
x = np.lcm(num1, num2)

# reduce() for working with arrays
# x = np.lcm.reduce(arr)


num1 = 6
num2 = 9
# find the greatest common denominator
x = np.gcd(num1, num2)

# arr = np.array([20, 8, 32, 36, 16])
# x = np.gcd.reduce(arr)

'''
np.cos()
ONLY sin cos tan NO cot()

np.pi/2 

convert degree to rad
np.degree2rad([])

calculate angles
np.arcsin(1.0) arccos arctan

calculate based on pythagoras formula
np.hypot(base, perp)


'''

# We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# remove duplicates, 1 dimension
x = np.unique(arr)
print(x)

# union two arrays return a 1D array
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
# To find the unique values of two arrays, use the union1d() method
newarr = np.union1d(arr1, arr2)

# find the intersection, assume-unique is set for better computation
newarr = np.intersect1d(arr1, arr2, assume_unique=True)

# setdiff1d() returns the difference Eg. returns A - B :A contains but B does not
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)

# setxor1d() returns the symmemtric difference, returns A and B without their intersection
newarr = np.setxor1d(arr1, arr2, assume_unique=True)




