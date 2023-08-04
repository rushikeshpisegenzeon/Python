import sqlite3

conn = sqlite3.connect('StudentDetails.db')
print(conn)

def input_data():
    data = {}
    g_id=int(input("Enter G_Id: "))
    name=input("Enter the Name: ")
    age = int(input("ENter the age: "))
    mail_id=input("Enter your mail_id: ")

    data["G_id"]=g_id
    data["name"]=name
    data["age"]=age
    data["mail_id"]=mail_id

    conn.execute('''
    insert into Students(G_id,name,age,mail_id) values(?,?,?,?)
    ''',(data.get("G_id"),data.get("name"),data.get("age"),data.get("mail_id")))

    conn.commit()
