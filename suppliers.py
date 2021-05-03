from tkinter import *

global dashboard_root
dashboard_root = Tk()
dashboard_root.title('EasyInv System - Suppliers')
dashboard_root.geometry("1920x1080")

# supplier category main frame
def supplier_frame():
    global supplier_category_content_frame

    supplier_category_content_frame = Frame(dashboard_root, width=1670, height=1080, bg="#EAEEF4")
    supplier_category_content_frame.place(x=250, y=0)

    supplier_label = Label(supplier_category_content_frame, text='Suppliers', font=('Roboto Slab', 18, 'bold'),
                           fg="#4E5154", bg="#EAEEF4")
    supplier_label.place(x=20, y=50)

    horizontal_bar = Frame(supplier_category_content_frame, width=1620, height=5, bg='#202020')
    horizontal_bar.place(x=25, y=100)


# frame to display database of suppliers
def supp_db_frame():
    global manage_supplier_frame
    global s1

    manage_supplier_frame = Frame(supplier_category_content_frame, width=1620, height=780, bg='#ffffff')
    manage_supplier_frame.place(x=25, y=160)

    manage_supplier = Label(manage_supplier_frame, text='Manage Supplier', font=('Roboto Slab', 17, 'bold'),
                            fg="#4E5154", bg="#ffffff")
    manage_supplier.place(x=30, y=20)



# function to create a frame and do the editing of suppliers
def edit_supplier_db():
    global edit_frame
    edit_frame = Frame(manage_supplier_frame, width=750, height=780, bg='#ffffff')
    edit_frame.place(x=870, y=0)

    vertical_seperator = Frame(edit_frame, width=3, height=755, bg='#202020')
    vertical_seperator.place(x=0, y=13)

    global supplier_name
    global pan_no
    global contact_no

    global name_supp
    global pan_supp
    global contact_supp

    supplier_name = StringVar()
    pan_no = StringVar()
    contact_no = StringVar()

    name_label = Label(edit_frame, text="Name of Supplier", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    name_label.place(x=150, y=75)
    name_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1, textvariable=supplier_name,
                      font=('Roboto', 9, 'normal'))
    name_supp.place(x=350, y=65, width="290", height="35")

    pan_label = Label(edit_frame, text="PAN no.", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    pan_label.place(x=152, y=140)
    pan_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1, textvariable=pan_no,
                     font=('Roboto', 9, 'normal'))
    pan_supp.place(x=350, y=130, width="290", height="35")

    contact_label = Label(edit_frame, text="Contact", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    contact_label.place(x=152, y=205)
    contact_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1, textvariable=contact_no,
                         font=('Roboto', 9, 'normal'))
    contact_supp.place(x=350, y=195, width="290", height="35")

    add_btn = Button(edit_frame, text="Add Supplier", bd=0, bg='#1A2C42', fg='#ffffff', font=('Roboto', 9, 'bold'))
    add_btn.place(x=160, y=300, width="110", height="40")

    update_btn = Button(edit_frame, text="Update", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'))
    update_btn.place(x=300, y=300, width="110", height="40")

    delete_btn = Button(edit_frame, text="Delete", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'))
    delete_btn.place(x=560, y=300, width="110", height="40")



supplier_frame()
supp_db_frame()
edit_supplier_db()

dashboard_root.state('zoomed')
dashboard_root.mainloop()
