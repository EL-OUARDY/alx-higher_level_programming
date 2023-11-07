#!/usr/bin/python3
if __name__ == "__main__":  # don't run if IMPORTED
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
