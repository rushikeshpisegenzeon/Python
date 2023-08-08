import sqlite3
conn=sqlite3.connect('Medication_Management.db')

def update_pname(p_id,new_name):
    conn.execute(f'update patients set name ="{new_name}" where p_id=={p_id}')
    conn.commit()


def update_page(p_id,new_age):
    conn.execute(f'update patients set age ="{new_age}" where p_id=={p_id}')
    conn.commit()

def update_pgender(p_id,new_gender):
    conn.execute(f'update patients set gender ="{new_gender}" where p_id=={p_id}')
    conn.commit()
