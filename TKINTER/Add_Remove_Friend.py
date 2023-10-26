from tkinter import *
root=Tk()
root.geometry('600x400')
root.title('NoteBook Friends Request !')

def add_friend():
    listbox.insert(ACTIVE,name.get())

def delete_friend():
    listbox.delete(ACTIVE)

f1=Frame(root,borderwidth=2,relief=SOLID,bg='blue')
f1.pack(fill='x')

l1=Label(f1,text='Make a new NoteBook Friends',font='verdana 28 bold',bg='blue',padx=10,pady=20,fg='ghostwhite')
l1.pack(padx=10,pady=20,fill='x')

name=StringVar()
Label(f1,text="Enter Friend Name :",font='verdana 20 bold',bg='blue',fg='white').pack(padx=20,pady=20)
Entry(f1,textvariable=name,font='verdana 20',bg='cyan').pack()

listbox=Listbox(f1,font='verdana 18 ',justify=CENTER,bg='cyan')
listbox.pack(fill='x',padx=10,pady=10)
listbox.insert(END,'End')

btn=Button(f1,text='Add Friend',command=add_friend,pady=10,padx=30,font='verdana 20 bold',bg='cyan')
btn.pack(side='left',padx=20,pady=20)

btn2=Button(f1,text='Remove Friend',command=delete_friend,pady=10,padx=30,font='verdana 20 bold',bg='gray')
btn2.pack(side='right',padx=20,pady=20)
root.mainloop()