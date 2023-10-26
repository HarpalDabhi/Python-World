import mysql.connector

con_db=mysql.connector.connect(host="localhost",user="root",password="",database="pisql")

cursor_2=con_db.cursor()

cursor_2.execute("SHOW TABLES")

for i in cursor_2:
    print(i)