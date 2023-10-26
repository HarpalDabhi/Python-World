import mysql.connector

print("Success in the Connection.")

db=mysql.connector.connect(host="localhost",user="root",password="")

print(db)