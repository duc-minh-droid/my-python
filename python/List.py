
# List is basically Array

# changeable, allows duplication, can use lens(array), can contain different data type

thislist = list(("apple", "banana", "cherry")) # convert Set to List

"""
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable, and un-indexed. No duplicate members.
    Dictionary is a collection which is ordered and changeable. No duplicate members.

    ordered means have index for each element
"""

myList = ['BMW',"Bucciarati", 'Giorno']

# insert() add item knowing the location to add
myList.insert(3,'Diavolo')

# append() push item to the end of list
myList.append([])

# extend() list concatenation << also work with other array type >>
myList.extend(['mandrake','poison ivy'])

# remove() delete ONE specified VALUE
myList.remove([])

# pop() delete ONE specified INDEX
myList.pop(-1)

# another way to delete an item knowing its index
del myList[0]

# clear() return an empty list
myList.clear()


newList = ['sadness', 'happiness', 'anger']

# for x in newList:
#     print(x) => x is the Value 

# for i in range(len(newList)):
#     print(i) => i is the Index

# i = 0
# while i < len(newList):
#     print(newList[i])
#     i = i + 1 
# => i++ do not exist / use i = i + 1 instead

# [print(x) for x in newList] => shorthand for looping, [] is REQUIRED

# newlist = ['expression' for 'item' in 'iterable' if 'condition == True']

fixedList = [x for x in newList if 's' in x]
# print(fixedList)

''' 
he expression is the current item in the iteration,
but it is also the outcome,
which you can manipulate before it ends up like a list item in the new list
'''

upperList = [x.upper() for x in fixedList]
# print(upperList)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruitList = [x if x != "banana" else "orange" for x in fruits] # function like the map() tho
# print(fruitList)

# sort() alphabetical and numerical
# reverse a list

fruitList.sort(reverse = True)
# all capital letters being sorted before lower case letters

# if you want a case-insensitive sort function, use str.lower as a key function
fruitList.sort(key = str.lower)

# reverse()
fruitList.reverse()

# 2 ways to copy a list
toBuyList = fruitList.copy()
toBuyListCopy = list(toBuyList)

# concatenate list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# to a new list
list3 = list1 + list2

# to an existing list
for x in list2:
    list1.append(x)

list2.extend(list1)

# count the number of an item in a list
item = list2.count(1)







