import math
from decimal import Decimal, getcontext, InvalidOperation

PRECISION = 12


class Complex():
    def __init__(self, im, real):
        self.im = im
        self.real = real

    def __str__(self):
        return "Complex(" + str(self.real) + ", " + str(self.im) + ")"

    def __eq__(self, other):
        return self.im == other.im and self.real == other.real

def start():
    first = float(raw_input("enter first operand: "))
    second = float(raw_input("enter second operand: "))
    action = str(raw_input("your operation: "))
    print str(interpretator(first, action, second))

def interpretator(x, operation, y):
    if operation == 'root by':
        return root(Decimal(x), Decimal(y))
    if operation == '+':
        return add(Decimal(x), Decimal(y))
    if operation == '-':
        return sub(Decimal(x), Decimal(y))
    if operation == '*':
        return mult(Decimal(x), Decimal(y))
    if operation == '/':
        return div(Decimal(x), Decimal(y))
    raise InvalidOperation


def root(x, y):
    getcontext().prec = PRECISION
    if float(y).is_integer() != True:
        raise ValueError
    if y < 1:
        raise ValueError
    if x < 0 and y % 2 != 0:
        return (-1) * float(abs(x) ** (Decimal(1) / y))
    elif x < 0 and y == 2:
        return Complex(1, float(abs(x) ** (Decimal(1) / y)))
    elif x < 0:
        raise ValueError
    else:
        return float(x ** (Decimal(1) / y))


def add(x, y):
    getcontext().prec = PRECISION
    return float(x + y)

def sub(x, y):
    getcontext().prec = PRECISION
    return float(x - y)

def mult(x, y):
    getcontext().prec = PRECISION
    return float(x * y)

def div(x, y):
    getcontext().prec = PRECISION
    res = float(x / y)
    return res

