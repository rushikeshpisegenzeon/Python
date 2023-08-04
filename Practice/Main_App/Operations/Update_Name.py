import sqlite3

conn = sqlite3.connect('StudentDetails.db')
print(conn)

def updateName(id,name):
    conn.execute(f'update Students set name = "{name}" where G_id=={id}')

    conn.commit()
