#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys

# initialize variables
size = 0
count = 0
status_codes = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']


def display_stats(status_codes, size):
    """ print metrics """
    print("File size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:  # loop through lines in standard input
        if count == 10:  # display metrics if count reaches 10
            display_stats(status_codes, size)
            count = 1  # reset count
        else:
            count += 1

        line = line.split()  # split the line into a list of words

        try:
            size += int(line[-1])  # add the last element to the size
        except (IndexError, ValueError):
            pass  # if the last element is not a number, ignore and continue

        try:
            # check if second last element is a valid status code
            if line[-2] in valid_status_codes:
                if status_codes.get(line[-2], -1) == -1:
                    # if status code not in dict, add it
                    status_codes[line[-2]] = 1
                else:  # if status code already exists, increment its count
                    status_codes[line[-2]] += 1
        except IndexError:
            pass  # if there's an index error, continue to the next line

    display_stats(status_codes, size)  # display final metrics

except KeyboardInterrupt:  # handle CTRL + C
    display_stats(status_codes, size)
    raise  # Re-raise the KeyboardInterrupt after displaying the metrics
