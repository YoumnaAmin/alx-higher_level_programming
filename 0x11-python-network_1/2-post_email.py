#!/usr/bin/python3
"""post email"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    email = {'email' : sys.argv[2]}
    email_enc = urllib.parse.urlencode(email)
    email_enc = email_enc.encode('ascii')
    req = urllib.request.Request(sys.argv[1], email_enc)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
