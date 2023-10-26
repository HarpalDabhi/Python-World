from tkinter import *
root=Tk()
root.geometry("500x300")
root.title("Status Bar")

def upload():
    statusvar.set("Uploading...")
    import time
    time.sleep(2)
    statusvar.set("Uploaded")
statusvar=StringVar()
statusvar.set("Upload")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor="nw",padx=10,pady=10)
sbar.pack(fill='x',side=BOTTOM)

Button(text="Click",command=upload,padx=10,pady=5,bg='red',fg='white').pack()
root.mainloop()