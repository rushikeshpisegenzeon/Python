#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)


conn.execute("insert into Participants values(101,'Rushikesh','B-TECH','rushikesh@genzeon.com')")
conn.execute("insert into Participants values(102,'ayush','CA','ayush@genzeon.com')")
conn.execute("insert into Participants values(103,'indramohan','DR.','indra@genzeon.com')")
conn.execute("insert into Participants values(104,'vivek','Physics','vivek@genzeon.com')")
conn.execute("insert into Participants values(105,'shivam','B-TECH','shivam@genzeon.com')")

conn.commit()
conn.close()