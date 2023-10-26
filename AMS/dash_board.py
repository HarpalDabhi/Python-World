from tkinter import *

root=Tk()

root.title("Attendance Management System")

root.geometry('1920x1080')

### TODO   👻👻👻 Header Frame ### 👻👻👻

header_text="Welcome to Tkinter"

head_frame=Frame(background='red')
head_frame.pack(side=TOP,fill='x')

heading=Label(head_frame,text=header_text,font="arial 18 ",bg='red',padx=10,pady=10).pack()

### TODO   👻👻👻 Sidebar  Frame ### 👻👻👻

side_bar_frame=Frame(root,background='blue')
side_bar_frame.pack(side=LEFT)

# bat_item_1= 



root.mainloop()