"""
-----------------
converter package
-----------------
Group the three core functional modules of the Number System Converter:

1. validator: input validation
2. engine: actual base-conversion logic
3. history: logging or session history of conversion
"""

from .engine import NumberConverter
from .validator import validate_base, validate_number, ValidationError
from .history import ConversionHistory

__all__ = [
    "NumberConverter",
    "validate_base",
    "validate_number",
    "ValidationError",
    "ConversionHistory",
]
