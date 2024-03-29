#!/usr/bin/python3
"""my github module"""


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    auth = (username, password)
    r = requests.get('https://api.github.com/user', auth=auth)
    data = r.json()
    if data:
        ID = data.get('id')
        print(ID)
    else:
        print("None")
