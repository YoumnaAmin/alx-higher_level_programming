#!/usr/bin/python3
"""function that appends a string"""


def append_write(filename="", text=""):
    """function that appends a string"""
    with open(filename, "a", encoding="UTF8") as f:
        return (f.write(text))
