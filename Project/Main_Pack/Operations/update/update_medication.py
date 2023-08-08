import sqlite3
conn=sqlite3.connect('Medication_Management.db')

def update_mname(m_id,new_mname):
    conn.execute(f'update medications set m_name ="{new_mname}" where m_id=={m_id}')
    conn.commit()


def update_disease(m_id,changed_disease_Name):
    conn.execute(f'update medications set disease ="{changed_disease_Name}" where m_id=={m_id}')
    conn.commit()

def update_dosage(m_id,new_dosage):
    conn.execute(f'update medications set dosage ="{new_dosage}" where m_id=={m_id}')
    conn.commit()

def update_frequency(m_id,new_frequency):
    conn.execute(f'update medications set frequency ="{new_frequency}" where m_id=={m_id}')
    conn.commit()

def update_startDate(m_id,new_date):
    conn.execute(f'update medications set start_date ="{new_date}" where m_id=={m_id}')
    conn.commit()

def update_endDate(m_id,new_date):
    conn.execute(f'update medications set end_date ="{new_date}" where m_id=={m_id}')
    conn.commit()