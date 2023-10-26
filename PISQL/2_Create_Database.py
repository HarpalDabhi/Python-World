# 1. import mysql
# 2. connection
# 3.move curser
# 4. Execute Query

import mysql.connector

connection_db=mysql.connector.connect(host="localhost", user="root", passwd="")

print(connection_db)

cursor_db=connection_db.cursor()

print(cursor_db)

cursor_db.execute("CREATE DATABASE pisql2")

print(cursor_db)