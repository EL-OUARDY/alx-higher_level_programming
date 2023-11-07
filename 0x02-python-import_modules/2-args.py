#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of program arguments"""
    import sys

    args_count = len(sys.argv) - 1
    # print arguments count
    if args_count == 0:
        print("0 arguments.")
    elif args_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    # loop through argv list and display each argument
    for i in range(args_count):
        print("{:d}: {:s}".format((i + 1), sys.argv[i + 1]))
