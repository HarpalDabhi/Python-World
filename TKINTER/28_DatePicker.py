from tkinter import *
from calendar import *

root=Tk()
cal=Calendar(root,selectmode="day",year=2023,month=5,day=10)


def grab():
    pass

mybtn=Button(text="Date",command=grab)
mybtn.pack(pady=20)

mylbl=Label(text="").pack()
root.mainloop()
