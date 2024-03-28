#!/usr/bin/python3
"""Error code module"""


if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            pass
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
