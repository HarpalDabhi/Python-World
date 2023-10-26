from tkinter import *

root=Tk()

def baught():
    print(f"You ordered {var.get()}")

root.geometry("800x600")

root.title("Radio Button")

h1=Label(root,text="Dabhi Rastaurant",fg="white",bg="green",font="verdana 30 bold",pady="30")

h1.pack(fill="x",padx="10",)

var =StringVar()
var.set("Radio")

Label(root,text="What you want to eat ?",fg="red",padx=14,font="verdana 20 italic").pack(anchor="w")

li_iems=["Dosa","Idli","Paneer","Rice","Carry"]

for i in li_iems:
    radio=Radiobutton(root,text=i,padx=14,variable=var,value=i,font="lucida 20 bold").pack(anchor="w")

Button(root,text="Order Now",padx=14,pady=14,font="lucida 22 bold",justify=LEFT,command=baught,fg="white",bg="red").pack()

root.mainloop()