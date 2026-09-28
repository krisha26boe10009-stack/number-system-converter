"""
Unit test for converter/validator.py 
all tests run by python -m unittest discover tests
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from converter.validator import validate_base, validate_number, ValidationError


class TestValidateBase(unittest.TestCase):

    def test_valid_base_accepted(self):
        # Should not raise
        validate_base(2)
        validate_base(16)
        validate_base(36)

    def test_base_too_low_rejected(self):
        with self.assertRaises(ValidationError):
            validate_base(1)

    def test_base_too_high_rejected(self):
        with self.assertRaises(ValidationError):
            validate_base(37)

    def test_non_integer_base_rejected(self):
        with self.assertRaises(ValidationError):
            validate_base("16")


class TestValidateNumber(unittest.TestCase):

    def test_valid_binary_number(self):
        self.assertEqual(validate_number("1010", 2), "1010")

    def test_valid_hex_number_lowercased_input(self):
        self.assertEqual(validate_number("ff", 16), "FF")

    def test_invalid_digit_for_base_rejected(self):
        with self.assertRaises(ValidationError):
            validate_number("129", 2)  # '9' and '2' invalid in binary

    def test_empty_string_rejected(self):
        with self.assertRaises(ValidationError):
            validate_number("", 10)

    def test_negative_number_accepted(self):
        self.assertEqual(validate_number("-101", 2), "-101")

    def test_lone_minus_sign_rejected(self):
        with self.assertRaises(ValidationError):
            validate_number("-", 10)


if __name__ == "__main__":
    unittest.main()
