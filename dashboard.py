from tkinter import *


def supplier_frame():
    supplier_category_content_frame = Frame(dashboard_root, width=1670, height=1080, bg="#EAEEF4")
    supplier_category_content_frame.place(x=250, y=0)

    supplier_label = Label(supplier_category_content_frame, text='Suppliers', font=('Roboto Slab', 18, 'bold'),
                           fg="#4E5154", bg="#EAEEF4")
    supplier_label.place(x=20, y=50)

    add_supplier_btn = Button(supplier_category_content_frame, text='Add Suppliers', bd=0, bg='#1A2C42', fg='#ffffff',
                              font=('Roboto', 9, 'bold'))
    add_supplier_btn.place(x=25, y=100, width=90, height=40)


def category_main_frame():
    global category_frame

    # frame to display categories
    category_frame = Frame(dashboard_root, bg="#0C1115", width=250, height=1080)
    category_frame.pack(side=LEFT)

    title_frame = Frame(dashboard_root, bg="#ECAF44", width=1920, height=50)
    title_frame.place(x=0, y=0)

    title_label = Label(title_frame, text="EasyInv System", font=("Times New Roman", 18, 'bold'), bg="#ECAF44",
                        fg="#0C1115")
    title_label.place(x=40, y=10)

    # creates a frame to display the content of categories
    category_content_frame = Frame(dashboard_root, width=1670, height=1080, bg="#EAEEF4")
    category_content_frame.place(x=250, y=50)


def category_buttons():
    supplier_btn = Button(category_frame, text='Suppliers', fg='#9BA9AF', bg='#0C1115', bd=0,
                          font=("arial", 12, 'bold',), command=supplier_frame)

    supplier_btn.place(x=-50, y=50, width=300, height=50)


def main_win():
    global dashboard_root
    dashboard_root = Tk()
    dashboard_root.title('EasyInv System - Dashboard')
    dashboard_root.geometry("1920x1080")

    category_main_frame()
    category_buttons()
    dashboard_root.state('zoomed')
    dashboard_root.mainloop()





