from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")

    def status(self):
        self.var=StringVar()
        self.var.set("Process..")
        self.statebar=Label(self,textvariable=self.var,relief=SUNKEN,anchor="w")
        self.statebar.pack(side=BOTTOM,fill='x')

    def click(self):
        print("Click !!!")
        

    def createbutton(self):
        Button(text="Submit",command=self.click).pack()

if __name__ == "__main__":
    window=GUI()
    window.status()
    window.createbutton()
    window.mainloop()