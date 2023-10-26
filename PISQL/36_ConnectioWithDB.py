import mysql.connector

conncet_db=mysql.connector.connect(host="localhost",user="root",password="")

cursor_a=conncet_db.cursor()

a=input("Enter Database Creating Queries :")
cursor_a.execute(a)

# for x in cursor_a:
    # print(x)