from tkinter import*

root=Tk()

root.geometry('800x500')

root.title("Harpal GUI")

Label(text="Home    About      contact    Help   Feedback   Submission      Modules ",fg="white",bg="black",font="verdana 18 ",borderwidth='5').pack(side=TOP,fill="x")

Button(text="Login",fg="white",bg="black",font="verdana 20 bold").pack(side=TOP,fill="x")

Label(text="Python Tkinter",font="Verdana 25 bold",fg='white',bg='red',).pack(fill='x',padx='10px')


y='''A search engine is a software system designed to carry out web \nsearches. They search the World Wide Web in a systematic way for \nparticular information specified in a textual web search query. The \nsearch results are generally presented in a line of results,\n '''

para1=Label(text=y,font='monospace 18 bold',fg='white',bg="red")
para1.pack(fill='x',pady='10px',padx='10px',)

x='''a computer program that lets you look at words and pictures from \nother computer systems by receiving information through telephone \nwires '''

para2=Label(text=x,font='monospace 18 bold',fg='white',bg="red")
para2.pack(fill='x',pady='10px',padx='10px')

root.mainloop()