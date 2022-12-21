from tkinter import *


def aman(event):
    print(f"You click button at {event.x},{event.y}")


root = Tk()
root.title("Events in tkinter")
root.geometry("600x300")
widget = Button(root, text="Click me please")
widget.pack()
widget.bind('<Button-1>', aman)
widget.bind('<Double-1>', quit)

root.mainloop()
