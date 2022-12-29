from tkinter import *


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")

    def Status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, anchor=W, relief=SUNKEN)
        self.statusbar.pack(fill=X, side=BOTTOM)

    def Click(self):
        print("button clicked")

    def Button(self, textinp):
        Button(text=textinp, command=self.Click).pack()


if __name__ == '__main__':
    window = GUI()
    window.geometry()
    window.Status()
    window.Button("apply")
    window.mainloop()
