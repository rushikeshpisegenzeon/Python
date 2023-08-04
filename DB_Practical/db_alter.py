#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

#extra column - mail_id
'''
alter table table_name add column col_name datatype constraints
'''

query='''

alter table Participants add mail_id text not null
'''

conn.execute(query)