#!/usr/bin/python3
"""
to read and print a file content
"""


def read_file(filename=""):
    """to read and print a file content"""
    with open (filename, encoding="UTF8") as f:
        for line in f:
            print(line, end='')
