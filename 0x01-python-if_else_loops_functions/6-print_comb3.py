#!/usr/bin/python3
for i in range(0, 10):
    for j in range((i + 1), 10):
        if i == 8 and j == 9:  # last combination
            print("{:d}{:d}".format(i, j))  # print with a new line
        else:
            print("{:d}{:d}".format(i, j), end=", ")
