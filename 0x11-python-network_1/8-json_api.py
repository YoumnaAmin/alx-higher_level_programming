#!/usr/bin/python3
"""json module"""


if __name__ == "__main__":
    import sys
    import requests
    if sys.argv < 1:
        letter = {'q': ""}
        r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
        print("No result")
    else:
        letter = {'q': sys.argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
        if r.json():
            print("[<[:]>] <[]>".formatr(r.json().get('id'), r.json().get('name')))
        else:
            print("Not a valid JSON")
