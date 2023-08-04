#step1
import sqlite3

#step2
conn = sqlite3.connect('StudentDetails.db')
print(conn)


details = conn.execute("pragma table_info(Students)")

for i in details:
    print(i)

