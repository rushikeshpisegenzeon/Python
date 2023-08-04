#step1
import sqlite3

#step2
conn = sqlite3.connect('StudentDetails.db')
print(conn)

#step3
query='''
create table Students(G_id int primary key,name text not null,age int not null,mail_id text not null)
'''
conn.execute(query)
conn.commit()
conn.close()

