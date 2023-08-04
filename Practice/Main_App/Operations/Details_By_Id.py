import sqlite3

conn = sqlite3.connect('StudentDetails.db')
print(conn)

def By_Id(g_id):
    result = conn.execute(f"SELECT * FROM Students WHERE G_id={g_id}")
    for i in result:
        print(i)
