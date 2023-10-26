from tkinter import *

root=Tk()

def data():
    print("Clicked")
    print(name.get())
    # print(email.get())
    # print(city.get())
    # print(tel.get())

root.geometry("600x400")


root.title("Fill Form Details Below")

Label(text=" Name : ",font="verdana 15 bold").grid(row=0,column=0)
name=Entry(bg="gray",font="verdana 15 ",).grid(row=0,column=1)

Label(text=" Email : ",font="verdana 15 bold").grid(row=1,column=0)
email=Entry(bg="gray",font="verdana 15 ",).grid(row=1,column=1)

Label(text=" City : ",font="verdana 15 bold").grid(row=2,column=0)
city=Entry(bg="gray",font="verdana 15 ",).grid(row=2,column=1)

Label(text=" Mobile : ",font="verdana 15 bold").grid(row=3,column=0)
tel=Entry(bg="gray",font="verdana 15 ",).grid(row=3,column=1)


button=Button(text="Submit",font="verdana 15 bold",bg="red",fg="white",command=data)
button.grid(row=4,column=1)

root.mainloop()