#!/usr/bin/python3
"""this the 0-hbtn module"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content_type = response.headers.get('Content-Type')
    content_length = response.headers.get('Content-Length')
    body = response.read().decode('utf-8')
    
    print("Body response:")
    print("\t- type:", content_type)
    print("\t- content:", content_length)
    print("\t- utf8 content:", body)
