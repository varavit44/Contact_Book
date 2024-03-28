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

#Placing components in the left frame
Label(left_frame, text='Name', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.05)

name_entry = Entry(left_frame, width=15, font=("verdana, 11"),
textvariable=name_strvar)
name_entry.place(relx=0.1, rely=0.1)

Label(left_frame, text='Phone no.', bg=lf_bg, 
font=frame_font).place(relx=0.23, rely=0.2)

phone_entry = Entry(left_frame, width=15, font=("Verdana", 11),
textvariable=phone_strvar)
phone_entry.place(relx=0.1, rely=0.25)

Label(left_frame, text='Email', bg=lf_bg, font=frame_font).place(relx=0.3, rely=0.35)

email_entry = Entry(left_frame ,width=15, font=("Verdana", 11),
                    textvariable=email_strvar)
email_entry.place(relx=0.1, rely=0.4)

Label(left_frame, text="Address", bg=lf_bg, font=frame_font).place(relx=0.28, rely=0.5)

address_entry = Text(left_frame, width=15, font=("Verdana", 11),
                     height=5)
address_entry.place(relx=0.1, rely=0.55)

#Placing component in middle frame
search_entry = Entry(center_frame, width=18, font=("Verdana", 12),
                     textvariable=search_strvar).place(relx=0.08, rely=0.04)

Button(center_frame, text='search', font=frame_font, width=15,
       command=search).place(relx=0.13, rely=0.1)
Button(center_frame, text='Add Record', font=frame_font, width=15,
       command=submit_record).place(relx=0.13, rely=0.2)
Button(center_frame, text='View Record', font=frame_font, width=15,
       command=view_record).place(relx=0.13,rely=0.3)
Button(center_frame, text='Clear Fields', font=frame_font, width=15,
       command=clear_fields).place(relx=0.13, rely=0.4)
Button(center_frame, text='Delete Record', font=frame_font, width=15,
       command=delete_record).place(relx=0.13, rely=0.5)
Button(center_frame, text='Delete All Record', font=frame_font, width=15,
       command=delete_all_record).place(relx=0.13, rely=0.6)

#Placing components in the right frame
Label(right_frame, text='Saved Contacts', font=("Noto sans CJK TC", 14),
      bg=rf_bg).place(relx=0.25, rely=0.05)

listbox = Listbox(right_frame, selectbackground='SkyBlue', bg='Gainsboro',
                  font=('Helvetica, 12'), height=20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.1, rely=0.15)

list_contacts()

#Defining the functions
def submit_record():
    global name_strvar, email_strvar, phone_strvar, address_entry
    global cursor
    name, email, phone, address = name_strvar.get(), email_strvar.get(),phone_strvar.get(), address_entry.get(1.0, END)
    
    if name=='' or email=='' or phone=='' or address=='':
        mb.showerror('Error!', "Please fill all the fields")
    else:
        cursor.execute(
            "INSERT INTO CONTACT_BOOK (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (?,?,?,?)", 
            (name, email, phone, address))
        connector.commit()
        mb.showinfo('Contact added', 'We have stored the contact successfully!')
        listbox.delete(0, END)
        list_contacts()
        clear_field()

def list_contacts():
    curr = connector.execute('SELECT NAME FROM CONTACT_BOOK')
    fetch = curr.fetchall()

    for data in fetch:
        listbox.insert(END, data)

def delete_record():
    global listbox, connector, cursor
    
    if not listbox.get(ACTIVE):
        mb.showerror("No item selected", "You have not selected any item!")

    cursor.execute('DELETE FROM CONTACT_BOOK WHERE NAME=?', (listbox.get(ACTIVE)))
    connector.commit()

    mb.showinfo('Contact deleted', 'The desired contact has been deleted')
    listbox.delete(0, END)
    list_contacts()

def view_record():
    global name_strvar, phone_strvar, email_strvar, address_entry, listbox

    curr = cursor.execute('SELECT * FROM CONTACT_BOOK WHWRE NAME=?',
                          listbox.get(ACTIVE))
    values = curr.fetchall()[0]

    name_strvar.set(values[1]); phone_strvar.set(values[3]); email_strvar.set(values[2])

    address_entry.delete(1.0, END)
    address_entry.insert(END, values[4])