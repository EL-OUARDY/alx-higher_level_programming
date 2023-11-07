#!/usr/bin/python3
if __name__ == "__main__":  # works only on direct execution
    """prints the result of the addition of all arguments"""
    import sys

    sum = 0

    # sum of all arguments
    for i in range(len(sys.argv) - 1):
        sum += int(sys.argv[i + 1])

    print(sum)
