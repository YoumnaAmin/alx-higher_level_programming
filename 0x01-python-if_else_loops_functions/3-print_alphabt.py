#!/usr/bin/python3
for alpha in range(97, 123):
    if (alpha != 101 and alpha != 113):
        print("{0:c}".format(alpha), end="")
