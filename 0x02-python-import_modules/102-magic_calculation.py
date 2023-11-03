#!/usr/bin/python3
# Python function def magic_calculation(a, b):

def magic_calculation(a, b):
    if a < b:
        return a + b
    else:
        return a - b

# Python bytecode equivalent:
# 2           0 LOAD_FAST                0 (a)
#             2 LOAD_FAST                1 (b)
#             4 COMPARE_OP               0 (<)
#             6 POP_JUMP_IF_FALSE       14
#
# 3           8 LOAD_FAST                0 (a)
#            10 LOAD_FAST                1 (b)
#            12 BINARY_ADD
#            14 RETURN_VALUE

# Example usage:
result = magic_calculation(5, 3)
print(result)  # Output: 8
