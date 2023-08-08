import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Medication_Management.db')
print(conn)
#cursor = conn.cursor()

def display():
    result = conn.execute("SELECT * FROM patients")
    for i in result:
        print(i)


# Fetch all rows
# rows = cursor.fetchall()

# Print the retrieved data
# for row in rows:
#     print("Medication:", row[0])
#     print("Disease:", row[1])
#     print("Dosage:", row[2])
#     print("Frequency:", row[3])
#     print("Start Date:", row[4])
#     print("End Date:", row[5])
#     print()
# for row in rows:
#     print(row)

# Close the database connection
#conn.close()