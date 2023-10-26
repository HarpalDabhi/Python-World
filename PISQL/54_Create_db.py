import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",passwd="",database='manisha_cr')

cursor1=connection.cursor()

if (connection):
    print("Conection was successful")
else:
    print("Fail !!!")

    # TODO Create database quare

# cursor1.execute("CREATE DATABASE  manisha_cr")

# TODO show database quarey

# cursor1.execute("SHOW DATABASES")

# print(cursor1)

# for i in cursor1:
#     print(i)

#TODO create table query

# cursor1.execute("CREATE TABLE studentlist(Name varchar(200), Enrollment int(20))")

# TODO inset query


# cursor1.execute('INSERT INTO studentlist values(name,roll) ')

sql="INSERT INTO studentlist(Name,Enrollment) values(%s,%s)"

vlslist=[("Krishna",12),("Krupa",45),("Kinjal",16)]

cursor1.executemany(sql,vlslist)

connection.commit()

if(cursor1):
    print("inserted")
else:
    print("un inserted")