from tkinter import *


def getvalue():
    with open("tut12.txt","a") as f:
        f.write(f"{namevalue.get(),Phonevalue.get(),gendervalue.get(),Emergencyvalue.get(),Paymentvalue.get(),foodservicevalue.get()}\n")
    print(f"{namevalue.get(),Phonevalue.get(),gendervalue.get(),Emergencyvalue.get(),Paymentvalue.get(),foodservicevalue.get()}")


root = Tk()
root.geometry("500x300")
Label(root, text="Welcome aman travels", font="comicsansms 16 bold", pady=20).grid(row=0, column=3)

name = Label(root, text="Name:")
Phone = Label(root, text="Phone:")
Gender = Label(root, text="Gender:")
Emergency_contact = Label(root, text="Emergency contact:", padx=20)
Payment_mode = Label(root, text="Payment mode:")

name.grid(row=1, column=0)
Phone.grid(row=2, column=0)
Gender.grid(row=3, column=0)
Emergency_contact.grid(row=4, column=0)

Payment_mode.grid(row=5, column=0)

namevalue = StringVar()
Phonevalue = StringVar()
gendervalue = StringVar()
Emergencyvalue = StringVar()
Paymentvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
Phoneentry = Entry(root, textvariable=Phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
Emergencyentry = Entry(root, textvariable=Emergencyvalue)
Paymententry = Entry(root, textvariable=Paymentvalue)

nameentry.grid(row=1, column=1)
Phoneentry.grid(row=2, column=1)
genderentry.grid(row=3, column=1)
Emergencyentry.grid(row=4, column=1)
Paymententry.grid(row=5, column=1)
foodservice = Checkbutton(text="want to pre book your meals?", variable=foodservicevalue)
foodservice.grid(row=6,column=1)

Button(root, text="submit", command=getvalue).grid()
root.mainloop()
