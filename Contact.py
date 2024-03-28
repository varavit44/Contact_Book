from tkinter import *
import tkinter.messagebox as mb
import sqlite3
#Create database using sqlite3
connector = sqlite3.connect('contacts.db')
#Assign database to variable
cursor = connector.cursor()

#Create variable in database
cursor.execute(
"CREATE TABLE IF NOT EXISTS CONTACT_BOOK (S_NO INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NUMBER TEXT, ADDRESS TEXT)"
)

#Initializing the GUI window
root = Tk()
root.title("TechVidvan Contact Book")
root.geometry('700x500')
root.resizable(0, 0)

#Creating the color and font variables
lf_bg = 'Gray70' # Lightest shade
cf_bg = 'Gray57'
rf_bg = 'Gray35' #Darkest shade
frame_font = ("Garamond, 14")

#Creating the StringVar variable
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()

#Creating and placing the components in the window
Label(root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"),
bg = 'Black', fg = 'White').pack(side=TOP, fill=X)

#Frame on the left
left_frame = Frame(root, bg=lf_bg)
left_frame.place(relx=0, relheight=1, y=30, relwidth=0.3)

#Frame on the center
center_frame = Frame(root, bg=cf_bg)
center_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)

#Frame on the right
right_frame = Frame(root, bg=rf_bg)
center_frame.place(relx=0.6, relheight=1, y=30, relwidth=0.4)
