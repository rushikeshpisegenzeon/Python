'''
1.import sqlite3 library
2.create database
3.establish connection
4.create table in db- write query
5.execute query

'''
#1.
import sqlite3

#2. and 3.
conn = sqlite3.connect('Bootcamp2023.db')
print(conn)
#
# '''
# describe tablename -sql
# pragma table_info(tablename) - sqlite3
# '''
#
# #4.
#
# '''
# create table tablename(col1 datatype constraints, ...)
# constraints -> unique, check, not null, foreign key
# '''

# query = '''
# create table participants(g_id int primary key, name text not null, branch text not null, study text not null DEFAULT 'Btech')
# '''

# conn.execute(query)
#
# # details = conn.execute("pragma table_info(participants)")
# #
# # for i in details:
# #     print(i)


''' 
add column emailid
ALTER TABLE tablename ADD COLUMN column_name datatype constraints
'''

conn.execute('''
alter table participants add column email_id text not null
''')

details = conn.execute("pragma table_info(participants)")

for i in details:
    print(i)