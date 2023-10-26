from tkinter import *

from PIL import Image,ImageTk

root=Tk()

root.geometry('420x400')

#   1.
# pvar=PhotoImage(file='select_photo.png')
# Label(image=pvar).pack()

#   2.
# pvar2=PhotoImage(file='princhhu.png')
# Label(image=pvar2).pack()

#   3.
# img=Image.open('harpal_kinju.jpg')
# photo=ImageTk.PhotoImage(img)
# Label(image=photo).pack()

#   4.
# img2=Image.open('you.ico')
# pht=ImageTk.PhotoImage(img2)
# Label(image=pht).pack()

#   5.
# img_exp=Image.open('experience.ico')
# ph=ImageTk.PhotoImage(img_exp)
# Label(image=ph).pack()

# 6.
y_img=Image.open('YouTube.png')
ph=ImageTk.PhotoImage(y_img)
Label(image=ph).pack()

root.mainloop()