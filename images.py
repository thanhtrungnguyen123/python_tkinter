from tkinter import*
from PIL import ImageTk,Image


root =Tk()
root.title('Learn To code at thanh trung')
# root.iconbitmap("D:\python/python window tkinter\images\icon.ico")

# my_img = ImageTk.PhotoImage(Image.open("thanh trung.png"))
# my_label = Label(image=my_img)
# my_label.pack()




button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()
