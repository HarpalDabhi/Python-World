from tkinter import *

root=Tk()

scroll=Scrollbar(root)

root.geometry('500x500')
scroll.pack(fill='y',side=RIGHT)

li=Listbox(root,yscrollcommand=scroll)

for i in range(50):
    li.insert(END,i)
li.pack()

scroll.config(command=li.yview)

root.mainloop()