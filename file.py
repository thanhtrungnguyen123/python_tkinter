from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("learn to code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")



def open():
    global my_image
    root.filename =filedialog.asksaveasfilename(initialdir="\python\python window tkinter/images",
    title="good lucy", filetypes=(("png files", "*.png"),("all files", ".")))
    my_label = Label(root, text="root.filename").pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()