#!/usr/bin/python3

exclude = {'q', 'e'}
alphabet = ''.join(
    chr(c) for c in range(ord('a'), ord('z')+1) if chr(c) not in exclude
)
print(alphabet, end='')
