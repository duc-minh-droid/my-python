import os

"""
    READ
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
"""

# open('path',method)
f = open("D:\Storage\python\Files\\read.txt",'r')
# read() return the value of the txt file
# print(f.read()) 

# specify how many character to read
# print(f.read(5))

# readline() read only one line
# print(f.readline())

# loop in a file to read line by line
# for x in f:
#     print(x)

# close() a file after done
f.close()

# append more text to existing file
f = open("D:\Storage\python\Files\\read.txt", "a")
# write() 
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("D:\Storage\python\Files\\read.txt", "r")
# print(f.read())
f.close()

# overwrite the content of the file
f = open("D:\Storage\python\Files\\read.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("D:\Storage\python\Files\\read.txt", "r")
# print(f.read())
f.close()


'''
    "x" - Create - will create a file, returns an error if the file exist
    "a" - Append - will create a file if the specified file does not exist
    "w" - Write - will create a file if the specified file does not exist
'''

# f = open("myfile.txt", "x")

# os.path.exists() return True if exists
if os.path.exists("D:\Storage\python\Files\myfile.txt"):
    # os.remove() remove a file
  os.remove("D:\Storage\python\Files\myfile.txt")
else:
  print("The file does not exist")

# os.rmdir() => remove a folder




