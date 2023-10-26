from tkinter import *
import mysql.connector
root=Tk()
root.geometry("600x400")
root.title("Registration Form")

def register():
    print("Name :",first.get())
    print("Father :",father.get())
    print("Surname :",surname.get())
    print("Roll :",roll.get())
    print("Gender :",rad.get())
    print("Stadard :",std.get())
    print("Contact :",contact.get())
    connection_db=mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")

    cursor_b=connection_db.cursor()


    sql = "INSERT INTO `registration` (`First Name`, `Father Name`, `Surname`, `Roll No`, `Standard`, `Gender`, `Contact No`) VALUES ( %s, %s, %s, %s, %s, %s, %s)"

    val = (first.get(), father.get(), surname.get(),roll.get(), std.get(), rad.get(),contact.get(), )

    cursor_b.execute(sql, val)

    connection_db.commit()
    

f1=Frame(root,borderwidth=2,relief=SOLID)
f1.pack()

l0=Label(text="Fill the Details to Register for Dance Competition",fg='white',bg='black',padx=10,pady=20,font='arial 24 bold')
l0.pack(fill='x',padx=10,pady=10)

f2=Frame(root,borderwidth=2,relief=SOLID,padx=10,pady=20)
f2.pack(padx=20,pady=20)

first=StringVar()
father=StringVar()
surname=StringVar()
roll=StringVar()
rad=StringVar()
std=StringVar()
contact=StringVar()
rad.set('none')

Label(f2,text='First Name :',font='arial 18',fg='gray',pady=3,).grid(row=0,column=0)
Entry(f2,textvariable=first,font='arial 18',fg='gray',).grid(row=0,column=1,pady=3)

Label(f2,text='Father Name :',font='arial 18',fg='gray',pady=3,).grid(row=1,column=0)
Entry(f2,textvariable=father,font='arial 18',fg='gray',).grid(row=1,column=1,pady=3)

Label(f2,text='Surname  :',font='arial 18',fg='gray',pady=3,).grid(row=2,column=0)
Entry(f2,textvariable=surname,font='arial 18',fg='gray',).grid(row=2,column=1,pady=3)

Label(f2,text='Roll No. :',font='arial 18',fg='gray',pady=3,).grid(row=3,column=0)
Entry(f2,textvariable=roll,font='arial 18',fg='gray',).grid(row=3,column=1,pady=3)

Label(f2,text='Standard :',font='arial 18',fg='gray',pady=3,).grid(row=4,column=0)
Entry(f2,textvariable=std,font='arial 18',fg='gray',).grid(row=4,column=1,pady=3)



li=['Male', 'Female', 'Other']

Label(f2,text='Gender :',font='arial 18',fg='gray',pady=3,).grid(row=5,column=0)
Radiobutton(f2,text=li[0],variable=rad,value=li[0],font="arial 12",fg='gray').grid(row=6,column=0)

Radiobutton(f2,text=li[1],variable=rad,value=li[1],font="arial 12",fg='gray').grid(row=6,column=1)

Radiobutton(f2,text=li[2],variable=rad,value=li[2],font="arial 12",fg='gray').grid(row=6,column=2)

Label(f2,text='Contact :',font='arial 18',fg='gray',pady=3,).grid(row=7,column=0)
Entry(f2,textvariable=contact,font='arial 18',fg='gray',).grid(row=7,column=1,pady=3)

Button(f2,text="Register Now",font='arial 18',fg='gray',pady=5,command=register).grid(row=8,columnspan=3,pady=15)





root.mainloop()