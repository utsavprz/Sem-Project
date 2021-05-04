from tkinter import *
import backend

global dashboard_root
dashboard_root = Tk()
dashboard_root.title('EasyInv System - Suppliers')
dashboard_root.geometry("1920x1080")

# function to add the user data into the database
def add_command():
    backend.insert(supplier_name.get(),pan_no.get(),contact_no.get())
    list1.delete(0,END)
    list1.insert(END,supplier_name.get(),pan_no.get(),contact_no.get())

    showINProductList() #called showINProductList method after inserting the data record to database

# function to show Firm table data scroll list
def showINProductList():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def get_selected_row(event):
    try:
        global pd

        searchPd = list1.curselection()[0]
        pd =list1.get(searchPd)
        name_supp.delete(0,END)
        name_supp.insert(END,pd[0])

        pan_supp.delete(0, END)
        pan_supp.insert(END,pd[1])

        contact_supp.delete(0, END)
        contact_supp.insert(END,pd[2])

    except IndexError:
        pass

# function to clear the entry field
def clear_command():
    name_supp.delete(0,END)
    pan_supp.delete(0, END)
    contact_supp.delete(0, END)

#function to delete the data from database
def delete_command():
    backend.delete(pd[0])
    clear_command()
    showINProductList()

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


    show_btn = Button(manage_supplier_frame, text="Show Data", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'),command=showINProductList)
    show_btn.place(x=30, y=80, width="453", height="40")


    supp_list = Label(manage_supplier_frame, text='Supplier List', font=('Roboto Slab', 17, 'bold'),
                            fg="#4E5154", bg="#ffffff")
    supp_list.place(x=30, y=20)



    global list1
    list1 = Listbox(manage_supplier_frame, height=29, width=50, font=("Roboto",12,'bold'))

    #show the selected row from list in the entry field
    list1.bind('<<ListboxSelect>>',get_selected_row)

    list1.place(x=30, y=130)



# function to create a frame and do the editing of suppliers
def edit_supplier_db():
    global edit_frame
    edit_frame = Frame(manage_supplier_frame, width=750, height=780, bg='#ffffff')
    edit_frame.place(x=800, y=0)

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

    add_btn = Button(edit_frame, text="Add Supplier", bd=0, bg='#1A2C42', fg='#ffffff', font=('Roboto', 9, 'bold'), command=add_command)
    add_btn.place(x=160, y=300, width="110", height="40")

    update_btn = Button(edit_frame, text="Update", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'))
    update_btn.place(x=300, y=300, width="110", height="40")

    delete_btn = Button(edit_frame, text="Delete", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'),command=delete_command)
    delete_btn.place(x=560, y=300, width="110", height="40")
    #delete_btn.bind("<Delete>", delete_command)

    clear_btn = Button(edit_frame, text="Clear", bd=0, bg="#202020", fg="#ffffff", font=('Roboto', 9, 'bold'),command=clear_command)
    clear_btn.place(x=430, y=300, width="110", height="40")




supplier_frame()
supp_db_frame()
edit_supplier_db()

dashboard_root.state('zoomed')
dashboard_root.mainloop()
