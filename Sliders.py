from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) 

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()



my_btn = Button(root, text="click me !", command=slide).pack()

root.mainloop()
