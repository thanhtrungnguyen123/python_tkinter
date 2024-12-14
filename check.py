from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")
root.geometry("400x400")

def show():
    my_label = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text=" your Supermaket", variable=var, onvalue="SuperSize", offvalue="hamburger")
c.deselect()
c.pack()

myButton = Button(root, text="show Selection", command=show).pack()

root.mainloop()
