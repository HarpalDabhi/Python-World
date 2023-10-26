from tkinter import *
root=Tk()
root.geometry('600x300')
root.title("Visual Studio Code")
mn=Menu(root)
root.config(menu=mn)

m1=Menu(mn,tearoff=0)
m1.add_command(label="New Text File")
m1.add_command(label="New File")
m1.add_command(label="New Windows")
m1.add_separator()

m1.add_command(label="Open File")
m1.add_command(label="Open Folder")
m1.add_command(label="Open Workspace from File")
m1.add_command(label="Open Recent")
m1.add_separator()

m1.add_command(label="Add Folder to Workspace...")
m1.add_command(label="Save Workspace As...")
m1.add_command(label="Duplicate Workspace...")
m1.add_separator()

m1.add_command(label="Save")
m1.add_command(label="Save As...")
m1.add_separator()

m1.add_command(label="Share >")
m1.add_separator()

m1.add_command(label=" < Auto Save")
m1.add_command(label="Preferences >")
m1.add_separator()

m1.add_command(label="Revert File")
m1.add_command(label="Close Editor")
m1.add_command(label="Close Folder")
m1.add_command(label="Close Windows")
m1.add_separator()

m1.add_command(label="Exit",command=quit)

mn.add_cascade(label="File",menu=m1)


# Edit Preview

m2=Menu(mn,tearoff=0)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()

m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m2.add_separator()

m2.add_command(label="Find")
m2.add_command(label="Replace")
m2.add_separator()

m2.add_command(label="Find in Files")
m2.add_command(label="Replace in Files")
m2.add_separator()

m2.add_command(label="Toggle line Comment")
m2.add_command(label="Toggle Block Comment")
m2.add_command(label="Emmet : Expand Abbreviation")

mn.add_cascade(label="Edit",menu=m2)

# Selection 
m3=Menu(mn,tearoff=0)
m3.add_command(label="Select All") 
m3.add_command(label="Expand Selection") 
m3.add_command(label="Shrink Selection") 
m3.add_separator()

m3.add_command(label="Copy Line Up")
m3.add_command(label="Copy Line Down")
m3.add_command(label="Move Line Up")
m3.add_command(label="Move Line Down")
m3.add_command(label="Duplicate Selection")
m3.add_separator()

m3.add_command(label="Add Cursor Above")
m3.add_command(label="Add Cursor Below")
m3.add_command(label="Add Cursors to Line Ends")
m3.add_command(label="Add Next Occurence")
m3.add_command(label="Add Previous Occurence")
m3.add_command(label="Select All Occurences")
m3.add_separator()

m3.add_command(label="Switch to Ctrl+Click for Multi-Cursor")
m3.add_command(label="Column Selection Mode")
m3.add_separator()

mn.add_cascade(label="Selection",menu=m3)
root.mainloop()