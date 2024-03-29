#!/usr/bin/python3
""" This scripts lists states with name start with 'n'
    fromt the database hbtn_0e_0_usa

Usage:
    1-filter_states.py
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    host_u, port_u = "localhost", 3306
    name_u, password_u, database_u = argv[1:4]

    with MySQLdb.connect(host=host_u, port=port_u, user=name_u,
                         password=password_u, database=database_u) as db:
        with db.cursor() as cur:
            cur.execute("\
SELECT * FROM States \
WHERE BINARY Name LIKE 'N%' \
ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
