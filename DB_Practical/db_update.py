
#step1
import  sqlite3

#step2
"QA_Automation_Camp2023.db"

#step3
conn= sqlite3.connect("QA_Automation_Camp2023.db") #it will create DB, and also create connection conn
print(conn)

'''
update table_name set col_name=new_value <where condition>
'''

query='''
update Participants set study='BioTech' where G_id=103
'''

conn.execute(query)
conn.commit()
conn.close()