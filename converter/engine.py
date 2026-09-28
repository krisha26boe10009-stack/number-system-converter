"""
---------
engine.py
---------
FUNCTIONAL MODULE 2: Conversion Engine

This is the actual "algorithm" part of the project (satisfies the
"correct application of subject concepts" technical expectation).

Strategy used: convert FROM any base TO decimal first and then
FROM decimal TO the target base. This is the standard textbook
approach and has the benefit of only requiring two algorithms
instead of one for every (from_base, to_base) pair -> Scalability
and Maintainability (non-functional requirements) are achieved.
"""

from .validator import DIGIT_SYMBOLS, validate_base, validate_number


class NumberConverter:
    """
    Encapculates logic for conversion between bases

    Class is used here rather than free floating functions to
    make adding states easier without changing the interface used by main.py
    """

    def __init__(self):
        self.digit_symbols = DIGIT_SYMBOLS
    
    #---------------------
    # any base -> decimal
    #---------------------

    def to_decimal(self, number_str, base):
        """
        Converts num_str written in base into Python int
        """
        validate_base(base)
        number_str = validate_number(number_str, base)

        negative = number_str.startswith("-")
        digits = number_str[1:] if negative else number_str

        result = 0
        for ch in digits:
            value = self.digit_symbols.index(ch)
            result = result * base + value

        return -result if negative else result

    #---------------------
    # deciaml -> any base
    #---------------------

    def from_decimal(self, decimal_value, base):
        """
        Convert a Python int 'decimal_value' into a string representation
        in 'base'.
        """
        validate_base(base)

        if decimal_value == 0:
            return "0"

        negative = decimal_value < 0
        n = abs(decimal_value)

        digits = []
        while n > 0:
            n, remainder = divmod(n, base)
            digits.append(self.digit_symbols[remainder])

        result = "".join(reversed(digits))
        return f"-{result}" if negative else result
    #-------------------------------------------------------
    # convinience wrapper: any base -> any base, in one call
    #-------------------------------------------------------

    def convert(self, number_str, from_base, to_base):
        """
        Full pipeline: from_base -> decimal -> to_base.
        Returns a dict with everything main.py / history.py need,
        so callers don't have to run to_decimal separately.
        """
        decimal_value = self.to_decimal(number_str, from_base)
        converted = self.from_decimal(decimal_value, to_base)
        return {
            "input": number_str,
            "from_base": from_base,
            "to_base": to_base,
            "decimal_value": decimal_value,
            "output": converted,
        }