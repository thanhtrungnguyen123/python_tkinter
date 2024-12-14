from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")

def frame_button():
    print('xin chao')

frame = LabelFrame(root, text="this is my Fram...", padx=50, pady=50,)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don 's Click here !", command=frame_button)
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)


root.mainloop()
