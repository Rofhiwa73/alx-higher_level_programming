#!/usr/bin/python3

# Replaces an element of a list at a specific position like in C.

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
