#loop
a = 'Hello World'
# print(a[0])

# for char in a:
    # print(char)

# print(len(a))

# print("Hello" in a)

# if ('Hello' in a):
#     print('Hi World')

# if ('Duc Minh' not in a):
#     print('Goodbye World')

#SLICING
# print(a[0:5]) == print(a[:5])

# print(a.upper().lower())

# print(a)

# .strip() remove white space

b = a.replace('H', "J")
# print(b)
c = a.split(" ")
# print(c)


x = 'Hello'
y = 123
z = 10.05

xyz = "{0} John, {2} years old, from Universe #{1}"

result = xyz.format(x,y,z)
# print(result)


# print("BaBy".center(20,"a")) 0000banana0000...
# print("BaBy".casefold()) baby
# print("BaBy".count('B')) 2
# print("BaBy".endswith('y')) True
# print("BaBy".find('A'))  -1
# print("BaBy".index('A')) error

'''

RETURN TRUE FALSE

isalnum() word and num
isalpha() alphabet
isdecimal() 0-9
isdigit() not for Roman
isidentifier() true if valid string
isnumeric() num
isprintable()
isspace() white space
istitle() all word capitalized
islower() and isupper()

'''
#JOIN

myArray = ['You', 'and', 'I']
mySeperator = ' '

myNewArray = mySeperator.join(myArray)
# print(myNewArray)


#LJUST
txt = 'abc'
# print(txt.ljust(20), 'd')

#LSTRIP functions opposite to txt

# maketrans() and translate()
_txt = "Hi Sam!"
x = "mSa"
y = "eLo"
myTable = _txt.maketrans(x, y)
# find each character and replace with new character
# print(txt.translate(myTable))

# replace()
new_txt = 'I love javascript'
text = new_txt.replace('javascript', 'python')
# print(text)

# partition()

txt2 = "I could eat bananas all day"
_x = txt2.partition("bananas")
# print(_x)

"""
Search for the word "bananas", and return a tuple with three elements:
1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
If the specified value is not found, the partition() method returns a tuple containing: 
1 - the whole string
2 - an empty string
3 - an empty string
"""

# splitlines() Splits the string at line breaks and returns a list

# swapcase() reverse case

# title() convert to Title

# zfill() Fills the string with a specified number of 0 values at the beginning











































