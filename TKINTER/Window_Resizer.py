from tkinter import *
root=Tk()
root.title("Python Window Resizer")

w=IntVar()
h=IntVar()

def resize():
    a=w.get()
    b=h.get()
    root.geometry(f"{a}x{b}")
    print(a,b)

f=Frame(root,borderwidth=2,relief=SUNKEN,padx=20,pady=20)
f.pack(pady=25)

w=IntVar()
Label(f,text="Enter Width :",font="verdana 20").pack()
Entry(f,textvariable=w,font="verdana 20").pack()
h=IntVar()
Label(f,text="Enter Height :",font="verdana 20").pack()
Entry(f,textvariable=h,font="verdana 20").pack()

Button(f,text='Apply Settings',font="verdana 22",command=resize).pack(pady=10)

root.mainloop()