
def numberGenerator(n):
     number = yield
     while number < n:
         yield number
         number += 1

myGenerator = numberGenerator(3)

print(next(myGenerator))
print(myGenerator.send(2))
# print(next(myGenerator))

li = [x for x in range(4)]
# print(li)

g = (x for x in range(4))
# print(list(g))
# print(next(li))
# print(next(li))
# print(next(li))
