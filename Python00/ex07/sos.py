import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            if any(not (c.isalnum() or c.isspace()) for c in sys.argv[1]):
                raise AssertionError("the arguments are bad")
            for c in sys.argv[1].upper():
                print(NESTED_MORSE[c], end="")
            print()
        else:
            raise AssertionError("the arguments are bad")
    except AssertionError as err:
        print(f"{AssertionError.__name__}: {err}")
