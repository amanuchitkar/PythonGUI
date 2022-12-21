from tkinter import *
from PIL import ImageTk, Image


def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text


root = Tk()
root.title("Apna Akhabaar")
root.geometry("1000x1000")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i + 1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i + 1}.png")
    # TODO: Resize these images
    image = image.resize((390, 210), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=30)
Label(f0, text="Cyber News", font="lucida 33 bold").pack()
Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()

f1 = Frame(root, width=900, height=150)
Label(f1, text=texts[0], padx=10).pack(side=LEFT)
Label(f1, image=photos[0], anchor="e").pack(pady=10, padx=0)
f1.pack(anchor="w")

f2 = Frame(root, width=900, height=150)
Label(f2, text=texts[1], padx=10).pack(side=RIGHT)
Label(f2, image=photos[1], anchor="w").pack(padx=10, pady=0)
f2.pack(anchor="e")

f3 = Frame(root, width=900, height=150)
Label(f3, text=texts[2], padx=10).pack(side=LEFT)
Label(f3, image=photos[2], anchor="e").pack(padx=10, pady=0)
f3.pack(anchor="w")

root.mainloop()
