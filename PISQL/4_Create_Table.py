import mysql.connector

add_db=mysql.connector.connect(host="localhost",user="root",password="",database="pisql")

mycursor=add_db.cursor()

create_table=mycursor.execute("CREATE TABLE login4 (Name VARCHAR(255), Email VARCHAR(255))")

print(create_table)    