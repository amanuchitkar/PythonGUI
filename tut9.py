from tkinter import *

root = Tk()
root.geometry("500x250")
frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")


def hello():
    print("Hello tkinter buttons")


def name():
    print("My name is aman ")


b1 = Button(frame, bg="black", fg="red", text="print now", command=hello)
b1.pack(side=LEFT, padx=20)
b2 = Button(frame, bg="black", fg="white", text="Tell me your name",command=name)
b2.pack(side=LEFT, padx=20)
b3 = Button(frame, bg="black", fg="red", text="print now")
b3.pack(side=LEFT, padx=20)
b4 = Button(frame, bg="black", fg="red", text="print now")
b4.pack(side=LEFT, padx=20)

root.mainloop()
