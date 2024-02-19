#!/usr/bin/python3
"""take an argument and display all values
in states table of hbtn_0e_0_usa
where name matches the argument
and is safe from SQL injections"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    import re
    host_u, port_u = "localhost", 3306
    name_u, password_u, database_u = argv[1:4]
    state_name = re.match(r"^([^';]+)", argv[4]).group(1)

    with MySQLdb.connect(host=host_u, port=port_u, user=name_u,
                         password=password_u, database=database_u) as db:
        with db.cursor() as cur:
            cur.execute(f"SELECT * FROM states WHERE name='{state_name}' \
ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
