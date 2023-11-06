#!/usr/bin/python3
letter = ord('a')   # ord() returns the ASCII value of a given character
while letter <= ord('z'):
    print(chr(letter), end='')  # chr() converts ASCII back to a character
    letter += 1
