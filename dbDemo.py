import mysql.connector

# host, database, username, password

conn = mysql.connector.connect(host="localhost", database='apidevelop', user='root', password='root')
print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from customerinfo')
row1 = cursor.fetchone()  # returns tuple of data
print(row1)
# In order to access any value, we have to access it by tuple property
print(row1[2])

rowAll = cursor.fetchall()  # returns list of tuples where each record is one tuple
print(rowAll)

print(len(rowAll))
for key in rowAll:
    print(key)


# for key in rowAll:
#     for kiki in key:
#         print(kiki , end='    ')
#     print()