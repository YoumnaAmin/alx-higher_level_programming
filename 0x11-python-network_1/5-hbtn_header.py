#!/usr/bin/python3
"""hbtn_header module"""


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    ID = r.headers['X-Request-Id']
    print(ID)
