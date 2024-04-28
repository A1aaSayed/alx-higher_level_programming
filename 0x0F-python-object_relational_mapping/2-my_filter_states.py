#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MYSQLdb
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
    cur.execute(f'SELECT * FROM states WHERE name LIKE BINARY "{sys.argv[4]}" \
                 ORDER BY states.id ASC')

    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
