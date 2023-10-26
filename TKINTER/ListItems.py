from tkinter import *

root=Tk()

def add():
    global li_item
    global i
    list_box.insert(ACTIVE,li_item[i])
    i+=1

li_item=['Banan',"Carry","Dosa","Edli","Fish","Grapes","Honey","Ice","Juice"]
i=0

root.geometry("800x600")

root.title("List Box")

h1=Label(root,text="Our Food Items",fg="blue",bg="yellow",font="verdana 30 bold",pady="25")

h1.pack(fill="x",padx="10",)

list_box=Listbox(root)
list_box.pack()
list_box.insert(END,"Apple")



Button(root,text="Add Items",padx=14,pady=5,font="lucida 22 bold",justify=LEFT,fg="yellow",bg="red",command=add).pack()

root.mainloop()