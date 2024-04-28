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

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password,
            db=database
        )

    cur = db.cursor()

    query = """SELECT * FROM states
                WHERE states.name LIKE BINARY '{}'
                ORDER BY states.id
            """.format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
