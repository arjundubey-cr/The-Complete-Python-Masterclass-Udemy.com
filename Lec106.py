from tkinter import *

def function1():
    print("Button Clicked")

root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)
subsubmenu=Menu(submenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Project", command = function1)
submenu.add_command(label="Save", command=function1)
submenu.add_separator()
submenu.add_cascade(label="Exit", menu=subsubmenu)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo", command=function1)





root.mainloop()
