#!/usr/bin/python3
"""
Module that takes in arguments and displays all values in the states table
where name matches argument, protected against MySQL injections.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
