#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    result = 0
    for i in range(0, len(argv)):
        if i > 0:
            result += int(argv[i])
    print (result)
