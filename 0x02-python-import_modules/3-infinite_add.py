#!/usr/bin/python3
# This program prints the result of the addition of all arguments.

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Get the list of arguments

    try:
        result = sum(int(arg) for arg in args)  # Convert to integers and sum.
        print(result)

    except ValueError as e:
        print(f"Error: {e}")
