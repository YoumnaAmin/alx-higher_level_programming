#!/usr/bin/python3
"""adds two int"""


def add_integer(a, b=98):
    """adds two int"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
