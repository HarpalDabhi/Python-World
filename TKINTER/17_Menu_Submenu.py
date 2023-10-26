from tkinter import *
root=Tk()

def func():
    i=1
    print(i,"File")
    
    
root.geometry('500x300')
f1=Frame(root,padx=10,pady=10).pack(padx=15,pady=20)
menu=Menu(root)
# menu.add_command(label='File',command=func,font="arial 20 ")
root.config(menu=menu,padx=15,pady=20)

m1=Menu(menu,tearoff=0)
m1.add_command(label="New File")
m1.add_command(label="Open File")
m1.add_separator()
m1.add_command(label="Save as")
m1.add_command(label="Save")
menu.add_cascade(label="File",menu=m1)

m2=Menu(menu,tearoff=0)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
menu.add_cascade(label="Edit",menu=m2)

menu.add_command(label="Exit",command=quit,font='arial 20 ')
root.mainloop()