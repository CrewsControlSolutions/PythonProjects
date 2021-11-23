import math

def exponentFunction(x,y):
    z = x**y
    return z


def getNumbers():
    a = float(input('Enter the operand that the exponent will act on, but not the exponent itelf. '))
    b = float(input('Enter the exponent. '))
    result = exponentFunction(a,b)
    print(result)

performCalculation = getNumbers

performCalculation()
