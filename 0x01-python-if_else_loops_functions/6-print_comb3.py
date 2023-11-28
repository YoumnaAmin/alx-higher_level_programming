#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i != 0):
            if (i != j and j / i > 1 and i != 8):
                print("{0:d}{1:d}, ".format(i, j), end="")
            elif (i != j and j / i > 1 and i == 8):
                print("{0:d}{1:d}\n".format(i, j), end="")
        elif (i == 0 and i != j):
            print("{0:d}{1:d}, ".format(i, j), end="")
