#!/usr/bin/python3

def print_last_digit(number):
    # Take the absolute value to handle negative numbers
    number = abs(number)

    # Get the last digit using the modulo operator
    last_digit = number % 10

    print(last_digit, end='')

    return last_digit
