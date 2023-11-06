#!/usr/bin/python3
def islower(c):
    '''
    check if a characer is lowercase

    Arguments:
    c: character to check

    Returns:
    True if c is lowercase, False otherwise
    '''
    return ord(c) >= ord('a') and ord(c) <= ord('z')
