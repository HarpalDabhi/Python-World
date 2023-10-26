from tkinter import *

root=Tk()

root.geometry("800x400")

x='''a computer program that lets you look at words and pictures from \nother computer systems by receiving information through telephone \nwires '''

table_test=Label(text=x,fg='white',bg='green',font='verdana 22 bold',padx='20',pady='30',justify='center',)
table_test.pack()

y='''A search engine is a software system designed to carry out web \nsearches. They search the World Wide Web in a systematic way for \nparticular information specified in a textual web search query. The \nsearch results are generally presented in a line of results,\n '''

para_test=Label(text=y,fg='white',bg='purple',font='arial 22 bold',padx='20',pady='30',justify='center',)
para_test.pack()
root.mainloop()