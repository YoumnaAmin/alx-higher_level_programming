#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{:d} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{:d} argument:".format(arg_len))
    else:
        print("{:d} arguments:".format(arg_len))
    for i in range(0, len(argv)):
        if i > 0:
            print("{:d}: {:s}".format(i, argv[i]))
