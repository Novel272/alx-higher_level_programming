#!/usr/bin/python3
""" The scripts takes in argument <state name> and displays values
    in states table where name matches arg <state name>
Usage:
    2-my_filter_states.py
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    host_u, port_u = "localhost", 3306
    name_u, password_u, database_u, state_name = argv[1:5]

    with MySQLdb.connect(host=host_u, port=port_u, user=name_u,
                         password=password_u, database=database_u) as db:
        with db.cursor() as cur:
            cur.execute("SELECT * FROM states WHERE BINARY name='{}' \
ORDER BY id ASC".format(state_name))
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
