from tkinter import *
from tkinter import messagebox
from dashboard import *


# closes the login window on logging with correct credentials
def login_win_close():
    root.destroy()


# function to authenticate the login credentials details with enter key
def enter_key_cred_match(event):
    uname = username_verify.get()
    passwd = password_verify.get()

    if uname == "admin" and passwd == "admin":
        messagebox.showinfo("", "Login Success")
        login_win_close()
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
        messagebox.showinfo("EasyInv", "Login Success")
        login_win_close()
        main_win()
    elif uname == "" and passwd == "":
        messagebox.showinfo("EasyInv", "Cannot be kept empty")
    elif uname == "":
        messagebox.showinfo("EasyInv", "Username cannot be kept empty")
    elif passwd == "":
        messagebox.showinfo("EasyInv", "Password cannot be kept empty")
    else:
        messagebox.showinfo("EasyInv", "Credentials do not match ")


def main_screen():
    global root
    root = Tk()
    root.title("EasyInv System")
    root.geometry('1366x768')

    root.iconbitmap('D:\sem project\icon_pack\ico\Database-Upload.ico')

    root.configure(bg="white")
    # creates a login frame
    login_frame = Frame(root, width=410, height=280, highlightbackground="#e7e7e7", bg="#e7e7e7")
    login_frame.grid(padx=500, pady=150)

    # heading of project
    title = Label(login_frame, text="EasyInv System")
    title.config(font=("Times New Roman", 15), bg="#e7e7e7")
    title.place(x=140, y=30)

    global usr_name
    global pwd
    global username_login_entry
    global password_login_entry
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    # username login and entry box
    usr_name = Label(login_frame, text="Username*", bg="#e7e7e7").place(x=75, y=80)
    username_login_entry = Entry(login_frame, textvariable=username_verify, bg="#c4c4c4", bd=0).place(x=80, y=100,
                                                                                                      width=250,
                                                                                                      height=30)

    # password login and entry box
    pwd = Label(login_frame, text="Password*", bg="#e7e7e7").place(x=75, y=140)
    password_login_entry = Entry(login_frame, textvariable=password_verify, show="*", bg="#c4c4c4", bd=0).place(x=80, y=160, width=250, height=30)

    # login button
    login_btn = Button(login_frame, text="Log in", command=button_cred_match, bg="#202020", fg="white", bd=0)
    login_btn.place(x=160, y=220, width=90, height=35)

    # binds the enter key to enter_key_cred_match'function to authenticate the credentials
    root.bind('<Return>', enter_key_cred_match)

    copyright_text = Label(root, text="© 2021 EasyInv System. All Rights Reserved", bg="white")
    copyright_text.place(x=585, y=450)

    root.resizable(False,False)
    root.mainloop()


main_screen()  # call the main login screen
