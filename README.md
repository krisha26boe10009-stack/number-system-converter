# Number System Converter

A menu-driven, calculator-style command-line tool that converts a number
from any base (2-36) into any other base, and lets you keep converting
new numbers (or re-use the result) without restarting the program.

## Overview

The user enters a number and the base it is currently written in, then
chooses the base they want it converted to. The tool validates the input,
performs the conversion, shows the result, and remembers it in a
session history — similar to how a scientific calculator lets you switch
number modes and keep going.

## Features

- Convert between any two bases from 2 (binary) up to 36 (digits 0-9 + A-Z)
- Friendly aliases: type `binary`, `octal`, `decimal`, or `hex` instead of the number
- Handles negative numbers
- Input validation with clear error messages instead of crashes
- Session history of every conversion performed, viewable on demand
- Optional persistent logging to a file (see `converter/history.py`)
- Loops back to the menu after each conversion — convert as many numbers
  as you like in one run, just like a calculator

## Technologies / Tools Used

- Python 3 (standard library only — no external dependencies)
- `unittest` for automated testing

## Project Structure

```
number_converter/
├── main.py                  # CLI entry point / menu loop
├── converter/
│   ├── __init__.py
│   ├── validator.py         # Module 1: input validation
│   ├── engine.py            # Module 2: base-conversion logic
│   └── history.py           # Module 3: session history / logging
├── tests/
│   ├── test_validator.py
│   └── test_engine.py
├── statement.md
└── README.md
```

## Steps to Install & Run

1. Make sure Python 3.8+ is installed.
2. Download / clone this repository.
3. From the project's root folder, run:
   ```
   python main.py
   ```
4. Follow the on-screen menu.

## Instructions for Testing

Run the full automated test suite from the project's root folder:

```
python -m unittest discover tests -v
```

All 21 tests should pass (validator edge cases + engine conversions,
including a base-7 → base-29 → base-7 round trip check).

## Screenshots



## Possible Future Enhancements

- Support fractional numbers (e.g. `101.101` in binary)
- Batch-convert numbers from a file
- Simple GUI (Tkinter) or web front-end reusing the same `converter` package
