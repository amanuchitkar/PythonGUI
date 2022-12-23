from tkinter import *


def myfunc():
    print("myfunc")
    # pass


root = Tk()
root.geometry("700x350")
root.title("Pycharm")

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mymenu = Menu(root)
m1 = Menu(mymenu, tearoff=0)
m1.add_command(label="New file", command=myfunc)
m1.add_command(label="Rename", command=myfunc)
mymenu.add_cascade(label="File", menu=m1)

m2 = Menu(mymenu, tearoff=0)
m2.add_command(label="undo")
m2.add_separator()
m2.add_command(label="copy")
m2.add_command(label="past")
m2.add_command(label="cut")
mymenu.add_cascade(label="Edit", menu=m2)

root.config(menu=mymenu)
root.mainloop()
