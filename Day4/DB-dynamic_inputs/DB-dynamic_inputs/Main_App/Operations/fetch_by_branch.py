import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

def get_by_branch(input_branch):
    query = f'select * from participants where branch = "{input_branch}"';


    details = conn.execute(query)
    for i in details:
        print(i)

