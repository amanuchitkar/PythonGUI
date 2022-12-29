from tkinter import *

root = Tk()
root.title("This is my Gui")
root.geometry("300x200")
root.wm_iconbitmap("images/notepad.ico")
root.configure(background="gray")
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
print(f"{width}x{height}")
Button(text="stop", command=root.destroy).pack()
root.mainloop()
