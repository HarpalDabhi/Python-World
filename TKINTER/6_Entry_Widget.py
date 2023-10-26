from tkinter import *
root=Tk()

def submit():
    print("Username :",user.get())
    print("Password :",pwd.get())
root.geometry('500x350')

l1=Label(root,text="Fill the Below Form",font='verdana 24',pady=15)
l1.grid(columnspan=2)

Label(root,text="Username",font='verdana 20',pady=20,padx=10).grid(row=1)
Label(root,text="Password",font='verdana 20').grid(row=2)

user=StringVar()
pwd=StringVar()

Entry(root,textvariable=user,font='verdana 20').grid(row=1,column=1)
Entry(root,textvariable=pwd,font='verdana 20').grid(row=2,column=1)

Button(text='Submit',font='verdana 20',padx=15,bg='gray',command=submit).grid(row=3,columnspan=2,pady=15,)
root.mainloop()