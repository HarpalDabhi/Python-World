from tkinter import *

hr=Tk()

def submit():
    x=name.get()
    y=email.get()
    print(x,y)

hr.geometry('800x500')

hr.iconbitmap('experience.ico')

name=Label(text="Enter Name :",font="verdana 20 bold",padx=3,pady=10).grid(row=0,column=0)
Entry(width=20,bg="black",fg="white",font="verdana 20 bold").grid(row=1,column=0)

email=Label(text="Enter Email :",font="verdana 20 bold",padx=3,pady=10).grid(row=2,column=0)
Entry(width=20,bg="black",fg="white",font="verdana 20 bold").grid(row=3,column=0,pady=10)

Button(text="Submit",font="arial 22 bold",bg="red",fg="blue",padx=15,pady=1,command=submit).grid(row=4,column=0,pady=10,padx=10)



hr.mainloop()