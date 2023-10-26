from tkinter import *
import mysql.connector
root=Tk()
root.geometry("600x400")
root.title("Registration Form")

def register():
    print("Name :",name.get())
    print("Enrollment :",enrollment.get())
    print("Roll :",roll.get())
    print("Gender :",rad.get())
    print("Contact :",email.get())
    statusvar.set("Adding...")
    connection_db=mysql.connector.connect(host="localhost",user="root",password="",database="tkinter")
    cursor_b=connection_db.cursor()
    import time
    time.sleep(2)
    statusvar.set("Added")
    time.sleep(6)
    statusvar.set("Add Student")


    sql = "INSERT INTO `registatus` ( `Name`, `Enrollment`, `Roll`, `Gender`, `Email`) VALUES ( %s, %s, %s, %s, %s)"

    val = ( name.get(),enrollment.get(), roll.get(), rad.get(),email.get(), )

    cursor_b.execute(sql, val)

    connection_db.commit()
    

f1=Frame(root,borderwidth=2,relief=SOLID)
f1.pack()

l0=Label(text="Fill the Details to Register for Dance Competition",fg='white',bg='black',padx=10,pady=20,font='arial 24 bold')
l0.pack(fill='x',padx=10,pady=10)

f2=Frame(root,borderwidth=2,relief=SOLID,padx=10,pady=20)
f2.pack(padx=20,pady=20)

name=StringVar()
enrollment=StringVar()
roll=StringVar()
rad=StringVar()
email=StringVar()
rad.set('none')

Label(f2,text='Name :',font='arial 18',fg='gray',pady=3,).grid(row=0,column=0)
Entry(f2,textvariable=name,font='arial 18',fg='gray',).grid(row=0,column=1,pady=3)

Label(f2,text='Enrollment No :',font='arial 18',fg='gray',pady=3,).grid(row=1,column=0)
Entry(f2,textvariable=enrollment,font='arial 18',fg='gray',).grid(row=1,column=1,pady=3)


Label(f2,text='Roll No. :',font='arial 18',fg='gray',pady=3,).grid(row=2,column=0)
Entry(f2,textvariable=roll,font='arial 18',fg='gray',).grid(row=2,column=1,pady=3)


li=['Male', 'Female', 'Other']

Label(f2,text='Gender :',font='arial 18',fg='gray',pady=3,).grid(row=3,column=0)
Radiobutton(f2,text=li[0],variable=rad,value=li[0],font="arial 12",fg='gray').grid(row=4,column=0)

Radiobutton(f2,text=li[1],variable=rad,value=li[1],font="arial 12",fg='gray').grid(row=4,column=1)

Radiobutton(f2,text=li[2],variable=rad,value=li[2],font="arial 12",fg='gray').grid(row=4,column=2)

Label(f2,text='Email :',font='arial 18',fg='gray',pady=3,).grid(row=5,column=0)
Entry(f2,textvariable=email,font='arial 18',fg='gray',).grid(row=5,column=1,pady=3)

Button(f2,text="Register Now",font='arial 18',fg='gray',pady=5,command=register).grid(row=8,columnspan=3,pady=15)

statusvar=StringVar()
statusvar.set("Upload")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="nw",padx=10,pady=10)
sbar.pack(fill='x',side=BOTTOM)

root.mainloop()