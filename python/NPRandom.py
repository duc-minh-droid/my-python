# https://www.w3schools.com/python/numpy/numpy_random.asp
from array import array
import numpy as np
from numpy import random

# random integer
x = random.randint(10)
print(x)

# random float to 1
y = random.rand()
print(y)

# random array of integer
z = random.randint(4, size=5)
print(z)

# random 1-D array
m = random.rand(5)
print(m)

# random 2-D array
n = random.rand(3, 2) # the shape of the array: 3 arrays with 2 elements
print(n)

# random element in an array
p = random.choice([10,2,3,9]) # returns a number from the array
print(p)

# random multidimensional array from an array
q = random.choice([1,3,5,7], size=(4,2))
print(q)

# PROBABILITY
a = random.choice(['6 stars unit','5 stars unit','4 stars unit','3 stars unit'],
                     p = [0.05,0.1,0.35,0.5], size=10) 
# p for probability, pass in p an array with the same length containing the probability
print(a) # returns an array with given size

# for x in a:
#     if x == '6 stars unit':
#         print('Ultra Rare')

# shuffle() an array
arr = np.array([0,1,2,3,4])
random.shuffle(arr) # change the original array
print(arr)

# permutation() like shuffle but better
new_arr = random.permutation(arr) # DOES NOT change the original array
print(new_arr)
















