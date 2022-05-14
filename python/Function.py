# Arbitrary Keyword Arguments - to deal with unknown number of arguments
def my_func(**name):
    # type '**' before a parameter
    print(name)

# pass in pairs of key - value, an object of parameters will be returned
my_func(name1 = 'Marc', name2 = 'Steve', name3 = 'Jake')

# Arbitrary Arguments - to deal with unknown number of arguments
def ur_func(*name):
    # type '*' before a parameter
    print(name)

# pass in value (primitive), a tuple will be returned
ur_func('Spector','Grant','Lockley')

def m_function(child3, child2, child1):
  print("The youngest child is " + child3)

# The parameters must equal to the arguments
m_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_sum(x, y):
    if (x < y):
        result = x + my_sum(x+1, y)
    else:
        result = x
    # print(result)
    return result

print(my_sum(1, 10))

def my_multiplier(a):
    return lambda b: b*a

# Call the function twice is actually OK
print(my_multiplier(2)(2))














































