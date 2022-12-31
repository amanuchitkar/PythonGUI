from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("All Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt", filetypes=[("All Files", "*.*"), ("All Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "a")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("file save")

    else:
        f = open(file, "a")
        f.write(textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad made by Aman")


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled-Notepad")
    textarea = Text(root, font="lucida 13")
    file = None
    textarea.pack(fill=BOTH, expand=True, padx=4)
    root.wm_iconbitmap("../images/notepad.ico")
    root.geometry("644x644")

    menubar = Menu(root)
    # file menu start
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=newfile)

    filemenu.add_command(label="Open", command=openfile)

    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitApp)
    menubar.add_cascade(label="File", menu=filemenu)
    # Edit menu starts
    Editmenu = Menu(menubar, tearoff=0)
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=Editmenu)
    # Help menu starts
    Helpmenu = Menu(menubar, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=menubar)
    # Adding scrollbar
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)
    root.mainloop()
