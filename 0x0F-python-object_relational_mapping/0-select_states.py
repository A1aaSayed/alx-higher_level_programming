#!/usr/bin/python3

import MySQLdb
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()

if __name__ == '__main__':
    main()
