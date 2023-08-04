import sqlite3

conn = sqlite3.connect('StudentDetails.db')
print(conn)

def display():
    result = conn.execute("SELECT * FROM Students")
    for i in result:
        print(i)

