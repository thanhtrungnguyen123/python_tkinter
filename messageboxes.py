from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn To code Radio ")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")

# showinfo, showwarning, showerror, askquaestion, askokcancel, askyesno

def popup():
    response = messagebox.showerror("this is my book", "Hello world trung")
    Label(root, text=response).pack()
    # if response == YES:
    #     Label(root, text="nguyen thanh trung").pack()
    # else:
    #     Label(root, text="dep trai qua").pack()


Button(root, text="popup", command=popup).pack()


mainloop()
