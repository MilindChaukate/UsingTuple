myTuple = (1, 2, 3, 4, 5)
print(myTuple)

myTuple2 = (2, 3)
print(myTuple + myTuple2)

print(type(myTuple))

for i in myTuple:
    print(i)

i = 0
while i < len(myTuple):
    print(myTuple[i])
    i = i + 1

print(myTuple[3])
print(myTuple[-3])
print(myTuple[-3:-1])
print(myTuple[:-3])
print(myTuple[-3:])

temp = list[myTuple2]
temp.clear
myTuple2 = tuple(temp)
print(myTuple2)