from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To code Radio ")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")

r = IntVar()
r.set("2")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Chese","Chese"),
    ("Musheroom","Musheroom"),
    ("onion","onion"),
]

pizza = StringVar()
pizza.set("pepperoni")

for text, mode in MODES:
    Radiobutton(root,text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()

myButton = Button(root, text="click me", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
