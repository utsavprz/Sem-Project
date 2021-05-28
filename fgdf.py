from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox


def connect():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profile(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    conn.commit()
    conn.close()

def insert(First,Surname):
    conn = sqlite3.connect("TRIAL.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO profile VALUES(NULL,?,?)",(First,Surname))
    conn.commit()
    conn.close()

def delete_all():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM profile")
    conn.commit()
    conn.close()

def add():
    insert(e1.get(),e2.get())
    tree.insert("", tk.END, values = ("",e1.get(),e2.get()))

def delete(id):
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM profile WHERE id=?", (id,))
    conn.commit()
    conn.close()

def clear():
    for records in tree.get_children():
        tree.delete(records)

def remove_all():
    clear()
    delete_all()

def View():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile")
    rows = cur.fetchall()
    conn.close()
    return rows

def display_records():
    clear()
    for rows in View():
        tree.insert("", tk.END, values=rows)

def get_selected(event):
    selectRow = tree.selection()
    for i in selectRow:

        itemdis = tree.item(i)
        valuesofRow = itemdis['values']

        global id
        id = valuesofRow[0]
        name = valuesofRow[1]
        surname = valuesofRow[2]

        e1.delete(0,'end')
        e1.insert(0,name)

        e2.delete(0,'end')
        e2.insert(0,surname)

def update_db(id,First,Surname):
    conn= sqlite3.connect("TRIAL.db")
    cur= conn.cursor()
    cur.execute("UPDATE profile SET First=?, Surname=? WHERE id=?", (First, Surname, id))
    conn.commit()
    conn.close()

def update():
    global id
    update_db(id, e1v.get(), e2v.get())
    for i in tree.selection():
        tree.delete(i)
    tree.insert("",tk.END,values=(e1.get(),e2.get()))

def remove_one():
    global id
    rem = tree.selection()
    for idGet in rem:
        print(id)
        tree.delete(idGet[3])
    delete(id)

connect()  #  this to create the db


root = tk.Tk()
root.geometry("800x800")

tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.bind("<Double-1>",get_selected)
tree.pack()

e1v = tk.StringVar()
e2v = tk.StringVar()

e1 = tk.Entry(root,textvariable=e1v)
e1.pack()
e2 = tk.Entry(root,textvariable=e2v)
e2.pack()

b1= tk.Button(root,text="add",command=add)
b1.pack()
b2 = tk.Button(root,text="view data", command=display_records)
b2.pack()
b2.bind("<FocusIn>",display_records)
b3=tk.Button(root,text="remove all",command=remove_all)
b3.pack()
b4=tk.Button(root,text="clear all",command=clear)
b4.pack()
b5 = tk.Button(root,text="remove",command=remove_one)
b5.pack()
b6 = tk.Button(root,text="print selected",command=get_selected)
b6.pack()
b7=tk.Button(root,text="Update",command=update)
b7.pack()
root.mainloop()