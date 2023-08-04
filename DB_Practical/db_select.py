
#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

records = conn.execute("select * from Participants")
for i in records:
    print(i)