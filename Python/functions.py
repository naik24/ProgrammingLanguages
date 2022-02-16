num1 = 15
num2 = 0

def addnum(n1, n2):
    return n1 + n2

def subnum(n1, n2):
    return n1 - n2

def divnum(n1, n2):
    if n2 == 0:
        raise ValueError('cannot divide by 0')
    else:
        return n1 / n2

def mulnum(n1, n2):
    return n1 * n2

print(addnum(num1, num2))
print(subnum(num1, num2))
print(mulnum(num1, num2))
print(divnum(num1, num2))
