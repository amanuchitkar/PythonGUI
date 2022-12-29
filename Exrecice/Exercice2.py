from tkinter import *


def Resizeit():
    root.geometry(f"{width.get()}x{height.get()}")


root = Tk()
root.title("Resize Window")
root.geometry("290x200")
Label(root, text="Resize Window", padx=50, pady=14, font="comicsansms 11 bold").grid(row=1, column=2)
Label(root, text="Height").grid(row=2, column=0)
Label(root, text="Width").grid(row=3, column=0)
height = StringVar()
width = StringVar()
Entry(root, textvariable=height).grid(row=2, column=2)
Entry(root, textvariable=width).grid(row=3, column=2)

Button(root, text="Resize it!!", command=Resizeit).grid(row=4, column=2)

root.mainloop()
