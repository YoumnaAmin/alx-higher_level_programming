#!/usr/bin/python3
"""hbtn_header module"""


if __name__ == "__main__":
    import requests
    import sys
    try:
        r = requests.get(sys.argv[1])
        ID = r.headers['X-Request-Id']
        print(ID)
    except Exception as e:
        pass
