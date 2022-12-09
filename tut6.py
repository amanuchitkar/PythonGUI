from tkinter import *

#  Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

root = Tk()
root.geometry("800x600")
root.title("My GUI")
d_label = Label(text='''A cybercrime is a crime that involves a computer or a computer network. The computer may 
have been used in committing the crime, or it may be the target. Cybercrime may harm someone's security or 
finances.

There are many privacy concerns surrounding cybercrime when confidential information is intercepted or disclosed, 
lawfully or otherwise. Internationally, both governmental and non-state actors engage in cybercrimes, 
including espionage, financial theft, and other cross-border crimes. Cybercrimes crossing international borders and 
involving the actions of at least one nation-state are sometimes referred to as cyberwarfare. Warren Buffett 
describes cybercrime as the "number one problem with mankind" and said that cybercrime "poses real risks to 
humanity."''', bg="black", fg="white", padx=100, pady=20, font=("comicsansms", 19, "bold"))
d_label.pack()
root.mainloop()
