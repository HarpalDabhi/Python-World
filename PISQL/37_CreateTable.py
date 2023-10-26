import mysql.connector

connection_db=mysql.connector.connect(host="localhost",user="root",password="",database="pythondb")

cursor_b=connection_db.cursor()

table_query=input("Enter Table Query :")
cursor_b.execute(table_query)