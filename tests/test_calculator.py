# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("..")
from calc import interpretator, Complex, div, root
from decimal import InvalidOperation


class CalculatorTestCase(unittest.TestCase):

    #some direct tests

    def test_zero_div_direct(self):
        self.assertRaises(ZeroDivisionError, div, 5, 0)

    def test_invalid_root(self):
        self.assertRaises(ValueError, root, -25, 4)

    def test_float_root(self):
        self.assertRaises(ValueError, root, 4, 2.12)

    def test_complex_sqrt(self):
        self.assertEqual(root(-4, 2), Complex(1, 2))


    #test operations directly through interpretator

    def test_right_root(self):
        self.assertEqual(interpretator(4, "root by", 2), 2)

    def test_rigth_float_root(self):
        self.assertEqual(interpretator(4.0, "root by", 2.0), 2.0)

    def test_right_real_float_root(self):
        self.assertEqual(interpretator(0.25, "root by", 2), 0.5)

    def test_root_neg_with_odd_pow(self):
        self.assertEqual(interpretator(-27, "root by", 3), -3)

    def test_precision_of_root(self):
        self.assertEqual(interpretator(15, "root by", 3), 2.46621207433)

    def test_zero_root(self):
        self.assertRaises(ValueError, interpretator, 16, "root by", 0)

    def test_root_str_param(self):
        self.assertEqual(interpretator('16', "root by", '2'), 4)

    def test_root_bad_operand(self):
        self.assertRaises(InvalidOperation, interpretator, '12s', "root by", 3)

    def test_add_right_operands(self):
        self.assertEqual(interpretator(1, "+", 1), 2)

    def test_add_right_real_numbers(self):
        self.assertEqual(interpretator(1.2, "+", 2.3), 3.5)

    def test_add_with_negative(self):
        self.assertEqual(interpretator(2.0, "+", -1.1), 0.9)

    def test_add_str_interpretation(self):
        self.assertEqual(interpretator('3.7', '+', '1.2'), 4.9)

    def test_add_bad_operand(self):
        self.assertRaises(InvalidOperation, interpretator, '1q', '+', 20)

    def test_sub_right(self):
        self.assertEqual(interpretator(4, '-', 2), 2)

    def test_sub_with_negative(self):
        self.assertEqual(interpretator(1, '-', -1), 2)

    def test_sub_negative_result(self):
        self.assertEqual(interpretator(10, '-', 20), -10)

    def test_sub_real_numbers(self):
        self.assertEqual(interpretator(1.9, '-', 0.5), 1.4)

    def test_sub_real_to_negative(self):
        self.assertEqual(interpretator(2.3, '-', 3.0), -0.7)

    def test_sub_from_zero(self):
        self.assertEqual(interpretator(0, '-', 5), -5)

    def test_sub_with_str(self):
        self.assertEqual(interpretator('4', '-', '2'), 2)

    def test_sub_from_negative_to_posit(self):
        self.assertEqual(interpretator(-5, '-', -10), 5)

    def test_sub_bad_operand(self):
        self.assertRaises(InvalidOperation, interpretator, 'test', '-', 20)

    def test_mult_right(self):
        self.assertEqual(interpretator(2, '*', 2), 4)

    def test_mult_with_neg(self):
        self.assertEqual(interpretator(2, '*', -3), -6)

    def test_mult_real_numbers(self):
        self.assertEqual(interpretator(2.5, '*', 2.0), 5)

    def test_mult_neg_real(self):
        self.assertEqual(interpretator(-2.5, '*', 2.0), -5)

    def test_mult_with_str(self):
        self.assertEqual(interpretator('1.2', '*', '2'), 2.4)

    def test_mult_bad_operand(self):
        self.assertRaises(InvalidOperation, interpretator, '3q1', '*', 1)

    def test_div_right(self):
        self.assertEqual(interpretator(4, '/', 2), 2)

    def test_div_real_numbers(self):
        self.assertEqual(interpretator(3.2, '/', 0.5), 6.4)

    def test_div_neg(self):
        self.assertEqual(interpretator(-5, '/', 2), -2.5)

    def test_div_str(self):
        self.assertEqual(interpretator('12', '/', '2.0'), 6)

    def test_div_bad_operand(self):
        self.assertRaises(InvalidOperation, interpretator, 'q', '/', 20)

    def test_bad_operation(self):
        self.assertRaises(InvalidOperation, interpretator, 1, '^', 2)