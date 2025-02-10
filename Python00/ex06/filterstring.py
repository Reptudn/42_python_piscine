import sys
from ft_filter import ft_filter

if __name__ == "__main__":
    """
    Accepts 2 arguments:
    1. string
    2. integer

    Returns a list of words whose are longer than the integer argument.
    """
    try:
        if len(sys.argv) != 3 or not sys.argv[2].isdigit() or not sys.argv[1]:
            raise AssertionError("the arguments are bad")
        elif any(not c.isalpha() and not c.isspace() for c in sys.argv[1]):
            raise AssertionError("the arguments are bad")

        words = sys.argv[1].split()
        words = ft_filter(lambda x: len(x) > int(sys.argv[2]), words)
        print(list(words))
    except AssertionError as err:
        print(f"{AssertionError.__name__}: {err}")
