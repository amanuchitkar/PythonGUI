from tkinter import *

root = Tk()
root.title("scroll bar")
root.geometry("400x300")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# listbox = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(50):
#     listbox.insert(END, f"Item {i}")
# listbox.pack(fill=BOTH, padx=15)
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill="both")
scrollbar.config(command=text.yview)
root.mainloop()
