import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)

#insert data
query ='''
 insert into participants values('1','Arjun','DAC','BTech','arjun.gmail.com')
'''

conn.execute(query)

conn.execute("insert into participants values('2','Ankit','Civil','BTech','ankit.gmail.com')")
conn.execute("insert into participants values('3','Sudhanshu','ECE','BTech','sud.gmail.com')")
conn.execute("insert into participants values('4','Shubham','Mechanical','BTech','shu.gmail.com')")

conn.commit()
conn.close()
