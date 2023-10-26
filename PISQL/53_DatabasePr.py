import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="")

if(con):
    print("Connetion Successfully")
else:
    print("Connetion Failure")

cursor_=con.cursor()

(cursor_.execute('SHOW DATABASES'))

li_db=list(cursor_)
print(li_db)

name=input("Enter Database Name :")
for i in li_db:
    print(i)
    if name !=i:
        print("Name Does Not Exist")
        cursor_.execute(f"Create database {name}")