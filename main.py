"""
--------
main.py
--------
Entry point / user interface for the Number System Converter. 
Workflow (Usability requirement - clear, logical, menu-driven) : 
1. User enters a number and the base it's currently in 
2. User enters the base they want to convert it to 
3. Result is shown, and logged into history 
4. User is asked whether to do another conversion, switch conversion type,
view history or quit - loops until they choose to exit. 
Run with: python main.py
"""

from converter import NumberConverter, ConversionHistory, ValidationError

# Optional friendly aliases so users can type binary instead of 2
BASE_ALIASES = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hex": 16,
    "hexadecimal": 16,
}

def resolve_base(raw_input: str) -> int:
    """Turn user input like '16', 'hex', or 'Binary' into an int base."""
    raw_input = raw_input.strip().lower()
    if raw_input in BASE_ALIASES:
        return BASE_ALIASES[raw_input]
    try:
        return int(raw_input)
    except ValueError:
        raise ValidationError(
            f"'{raw_input}' is not a valid base. Enter a number (2-36) "
            f"or one of: {', '.join(BASE_ALIASES)}."
        )


def do_conversion(converter: NumberConverter, history: ConversionHistory):
    """Runs a single convert-one-number interaction."""
    try:
        number_str = input("Enter the number to convert: ").strip()
        from_base = resolve_base(input("What base is it currently in? (e.g. 2, 10, 16, hex): "))
        to_base = resolve_base(input("Convert it to which base?: "))

        result = converter.convert(number_str, from_base, to_base)

        print(
            f"\nResult: {result['input']} (base {from_base}) "
            f"= {result['output']} (base {to_base})"
        )
        print(f"(Decimal equivalent along the way: {result['decimal_value']})\n")

        history.add_entry(result)

    except ValidationError as e:
        # known nd expected error are caught here and shown as friendly msg instead of stack trace
        print(f"\nInput error: {e}\n")
    #except Exception as e:
        # Anything truly unexpected still gets caught so the whole program doesnt crash
     #   print(f"\nSomething went wrong: {e}\n")


def print_menu():
    print("=" * 40)
    print(" NUMBER SYSTEM CONVERTER")
    print("=" * 40)
    print("1. Convert a number")
    print("2. View conversion history")
    print("3. Clear history")
    print("4. Quit")


def main():
    converter = NumberConverter()
    # Pass a filename here also persists.
    history = ConversionHistory()

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            do_conversion(converter, history)
        elif choice == "2":
            history.show()
        elif choice == "3":
            history.clear()
            print("History cleared.\n")
        elif choice == "4":
            print("See you later alligator!")
            break
        else:
            print("Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()