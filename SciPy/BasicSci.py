from scipy import constants
from scipy.optimize import root
from scipy.optimize import minimize
from math import cos

# 1 liter = 1000 cubic meters
print(constants.liter)
# dir(constants) => all constants

def eqn(x):
    return x + cos(x)

# root func takes in an equation and an initial guess of the value
myroot = root(eqn,0)
print(myroot.x)

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')
print(mymin.x)


# sparse data
from scipy.sparse import csr_matrix
import numpy as np

# remove the 0
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
# return a tuple (containing which row the element is in and its index) and its value

# get only the value
print(csr_matrix(arr).data)
# count non zero value
print(csr_matrix(arr).count_nonzero())

# csr_matrix(arr) .eliminate_zeros()
mat = csr_matrix(arr)
mat.sum_duplicates()
# remove duplicates

# tocsc() convert to csc














