import sys


def main():
    """
    Docstring for main
    """
    text = [""]
    if argVerif(text):
        total = [0, 0, 0, 0, 0, 0]
        count(text[0], total)
        print(f"The text contains {total[5]} characters:")
        print(f"{total[0]} upper letters")
        print(f"{total[1]} lower letters")
        print(f"{total[2]} punctuation marks")
        print(f"{total[3]} spaces")
        print(f"{total[4]} digits")
    # print(argVerif.__doc__)


def argVerif(text: str):
    """
    Docstring for argVerif
    :return: true or false
    """
    size = sys.getsizeof(sys.argv)
    if size < 72:
        print("What is the text to count?")
        text[0] = sys.stdin.read()
        if text[0] == "":
            sys.exit(0)
        return True
    elif size > 72:
        print("AssertionError: more than one argument is provided")
        return False
    text[0] = sys.argv[1]
    return True


def count(arg: str, total: list):
    """
    Docstring for count
    :param arg: str to parse
    :type arg: str
    :param total: all the counters
    :type total: list
    """
    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in arg:
        total[5] += 1
        if c.isupper():
            total[0] += 1
        elif c.islower():
            total[1] += 1
        elif c in punct:
            total[2] += 1
        elif c.isspace():
            total[3] += 1
        elif c.isdigit():
            total[4] += 1
        else:
            print("wtf")
    return 0


if __name__ == "__main__":
    main()
