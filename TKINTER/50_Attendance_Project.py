from tkinter import *
import tkinter.messagebox as msg2

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")

    

    def menus(self):
        menu=Menu(self)
        self.config(menu=menu,padx=15,pady=20)
        m1=Menu(menu,tearoff=0)
        m1.add_command(label="Dashboard")
        m1.add_command(label="Chart")
        m1.add_separator()
        m1.add_command(label="Exit",command=exit)
        menu.add_cascade(label="Home",menu=m1)

        

        m2=Menu(menu,tearoff=0)
        self.config(menu=menu,padx=15,pady=20)
        m2.add_command(label="Division-A",command=self.divA)
        m2.add_command(label="Division-B",command=self.divB)
        m2.add_command(label="Division-C",command=self.divC)
        m2.add_command(label="Division-D",command=self.msg)
        menu.add_cascade(label="Class",menu=m2)

        m3=Menu(menu,tearoff=0)
        self.config(menu=menu,padx=15,pady=20)
        m3.add_command(label="Take Attendance")
        m3.add_command(label="Check Attendance")
        m3.add_command(label="Edit Attendance")
        menu.add_cascade(label="Attendance",menu=m3)


    def click(self):
        print("Click !!!")
    def msg(self):
         msg2.showinfo("Information","No Data Found !!!")

    
    def divA(self):
        root=Tk()

        def submit():
            print("Username :",var.get())
            print("Username 2 :",var2.get())
            print("Username 2 :",var3.get())
            print("Username 2 :",var4.get())
            print("Username 2 :",var5.get())
            print("Username 2 :",var6.get())
        root.geometry('500x350')

        l1=Label(root,text="Fill the Below Form",font='verdana 24',pady=15)
        l1.grid(columnspan=2)

        var=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()

        Label(root,text="Harpal Dabhi",font='verdana 20',pady=20,padx=10).grid(row=1)
        c=Checkbutton(root,variable=var,font='verdana 20',onvalue=1,offvalue=0).grid(row=1,column=1,padx=5,pady=5,)

        Label(root,text="Vipul Jadav",font='verdana 20',pady=20,padx=10).grid(row=2)
        c=Checkbutton(root,variable=var2,font='verdana 20',onvalue=1,offvalue=0).grid(row=2,column=1,padx=5,pady=5,)

        Label(root,text="Malay Goletar",font='verdana 20',pady=20,padx=10).grid(row=3)
        c=Checkbutton(root,variable=var3,font='verdana 20',onvalue=1,offvalue=0).grid(row=3,column=1,padx=5,pady=5,)

        Label(root,text="Jayraj Bhuva",font='verdana 20',pady=20,padx=10).grid(row=4)
        c=Checkbutton(root,variable=var4,font='verdana 20',onvalue=1,offvalue=0).grid(row=4,column=1,padx=5,pady=5,)

        Label(root,text="Elesh Kachchi",font='verdana 20',pady=20,padx=10).grid(row=5)
        c=Checkbutton(root,variable=var5,font='verdana 20',onvalue=1,offvalue=0).grid(row=5,column=1,padx=5,pady=5,)

        Label(root,text="Kuldip Mori",font='verdana 20',pady=20,padx=10).grid(row=6)
        c=Checkbutton(root,variable=var6,font='verdana 20',onvalue=1,offvalue=0).grid(row=6,column=1,padx=5,pady=5,)

        Button(text='Submit',font='verdana 20',padx=15,bg='gray',command=submit).pack(row=8,columnspan=2,pady=15,)
        root.mainloop()

    def divB(self):
        root=Tk()

        def submit():
            print("Username :",var.get())
            print("Username 2 :",var2.get())
            print("Username 2 :",var3.get())
            print("Username 2 :",var4.get())
            print("Username 2 :",var5.get())
            print("Username 2 :",var6.get())
        root.geometry('500x350')

        l1=Label(root,text="Fill the Below Form",font='verdana 24',pady=15)
        l1.grid(columnspan=2)

        var=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()

        Label(root,text="Kanzariya Abhishekh",font='verdana 20',pady=20,padx=10).grid(row=1)
        c=Checkbutton(root,variable=var,font='verdana 20',onvalue=1,offvalue=0).grid(row=1,column=1,padx=5,pady=5,)

        Label(root,text="Keyur Parmar",font='verdana 20',pady=20,padx=10).grid(row=2)
        c=Checkbutton(root,variable=var2,font='verdana 20',onvalue=1,offvalue=0).grid(row=2,column=1,padx=5,pady=5,)

        Label(root,text="Sarvaiya Roanak",font='verdana 20',pady=20,padx=10).grid(row=3)
        c=Checkbutton(root,variable=var3,font='verdana 20',onvalue=1,offvalue=0).grid(row=3,column=1,padx=5,pady=5,)

        Label(root,text="Aron Christian",font='verdana 20',pady=20,padx=10).grid(row=4)
        c=Checkbutton(root,variable=var4,font='verdana 20',onvalue=1,offvalue=0).grid(row=4,column=1,padx=5,pady=5,)

        Label(root,text="Zala Indrajit",font='verdana 20',pady=20,padx=10).grid(row=5)
        c=Checkbutton(root,variable=var5,font='verdana 20',onvalue=1,offvalue=0).grid(row=5,column=1,padx=5,pady=5,)

        Label(root,text="Ladumor Trushit",font='verdana 20',pady=20,padx=10).grid(row=6)
        c=Checkbutton(root,variable=var6,font='verdana 20',onvalue=1,offvalue=0).grid(row=6,column=1,padx=5,pady=5,)

        Button(text='Submit',font='verdana 20',padx=15,bg='gray',command=submit).pack(row=8,columnspan=2,pady=15,)
        root.mainloop()

    def divC(self):
        root=Tk()

        def submit():
            print("Username :",var.get())
            print("Username 2 :",var2.get())
            print("Username 2 :",var3.get())
            print("Username 2 :",var4.get())
            print("Username 2 :",var5.get())
            print("Username 2 :",var6.get())
        root.geometry('500x350')

        l1=Label(root,text="Fill the Below Form",font='verdana 24',pady=15)
        l1.grid(columnspan=2)

        var=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=StringVar()
        var5=StringVar()
        var6=StringVar()

        Label(root,text="Chavda Deep",font='verdana 20',pady=20,padx=10).grid(row=1)
        c=Checkbutton(root,variable=var,font='verdana 20',onvalue=1,offvalue=0).grid(row=1,column=1,padx=5,pady=5,)

        Label(root,text="Zaldeja Ajay",font='verdana 20',pady=20,padx=10).grid(row=2)
        c=Checkbutton(root,variable=var2,font='verdana 20',onvalue=1,offvalue=0).grid(row=2,column=1,padx=5,pady=5,)

        Label(root,text="Vadiya Om",font='verdana 20',pady=20,padx=10).grid(row=3)
        c=Checkbutton(root,variable=var3,font='verdana 20',onvalue=1,offvalue=0).grid(row=3,column=1,padx=5,pady=5,)

        Label(root,text="Sorathiya Sunil",font='verdana 20',pady=20,padx=10).grid(row=4)
        c=Checkbutton(root,variable=var4,font='verdana 20',onvalue=1,offvalue=0).grid(row=4,column=1,padx=5,pady=5,)

        Label(root,text="Vatukiya Ravi",font='verdana 20',pady=20,padx=10).grid(row=5)
        c=Checkbutton(root,variable=var5,font='verdana 20',onvalue=1,offvalue=0).grid(row=5,column=1,padx=5,pady=5,)

        Label(root,text="Dodiya Suresh",font='verdana 20',pady=20,padx=10).grid(row=6)
        c=Checkbutton(root,variable=var6,font='verdana 20',onvalue=1,offvalue=0).grid(row=6,column=1,padx=5,pady=5,)

        Button(text='Submit',font='verdana 20',padx=15,bg='gray',command=submit).pack(row=8,columnspan=2,pady=15,)
        root.mainloop()

    
        

    def createbutton(self):
        Button(text="Submit",command=self.click).pack()

if __name__ == "__main__":
    window=GUI()
    window.menus()
    window.createbutton()
    window.mainloop()