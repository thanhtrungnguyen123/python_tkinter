from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Learn To code at thanh trung")
root.iconbitmap("D:\python\python window tkinter\images\icon.ico")
root.geometry("400x400")

# Databeses

# Create a databese or connect to one
conn = sqlite3.connect('address_book.db')

# # Create cursor 
c = conn.cursor()

# Create table

# c.execute("""CREATE TABLE addresses (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#           )""")




# Commit changes
conn.commit()

# close
conn.close()


root.mainloop()
