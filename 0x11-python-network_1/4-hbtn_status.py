#!/usr/bin/python3
"""hbtn status"""


if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    req = r.text
    print("Body response:")
    print("\t- type:", type(req))
    print("\t- content:", req)
