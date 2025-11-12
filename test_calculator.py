# https://github.com/natecl/Lab11-HG-NC.git
# Partner 1: Hanna Green
# Partner 2: Nathan Chin-Lue

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertAlmostEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(-1, -9), -10)
        self.assertAlmostEqual(add(678, 0), 678)

    def test_subtract(self): # 3 assertions
        self.assertAlmostEqual(sub(0, 0), 0)
        self.assertAlmostEqual(sub(-1, -9), 8)
        self.assertAlmostEqual(sub(678, 0), 678)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertAlmostEqual(mul(0, 0), 0)
        self.assertAlmostEqual(mul(-1, -9), 9)
        self.assertAlmostEqual(mul(678, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(4, 2), 2)
        self.assertEqual(div(-100, 10), -10)
        self.assertEqual(div(0, 50), 0)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(log(10, 10), 1)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(1, 10), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-45)
            square_root(-1)
        self.assertEqual(square_root(9), 3)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()