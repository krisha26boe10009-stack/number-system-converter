"""
------------
validator.py
------------

FUNCTIONAL MODULE 1: Input Validation

Responsible for ensuring that whatever the user inputs 
is indeed valid before it gets processed by the conversion engine. 
Decoupling this step from the engine proper in
engine.py satisfies “modular, clean implementation” and also helps fulfill 
the following non-functional requirements stated above:

Security / Reliability
: rejects invalid inputs before they can cause a crash or erroneous output
Error handling strategy
: raising one custom, descriptive exception type (ValidationError) 
instead of multiple possible built-in exceptions (ValueError/IndexError) 
would be more informative to the end-user.
"""

MIN_BASE = 2
MAX_BASE = 36
DIGIT_SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ValidationError(Exception):
    """Raised whenever a base or a number string fails validation."""
    pass
def validate_base(base):
    """
    Check that base is an integer within the supported range.

    ----------
    Parameters
    ----------
    base: int

    ------
    Raises 
    ------

    ValidationError if base is not int, or is outside
    """

    if not isinstance(base, int):
        raise ValidationError(f"Base must be a whole number, got: {base!r}")
    if base < MIN_BASE or base > MAX_BASE:
        raise ValidationError(
            f"Base must be between {MIN_BASE} and {MAX_BASE}, got: {base}"
        )
def validate_number(number_str, base):
    """
    Check that every char in num str is a legal digit for base.

    E.g. 9 is invalid for base 8, 6 is invalid in base 16.

    ----------
    Parameters
    ----------

    num str: str
    base: int

    ------
    Raises
    ------
    ValidationError on enpty input or any illegal digit.
    """

    if not number_str:
        raise ValidationError("Number cannot be empty.")

    number_str = number_str.strip().upper()
    # allow single leading minus sign for negetive nums.
    body = number_str[1:] if number_str[0] == "-" else number_str

    if body == "":
        raise ValidationError("Number cannot be just a minus sign.")

    allowed_digits = set(DIGIT_SYMBOLS[:base])
    for ch in body:
        if ch not in allowed_digits:
            raise ValidationError(
                f"'{ch}' is not a valid digit in base {base} "
                f"(allowed digits: {DIGIT_SYMBOLS[:base]})"
            )

    return number_str
