from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To code at thanh trung')
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")

my_img_1 = ImageTk.PhotoImage(Image.open("D:\python\python window tkinter\images\meo.jpg"))
my_img_2 = ImageTk.PhotoImage(Image.open("D:\python\python window tkinter\images\meocon.jpg",))
my_img_3 = ImageTk.PhotoImage(Image.open("D:\python\python window tkinter\images\doraemon.webp"))


image_list = [my_img_1, my_img_2, my_img_3 ]

my_label = Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3,)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root,text="image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root,text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root,text="image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_Exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2),)

button_back.grid(row=1, column=0)
button_Exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

root.mainloop()
