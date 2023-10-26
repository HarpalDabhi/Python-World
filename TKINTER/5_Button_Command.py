from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry("600x400")
root.title('Button Click!')

def printMe():
    print("Good Mornings Friens")
    Label(text='Hello',font='verdana 20',padx=10,pady=10).pack()

f1=Frame(root,borderwidth=2,relief=SOLID)
f1.pack(fill='x')

img=Image.open('Sunday.png')
pht=ImageTk.PhotoImage(img)
Label(f1,image=pht).pack(side=LEFT)

t1="""Happy Day of this sunday to all Nice to meet Your \nall By Looking on This Day I am looking You happy always"""
l1=Label(f1,text=t1,fg='blue',font='arial 20')
l1.pack(side=RIGHT,padx=20,pady=20)

b1=Button(root,text='Click Me!',fg='ghostwhite',bg="black",font='arial 20',command=printMe)
b1.pack(side=BOTTOM,pady=25)
root.mainloop()