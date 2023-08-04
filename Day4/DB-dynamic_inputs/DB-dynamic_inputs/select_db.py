import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

details = conn.execute("SELECT * FROM participants")
for i in details:
    print(i)