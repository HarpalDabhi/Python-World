from tkinter import *
root=Tk()
def add_friend():
    global fr_name
    global i
    fr_box.insert(ACTIVE,fr_name[i])
    i+=1

fr_name=['Purvi','Kinjal','Harpal','Vishal','Jay','Om','Sahil','Kiran','Jayraj','Malay','Khushi','Kijal','Komal','Tulsi','Ashish','Kuldip','Karan','abhi','bandan','vipul','sonal','shambhu','jay','dhaval','kano','anuj','nikunj','niraj','dhruv','priya','vansh']
i=0

fr_box=Listbox(root)
fr_box.pack()

Button(root,text="Add Items",padx=14,pady=5,font="lucida 22 bold",justify=LEFT,fg="yellow",bg="red",command=add_friend).pack()

scrollbar=Scrollbar(root)
scrollbar.pack(fill='y',side=RIGHT)


for i in fr_name:
    fr_box.insert(END,i)
fr_box.pack(fill="both",padx=10,pady=10)

scrollbar.config(command=fr_box.yview)
root.mainloop()