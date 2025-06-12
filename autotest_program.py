import unittest
from math import pi

def area(r):
    if isinstance(r, str) is True:
        area = "TypeError"
    elif r < 0:
        area = "ValueError: radius can't be negative"
    else:
        area = pi * r * r
    return area

def circumference(r):
    if not isinstance(r, (int,float)):
        raise TypeError("Expected numeral")
    if r < 0:
        raise ValueError("Radius can't be negative")
    else:
        area = pi * r * r
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
        with self.assertRaises(TypeError):
            circumference("bggg")
            circumference("")
            circumference("10**-9")
            
if __name__ == "__main__":
    unittest.main()