#!/usr/bin/python3
"""take in name of state as argument and
list all cities of that state,
using database hbtn_0e_4_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    host_u, port_u = "localhost", 3306
    name_u, password_u, database_u, state_name = argv[1:5]

    with MySQLdb.connect(host=host_u, port=port_u, user=name_u,
                         password=password_u, database=database_u) as db:
        with db.cursor() as cur:
            cur.execute("\
SELECT ct.name \
FROM cities ct \
LEFT JOIN states st \
ON ct.state_id=st.id \
WHERE st.name='{}' \
ORDER BY ct.id ASC\
".format(state_name))
            query_rows = [row[0] for row in cur.fetchall()]
            print(", ".join(query_rows))
