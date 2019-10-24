import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='samboo',user='root',password='xxxxxxxx')

if conn.is_connected():
    print("Connected to mysql db")

cursor = con.cursor()

cursor.execute('select * from emp')
print("Total Number of records",cursor.rowcont)

#fetch one record at a time
row = cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fechone() #fetch next record

#fetch all record at once
row = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
# close connection
conn.close()