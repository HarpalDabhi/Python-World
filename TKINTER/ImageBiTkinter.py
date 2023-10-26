from tkinter import *
from PIL import Image,ImageTk
root=Tk()

image=Image.open("harpal_kinju.jpg")

photo=ImageTk.PhotoImage(image) 
# img=PhotoImage(file="harpal_kinju.jpg")

image_label=Label(image=photo).pack()

l1=Label(text="Harpal Dabhi").pack()

root.mainloop()