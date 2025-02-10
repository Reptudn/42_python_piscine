import sys

try:
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")

    num = sys.argv[1]
    try:
        num = int(num)
    except ValueError:
        raise AssertionError("argument is not an integer")

    print(f"I'm {'Even' if num % 2 == 0 else 'Odd'}")
except AssertionError as err:
    print(f"{AssertionError.__name__} : {err}")
