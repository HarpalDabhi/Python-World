import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="")

print(mydb)

if(mydb):
    print("Successfully connected !!!")
else:
    print("Failed to connect to MySQL")

cur=mydb.cursor()

# print(cur)

# slq="CREATE DATABASE  malibhai"

# cur.execute(slq)

# print(cur)

sql2='SHOW DATABASES '

cur.execute(sql2)

# for i in cur:
    # print(i)
cur=list(cur)
print(cur)
print(len(cur))
