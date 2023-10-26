import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="lovedatabase3"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE lover_2 (name VARCHAR(255) , address varchar(255) )")
