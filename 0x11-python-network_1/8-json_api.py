#!/usr/bin/python3
"""json module"""


if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) < 2:
        letter = {'q': ""}
    else:
        letter = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get('id'),
                                   data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
