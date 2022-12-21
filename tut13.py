from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0)

can_widget.create_rectangle(20, 30, 600, 300, fill="light blue")

can_widget.create_text(200, 100, text="python")

can_widget.create_oval(200, 100, 700, 230)

can_widget.create_arc(100, 300, 700, 200)

can_widget.create_bitmap(100, 100)

can_widget.create_window(200, 100)

root.mainloop()
