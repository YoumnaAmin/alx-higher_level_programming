#!/usr/bin/python3
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
    cursor.execute("SELECT cities.id, cities.name,\
                    states.name FROM cities \
                   JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC;")
    cities = cursor.fetchall()

    for city in cities:
        print("{}".format(city))

    cursor.close()
    db.close()
