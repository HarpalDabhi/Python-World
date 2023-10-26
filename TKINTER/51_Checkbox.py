from tkinter import *
root=Tk()

def submit():
    print("Username :",var.get())
    print("Username 2 :",var2.get())
    print("Username 2 :",var3.get())
    print("Username 2 :",var4.get())
    print("Username 2 :",var5.get())
    print("Username 2 :",var6.get())
root.geometry('500x350')

l1=Label(root,text="Fill the Below Form",font='verdana 24',pady=15)
l1.grid(columnspan=2)

var=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()

Label(root,text="Harpal Dabhi",font='verdana 20',pady=20,padx=10).grid(row=1)
c=Checkbutton(root,variable=var,font='verdana 20',onvalue=1,offvalue=0).grid(row=1,column=1,padx=5,pady=5,)

Label(root,text="Vipul Jadav",font='verdana 20',pady=20,padx=10).grid(row=2)
c=Checkbutton(root,variable=var2,font='verdana 20',onvalue=1,offvalue=0).grid(row=2,column=1,padx=5,pady=5,)

Label(root,text="Malay Goletar",font='verdana 20',pady=20,padx=10).grid(row=3)
c=Checkbutton(root,variable=var3,font='verdana 20',onvalue=1,offvalue=0).grid(row=3,column=1,padx=5,pady=5,)

Label(root,text="Jayraj Bhuva",font='verdana 20',pady=20,padx=10).grid(row=4)
c=Checkbutton(root,variable=var4,font='verdana 20',onvalue=1,offvalue=0).grid(row=4,column=1,padx=5,pady=5,)

Label(root,text="Elesh Kachchi",font='verdana 20',pady=20,padx=10).grid(row=5)
c=Checkbutton(root,variable=var5,font='verdana 20',onvalue=1,offvalue=0).grid(row=5,column=1,padx=5,pady=5,)

Label(root,text="Kuldip Mori",font='verdana 20',pady=20,padx=10).grid(row=6)
c=Checkbutton(root,variable=var6,font='verdana 20',onvalue=1,offvalue=0).grid(row=6,column=1,padx=5,pady=5,)

Button(text='Submit',font='verdana 20',padx=15,bg='gray',command=submit).grid(row=7,columnspan=2,pady=15,)
root.mainloop()