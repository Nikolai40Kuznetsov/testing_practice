import unittest
from math import pi

def area(r):
    return pi * r * r
def circumference(r):
    return r * pi * 2

class TestArea(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(area(2), 4*pi)

    def test_integer_negative_numbers(self):
        self.assertEqual(area(-2), "ValueError: radius can't be negative")

    def test_zero_number(self):
        self.assertEqual(area(0), 0.0)

    def test_float_positive_numbers(self):
        self.assertEqual(area(0.1), 0.01*pi)

    def test_error_input(self):
        self.assertEqual(area("bggg"), TypeError)
        self.assertEqual(area(""), TypeError)
        self.assertEqual(area("10**-9"), ValueError)

if __name__ == "__main__":
    unittest.main()