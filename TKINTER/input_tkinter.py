from tkinter import *

root=Tk()

def print_cmd():
    print("Clicked")
    x=input_text.get()
    y=input_text2.get()
    print(x,y)

root.geometry('800x500')


Label(text="Harpal Dabhi",fg="blue",bg="orange",font="verdana 18 bold").pack(side=LEFT,fill="y")

Label(text="Home    About      contact",fg="white",bg="black",font="verdana 18 bold",borderwidth='5').pack(side=TOP,fill="x")

root.title("Harpal Dabhi GUI")

input_text=Entry(text="Enter Your Name ",fg="white",bg="orange",font="verdana 18 bold",borderwidth='5')
input_text.pack()

input_text2=Entry(text="Enter Your Surname ",fg="white",bg="orange",font="verdana 18 bold",borderwidth='5')
input_text2.pack()

button=Button(text="Print",fg="white",bg="red",font="verdana 18 bold",borderwidth="6",padx="10",command=print_cmd)
button.pack()

root.mainloop()