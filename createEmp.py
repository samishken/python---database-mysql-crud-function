import mysql.connector;

conn = mysql.connector.connect(host='localhost',database='mydb2',user='testuser',password='xxxxxxxx')

if conn.is_connected():
    print("Connected to mysql db")

    cursor = conn.cursor()

    try:
        cursor.execute("insert into emp value(3,'Abby',20000)")
        conn.commit()
        print("Employee Added")
    except:
       conn.rollback()


    cursor.close()
    # close connection
    conn.close()
