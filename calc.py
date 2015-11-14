import math
from decimal import *


class Calc:
    def __init__(self):
        getcontext().prec = 10

    @staticmethod
    def add(x, y):
        return float(Decimal(x) + Decimal(y))

    @staticmethod
    def sub(x, y):
        return float(Decimal(x) - Decimal(y))

    @staticmethod
    def mul(x, y):
        return float(Decimal(x) * Decimal(y))

    @staticmethod
    def div(x, y):
        return float(Decimal(x) / Decimal(y))

    @staticmethod
    def root(x, y):
        return float(math.pow(x, float(Decimal(1) / Decimal(y))))