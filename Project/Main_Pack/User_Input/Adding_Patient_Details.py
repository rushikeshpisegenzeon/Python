import sqlite3

conn = sqlite3.connect('Medication_Management.db')
print(conn)

def patient_details():
    data = {}
    name=input("Enter the Name: ")
    age = int(input("Enter the age: "))
    gender=input("Enter your gender: ")

    data["name"]=name
    data["age"]=age
    data["gender"]=gender

    conn.execute('''
    insert into patients(name,age,gender) values(?,?,?)
    ''',(data.get("name"),data.get("age"),data.get("gender")))

    conn.commit()