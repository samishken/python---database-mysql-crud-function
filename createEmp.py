import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='samboo',user='root',password='xxxxxxxx')

if conn.is_connected():
    print("Connected to mysql db")

cursor = con.cursor()

try:
    cursor.execute("insert into emp value(3,'Abby',20000)")
    conn.commit()
    print("Employee Added")
except:
    conn.rollback()


cursor.close()
# close connection
conn.close()
