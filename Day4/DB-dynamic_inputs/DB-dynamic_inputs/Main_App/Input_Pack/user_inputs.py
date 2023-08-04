import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

def input_data():
    data = {}
    g_id=int(input("Enter G_ID:-"))
    name=input("Enter Name:-")
    branch = input("Enter Branch:-")
    study=input("Enter Study:-")
    email_id=input("Enter EmailID:-")

    data["g_id"] = g_id
    data["name"] = name
    data["branch"] = branch
    data["study"] = study
    data["email_id"] = email_id

    conn.execute('''
    insert into participants(g_id,name,branch,study,email_id) values(?,?,?,?,?)
    ''',(data.get("g_id"),data.get("name"),data["branch"],data["study"],data["email_id"]))

    conn.commit()

