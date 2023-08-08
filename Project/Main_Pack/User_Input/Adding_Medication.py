import sqlite3
import datetime
conn = sqlite3.connect('Medication_Management.db')
print(conn)

def medication_details():
    data = {}
    m_name=input("Enter the Medication Name: ")
    disease=input("Enter the disease name: ")
    dosage=int(input("Enter the dosage in mg: "))
    frequency=input(" Enter the freqency in day: ")
    s_date=datetime.date.today()
    days=int(input("Enter the number of days: "))
    e_date=s_date + datetime.timedelta(days)

    data["m_name"] = m_name
    data["disease"] = disease
    data["dosage"] = dosage
    data["frequency"] = frequency
    data["start_date"] = s_date
    data["end_date"] = e_date


    conn.execute('''
    insert into medications(m_name,disease,dosage,frequency,start_date,end_date) values(?,?,?,?,?,?)
    ''',(data.get("m_name"),data.get("disease"),data.get("dosage"),data.get("frequency"),data.get("start_date"),data.get("end_date")))

    conn.commit()