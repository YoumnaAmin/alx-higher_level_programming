#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1
    if (argv_len == 0):
        print("{0:d} argument.".format(argv_len))
    else:
        print("{0:d} arguments:".format(argv_len))
        for i in range(1, argv_len + 1):
            print("{0:d}: {1}".format(i, sys.argv[i]))
