import sys


if __name__ == '__main__':
    if (len(sys.argv) <= 2):
        print("Usage: python operations.py < number1 > <number2 >\nExample:\n\tpython operations.py 10 3")
        exit()

    try:
        assert len(sys.argv) < 4, "too many arguments"
        assert sys.argv[1].isnumeric(
        ) and sys.argv[2].isnumeric(), "only integers"

        a: int = int(sys.argv[1])
        b: int = int(sys.argv[2])

        print(f"Sum: {a+b}")
        print(f"Difference: {a-b}")
        print(f"Product: {a*b}")
        print("Quotient: ", end='')
        try:
            print(f"{a/b}")
        except ZeroDivisionError:
            print("ERROR (division by zero)")
        print("Remainder: ", end='')
        try:
            print(f"{a%b}")
        except ZeroDivisionError:
            print("ERROR (modulo by zero)")
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
