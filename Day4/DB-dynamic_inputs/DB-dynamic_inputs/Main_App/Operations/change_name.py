import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

def update_name(id,name):
    conn.execute(f'update participants set name = "{name}" where g_id == {id}')

    conn.commit()