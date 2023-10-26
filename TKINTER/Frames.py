from tkinter import *

root=Tk()

root.geometry('500x500')

f1=Frame()
text=Label(f1,text="Hi Hello I am Top",bg='orange',borderwidth='5',padx='10',font='verdana 18 bold',pady=65)
text.pack(fill='x')
f1.pack(side=TOP,fill='x')

f2=Frame(borderwidth='5')
text2=Label(f2,text="Hi Hello I am Bottom",bg='green',borderwidth='5',padx='10',font='verdana 18 italic',pady=65)
text2.pack(fill='x')
f2.pack(side=BOTTOM,fill='x')

root.mainloop()