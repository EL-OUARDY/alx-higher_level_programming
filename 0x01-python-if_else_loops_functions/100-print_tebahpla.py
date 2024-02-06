#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    sub = 0
    if i % 2 != 0:
        sub = 32
    print('{}'.format(chr(i - sub)), end='')
