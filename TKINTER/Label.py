from tkinter import *

root=Tk()

root.geometry('600x600')

# root.minsize(200,200)

# root.maxsize(1000,500)
car=['Kinjal', 'Purvi', 'Kajal','Komal']

for x in car:

    lable_text=Label(text=x+" is My Sister",fg="white",bg="black",padx='40',pady='40',font='bold',)

    lable_text.pack() 


root.mainloop()