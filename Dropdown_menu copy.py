from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn To code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")
root.geometry("400x400")

# Drop down  boxes
clicked = StringVar()

drop = OptionMenu(root, clicked, "monday", "Tueday", "wedneday", "Thursday", "friday")
drop.pack()

root.mainloop()
