#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = conn.cursor()

    cursor.execute(
        """SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"""
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
