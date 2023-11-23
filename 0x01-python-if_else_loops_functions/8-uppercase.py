#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Check if char is a lowercase letter.
        if 'a' <= char <= 'z':
            # Convert the lowercase to uppercase using ASCII values.
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            print("{}".format(char), end="")
    print() # Print a new line at the end.
