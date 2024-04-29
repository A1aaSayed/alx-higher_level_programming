#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print(f'Error Connecting to Database {e}')
        sys.exit(1)

    cur = db.cursor()

    name = sys.argv[4]

    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities c \
                INNER JOIN states s ON c.id = s.id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
