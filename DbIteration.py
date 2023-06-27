import mysql.connector

from Utils.Configurations import *

# host, database, username, password

conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from customerinfo')
rowAll = cursor.fetchall()
print(rowAll)

sum = 0
for key in rowAll:
    sum = sum + key[2]

print(sum)
assert sum == 340

# procedure to execute sql query through python
query = "update customerinfo set Location = %s where CourseName =%s"
data = ('India', "Jmeter")
cursor.execute(query, data)
conn.commit()

conn.close()