from tkinter import *

root = Tk()
root.title("scroll bar")
root.geometry("400x300")
scrollbary = Scrollbar(root)
scrollbary.pack(side=RIGHT, fill=Y)
lbx = Listbox(root, yscrollcommand=scrollbary.set)
for i in range(38):
    lbx.insert(END, f"Item {i}")
scrollbary.config(command=lbx.yview)
lbx.pack()

root.mainloop()
