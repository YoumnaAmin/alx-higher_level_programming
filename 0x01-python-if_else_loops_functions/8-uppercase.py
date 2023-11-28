#!/usr/bin/python3
def uppercase(str):
    str_res = ""
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            i = chr(ord(i) - 32)
        str_res += i
        print("{0:s}".format(i), end="")
