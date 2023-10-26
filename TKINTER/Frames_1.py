from tkinter import *

root=Tk()

root.title("Python Frames GUI")

root.geometry("800x600")

f1=Frame(root,bg="green",borderwidth=6,padx=10,relief=SUNKEN)
f1.pack(side=TOP,fill="x",padx=30,pady=30)

l1=Label(f1,text="Python tkinter",font="verdana 20 bold",padx=30,pady=10)
l1.pack()


root.mainloop()