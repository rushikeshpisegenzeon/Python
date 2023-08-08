#this file is useful to check created tables/schemas as per our requrements or not
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('Medication_Management.db')


details = conn.execute("pragma table_info('patients')")
print(details)
for i in details:
    print(i)

details = conn.execute("pragma table_info('medications')")
print(details)
for i in details:
    print(i)

details = conn.execute("pragma table_info('records')")
print(details)
for i in details:
    print(i)

