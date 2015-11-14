import math
from decimal import *

def set_precision(func):
        def nfunc(*args):
            getcontext().prec = 10
            return float(func(*args))
        return nfunc

class Calc:
    def __init__(self):
        getcontext().prec = 10

    @staticmethod
    @set_precision
    def add(x, y):
        return Decimal(x) + Decimal(y)

    @staticmethod
    @set_precision
    def sub(x, y):
        return Decimal(x) - Decimal(y)

    @staticmethod
    @set_precision
    def mul(x, y):
        return Decimal(x) * Decimal(y)

    @staticmethod
    @set_precision
    def div(x, y):
        return Decimal(x) / Decimal(y)

    @staticmethod
    @set_precision
    def root(x, y):
        if y < 1 or x < 0:
            raise ValueError
        return Decimal(x) ** (Decimal(1) / Decimal(int(y)))