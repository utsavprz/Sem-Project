from tkinter import *
from tkinter import messagebox
from dashboard import *


# function to authenticate the login credentials details with enter key
def enter_key_cred_match(self):
    uname = username_verify.get()
    passwd = password_verify.get()

    if uname == "admin" and passwd == "admin":
        #messagebox.showinfo("EasyInv", "Login Success")
        root.destroy()
        main_win()
    elif uname == "" and passwd == "":
        messagebox.showinfo("EasyInv", "Cannot be kept empty")
    elif uname == "":
        messagebox.showinfo("EasyInv", "Username cannot be kept empty")
    elif passwd == "":
        messagebox.showinfo("EasyInv", "Password cannot be kept empty")
    else:
        messagebox.showinfo("EasyInv", "Credentials do not match ")


# function to authenticate the login credentials details with login button
def button_cred_match():
    uname = username_verify.get()
    passwd = password_verify.get()

    if uname == "admin" and passwd == "admin":
        # messagebox.showinfo("EasyInv", "Login Success")
        root.destroy()
        main_win()
    elif uname == "" and passwd == "":
        messagebox.showinfo("EasyInv", "Cannot be kept empty")
    elif uname == "":
        messagebox.showinfo("EasyInv", "Username cannot be kept empty")
    elif passwd == "":
        messagebox.showinfo("EasyInv", "Password cannot be kept empty")
    else:
        messagebox.showinfo("EasyInv", "Credentials do not match ")


def usrname_on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if username_login_entry.get() == 'Username':
       username_login_entry.config(fg = '#ffffff')
       username_login_entry.delete(0, "end") # delete all the text in the entry
       username_login_entry.insert(0, '') #Insert blank for user input


def usrname_on_focusout(event):
    if username_login_entry.get() == '':
        username_login_entry.insert(0, 'Username')
        username_login_entry.config(fg = '#ffffff')


def password_on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if password_login_entry.get() == 'Password':
       password_login_entry.delete(0, "end") # delete all the text in the entry
       password_login_entry.insert(0, '') #Insert blank for user input
       password_login_entry.config(fg = '#ffffff',show="*")


def password_on_focusout(event):
    if password_login_entry.get() == '':
        password_login_entry.insert(0, 'Password')
        password_login_entry.config(fg = '#ffffff',show="*")


def main_screen():
    global root
    root = Tk()

    root.title("EasyInv")
    root.geometry("1366x768")
    root.resizable(0,0)
    root.configure(bg="#25333C")

    root.iconbitmap('D:\sem project\icon_pack\ico\Database-Upload.ico')

    # creates a login frame
    login_frame = Frame(root, width=1000, height=550, highlightbackground="#e7e7e7", bg="#25333C")
    login_frame.place(x=200,y=100)

    global usr_name
    global pwd
    global username_login_entry
    global password_login_entry
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    logo = PhotoImage(file ='D:\sem project\logo\easyinv_concept.png')
    Label(login_frame, image=logo, bd=0).place(x=100, y=180)

    vertical_seperator = Frame(login_frame, width=1, height=220, bg='#49535B')
    vertical_seperator.place(x=460, y=135)

    # username login and entry box
    username_login_entry = Entry(login_frame, textvariable=username_verify, highlightbackground="#6DDBA0", highlightthickness=1, bg="#25333C", fg="#ffffff", bd=0)
    username_login_entry.place(x=580, y=150, width=250,height=39)

    username_login_entry.insert(0, 'Username')
    username_login_entry.bind('<FocusIn>', usrname_on_entry_click)
    username_login_entry.bind('<FocusOut>', usrname_on_focusout)
    username_login_entry.config(fg="grey")

    # password login and entry box
    password_login_entry = Entry(login_frame, textvariable=password_verify, highlightbackground="#6DDBA0", highlightthickness=1, bg="#25333C", fg="#ffffff", bd=0)
    password_login_entry.place(x=580, y=210, width=250, height=39)

    password_login_entry.insert(0, 'Password')
    password_login_entry.bind('<FocusIn>', password_on_entry_click)
    password_login_entry.bind('<FocusOut>', password_on_focusout)
    password_login_entry.config(fg="grey")

    # login button
    login_btn = Button(login_frame, text="Log in", command=button_cred_match, bg="#6DDBA0", fg="white", bd=0, font=("Roboto",10,'bold'))
    login_btn.place(x=580, y=285, width=250, height=39)

    # binds the enter key to enter_key_cred_match'function to authenticate the credentials
    root.bind('<Return>', enter_key_cred_match)

    copyright_text = Label(login_frame, text="© 2021 EasyInv System. All Rights Reserved", bg="#25333C",fg="#49535B")
    copyright_text.place(x=585, y=350)

    root.mainloop()


main_screen()  # call the main login screen


