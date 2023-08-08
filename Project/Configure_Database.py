#step1 import the sqlite3 library
import sqlite3

#step2 establish the connection
conn = sqlite3.connect('Medication_Management.db')
print(conn)

#creation of tables
#1.patients table
#id will be increase automatically
create_patient_table='''
CREATE TABLE IF NOT EXISTS patients(
p_id INTEGER PRIMARY KEY AUTOINCREMENT,  
name TEXT NOT NULL,
age INTEGER NOT NULL,
gender TEXT NOT NULL
);
'''
#execution
conn.execute(create_patient_table)

#medication table
create_medication_table='''
CREATE TABLE IF NOT EXISTS medications(
m_id INTEGER PRIMARY KEY AUTOINCREMENT,
m_name TEXT NOT NULL,
disease TEXT NOT NULL,
dosage INTEGER NOT NULL,
frequency TEXT NOT NULL,
start_date DATE NOT NULL,
end_date DATE NOT NULL
);
'''
conn.execute(create_medication_table)

#record table which will help to join above two tables
create_record_table='''
CREATE TABLE IF NOT EXISTS records(
r_id INTEGER PRIMARY KEY AUTOINCREMENT,
p_id INTEGER NOT NULL,
m_id INTEGER NOT NULL,
FOREIGN KEY (p_id) REFERENCES patients(p_id),
FOREIGN KEY (m_id) REFERENCES medications(m_id)
);
'''

conn.execute(create_record_table)

#its good practice to always close the connection after use
conn.close()