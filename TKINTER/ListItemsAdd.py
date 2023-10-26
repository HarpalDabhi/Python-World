from tkinter import *
root=Tk()
list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
i=0

root.geometry('600x450')
def addItem():
    global i
    li.insert(ACTIVE,list[i])
    i+=1

li=Listbox(root,justify='center',font="verdana 20")
li.pack(fill='x')
li.insert(END,'A')
Button(text="Add +",command=addItem,bg='red',fg='white',padx=50,pady=10).pack(fill='x')
root.mainloop()