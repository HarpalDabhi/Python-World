from tkinter import *

root=Tk()

root.title("Scroll Bar")

root.geometry("800x600")

Label(text="Scroll Bar Harapal Dabhi",fg="white",bg="red",font="verdana 20 bold",padx=10,pady=20).pack(fill='x',padx=10,pady=10)

scrollbar=Scrollbar(root)
scrollbar.pack(fill='y',side=RIGHT)

listbox=Listbox(root,yscrollcommand=scrollbar.set,font="verdana 20 bold",fg="red",bg="gray")

for i in range(20):
    listbox.insert(END,i)
listbox.pack(fill="both",padx=10,pady=10)

scrollbar.config(command=listbox.yview)

root.mainloop()