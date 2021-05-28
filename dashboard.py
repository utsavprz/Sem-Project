from tkinter import *
import backend
import product_backend
from tkinter import ttk

def supplier_frame():
    # function to add the user data into the database
    def add_command():
        global supplier_dbTable
        global id
        backend.insert(supplier_name.get(), pan_no.get(), contact_no.get())

        supplier_dbTable.insert("",END,value = (" ",supplier_name.get(), pan_no.get(), contact_no.get()))

    def clear_table():
        global supplier_dbTable
        for records in supplier_dbTable.get_children():
            supplier_dbTable.delete(records)

    def display_supp_data():
        clear_table()
        for rows in backend.view():
            supplier_dbTable.insert("",END,values=rows)

    def get_selected_row(event):
        global supplier_dbTable
        try:
            global selectRow
            selectRow = supplier_dbTable.selection()
            for i in selectRow:

                giveitem = supplier_dbTable.item(i)
                valuesofRow = giveitem['values']

                global id
                id = valuesofRow[0]
                nameofSupplier = valuesofRow[1]
                panofSupplier = valuesofRow[2]
                contactofSupplier = valuesofRow[3]


                name_supp.delete(0, 'end')
                name_supp.insert(END, nameofSupplier)

                pan_supp.delete(0, 'end')
                pan_supp.insert(END, panofSupplier)

                contact_supp.delete(0, 'end')
                contact_supp.insert(END, contactofSupplier)

        except Exception as e:
            print(e)
            pass

    # function to clear the entry field
    def clear_command():
        name_supp.delete(0, END)
        pan_supp.delete(0, END)
        contact_supp.delete(0, END)

    # function to delete the data from database
    def delete_command():
        global supplier_dbTable
        global id
        for idGet in supplier_dbTable.selection():
            supplier_dbTable.delete(idGet)
        backend.delete(id)
        clear_command()

    # function to search the info from database
    def search_command():
        clear_table()
        for rows in backend.search(supplier_name.get(), pan_no.get(), contact_no.get()):
            supplier_dbTable.insert("",END,values=rows)

    # function to update the information
    def update_command():
        global supplier_dbTable
        global id
        backend.update(id, supplier_name.get(), pan_no.get(), contact_no.get())
        clear_table()
        supplier_dbTable.insert("",END,values= (id, supplier_name.get(), pan_no.get(), contact_no.get()))

    def supplier_frame():
        global supplier_category_content_frame

        supplier_category_content_frame = Frame(dashboard_root, width=1366, height=728, bg="#EAEEF4")
        supplier_category_content_frame.place(x=230, y=40)


    # frame to display database of suppliers
    def supp_db_frame():
        global manage_supplier_frame
        global s1

        manage_supplier_frame = Frame(supplier_category_content_frame, width=1120, height=780, bg='#EAEEF4')
        manage_supplier_frame.place(x=5, y=10)

        supp_list = Label(manage_supplier_frame, text='Supplier List', font=('Roboto Slab', 15, 'bold'),
                          fg="#4E5154", bg="#EAEEF4")
        supp_list.place(x=15, y=10)



    # function to create a frame and do the editing of suppliers
    def edit_supplier_db():
        global edit_frame
        edit_frame = Frame(manage_supplier_frame, width=1200, height=250, bg='#EAEEF4')
        edit_frame.place(x=10, y=40)

        dbTable_frame = Frame(manage_supplier_frame, width=1200, height=410, bg='grey')
        dbTable_frame.place(x=10,y=295)


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
        name_label.place(x=5, y=30)
        name_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=supplier_name,
                          font=('Roboto', 9, 'normal'))
        name_supp.place(x=200, y=30, width="290", height="35")

        pan_label = Label(edit_frame, text="PAN no.", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        pan_label.place(x=5, y=80)
        pan_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1, textvariable=pan_no,
                         font=('Roboto', 9, 'normal'))
        pan_supp.place(x=200, y=80, width="290", height="35")

        contact_label = Label(edit_frame, text="Contact", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        contact_label.place(x=5, y=130)
        contact_supp = Entry(edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                             textvariable=contact_no,
                             font=('Roboto', 9, 'normal'))
        contact_supp.place(x=200, y=130, width="290", height="35")

        add_btn = Button(edit_frame, text="Add Supplier", bd=0, bg='#1A2C42', fg='#EAEEF4', font=('Roboto', 9, 'bold'),
                         command=add_command)
        add_btn.place(x=5, y=190, width="110", height="40")

        update_btn = Button(edit_frame, text="Update", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=update_command)
        update_btn.place(x=140, y=190, width="110", height="40")

        clear_btn = Button(edit_frame, text="Clear", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                           command=clear_command)
        clear_btn.place(x=275, y=190, width="110", height="40")

        search_btn = Button(edit_frame, text="Search", bd=0, bg="#1A2C42", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=search_command)
        search_btn.place(x=410, y=190, width="110", height="40")

        show_btn = Button(edit_frame, text="Show Data", bd=0, bg="#1A2C42", fg="#ffffff",
                           font=('Roboto', 9, 'bold'), command=display_supp_data)
        show_btn.place(x=545, y=190, width="110", height="40")

        delete_btn = Button(edit_frame, text="Delete", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command)
        delete_btn.place(x=690, y=190, width="110", height="40")
        #delete_btn.bind("<Delete>", delete_command)

        global supplier_dbTable
        supplier_dbTable = ttk.Treeview(dbTable_frame, column=('column1','column2','column3','column4'),show='headings')
        supplier_dbTable.heading('#1',text="Id")
        supplier_dbTable.heading('#2', text="Supplier Name")
        supplier_dbTable.heading('#3',text="PAN")
        supplier_dbTable.heading('#4', text="Contact")
        supplier_dbTable.pack()
        supplier_dbTable.bind('<Double-1>',get_selected_row)


    supplier_frame()
    supp_db_frame()
    edit_supplier_db()

def product_frame():
    # function to add the user data into the database
    def add_command():
        global product_dbTable
        product_backend.insert(prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),prodTotal.get())
        product_dbTable.insert("",END,value=("",prodDate.get(),prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),prodTotal.get()))

    def clear_table():
        global product_dbTable
        for records in product_dbTable.get_children():
            product_dbTable.delete(records)

    # function to show Firm table data scroll list
    def display_prod_data():
        clear_table()
        for rows in product_backend.view():
            product_dbTable.insert("",END,values=rows)


    def get_selected_row(event):
        try:
            global selectRow
            selectRow = product_dbTable.selection()
            for i in selectRow:
                giveitem = product_dbTable.item(i)
                valuesofRow = giveitem['values']

                global id
                id = valuesofRow[0]
                dateofProduct = valuesofRow[1]
                nameofProduct = valuesofRow[2]
                priceofProduct = valuesofRow[3]
                quantityofProduct = valuesofRow[4]
                supplierofProduct = valuesofRow[5]
                totalamtofProduct = valuesofRow[6]

                date_prod.delete(0, 'end')
                date_prod.insert(END, dateofProduct)

                name_prod.delete(0, 'end')
                name_prod.insert(END, nameofProduct)

                price_prod.delete(0, 'end')
                price_prod.insert(END, priceofProduct)

                quantity_prod.delete(0, 'end')
                quantity_prod.insert(END, quantityofProduct)

                supp_prod.delete(0, 'end')
                supp_prod.insert(END, supplierofProduct)

                total_prod.delete(0, 'end')
                total_prod.insert(END, totalamtofProduct)

        except Exception as e:
            print(e)
            pass

    # function to clear the entry field
    def clear_command():
        date_prod.delete(0,END)
        name_prod.delete(0, END)
        price_prod.delete(0, END)
        quantity_prod.delete(0, END)
        supp_prod.delete(0, END)
        total_prod.delete(0,END)

    # function to delete the data from database
    def delete_command():
        global product_dbTable
        global id
        for idGet in product_dbTable.selection():
            product_dbTable.delete(idGet)
        product_backend.delete(id)
        clear_command()

    # function to search the info from database
    def search_command():
        clear_table()
        for rows in product_backend.search(prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(), prodTotal.get()):
            product_dbTable.insert("", END, values=rows)

    # function to update the information
    def update_command():
        product_backend.update(id, prodDate.get(),prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),prodTotal.get())
        clear_table()
        product_dbTable.insert("",END,values= (id, prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),prodTotal.get()))

    def onclick_focusin(event):
        price_val = int(price_prod.get())
        quan_val = int(quantity_prod.get())
        tot = price_val * quan_val
        if total_prod.get() == "":
            total_prod.insert(0, tot)
            total_prod.config(fg='black')
            print(type(tot))

    def onclick_focusout(event):
        if total_prod.get() == '':
            total_prod.insert(0, tot)
            total_prod.config(fg='black')


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


        prod_list = Label(manage_product_frame, text='Stock Inventory', font=('Roboto Slab', 15, 'bold'),
                          fg="#4E5154", bg="#EAEEF4")
        prod_list.place(x=15, y=10)


    # function to create a frame and do the editing of suppliers
    def edit_product_db():

        global product_edit_frame
        product_edit_frame = Frame(manage_product_frame, width=1200, height=250, bg='#EAEEF4')
        product_edit_frame.place(x=10, y=40)

        dbTable_frame = Frame(manage_product_frame, width=1200, height=410, bg='grey')
        dbTable_frame.place(x=10,y=295)


        global prodName
        global prodPrice
        global prodQuan
        global prodSupp
        global prodDate
        global prodTotal

        global name_prod
        global price_prod
        global quantity_prod
        global supp_prod
        global date_prod
        global total_prod

        prodName = StringVar()
        prodPrice = StringVar()
        prodQuan = StringVar()
        prodSupp = StringVar()
        prodDate = StringVar()
        prodTotal= StringVar()

        date_label = Label(product_edit_frame, text="Date", font=("Roboto",10,'bold'), bg='#EAEEF4', fg="#202020")
        date_label.place(x=5, y=30)

        date_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=prodDate,
                          font=('Roboto', 9, 'normal'))
        date_prod.place(x=200, y=30, width="115", height="35")

        name_label = Label(product_edit_frame, text="Product Name", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                           fg="#202020")
        name_label.place(x=5, y=80)
        name_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=prodName,
                          font=('Roboto', 9, 'normal'))
        name_prod.place(x=200, y=80, width="290", height="35")

        price_label = Label(product_edit_frame, text="Price", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        price_label.place(x=5, y=130)
        price_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                           textvariable=prodPrice,
                           font=('Roboto', 9, 'normal'))
        price_prod.place(x=200, y=130, width="290", height="35")

        quantity_label = Label(product_edit_frame, text="Quantity", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                               fg="#202020")
        quantity_label.place(x=600, y=30)
        quantity_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                              textvariable=prodQuan,
                              font=('Roboto', 9, 'normal'))
        quantity_prod.place(x=795, y=30, width="290", height="35")

        supp_label = Label(product_edit_frame, text="Supplier", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        supp_label.place(x=600, y=80)
        supp_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,
                          textvariable=prodSupp,
                          font=('Roboto', 9, 'normal'))
        supp_prod.place(x=795, y=80, width="290", height="35")

        total_amt_label = Label(product_edit_frame, text="Total Amount", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        total_amt_label.place(x=600, y=130)
        total_prod = Entry(product_edit_frame, bd=0, highlightbackground="#757575", highlightthickness=1,textvariable=prodTotal,font=('Roboto', 9, 'normal'))
        total_prod.place(x=795, y=130, width="290", height="35")
        total_prod.insert(0,'')
        total_prod.bind("<FocusIn>",onclick_focusin)
        total_prod.bind("<FocusOut>",onclick_focusout)


        add_btn = Button(product_edit_frame, text="Add Product", bd=0, bg='#1A2C42', fg='#ffffff',
                         font=('Roboto', 9, 'bold'), command=add_command)
        add_btn.place(x=5, y=190, width="110", height="40")

        update_btn = Button(product_edit_frame, text="Update", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=update_command)
        update_btn.place(x=140, y=190, width="110", height="40")

        clear_btn = Button(product_edit_frame, text="Clear", bd=0, bg="#1A2C42", fg="#ffffff",
                           font=('Roboto', 9, 'bold'),
                           command=clear_command)
        clear_btn.place(x=275, y=190, width="110", height="40")

        search_btn = Button(product_edit_frame, text="Search", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=search_command)
        search_btn.place(x=410, y=190, width="110", height="40")

        show_btn = Button(product_edit_frame, text="Show Data", bd=0, bg="#1A2C42", fg="#ffffff",
                          font=('Roboto', 9, 'bold'), command=display_prod_data)
        show_btn.place(x=545, y=190, width="110", height="40")

        delete_btn = Button(product_edit_frame, text="Delete", bd=0, bg="#1A2C42", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command)
        delete_btn.place(x=690, y=190, width="110", height="40")
        delete_btn.bind("<Delete>", delete_command)

        global product_dbTable
        product_dbTable = ttk.Treeview(dbTable_frame, column=('column1','column2','column3','column4','column5','column6','column7'),show='headings')
        product_dbTable.heading('#1',text="Id")
        product_dbTable.column("#1",width=30)
        product_dbTable.heading('#2', text="Date")
        product_dbTable.column("#2", width=120)
        product_dbTable.heading('#3',text="Product Name")
        product_dbTable.column("#3", width=250)
        product_dbTable.heading('#4', text="Price")
        product_dbTable.column("#4", width=100)
        product_dbTable.heading('#5', text="Quantity")
        product_dbTable.column("#5", width=100)
        product_dbTable.heading('#6', text="Supplier")
        product_dbTable.column("#6", width=250)
        product_dbTable.heading('#7', text="totalAmount")
        product_dbTable.pack()
        product_dbTable.bind('<Double-1>',get_selected_row)



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
    title_label.place(x=70, y=8)

    dashboard_btn = Button(category_frame, text='Dashboard', fg='#9BA9AF', bg='#0C1115', bd=0,
                          font=("TechnicBoldRegular", 11, "bold"), command=dashboard)

    dashboard_btn.place(x=-45, y=50, width=300, height=50)

    supplier_btn = Button(category_frame, text='Suppliers', fg='#9BA9AF', bg='#0C1115', bd=0,
                          font=("TechnicBoldRegular", 11, "bold"), command=supplier_frame)

    supplier_btn.place(x=-50, y=105, width=300, height=50)

    product_btn = Button(category_frame, text='Products', fg='#9BA9AF', bg='#0C1115', bd=0,
                         font=("TechnicBoldRegular", 11, "bold"), command=product_frame)

    product_btn.place(x=-50, y=160, width=300, height=50)

def dashboard():
    # creates a frame to display the content of categories
    dashboard_frame = Frame(dashboard_root, width=1366, height=768, bg="#EAEEF4")
    dashboard_frame.place(x=230, y=40)

    dashboard_title = Label(dashboard_frame, text='Dashboard', font=('Roboto Slab', 15, 'bold'),
                      fg="#4E5154", bg="#EAEEF4")
    dashboard_title.place(x=20, y=20)





def main_win():
    global dashboard_root
    dashboard_root = Tk()
    dashboard_root.resizable(False, False)
    dashboard_root.title('EasyInv - Dashboard')
    dashboard_root.geometry("1366x768")
    dashboard_root.iconbitmap('D:\sem project\icon_pack\ico\Database-Upload.ico')

    category_main_frame()
    dashboard()
    dashboard_root.mainloop()
