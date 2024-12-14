from tkinter import*

root = Tk()

# e = Entry(root, width=50, fg="white", bg="blue", borderwidth=5)
# e.pack()
#Creating a Buttons wedget
# def Mycilck():
#     mylabel = Label(root, text='I am thanh trung')
#     mylabel.pack()

# my_button = Button(root, text='cilck me!', fg='blue', command=Mycilck,).pack()
# .get()
e = Entry(root, width=50)
e.pack()

def Mycilck():
    hello = "hello " + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()

my_button = Button(root, text="Enter your Name stock Quocte", command=Mycilck)
my_button.pack()
root.mainloop()