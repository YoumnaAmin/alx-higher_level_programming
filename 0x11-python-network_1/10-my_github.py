#!/usr/bin/python3
"""my github module"""


if __name__ == "__main__":
    import requests
    import sys
    
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization':
               'github_pat_11BBM752Y0gxnEiz1Diti5\
                _qLpHn1SdtWkc591WajLWdYS3Z8lq8vkHLWW0h2ijeNt3RIHHR3PQ9462ypq'}
    r = requests.get('https://api.github.com/YoumnaAmin', headers=headers)
    data = r.json()
    ID = data.get('id')
    print(ID)
