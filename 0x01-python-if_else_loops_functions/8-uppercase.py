#!/usr/bin/python3
def uppercase(str):
    '''
    convert a string to uppercase

    Arguments:
    str: target string
    '''
    for i in str:   # loop through the string
        if ord(i) >= ord('a') and ord(i) <= ord('z'):   # lowercase
            i = chr(ord(i) - 32)    # -32 to move from UPPER to LOWER case
        print("{:s}".format(i), end="")
    print()  # new line
