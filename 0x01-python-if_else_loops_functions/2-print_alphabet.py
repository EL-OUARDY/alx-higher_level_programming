#!/usr/bin/python3
letter = ord('a')   # ord() returns the ASCII value of a given character
while letter <= ord('z'):
    # print the alphabet, chr() converts the ASCII value back to a character
    print("{:s}".format(chr(letter)), end='')
    letter += 1
