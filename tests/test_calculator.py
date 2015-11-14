# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("..")
from calc import Calc


class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    #add
    
    def test_add_integer(self):
        self.assertEqual(self.calc.add(20, 10), 30)

    def test_add_float(self):
        self.assertEqual(self.calc.add(3.5, 2.7), 6.2)

    def test_add_swap_operands(self):
        self.assertEqual(self.calc.add(2.7, 3.5), 6.2)

    def test_add_negative_and_positive(self):
        self.assertEqual(self.calc.add(-2.7, 3), 0.3)

    def test_add_negative_operands(self):
        self.assertEqual(self.calc.add(-0.3, -4.2), -4.5)

    #sub
        
    def test_sub_integer(self):
        self.assertEqual(self.calc.sub(20, 10), 10)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub(3.5, 2.7), 0.8)

    def test_sub_swap_operands(self):
        self.assertEqual(self.calc.sub(2.7, 3.5), -0.8)

    def test_sub_negative_and_positive(self):
        self.assertEqual(self.calc.sub(-2.7, 3), -5.7)

    def test_sub_negative_operands(self):
        self.assertEqual(self.calc.sub(-0.3, -4.2), 3.9)

    #mul

    def test_mul_integer(self):
        self.assertEqual(self.calc.mul(20, 10), 200)

    def test_mul_float(self):
        self.assertEqual(self.calc.mul(3.5, 2.7), 9.45)

    def test_mul_swap_operands(self):
        self.assertEqual(self.calc.mul(2.7, 3.5), 9.45)

    def test_mul_negative_and_positive(self):
        self.assertEqual(self.calc.mul(-2.7, 3), -8.1)

    def test_mul_negative_operands(self):
        self.assertEqual(self.calc.mul(-0.3, -4.2), 1.26)

    #div

    def test_div_integer(self):
        self.assertEqual(self.calc.div(20, 10), 2)

    def test_div_float(self):
        self.assertEqual(self.calc.div(7.22, 0.1), 72.2)

    def test_div_negative_and_positive(self):
        self.assertEqual(self.calc.div(-8.88, 0.1), -88.8)

    def test_div_negative_operands(self):
        self.assertEqual(self.calc.div(-8.65, -0.01), 865)

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, self.calc.div, 5, 0)

    #root

    def test_root_integer(self):
        self.assertEqual(self.calc.root(4, 2), 2)

    def test_root_float(self):
        self.assertEqual(self.calc.root(0.25, 2), 0.5)

    def test_zero_root(self):
        self.assertRaises(ValueError, self.calc.root, 10, 0)

    def test_root_negative(self):
        self.assertRaises(ValueError, self.calc.root, -27, 3)