#!/usr/bin/python3
"""This is the state module"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    search = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;", (search,))
    states = cursor.fetchall()

    for state in states:
            print("({}, {})".format(state[0], state[1]))

    cursor.close()
    db.close()
