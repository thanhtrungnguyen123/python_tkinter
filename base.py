from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("learn to code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")

def open():
    global my_img
    top = Tk()
    top.title("my consecond window ")
    top.iconbitmap("D:\python\python window tkinter\images\icon.ico")
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("D:\python\python window tkinter\images\doraemon.webp"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.deiconify).pack()

btn = Button(root, text="Open Second widow", command=open).pack()

mainloop()
