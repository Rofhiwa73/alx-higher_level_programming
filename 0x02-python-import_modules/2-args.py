#!/usr/bin/python3
#This program prints the number of and the list of its arguments.

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1 # Exclude the script name from the arguments
    args = sys.argv[1:] # Get the list of arguments (excluding the script name)

    print("{} argument{}{}".format(num_args, "s" if num_args != 1 else "", ":" if num_args > 0 else "."))

    if num_args > 0:
        for i, arg in enumerate (args):
            print("{}: {}".format(i + 1, arg))
