from tkinter import *
from PIL import Image,ImageTk

root=Tk()

root.geometry('600x400')

Y_img=Image.open('YouTube.png')
pht=ImageTk.PhotoImage(Y_img)
Label(image=pht,bg='cyan').pack(fill='x')

root.title("Harpal Tkinter")

a=Label(text='''A search engine is a software system designed to carry out web \nsearches. They search the World Wide Web in a systematic way for \nparticular information specified in a textual web search query. The \nsearch results are generally presented in a line of results''',fg="blue",bg="cyan",padx='50',pady=50,font=('verdana',20),borderwidth=5,relief=SUNKEN)

a.pack(fill='x')

x='''a computer program that lets you look \n at words and pictures from \nother computer systems by \nreceiving information through telephone \nwires '''

table_test=Label(text=x,fg='blue',bg='cyan',font='verdana 22 ',padx='95',pady='30',justify='center',borderwidth=5,relief=SUNKEN)
table_test.pack(anchor='ne',side=LEFT,fill='y')

y='''a computer program that lets you look \n at words and pictures from \nother computer systems by \nreceiving information through telephone \nwires '''

table_test=Label(text=y,fg='blue',bg='cyan',font='verdana 22 ',padx='95',pady='30',justify='center',borderwidth=5,relief=SUNKEN)
table_test.pack(anchor='nw',side=RIGHT,fill='y')

root.mainloop()

# Fore Ground Color || Bg Color || Font Style Size Type || Padx || Pady || borderwidth || relief || justify || side || anchor || fill || 