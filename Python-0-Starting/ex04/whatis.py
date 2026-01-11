import sys

size = sys.getsizeof(sys.argv)

if size < 72:
    exit(1)
elif size > 72:
    print("AssertionError: more than one argument is provided")
    exit(1)
try:
    test = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit(1)

if (test % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")