from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.geometry('700x400')
root.title("Harpal Blogger")

f1=Frame(root,borderwidth=2,relief=SUNKEN).pack()
l1=Label(f1,text="Welcome to My Blogger Website",font="arial 20",fg='white',bg='gray',padx=10,pady=30).pack(fill='x')

f2=Frame(root,borderwidth=3,relief=SOLID).pack(side=LEFT,anchor='ne',padx=10)
pht=PhotoImage(file='A_YouTube.png')
Label(f2,image=pht,bg='gray').pack(side=LEFT)

txt='''lorem inpsum dolor sit amet, consectetur adipiscing el aspect, sed do eiusmod 
tempor incididunt ut labore et and so the temp dir temp vars are there instead of in 
this directory (     Temporary directory for storing temporary files under  
different       jars names why this is so on html is the programming not language but it 
is only a markup language'''
f3=Frame(root,borderwidth=3,relief=SOLID,padx=20,bg='blue').pack(side=RIGHT,anchor='nw',padx=10)
Label(f3,text=txt,font='arial 18',fg='gray',padx=20,pady=20).pack(side=RIGHT)
root.mainloop()