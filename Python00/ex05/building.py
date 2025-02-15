import sys


def count_stuff(s: str) -> None:
    """
    s (input string): The text to analyze

    Prints some information about the given text like:
    - Number of characters
    - Number of upper case letters
    - Number of lower case letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits
    """
    print(f"The text contains {len(s)} characters:")
    print(f"{sum(1 for c in s if c.isupper())} upper letters")
    print(f"{sum(1 for c in s if c.islower())} lower letters")
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(f'{sum(1 for c in s if c in punc)} punctuation marks')
    print(f"{sum(1 for c in s if c.isspace())} spaces")
    print(f"{sum(1 for c in s if c.isdigit())} digits")


if __name__ == "__main__":
    """
    Analyzes the given text and prints information about its char composition.

    Asks for input if no argument is given:

    raises AssertionError: Too many arguments provided
    """
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("top many args")

        if len(sys.argv) == 1:
            count_stuff(input("What is the text to count?:\n"))
        else:
            count_stuff(sys.argv[1])

    except AssertionError as err:
        print(f"{AssertionError.__name__}: {err}")
