#!/usr/bin/python3
"""post email"""

if __name__ == "__main__":
    import requests
    import sys
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=email)
    body = r.text
    print(body)
