


# 1. UNORDERED 
# items appear in a different order every time you use
# no index or key

# 2. UNCHANGEABLE
# 3. NO DUPLICATE  - duplication will be ignored

mySet = {'a', 'b', 'c'}

# The only way to access a set LMAO
for x in mySet:
    print(" ")

# add()
mySet.add('d')

# update() => Set concatenation
herSet = {'e','f','g'}
mySet.update(herSet)
# update() can add any type of object

# remove()
mySet.remove('g')
# If the item to remove does not exist, remove() will raise an error.

# discard()
mySet.discard('f')
# will NOT raise an error

# pop()
mySet.pop()

# clear() the same as key word 'del'
mySet.clear()

# union()
set1 = {"a","b","c", 1}
set2 = {1, 2, 3}

# The union() method returns a new set with all items from both sets:
set3 = set1.union(set2)
# the same as update() lel

# Both union() and update() will exclude any duplicate items.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# intersection_update() get the intersection
x.intersection_update(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# symmetric_difference_update() get everything leaving the intersection
x.symmetric_difference_update(y)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# same as the s_d_update but can be assigned to a value
z = x.symmetric_difference(y)

# copy() is available

"""
    isdisjoint() Returns whether two sets have a intersection or not
    issubset() True if all items in the set exists in the specified set
    issuperset() True if all items in the specified set exists in the original set
"""
















