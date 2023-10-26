from tkinter import *

root=Tk()

root.geometry("500x500")


for i in range(1,11):
    
    # table_test=Label(text='22   x   =  ' + str(i),fg='white',bg="gray",font='verdana 19 bold')
    x=f"22 x {i} = {i*22}"
    table_test=Label(text=x,fg='white',bg='black',font='verdana 22 bold',padx='10',pady='10')
    table_test.pack(fill='x')

resul=12-4 * (16//2**4)+32
print(resul)
root.mainloop()