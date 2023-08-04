#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

'''
describe table_name - MySQL
pragma table_info(table_name) - sqlite3
'''

query = "pragma table_info('Participants')"
details = conn.execute(query)
print(details)

for i in details:
    print(i)