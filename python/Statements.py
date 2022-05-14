
a = 1
b = 10
c = 100

if a > c or b > c:
    pass #print("A")
elif a < c and b < c:
    pass #print("B")
else:
    pass # do nothing only for no errors

x = 1
y = 2
z = 3

# print('Haizz') if x > z else print('I lost') if y > z else print('Couldn\'t do anything')

i = 0
while(i < 10):
    i+=1
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print('No bugs') # if breakout of loop, the else block will not be executed

# range(start, end, step)
for x in range(0,10,2): # if x is already declared, still works smh
    print(x)
else:
    print('...')


































