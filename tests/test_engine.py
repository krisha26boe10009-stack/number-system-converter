"""
Unit tests for converter/engine.py
all tests run with python -m unittest tests
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from converter.engine import NumberConverter
from converter.validator import ValidationError


class TestToDecimal(unittest.TestCase):

    def setUp(self):
        self.conv = NumberConverter()

    def test_binary_to_decimal(self):
        self.assertEqual(self.conv.to_decimal("1010", 2), 10)

    def test_hex_to_decimal(self):
        self.assertEqual(self.conv.to_decimal("FF", 16), 255)

    def test_octal_to_decimal(self):
        self.assertEqual(self.conv.to_decimal("17", 8), 15)

    def test_negative_number_to_decimal(self):
        self.assertEqual(self.conv.to_decimal("-1010", 2), -10)


class TestFromDecimal(unittest.TestCase):

    def setUp(self):
        self.conv = NumberConverter()

    def test_decimal_to_binary(self):
        self.assertEqual(self.conv.from_decimal(10, 2), "1010")

    def test_decimal_to_hex(self):
        self.assertEqual(self.conv.from_decimal(255, 16), "FF")

    def test_zero_in_any_base(self):
        self.assertEqual(self.conv.from_decimal(0, 16), "0")

    def test_negative_decimal(self):
        self.assertEqual(self.conv.from_decimal(-10, 2), "-1010")


class TestFullConvertRoundTrip(unittest.TestCase):

    def setUp(self):
        self.conv = NumberConverter()

    def test_binary_to_hex_directly(self):
        result = self.conv.convert("11111111", 2, 16)
        self.assertEqual(result["output"], "FF")
        self.assertEqual(result["decimal_value"], 255)

    def test_round_trip_returns_original(self):
        # Convert base 7 -> base 29 -> back to base 7, should match.
        original = "6543"
        mid = self.conv.convert(original, 7, 29)
        back = self.conv.convert(mid["output"], 29, 7)
        self.assertEqual(back["output"], original)

    def test_invalid_digit_raises(self):
        with self.assertRaises(ValidationError):
            self.conv.convert("129", 2, 10)


if __name__ == "__main__":
    unittest.main()
