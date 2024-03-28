#!/usr/bin/python3
"""hbtn_header module"""


if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        id = response.headers.get('X-Request-Id')
        print(id)
