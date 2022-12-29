from tkinter import *


def Upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now..")


root = Tk()
root.title("Status bar")
root.geometry("600x200")
statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W)
sbar.pack(fill=X, side=BOTTOM, pady=2, padx=1)
Button(root, text="Upload", command=Upload).pack()
root.mainloop()
