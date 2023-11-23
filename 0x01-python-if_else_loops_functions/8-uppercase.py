#!/usr/bin/python3

def uppercase(str):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            # Append the uppercase character to the result string
            result += uppercase_char
        else:
            # If the character is not a lowercase letter, append it unchanged
            result += char

    # Print the final result
    print(result, end="")
