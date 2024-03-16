#!/usr/bin/python3
"""This is the state module"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name \
                   LIKE 'N%' ORDER BY id ASC;")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
