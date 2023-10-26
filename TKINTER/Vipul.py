from tkinter import*

root=Tk()

root.geometry('700x500')

t1=root.title("Sardhar 2.0.3")

l1=Label(text="Vipul at Saradhar",fg='blue',font='arial 25 bold')
l1.pack()

text1="I am studing in the RK University of Technology wherer I am studying in the 4th semester and I am very big lover of the project"
para1=Label(text=text1,borderwidth="5px",fg="red",font='arial 18 bold',padx='15px')
para1.pack(fill='x',padx='10px',pady='10px')

root.iconbitmap('you.ico')

Label(text=" Name : ",font="verdana 15 bold").grid(row=0,column=0)
name=Entry(bg="gray",font="verdana 15 ",).grid(row=0,column=1)

Label(text=" Email : ",font="verdana 15 bold").grid(row=1,column=0)
email=Entry(bg="gray",font="verdana 15 ",).grid(row=1,column=1)

Label(text=" City : ",font="verdana 15 bold").grid(row=2,column=0)
city=Entry(bg="gray",font="verdana 15 ",).grid(row=2,column=1)

Label(text=" Mobile : ",font="verdana 15 bold").grid(row=3,column=0)
tel=Entry(bg="gray",font="verdana 15 ",).grid(row=3,column=1)


button=Button(text="Submit",font="verdana 15 bold",bg="red",fg="white",)
button.grid(row=4,column=1)

root.mainloop()