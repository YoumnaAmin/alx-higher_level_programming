#!/usr/bin/python3
"""this the 0-hbtn module"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
