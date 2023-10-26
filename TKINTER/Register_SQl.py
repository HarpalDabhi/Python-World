# CREATE TABLE `tkinter`.`registration` (`Sr.No.` INT NOT NULL AUTO_INCREMENT , `First Name` VARCHAR(50) NOT NULL , `Father Name` VARCHAR(50) NOT NULL , `Surname` VARCHAR(50) NOT NULL , `Roll No` VARCHAR(50) NOT NULL , `Standard` VARCHAR(50) NOT NULL , `Gender` VARCHAR(50) NOT NULL , `Contact No` VARCHAR(50) NOT NULL , PRIMARY KEY (`Sr.No.`)) ENGINE = InnoDB;

import mysql.connector

connection_db=mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")

cursor_b=connection_db.cursor()

sql_query="INSERT INTO `registration` (`First Name`, `Father Name`, `Surname`, `Roll No`, `Standard`, `Gender`, `Contact No`) VALUES ( first, 'Ranjit bhai', 'Dabhi', '12', '4th', 'Male', '9924680675')"

cursor_b.execute(sql_query)
