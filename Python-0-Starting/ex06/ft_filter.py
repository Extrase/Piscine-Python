import sys
import filterstring


def main():
    """
    Docstring for main
    """
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
    iterable = ["coucou", "comment", "nn", "tu vas ?"]
    print(list(ft_filter(None, iterable)))
    print(list(ft_filter(uOrNOt, iterable)))
    print(list(filter(None, iterable)))
    print(list(filter(uOrNOt, iterable)))


def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is not None:
        return [x for x in iterable if func(x)]
    else:
        return [x for x in iterable if x]


def uOrNOt(text):
    if "u" in text:
        return False
    return True


if __name__ == "__main__":
    main()
