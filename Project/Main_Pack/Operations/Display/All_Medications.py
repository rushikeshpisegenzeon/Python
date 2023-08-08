import sqlite3



# Connect to the SQLite database
conn = sqlite3.connect('Medication_Management.db')
print(conn)

def display():
    result = conn.execute("SELECT * FROM medications")
    for i in result:
        print(i)

