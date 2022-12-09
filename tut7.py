from tkinter import *

root = Tk()
root.geometry("600x300")
root.title("Pycharm")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project-Pycharm")
l.pack(pady=10, padx=5)
m = Label(f2, text="Python-GUI", font="Helvetica 16 bold", pady=2, fg="red")
m.pack()
root.mainloop()
