import math

listOfNumbers = [4,8,3,9,0,7,3,1]
x = 0

for i in listOfNumbers:
    print(i)

print(listOfNumbers)

x = listOfNumbers.count(3)
print(x)

listOfNumbers.sort()
print(listOfNumbers)

a=lambda b, c: b**c

print(a(2,3))

d='merciful'
e='just'

print("God is sovereign, {}, and {}.".format(d,e))

print('binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}'.format(1))

