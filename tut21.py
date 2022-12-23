from tkinter import *


def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1


i = 0
root = Tk()
root.geometry("500x400")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "Plz enter a eliment")
Button(root, text="add item", command=add).pack()

root.mainloop()
