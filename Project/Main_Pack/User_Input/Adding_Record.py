import sqlite3

def insert_record(p_id, m_id):
    # Connect to the database
    conn = sqlite3.connect('Medication_Management.db')
    cursor = conn.cursor()

    # Check if the provided p_id and m_id exist in the respective tables
    check_patient_query = "SELECT * FROM patients WHERE p_id = ?;"
    check_medication_query = "SELECT * FROM medications WHERE m_id = ?;"

    cursor.execute(check_patient_query, (p_id,))
    patient_data = cursor.fetchone()

    cursor.execute(check_medication_query, (m_id,))
    medication_data = cursor.fetchone()

    if not patient_data:
        print(f"Patient with p_id {p_id} does not exist in the patients table.")
        conn.close()
        return

    if not medication_data:
        print(f"Medication with m_id {m_id} does not exist in the medications table.")
        conn.close()
        return

    # SQL query to insert data into the records table
    insert_query = '''
    INSERT INTO records (p_id, m_id)
    VALUES (?, ?);
    '''

    # Execute the query with the provided p_id and m_id
    try:
        cursor.execute(insert_query, (p_id, m_id))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")

    # Close the connection
    conn.close()

