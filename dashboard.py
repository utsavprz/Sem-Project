from tkinter import *
import backend
import product_backend



def supplier_frame():
    # function to add the user data into the database
    def add_command():
        backend.insert(supplier_name.get(), pan_no.get(), contact_no.get())
        list1.delete(0, END)
        list1.insert(END, supplier_name.get(), pan_no.get(), contact_no.get())

        showINProductList()  # called showINProductList method after inserting the data record to database

    # function to show Firm table data scroll list
    def showINProductList():
        list1.delete(0, END)
        for row in backend.view():
            list1.insert(END, row)

    def get_selected_row(event):
        try:
            global pd

            searchPd = list1.curselection()[0]
            pd = list1.get(searchPd)
            name_supp.delete(0, END)
            name_supp.insert(END, pd[1])

            pan_supp.delete(0, END)
            pan_supp.insert(END, pd[2])

            contact_supp.delete(0, END)
            contact_supp.insert(END, pd[3])

        except IndexError:
            pass

    # function to clear the entry field
    def clear_command():
        name_supp.delete(0, END)
        pan_supp.delete(0, END)
        contact_supp.delete(0, END)

    # function to delete the data from database
    def delete_command():
        backend.delete(pd[0])
        clear_command()
        showINProductList()

    # function to search the info from database
    def search_command():
        list1.delete(0, END)
        for row in backend.search(supplier_name.get(), pan_no.get(), contact_no.get()):
            list1.insert(END, row)

    # function to update the information
    def update_command():
        backend.update(pd[0], supplier_name.get(), pan_no.get(), contact_no.get())
        list1.delete(0, END)
        list1.insert(END, (pd[0], supplier_name.get(), pan_no.get(), contact_no.get()))

    def supplier_frame():
        global supplier_category_content_frame

        supplier_category_content_frame = Frame(dashboard_root, width=1366, height=728, bg="#EAEEF4")
        supplier_category_content_frame.place(x=230, y=40)

        #supplier_label = Label(supplier_category_content_frame, text='Suppliers', font=('Roboto Slab', 15, 'bold'),
                               #fg="#4E5154", bg="#EAEEF4")
       # supplier_label.place(x=10, y=15)

       # horizontal_bar = Frame(supplier_category_content_frame, width=1050, height=5, bg='#202020')
        #horizontal_bar.place(x=25, y=55)

    # frame to display database of suppliers
    def supp_db_frame():
        global manage_supplier_frame
        global s1

        manage_supplier_frame = Frame(supplier_category_content_frame, width=1120, height=780, bg='#EAEEF4')
        manage_supplier_frame.place(x=5, y=10)

        show_btn = Button(manage_supplier_frame, text="Show Data", bd=0, bg="#1A2C42", fg="#ffffff",
                          font=('Roboto', 9, 'bold'), command=showINProductList)
        show_btn.place(x=20, y=60, width="410", height="40")

        delete_btn = Button(manage_supplier_frame, text="Delete", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command)
        delete_btn.place(x=20, y=583, width="410", height="40")
        # delete_btn.bind("<Delete>", delete_command)

        supp_list = Label(manage_supplier_frame, text='Supplier List', font=('Roboto Slab', 15, 'bold'),
                          fg="#4E5154", bg="#EAEEF4")
        supp_list.place(x=15, y=10)

        global list1
        list1 = Listbox(manage_supplier_frame, height=23, width=45, font=("Roboto", 12, 'bold'))

        # show the selected row from list in the entry field
        list1.bind('<<ListboxSelect>>', get_selected_row)

        list1.place(x=20, y=110)

    # function to create a frame and do the editing of suppliers
    def edit_supplier_db():
        global edit_frame
        edit_frame = Frame(manage_supplier_frame, width=750, height=780, bg='#EAEEF4')
        edit_frame.place(x=500, y=0)

        vertical_seperator = Frame(edit_frame, width=3, height=690, bg='#202020')
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

        name_label = Label(edit_frame, text="Name of Supplier", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        name_label.place(x=100, y=75)
        name_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=supplier_name,
                          font=('Roboto', 9, 'normal'))
        name_supp.place(x=290, y=65, width="290", height="35")

        pan_label = Label(edit_frame, text="PAN no.", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        pan_label.place(x=100, y=140)
        pan_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1, textvariable=pan_no,
                         font=('Roboto', 9, 'normal'))
        pan_supp.place(x=290, y=130, width="290", height="35")

        contact_label = Label(edit_frame, text="Contact", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        contact_label.place(x=100, y=205)
        contact_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                             textvariable=contact_no,
                             font=('Roboto', 9, 'normal'))
        contact_supp.place(x=290, y=195, width="290", height="35")

        add_btn = Button(edit_frame, text="Add Supplier", bd=0, bg='#1A2C42', fg='#EAEEF4', font=('Roboto', 9, 'bold'),
                         command=add_command)
        add_btn.place(x=100, y=300, width="110", height="40")

        update_btn = Button(edit_frame, text="Update", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=update_command)
        update_btn.place(x=225, y=300, width="110", height="40")

        clear_btn = Button(edit_frame, text="Clear", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                           command=clear_command)
        clear_btn.place(x=350, y=300, width="110", height="40")

        search_btn = Button(edit_frame, text="Search", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=search_command)
        search_btn.place(x=475, y=300, width="110", height="40")

    supplier_frame()
    supp_db_frame()
    edit_supplier_db()

def product_frame():
    # function to add the user data into the database
    def add_command():
        product_backend.insert(prodName.get(), prodPrice.get(), prodQuan.get(), ProdSupp.get())
        list2.delete(0, END)
        list2.insert(END, prodName.get(), prodPrice.get(), prodQuan.get(), ProdSupp.get())

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

        product_category_content_frame = Frame(dashboard_root, width=1366, height=728, bg="#EAEEF4")
        product_category_content_frame.place(x=230, y=40)


    # frame to display database of suppliers
    def product_db_frame():
        global manage_product_frame
        global s1

        manage_product_frame = Frame(product_category_content_frame, width=1120, height=780, bg='#EAEEF4')
        manage_product_frame.place(x=5, y=10)

        show_btn = Button(manage_product_frame, text="Show Data", bd=0, bg="#1A2C42", fg="#ffffff",
                          font=('Roboto', 9, 'bold'), command=showINProductList)
        show_btn.place(x=20, y=60, width="410", height="40")

        delete_btn = Button(manage_product_frame, text="Delete", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command)
        delete_btn.place(x=20, y=583, width="410", height="40")
        # delete_btn.bind("<Delete>", delete_command)

        prod_list = Label(manage_product_frame, text='Product List', font=('Roboto Slab', 15, 'bold'),
                          fg="#4E5154", bg="#EAEEF4")
        prod_list.place(x=15, y=10)

        global list2
        list2 = Listbox(manage_product_frame, height=23, width=45, font=("Roboto", 12, 'bold'))

        # show the selected row from list in the entry field
        list2.bind('<<ListboxSelect>>', get_selected_row)

        list2.place(x=20, y=110)

    # function to create a frame and do the editing of suppliers
    def edit_product_db():
        global product_edit_frame
        product_edit_frame = Frame(manage_product_frame, width=750, height=780, bg='#EAEEF4')
        product_edit_frame.place(x=500, y=0)

        vertical_seperator = Frame(product_edit_frame, width=3, height=690, bg='#202020')
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

        name_label = Label(product_edit_frame, text="Product Name", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                           fg="#202020")
        name_label.place(x=100, y=75)
        name_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=prodName,
                          font=('Roboto', 9, 'normal'))
        name_prod.place(x=290, y=65, width="290", height="35")

        price_label = Label(product_edit_frame, text="Price", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        price_label.place(x=100, y=140)
        price_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                           textvariable=prodPrice,
                           font=('Roboto', 9, 'normal'))
        price_prod.place(x=290, y=130, width="290", height="35")

        quantity_label = Label(product_edit_frame, text="Quantity", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                               fg="#202020")
        quantity_label.place(x=100, y=205)
        quantity_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                              textvariable=prodQuan,
                              font=('Roboto', 9, 'normal'))
        quantity_prod.place(x=290, y=195, width="290", height="35")

        supp_label = Label(product_edit_frame, text="Supplier", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        supp_label.place(x=100, y=270)
        supp_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=ProdSupp,
                          font=('Roboto', 9, 'normal'))
        supp_prod.place(x=290, y=260, width="290", height="35")

        add_btn = Button(product_edit_frame, text="Add Product", bd=0, bg='#1A2C42', fg='#ffffff',
                         font=('Roboto', 9, 'bold'), command=add_command)
        add_btn.place(x=100, y=350, width="110", height="40")

        update_btn = Button(product_edit_frame, text="Update", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=update_command)
        update_btn.place(x=225, y=350, width="110", height="40")

        clear_btn = Button(product_edit_frame, text="Clear", bd=0, bg="#1A2C42", fg="#ffffff",
                           font=('Roboto', 9, 'bold'),
                           command=clear_command)
        clear_btn.place(x=350, y=350, width="110", height="40")

        search_btn = Button(product_edit_frame, text="Search", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=search_command)
        search_btn.place(x=475, y=350, width="110", height="40")

    product_frame()
    product_db_frame()
    edit_product_db()

def category_main_frame():
    global category_frame

    # frame to display categories
    category_frame = Frame(dashboard_root, bg="#0C1115", width=230, height=768)
    category_frame.pack(side=LEFT)

    title_frame = Frame(dashboard_root, bg="#ECAF44", width=1366, height=40)
    title_frame.place(x=0, y=0)

    title_label = Label(title_frame, text="EasyInv", font=("Helvetica", 13, 'bold'), bg="#ECAF44",
                        fg="#0C1115")
    title_label.place(x=80, y=8)

    # creates a frame to display the content of categories
    category_content_frame = Frame(dashboard_root, width=1366, height=768, bg="#EAEEF4")
    category_content_frame.place(x=250, y=50)


def category_buttons():
    supplier_btn = Button(category_frame, text='Suppliers', fg='#9BA9AF', bg='#0C1115', bd=0,
                          font=("TechnicBoldRegular", 11,"bold"), command=supplier_frame)

    supplier_btn.place(x=-50, y=50, width=300, height=50)

    product_btn = Button(category_frame, text='Products', fg='#9BA9AF', bg='#0C1115', bd=0,
                          font=("TechnicBoldRegular", 11,"bold"), command=product_frame)

    product_btn.place(x=-50, y=105, width=300, height=50)




def main_win():
    global dashboard_root
    dashboard_root = Tk()
    dashboard_root.title('EasyInv System - Dashboard')
    dashboard_root.geometry("1366x768")

    category_main_frame()
    category_buttons()
    dashboard_root.resizable(False,False)
    dashboard_root.mainloop()
main_win()








