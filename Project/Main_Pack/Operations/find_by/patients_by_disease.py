import sqlite3


def find_patients_with_common_disease(disease):
    # Connect to the SQLite database
    conn = sqlite3.connect('Medication_Management.db')
    cursor = conn.cursor()

    # Use a SQL query with JOIN to find patients with a common disease
    select_query = '''
    SELECT p.name
    FROM patients p
    JOIN records r ON p.p_id = r.p_id
    JOIN medications m ON r.m_id = m.m_id
    WHERE m.disease = ?
    '''

    # Execute the SELECT query with the disease as a parameter
    cursor.execute(select_query, (disease,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the retrieved data
    if len(rows) > 0:
        print(f"Patients with the disease '{disease}':")
        for row in rows:
            print(row[0])
    else:
        print(f"No patients found with the disease '{disease}'.")

    # Close the database connection
    conn.close()





