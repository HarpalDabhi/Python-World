from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.geometry("700x350")
root.title("Message Box Alert !!!")

def prints():
    print("I am a Print Function!!!")

def info():
    a=msg.showinfo("Information Title","I am Information !!!")

def askquestion():
    b=msg.askquestion("Recharge Expired","Your Confirm is Ready ??")

def retry():
    c=msg.askretrycancel("Cancel ??? ")

def xyz():
    d=msg.askyesnocancel("Hello")

def abc():
    e=msg.askokcancel("Ok Cancel")
manu=Menu(root)
root.config(menu=manu)

m1=Menu(manu,tearoff=0)
m1.add_command(label="B.Tech")
m1.add_command(label="B.A.")
m1.add_command(label="B.B.A.")
m1.add_command(label="B.Com")
manu.add_cascade(label="Branch",menu=m1)

m2=Menu(manu,tearoff=0)
m2.add_command(label="Print",command=prints)
m2.add_command(label="Info",command=info)
m2.add_command(label="Ask",command=askquestion)
m2.add_command(label="Retry",command=retry)
m2.add_command(label="Ask no Cancel",command=xyz)
m2.add_command(label="Ok Cancel",command=abc)
manu.add_cascade(label="Message",menu=m2)

root.mainloop()