from tkinter import *


def getvalue():
    print(f"username is {uservalue.get()}")
    print(f"Password is {passvalue.get()}")


root = Tk()
root.geometry("500x250")
user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)
# BooleanVar,IntVar,StringVar,DoubleVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit", command=getvalue).grid(column=1)
root.mainloop()
