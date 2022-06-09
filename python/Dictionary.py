


import this


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict['brand']
x = thisdict.get('brand')

y = thisdict.keys() # return a list of keys
# for x in y:
#     print(thisdict[x])

z = thisdict.values() # return a list of values

m = thisdict.items() # return pairs of tuple in a list

# update()
thisdict.update({
    'brand': 'BMW',
    'year': 2023
})

thisdict.update({
    'color': 'red'
})

# Removal

thisdict.pop('brand')
thisdict.popitem()
del thisdict['model']
thisdict.clear()

# Copy
# newDict = yourDict.copy() or dict(yourDict)

# fromkeys()
x = ('key1', 'key2', 'key3')
y = ('same','not same') # All keys keep the same values
thisdict = dict.fromkeys(x, y)
# print(thisdict) => {'key1': 'same', 'key2': 'same', 'key3': 'same'}

# setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
# if "model" exists, return its value 'Mustang'
# if "model" does not exist, return the default value 'Bronco













































































