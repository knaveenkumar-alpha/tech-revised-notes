import psycopg2
import sys

con = None

try:

    con = psycopg2.connect(database='postgres', user='postgres',
                           password='naveen1213')

    cur = con.cursor()
    cur.execute('SELECT version()')

    version = cur.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f"Error {e}")
    sys.exit(1)

finally:

    if con:
        con.close()
# this is test commit to test the change from local to git
