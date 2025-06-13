import programm_13_06 as p_13
import unittest as ut
import math as m

class TestEqualize(ut.TestCase):
    def test_zero_number(self):
        self.assertListEqual(p_13(0, 0, 0), ["There is zero division",])
        self.assertListEqual(p_13(0, 0, 0), ["There is zero division",])
        self.assertListEqual(p_13(0, 0, 0), ["There is zero division",])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            p_13.equalize(1, -2, 3)

    def test_integer_positive_numbers(self):
        self.assertGreater(p_13(1, 1, 1), 0)
        self.assertLess(p_13(1, 1, 1), 0)

    def test_error_input(self):
        with self.assertRaises(TypeError):
            p_13.equalize("bggg", "bggg", "bggg")
            p_13.equalize("", "", "")
            p_13.equalize("10**-9", "10**-9", "10**-9")

if __name__ == "__main__":
    ut.main()
    