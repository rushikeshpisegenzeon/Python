#steps

'''
sqlite3
1. importing sqlite3 module
2. Create a DB
3. Connecting to the DB
4. Query - create a table in the DB
5. Execute the query
'''

#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

#step4

'''
create table table_name(col1 datatype constraints,clo2 datatype constraints..)
'''

query='''
create table Participants(G_id int primary key, name text not null,study text not null DEFAULT 'B-TECH')
'''

#step5
conn.execute(query)
