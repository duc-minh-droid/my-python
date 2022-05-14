import json

x = { 'name': 'python' }

# dumps() - stringify
y = json.dumps(x)

# loads() - parse
z =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
p = json.loads(z)
print(p)

# legal convert

"""
    dict
    list
    tuple
    string
    int
    float
    True
    False
    None
"""

"""
    Python	JSON
    dict	Object
    list	Array
    tuple	Array
    str	    String
    int	    Number
    float	Number
    True	true
    False	false
    None	null
"""


# dumps(data, indent, seperator, sort_keys)
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(", ", " = ")))




