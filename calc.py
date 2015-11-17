import math
from decimal import Decimal, getcontext, InvalidOperation

PRECISION = 12

def calc():
    first = float(raw_input("enter first operand: "))
    second = float(raw_input("enter second operand: "))
    action = raw_input("your operation: ")
    print interpretator(first, action, second)

def interpretator(x, operation, y):
    print "first operand: " + x
    print "operation: " + operation
    print "second operand: " + y
    if operation == 'root by':
        return root(x, y)
    if operation == '+':
        return add(x, y)
    if operation == '-':
        return sub(x, y)
    if operation == '*':
        return mult(x, y)
    if operation == '/':
        return div(x, y)

def root(x, y):
    getcontext().prec = PRECISION
    if y < 1 or x < 0:
        raise ValueError
    return float(Decimal(x) ** (Decimal(1) / Decimal(int(y))))

def add(x, y):
    getcontext().prec = PRECISION
    return float(Decimal(x) + Decimal(y))

def sub(x, y):
    getcontext().prec = PRECISION
    return float(Decimal(x) - Decimal(y))

def mult(x, y):
    getcontext().prec = PRECISION
    return float(Decimal(x) * Decimal(y))

def div(x, y):
    getcontext().prec = PRECISION
    try:
        res = float(Decimal(x) / Decimal(y))
    except ZeroDivisionError:
        print "Can't divide by zero"
        raise
    except InvalidOperation:
        print "Invalid format of operand"
        raise

    return res
