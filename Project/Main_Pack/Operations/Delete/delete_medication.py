import sqlite3

conn = sqlite3.connect('Medication_Management.db')
print(conn)

def del_medication(m_id):
    conn.execute(f'delete from medications where m_id == {m_id}')
    print("deleted medication successfully!")
    conn.commit()