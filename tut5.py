from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x400")
# photo = PhotoImage(file="cyber.png")
# photo = PhotoImage(file="2.jpg")
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)
labal = Label(image=photo)
labal.pack()
root.mainloop()
