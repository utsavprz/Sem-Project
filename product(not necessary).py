from tkinter import *
import product_backend

global dashboard_root
dashboard_root = Tk()
dashboard_root.title('EasyInv System - Suppliers')
dashboard_root.geometry("1920x1080")


# function to add the user data into the database
def add_command():
    product_backend.insert(prodName.get(), prodPrice.get(), prodQuan.get(),ProdSupp.get())
    list2.delete(0, END)
    list2.insert(END, prodName.get(), prodPrice.get(), prodQuan.get(),ProdSupp.get())

    showINProductList()  # called showINProductList method after inserting the data record to database


# function to show Firm table data scroll list
def showINProductList():
    list2.delete(0, END)
    for row in product_backend.view():
        list2.insert(END, row)


def get_selected_row(event):
    try:
        global pd

        searchPd = list2.curselection()[0]
        pd = list2.get(searchPd)

        name_prod.delete(0, END)
        name_prod.insert(END, pd[1])

        price_prod.delete(0, END)
        price_prod.insert(END, pd[2])

        quantity_prod.delete(0, END)
        quantity_prod.insert(END, pd[3])

        supp_prod.delete(0, END)
        supp_prod.insert(END, pd[4])

    except IndexError:
        pass


# function to clear the entry field
def clear_command():
    name_prod.delete(0, END)
    price_prod.delete(0, END)
    quantity_prod.delete(0, END)
    supp_prod.delete(0, END)


# function to delete the data from database
def delete_command():
    product_backend.delete(pd[0])
    clear_command()
    showINProductList()


# function to search the info from database
def search_command():
    list2.delete(0, END)
    for row in product_backend.search(prodName.get(), prodPrice.get(), prodQuan.get(), ProdSupp.get()):
        list2.insert(END, row)


# function to update the information
def update_command():
    product_backend.update(pd[0], prodName.get(), prodPrice.get(), prodQuan.get(), ProdSupp.get())
    list2.delete(0, END)
    list2.insert(END, (pd[0], prodName.get(), prodPrice.get(), prodQuan.get(), ProdSupp.get()))


# supplier category main frame
def product_frame():
    global product_category_content_frame

    product_category_content_frame = Frame(dashboard_root, width=1670, height=1080, bg="#EAEEF4")
    product_category_content_frame.place(x=250, y=0)

    supplier_label = Label(product_category_content_frame, text='Products', font=('Roboto Slab', 18, 'bold'),
                           fg="#4E5154", bg="#EAEEF4")
    supplier_label.place(x=20, y=50)

    horizontal_bar = Frame(product_category_content_frame, width=1620, height=5, bg='#202020')
    horizontal_bar.place(x=25, y=100)


# frame to display database of suppliers
def product_db_frame():
    global manage_product_frame
    global s1

    manage_product_frame = Frame(product_category_content_frame, width=1620, height=780, bg='#ffffff')
    manage_product_frame.place(x=25, y=160)

    show_btn = Button(manage_product_frame, text="Show Data", bd=0, bg="#1A2C42", fg="#ffffff",
                      font=('Roboto', 9, 'bold'), command=showINProductList)
    show_btn.place(x=30, y=80, width="453", height="40")

    delete_btn = Button(manage_product_frame, text="Delete", bd=0, bg="#1A2C42", fg="#ffffff",
                        font=('Roboto', 9, 'bold'), command=delete_command)
    delete_btn.place(x=30, y=705, width="453", height="40")
    # delete_btn.bind("<Delete>", delete_command)

    supp_list = Label(manage_product_frame, text='Product List', font=('Roboto Slab', 17, 'bold'),
                      fg="#4E5154", bg="#ffffff")
    supp_list.place(x=30, y=20)

    global list2
    list2 = Listbox(manage_product_frame, height=28, width=50, font=("Roboto", 12, 'bold'))

    # show the selected row from list in the entry field
    list2.bind('<<ListboxSelect>>', get_selected_row)

    list2.place(x=30, y=130)


# function to create a frame and do the editing of suppliers
def edit_product_db():
    global product_edit_frame
    product_edit_frame = Frame(manage_product_frame, width=750, height=780, bg='#ffffff')
    product_edit_frame.place(x=800, y=0)

    vertical_seperator = Frame(product_edit_frame, width=3, height=755, bg='#202020')
    vertical_seperator.place(x=0, y=13)

    global prodName
    global prodPrice
    global prodQuan
    global ProdSupp

    global name_prod
    global price_prod
    global quantity_prod
    global supp_prod

    prodName = StringVar()
    prodPrice = StringVar()
    prodQuan = StringVar()
    ProdSupp = StringVar()


    name_label = Label(product_edit_frame, text="Product Name", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    name_label.place(x=150, y=75)
    name_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                      textvariable=prodName,
                      font=('Roboto', 9, 'normal'))
    name_prod.place(x=350, y=65, width="290", height="35")

    price_label = Label(product_edit_frame, text="Price", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    price_label.place(x=152, y=140)
    price_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                       textvariable=prodPrice,
                       font=('Roboto', 9, 'normal'))
    price_prod.place(x=350, y=130, width="290", height="35")

    quantity_label = Label(product_edit_frame, text="Quantity", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    quantity_label.place(x=152, y=205)
    quantity_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=prodQuan,
                          font=('Roboto', 9, 'normal'))
    quantity_prod.place(x=350, y=195, width="290", height="35")

    supp_label = Label(product_edit_frame, text="Supplier", font=("Roboto", 10, 'bold'), bg='#ffffff', fg="#202020")
    supp_label.place(x=152, y=270)
    supp_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                      textvariable=ProdSupp,
                      font=('Roboto', 9, 'normal'))
    supp_prod.place(x=350, y=260, width="290", height="35")



    add_btn = Button(product_edit_frame, text="Add Supplier", bd=0, bg='#1A2C42', fg='#ffffff',
                     font=('Roboto', 9, 'bold'), command=add_command)
    add_btn.place(x=160, y=330, width="110", height="40")

    update_btn = Button(product_edit_frame, text="Update", bd=0, bg="#1A2C42", fg="#ffffff", font=('Roboto', 9, 'bold'),
                        command=update_command)
    update_btn.place(x=290, y=330, width="110", height="40")

    clear_btn = Button(product_edit_frame, text="Clear", bd=0, bg="#1A2C42", fg="#ffffff", font=('Roboto', 9, 'bold'),
                       command=clear_command)
    clear_btn.place(x=420, y=330, width="110", height="40")

    search_btn = Button(product_edit_frame, text="Search", bd=0, bg="#1A2C42", fg="#ffffff", font=('Roboto', 9, 'bold'),
                        command=search_command)
    search_btn.place(x=550, y=330, width="110", height="40")


product_frame()
product_db_frame()
edit_product_db()

dashboard_root.state('zoomed')
dashboard_root.mainloop()
