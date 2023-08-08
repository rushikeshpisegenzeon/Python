import sqlite3

conn = sqlite3.connect('Medication_Management.db')
print(conn)

cursor = conn.cursor()

def find_by_id(p_id):
    print(f'Patient Details of {p_id}')

        # SQL query with INNER JOIN
    query = f'''
       SELECT records.r_id AS R_Id,patients.name AS patient_name, patients.age AS patient_age, patients.gender AS patient_gender,
       medications.m_name AS medication_name, medications.disease, medications.dosage,
       medications.frequency, medications.start_date, medications.end_date
       FROM records
       INNER JOIN patients ON records.p_id = patients.p_id
       INNER JOIN medications ON records.m_id = medications.m_id
       WHERE records.p_id=={p_id};
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch all records
    all_records = cursor.fetchall()
    for r in all_records:
        print(r)