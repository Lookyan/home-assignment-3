import math
from decimal import Decimal, getcontext, InvalidOperation

PRECISION = 12

def start():
    lookCalc(input_func, action_input)

def input_func(message):
    return float(raw_input(message))

def action_input(message):
    return str(raw_input(message))

class Complex():
    def __init__(self, im, real):
        self.im = im
        self.real = real

    def __str__(self):
        return "Complex(" + str(self.real) + ", " + str(self.im) + ")"

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.im == other.im and self.real == other.real
        return NotImplemented

def lookCalc(get_inp, act_inp):
    first = get_inp("enter first operand: ")
    second = get_inp("enter second operand: ")
    action = act_inp("your operation: ")
    res = interpretator(first, action, second)
    print_result(res)
    return res

def interpretator(x, operation, y):
    output(x, operation, y)
    if operation == 'root by':
        return root(Decimal(x), Decimal(int(y)))
    if operation == '+':
        return add(Decimal(x), Decimal(y))
    if operation == '-':
        return sub(Decimal(x), Decimal(y))
    if operation == '*':
        return mult(Decimal(x), Decimal(y))
    if operation == '/':
        return div(Decimal(x), Decimal(y))
    raise InvalidOperation

def output(first, operation, second):
    print "first operand: " + str(first)
    print "operation: " + operation
    print "second operand: " + str(second)

def print_result(result):
    print "Result: " + str(result)

def root(x, y):
    getcontext().prec = PRECISION
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

