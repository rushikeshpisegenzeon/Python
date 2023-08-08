import sqlite3

conn = sqlite3.connect('Medication_Management.db')
print(conn)

def del_patient(p_id):
    conn.execute(f'delete from patients where p_id == {p_id}')
    print("deleted patient successfully!")
    conn.commit()