from tkinter import *

root = Tk()
root.title("Stock Management System")

l = Label(root, text = "Stock Management System")
l.config(font = ("Times New Roman", 30))

usr_name = Label(root,text ="Username").place(x = 560, y = 260)
pwd = Label(root,text ="Password").place(x = 560, y = 330)
e1 = Entry(root).place(x=630, y = 250, width = 190, height = 30)
e2 = Entry(root).place(x=630, y = 320,  width = 190, height = 30)

l.pack()
root.mainloop()