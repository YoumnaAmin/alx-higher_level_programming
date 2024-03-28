#!/usr/bin/python3
"""this the 0-hbtn module"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
print(res)
