

#1 Ordered
#2 Unchangeable - No change, add, remove, delete, ...
#3 Allow duplicate


# HOW TO CHANGE A TUPLE?

x = ('apple','pineapple', 'pen')
y = list(x)
y[2] = 'ppap'
x = tuple(y)

# tuple do not support append()
x += ('banana',)

# convert to a list to use remove()
y.remove('ppap')
x = tuple(y)

# UNPACKING A TUPLE
(a, b) = x

longTuple = ('a','b','c','d','e','f','g')
(m, n, *p) = longTuple

# print(p) => ['c', 'd', 'e', 'f', 'g']

# MULTIPLY THE CONTENT
longerTuple = longTuple * 2
# totally work with list too !

# TWO FUCKING METHODS HAHA
# count() index()


































































