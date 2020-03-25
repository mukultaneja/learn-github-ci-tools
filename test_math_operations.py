
import unittest
from math_operations import MathOperations


class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.math_operations = MathOperations()

    def test_add(self):
        a, b = 5, 6
        result = self.math_operations.add(a, b)
        self.assertEqual(result, 11)

    def test_multiply(self):
        a, b = 5, 6
        result = self.math_operations.multiply(a, b)
        self.assertEqual(result, 30)

    def test_divide(self):
        a, b = 50, 10
        result = self.math_operations.divide(a, b)
        self.assertEqual(result, 5.0)

    def test_pow(self):
        a, b = 5, 2
        result = self.math_operations.pow(a, b)
        self.assertEqual(result, 25.0)


if __name__ == '__main__':
    unittest.main()
