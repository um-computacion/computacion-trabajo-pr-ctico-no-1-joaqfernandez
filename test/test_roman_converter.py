import unittest
from src.roman_converter import roman_to_decimal

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        decimal = roman_to_decimal('I')
        self.assertEqual(decimal, 1)

    def test_II(self):
        decimal = roman_to_decimal('II')
        self.assertEqual(decimal, 2)

    def test_III(self):
        decimal = roman_to_decimal('III')
        self.assertEqual(decimal, 3)

    def test_V(self):
        decimal = roman_to_decimal('V')
        self.assertEqual(decimal, 5)

    def test_VI(self):
        decimal = roman_to_decimal('VI')
        self.assertEqual(decimal, 6)

    def test_VIII(self):
        decimal = roman_to_decimal('VIII')
        self.assertEqual(decimal, 8)

    def test_IV(self):
        decimal = roman_to_decimal('IV')
        self.assertEqual(decimal, 4)

    def test_IX(self):
        decimal = roman_to_decimal('IX')
        self.assertEqual(decimal, 9)


if __name__ == '__main__':
    unittest.main()
