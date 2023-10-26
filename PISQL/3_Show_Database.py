import mysql.connector

con_db=mysql.connector.connect(host="localhost",user="root",password="")

print(con_db)

cursor_1=con_db.cursor()

cursor_1.execute("SHOW DATABASES")

for i in cursor_1:
    print(i)

