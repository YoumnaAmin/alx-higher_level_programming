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
    cursor.execute("SELECT cities.name \
                   FROM cities \
                   JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s \
                   ORDER BY cities.id ASC;", (search,))
    cities = cursor.fetchall()

    cities = [i[0] for i in cities]

    print(', '.join(cities))

    cursor.close()
    db.close()
