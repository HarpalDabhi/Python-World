from tkinter import *
hr=Tk()
hr.geometry('500x350')
hr.title('List Box Items')

def add_item():
    global i
    list_box.insert(ACTIVE,f"Item -{i}")
    i+=1
i=1

def delete_item():
    list_box.delete(ACTIVE)
list_box=Listbox(hr,font='verdana 18 bold',justify=CENTER,bg='pink',fg='cyan',borderwidth=2,relief=SOLID)
list_box.pack()
list_box.insert(END,'__END__',)


btn=Button(text='ADD ITEM',command=add_item,pady=10,padx=30,font='verdana 20 bold')
btn.pack(side='left')

btn2=Button(text='REMOVE ITEM',command=delete_item,pady=10,padx=30,font='verdana 20 bold')
btn2.pack(side='right')
hr.mainloop()