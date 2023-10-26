from tkinter import *
root=Tk()
root.geometry('500x350')
root.title("Handle Events")

def write(event):
    print("Writing..")
    Label(text='Write Event',fg='red').pack()

f=Frame(root,borderwidth=1,relief=SOLID,bg='cyan')
f.pack(fill='x')

data='''Lorem ipsum, dolor sit amet consectetur adipisicing elit. Qui, vero,\n autem quam magnam veniam iste in aut vel ratione voluptate quaerat\nsaepe, id provident ipsum dignissimos rem laudantium hic \ndoloremque.'''

l0=Label(f,text=data,font="verdana 18",bg='cyan',fg='red')
l0.pack(padx=20,pady=15)

w=Button(f,text="Write Me",font='arial 20',bg='red',fg='cyan',padx=10)
w.pack(padx=15,pady=20,side=LEFT)

z=Button(f,text="Exit",font='arial 20',fg='cyan',padx=25,bg='gray')
z.pack(padx=15,pady=20,side=RIGHT)

w.bind('<Button-1>',write)
z.bind('<Double-1>',quit)
root.mainloop()