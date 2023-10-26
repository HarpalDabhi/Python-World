from tkinter import *
root=Tk()
root.geometry('600x400')
f1=Frame(root,borderwidth=1,bg="red",relief=SOLID)
f1.pack(fill='x')
t1="Welcome to My Framework in Python tkinter"
t1=t1.upper()
l1=Label(f1,text=t1,font="Mageto 20",padx=20,pady=20,bg="red",fg="ghostwhite")
l1.pack(pady=20)

f2=Frame(root,borderwidth=1,bg="red",relief=SOLID)
f2.pack(fill='y',side=LEFT,pady=20)

l2=Label(f2,text="Home",font="Mageto 20",padx=40,pady=10,bg="pink")
l2.pack(padx=25,pady=5,anchor='nw')

l3=Label(f2,text="Security",font="Mageto 20",padx=40,pady=10,bg="pink")
l3.pack(padx=25,pady=5,anchor='nw')

l4=Label(f2,text="Reports",font="Mageto 20",padx=40,pady=10,bg="pink")
l4.pack(padx=25,pady=5,anchor='nw')

l5=Label(f2,text="Fitness",font="Mageto 20",padx=40,pady=10,bg="pink")
l5.pack(padx=25,pady=5,anchor='nw')

l6=Label(f2,text="Marketing",font="Mageto 20",padx=40,pady=10,bg="pink")
l6.pack(padx=25,pady=5,anchor='nw')

l7=Label(f2,text="Setting",font="Mageto 20",padx=40,pady=10,bg="pink")
l7.pack(padx=25,pady=5,anchor='nw')

f3=Frame(root,borderwidth=5,bg="red")
f3.pack(padx=20,pady=30)

l9=Label(f3,text="Vivo v23 Pro",font='verdana 25 bold',bg='red')
l9.pack(padx=20,pady=12)

x="""
For the quarter ended 30-09-2022,\n 
the company has reported a Consolidated \n
Total Income  of Rs 12.68 Crore, up\n 
12.56  % from last quarter   Total Income \n
of Rs 11.26 Crore and up 24.32 % from \n 
last  year same quarter Total Income of \n
Rs 10.20 Crore. Company has   reported \n 
net   profit after tax of Rs """
l8=Label(f3,text=x,font='arial 15',borderwidth=5,padx=200,pady=50)
l8.pack(fill='x')

# this is footer 
# f4=Frame(root,borderwidth=1,relief=SOLID,bg='gray')
# l10=Label(f4,text="All Rights Reserved",font='arial 25',borderwidth=1,relief=SOLID)
# l10.pack(fill='x')
root.mainloop()