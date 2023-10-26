from tkinter import *
import datetime



root=Tk()
root.title("Radio Button Tkinter")
root.geometry("600x400")

dt=datetime.datetime.now()
day=dt.strftime("%A")

def printDay():
    print(var.get())
    if var.get()==day:
        Label(f3,text=var.get(),fg='green',font='arial 18',justify='left').pack(pady='5',side=LEFT,padx=10)
    else:
        Label(f3,text=var.get(),fg='red',font='arial 18',justify='left').pack(pady='5',side=LEFT,padx=10)

f1=Frame(root,borderwidth=2,relief=SUNKEN,bg="green")
f1.pack(fill='x')

f2=Frame(root,borderwidth=2,relief=SUNKEN,bg="gold")
f2.pack(fill='x')

f3=Frame(root,borderwidth=2,relief=SUNKEN,bg="gold")
f3.pack(fill='x')
Label(f1,text="Welcom to Practice of Radio Button Tkinter",bg="green",font="arial 25",padx=10,pady=20).pack(fill='x',padx=10,pady=10)

Label(f2,text="What is the Day Today ?",bg="gold",font="arial 20",padx=10,pady=20,justify=LEFT).pack(anchor='nw',padx=10,pady=10,)

var=StringVar()
var.set('none')

li=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

Radiobutton(f2,text=li[0],variable=var,value=li[0],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[1],variable=var,value=li[1],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[2],variable=var,value=li[2],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[3],variable=var,value=li[3],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[4],variable=var,value=li[4],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[5],variable=var,value=li[5],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Radiobutton(f2,text=li[6],variable=var,value=li[6],bg="gold",font="arial 18").pack(side=LEFT,padx=5)

Button(f2,text="Check Answer",fg="white",bg="red",font="arial 20",command=printDay).pack(side=RIGHT,padx=20,pady=20)

root.mainloop()