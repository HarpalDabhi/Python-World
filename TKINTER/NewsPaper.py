from tkinter import *

from PIL import ImageTk , Image

root=Tk()

root.title("ABP News - HR Dabhi")

root.iconbitmap("you.ico")

root.geometry("900x600")

l1=Label(text="! Launchin New Andoid Vivo v23 pro !",font="Arial 33 bold ",bg="gray",pady=10)
l1.pack(fill='x')

l2=Label(text="2nd February , 2023",fg="white",bg="black",pady=10,padx=10)
l2.pack(fill='x')

x="""
For the quarter ended 30-09-2022,\n 
the company has reported a Consolidated \n
Total Income  of Rs 12.68 Crore, up\n 
12.56  % from last quarter   Total Income \n
of Rs 11.26 Crore and up 24.32 % from \n 
last  year same quarter Total Income of \n
Rs 10.20 Crore. Company has   reported \n 
net   profit after tax of Rs """
text1=Label(text=x,font='verdana 15',borderwidth=5,relief=SUNKEN,padx=200,pady=50)
text1.pack(side=LEFT)

# photo=PhotoImage(file="select_Photo.png",width=500,height=500)

# im=Label(image=photo)
# im.pack(side=LEFT)

img=Image.open('experience.ico')
photo=ImageTk.PhotoImage(image=img)
Label(image=photo,borderwidth=5,padx=10).pack(side=RIGHT,padx=150,pady=150)

root.mainloop()


