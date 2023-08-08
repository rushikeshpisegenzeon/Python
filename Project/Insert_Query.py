# To insert dummy data for development purpose
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('Medication_Management.db')
print(conn)
cursor = conn.cursor()

# Insert sample data into the "patients" table
insert_patient_table = '''
INSERT INTO patients(name,age,gender)
VALUES
    ('ramesh disuja',25,'male'),
    ('john patil',45,'male'),
     ('shivaji patel',52,'male'),
    ('ujwala farnandis',35,'female')
'''
cursor.execute(insert_patient_table)

# Insert sample data into the "medications" table
insert_medication_query = '''
INSERT INTO medications(m_name, disease, dosage, frequency, start_date, end_date)
VALUES
    ('Aspirin', 'Upset stomach', '100', 'Twice', '2023-08-07', '2023-08-15'),
    ('Warfarin', 'Thrombosis', '250', 'Day', '2023-08-09', '2023-08-16'),
    ('Metformin', 'Diabetes', '500', 'Day', '2023-10-06', '2023-10-12'),
    ('Lisinopril', 'Blood Pressure', '150', 'Twice', '2023-09-09', '2023-09-16')
'''
#current_date = date.today().isoformat()
cursor.execute(insert_medication_query)



#Insert sample data into the "records" table
insert_records_query = '''
INSERT INTO records(p_id,m_id)
VALUES
    (1,1),
    (2,2)
'''

cursor.execute(insert_records_query)

# Commit the changes and close the connection
conn.commit()
#conn.close()