#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

query = '''
delete from Participants where study='B-TECH'
'''
conn.execute(query)
print(conn.total_changes)
#rollback - revert back delete operation
conn.execute("ROlLBACK")
print(conn.total_changes)
