import datetime
import time
from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image

import backend
import product_backend
import recentActivity_backend


def category_main_frame():
    global category_frame
    global product_category_content_frame
    # frame to display categories
    category_frame = Frame(dashboard_root, bg="#051620", width=200, height=768)
    category_frame.pack(side=LEFT)

    # frame for logo
    title_frame = Frame(dashboard_root, bg="#25333C", width=1366, height=50)
    title_frame.place(x=0, y=0)

    # Displays the date in title frame
    time_string = time.strftime('%H:%M')
    datetimeLabel = Label(title_frame, text=f"{time_string}  |  {datetime.datetime.now():%a, %b %d %Y}", fg="#ffffff",
                          bg="#25333C", font=("Arial", 9, "bold"))
    datetimeLabel.place(x=1180, y=14)

    # Setting up logo in the title frame
    logo_image = Image.open("D:\sem project\logo\easyinv_concept.png")
    photo = ImageTk.PhotoImage(logo_image.resize((140, 60),
                                                 Image.ANTIALIAS))  # resizes the logo to width 150, height 60 along with antialiasing(smoothing edges)
    logo_label = Label(title_frame, image=photo, bd=0)
    logo_label.image = photo
    logo_label.place(x=30, y=-4)

    # logout = Button(title_frame, bd=0, width=5, height=10)
    # logout.place(x=400,y=0)

    dashboard_btn = Button(category_frame, text='Dashboard', fg='#EAEEF4', bg='#051620', bd=0,
                           font=("Helvetica", 10, "bold"), command=dashboard, cursor="hand2")

    dashboard_btn.place(x=-45, y=60, width=300, height=50)
    # Setting up image for dashboard
    dash_image = Image.open("D:\sem project\icon_pack\dashboard.png")
    dash_photo = ImageTk.PhotoImage(dash_image.resize((15, 15),
                                                      Image.ANTIALIAS))  # resizes the logo to width 150, height 60 along with antialiasing(smoothing edges)
    dash_label = Label(category_frame, image=dash_photo, bd=0, bg='#28282E')
    dash_label.image = dash_photo
    dash_label.place(x=40, y=78)

    supplier_btn = Button(category_frame, text='Suppliers', fg='#EAEEF4', bg='#051620', bd=0,
                          font=("Helvetica", 10, "bold"), command=supplier_frame, cursor="hand2")
    supplier_btn.place(x=-50, y=115, width=300, height=50)
    # Setting up image for suppliers
    supp_image = Image.open("D:\sem project\icon_pack\supplier.png")
    supp_photo = ImageTk.PhotoImage(supp_image.resize((15, 15),
                                                      Image.ANTIALIAS))  # resizes the logo to width 150, height 60 along with antialiasing(smoothing edges)
    supp_label = Label(category_frame, image=supp_photo, bd=0, bg='#28282E')
    supp_label.image = supp_photo
    supp_label.place(x=40, y=133)

    product_btn = Button(category_frame, text='Products', fg='#EAEEF4', bg='#051620', bd=0,
                         font=("Helvetica", 10, "bold"), command=product_frame, cursor="hand2")
    product_btn.place(x=-50, y=170, width=300, height=50)
    # Setting up image for products
    prod_image = Image.open("D:\sem project\icon_pack\product.png")
    prod_photo = ImageTk.PhotoImage(prod_image.resize((15, 15),
                                                      Image.ANTIALIAS))  # resizes the logo to width 150, height 60 along with antialiasing(smoothing edges)
    prod_label = Label(category_frame, image=prod_photo, bd=0, bg='#28282E')
    prod_label.image = prod_photo
    prod_label.place(x=40, y=188)

    # Add style for table
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", rowheight=25)
    style.configure("Treeview.Heading", background="#25333C", foreground="#ffffff", font=('Helvetica', 9, 'bold'),
                    relief="flat")


def dashboard():
    global recentActivityData

    def clear_table():
        global recentActivityTable
        for records in recentActivityTable.get_children():
            recentActivityTable.delete(records)

    def delete_activity():
        clear_table()
        recentActivity_backend.delete()

    def recentActivityData():
        clear_table()
        for rows in recentActivity_backend.view():
            recentActivityTable.insert("", END, values=rows)

    global dashboard_frame
    # creates a frame to display the content of categories
    dashboard_frame = Frame(dashboard_root, width=1366, height=768, bg="#EAEEF4")
    dashboard_frame.place(x=200, y=50)

    dashboard_title = Label(dashboard_frame, text='Dashboard', font=('Lato', 20, 'bold'),
                            fg="#25333C", bg="#EAEEF4")
    dashboard_title.place(x=25, y=15)

    # Mini Product Report 1 Section
    miniReport_frame = Frame(dashboard_frame, width=1150, height=350, bg="#EAEEF4")
    miniReport_frame.place(x=20, y=70)

    # Total Supplier Report
    totalSuppReport_frame = Frame(miniReport_frame, width=260, height=130, bg="#FEFFFE", highlightthickness=2,
                                  highlightbackground='#E5856E')
    totalSuppReport_frame.place(x=10, y=5)
    totalSuppReport_data = backend.count_suppliers()
    totalSuppReport_data = Label(totalSuppReport_frame, text=totalSuppReport_data, font=('Monosten', 40, 'bold'),
                                 bg='#FEFFFE', fg='#E5856E')
    totalSuppReport_data.place(x=20, y=5)
    info_label = Label(totalSuppReport_frame, text="Total Suppliers", font=('Assistant', 10, 'bold'), bg='#FEFFFE',
                       fg='#4E5154')
    info_label.place(x=20, y=90)

    # Total Products Report
    totalProdReport_frame = Frame(miniReport_frame, width=260, height=130, bg="#FEFFFE", highlightthickness=2,
                                  highlightbackground='#6870B3')
    totalProdReport_frame.place(x=290, y=5)
    totalProdReport_data = product_backend.count_products()
    totalProdReport_data = Label(totalProdReport_frame, text=totalProdReport_data, font=('Monosten', 40, 'bold'),
                                 bg='#FEFFFE', fg='#6870B3')
    totalProdReport_data.place(x=20, y=5)
    info_label2 = Label(totalProdReport_frame, text="Total Products", font=('Assistant', 10, 'bold'), bg='#FEFFFE',
                        fg='#4E5154')
    info_label2.place(x=20, y=90)

    # Total Invoices Report
    totalInvoiceReport_frame = Frame(miniReport_frame, width=260, height=130, bg="#FEFFFE", highlightthickness=2,
                                     highlightbackground='#98D165')
    totalInvoiceReport_frame.place(x=570, y=5)
    totalInvoiceReport_data = product_backend.count_invoices()
    totalInvoiceReport_data = Label(totalInvoiceReport_frame, text=totalInvoiceReport_data,
                                    font=('Monosten', 40, 'bold'),
                                    bg='#FEFFFE', fg='#98D165')
    totalInvoiceReport_data.place(x=20, y=5)
    info_label2 = Label(totalInvoiceReport_frame, text="Total Invoices", font=('Assistant', 10, 'bold'), bg='#FEFFFE',
                        fg='#4E5154')
    info_label2.place(x=20, y=90)

    # Total Purchased Amount Report
    totalAmtReport_frame = Frame(miniReport_frame, width=260, height=130, bg="#FEFFFE", highlightthickness=2,
                                 highlightbackground='#E26770')
    totalAmtReport_frame.place(x=850, y=5)
    totalAmtReport_data = product_backend.purchase_amount()
    nrs = Label(totalAmtReport_frame, text="??????", font=('Monosten', 20, 'bold'), bg='#FEFFFE', fg='#E26770')
    nrs.place(x=15, y=21)
    totalAmtReport_data = Label(totalAmtReport_frame, text=totalAmtReport_data, font=('Monosten', 25, 'bold'),
                                bg='#FEFFFE', fg='#E26770')
    totalAmtReport_data.place(x=45, y=15)
    info_label3 = Label(totalAmtReport_frame, text="Total Purchase Amount", font=('Assistant', 10, 'bold'),
                        bg='#FEFFFE', fg='#4E5154')
    info_label3.place(x=20, y=90)

    # Mini Product Report 2 Section
    # Report for product with highest price
    prodWithHighestPriceReport = product_backend.expensiveProd()

    prodWithHighestPriceTable = ttk.Treeview(dashboard_frame, column='column1', show='headings', height=2)

    prodWithHighestPriceTable.heading('#1', text="Product with the highest price")
    prodWithHighestPriceTable.column("#1", width=260, anchor="center")
    prodWithHighestPriceTable.insert("", END, value=(prodWithHighestPriceReport))
    prodWithHighestPriceTable.place(x=870, y=285)

    # Report for product with highest stock quantity
    prodWithQuanReport = product_backend.highestQuanProd()
    prodWithHighestQuanTable = ttk.Treeview(dashboard_frame, column='column1', show='headings', height=5)

    prodWithHighestQuanTable.heading('#1', text="Product with the high stock quantity")
    prodWithHighestQuanTable.column("#1", width=260, anchor="center")
    for i in prodWithQuanReport:
        prodWithHighestQuanTable.insert("", END, value=i)
    prodWithHighestQuanTable.place(x=870, y=375)

    # Report for product with least stock quantity
    prodWithQuanReport2 = product_backend.leastQuanProd()
    prodWithleastQuanTable = ttk.Treeview(dashboard_frame, column='column1', show='headings', height=5)

    prodWithleastQuanTable.heading('#1', text="Product with the low stock quantity")
    prodWithleastQuanTable.column("#1", width=260, anchor="center")
    for i in prodWithQuanReport2:
        prodWithleastQuanTable.insert("", END, value=i)
    prodWithleastQuanTable.place(x=870, y=535)

    # Recent Activity
    recentActivityLabel = Label(dashboard_frame, text='Recent Activity', font=('Lato', 15, 'bold'),
                                fg="#25333C", bg="#EAEEF4")
    recentActivityLabel.place(x=25, y=230)

    # Button to clear recent activity
    clearActivitybtn = Button(dashboard_frame, text="Clear", bg="#EAEEF4", fg="grey", bd=0, command=delete_activity,
                              font=("Lato", 8, "normal", 'underline'), cursor="hand2")
    clearActivitybtn.place(x=185, y=238)
    global recentActivityTable
    recentActivityTable = ttk.Treeview(dashboard_frame, column=(
        'column1', 'column2', 'column3', 'column4'), show='headings', height=15)

    recentActivityTable.heading('#1', text="Date")
    recentActivityTable.column("#1", width=120, anchor="center")

    recentActivityTable.heading('#2', text="Time")
    recentActivityTable.column("#2", width=120, anchor="center")

    recentActivityTable.heading('#3', text="Product / Supplier")
    recentActivityTable.column("#3", width=300, anchor="center")

    recentActivityTable.heading('#4', text="Action")
    recentActivityTable.column("#4", width=285, anchor="center")

    recentActivityTable.place(x=25, y=285)

    recentActivityData()


def supplier_frame():
    time_string = time.strftime('%H:%M:%S')
    date_sting = f"{datetime.datetime.now(): %a, %b %d %Y}"

    # function to add the user data into the database
    def add_command():
        global supplier_dbTable
        global id
        if supplier_name.get() or pan_no.get() or contact_no.get() != "":
            try:
                backend.insert(supplier_name.get().capitalize(), pan_no.get(), contact_no.get())
                recentActivity_backend.insert(date_sting, time_string, supplier_name.get(), "Supplier Added")
                supplier_dbTable.insert("", END, value=(" ", supplier_name.get(), pan_no.get(), contact_no.get()))

                # displays a information status of adding the entry
                addedLabel = Label(edit_frame, text="Supplier Added Successfully", bg='#EAEEF4', fg="#202020")
                addedLabel.place(x=5, y=240)
                addedLabel.after(3000, lambda: addedLabel.destroy())  # timer for information
            except:
                NotaddedLabel = Label(edit_frame, text="Supplier Not Added", bg='#EAEEF4', fg="#202020")
                NotaddedLabel.place(x=5, y=240)
                NotaddedLabel.after(3000, lambda: NotaddedLabel.destroy())  # timer for information
        else:
            emptyaddedLabel = Label(edit_frame, text="Entry Empty", bg='#EAEEF4', fg="#202020")
            emptyaddedLabel.place(x=5, y=240)
            emptyaddedLabel.after(3000, lambda: emptyaddedLabel.destroy())  # timer for information

        clear_command()
        display_supp_data()

    def clear_table():
        global supplier_dbTable
        for records in supplier_dbTable.get_children():
            supplier_dbTable.delete(records)

    def display_supp_data():
        clear_table()
        for rows in backend.view():
            supplier_dbTable.insert("", END, values=rows)

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
        suppId = backend.supp_id_list()
        # print(suppId)

        if id in suppId:
            backend.delete(id)
            recentActivity_backend.insert(date_sting, time_string, supplier_name.get(), "Supplier Data Deleted")
            # displays a information status of deleting entry
            deletedLabel = Label(edit_frame, text="Data Deleted Successfully", bg='#EAEEF4', fg="#202020")
            deletedLabel.place(x=5, y=240)
            deletedLabel.after(3000, lambda: deletedLabel.destroy())  # timer for information

        if id not in suppId:
            # print("nothing to delete")
            nothingTodeleteLabel = Label(edit_frame, text="No Data Selected To Delete", bg='#EAEEF4', fg="#202020")
            nothingTodeleteLabel.place(x=5, y=240)
            nothingTodeleteLabel.after(3000, lambda: nothingTodeleteLabel.destroy())  # timer for information

        clear_command()

    # function to search the info from database
    def search_command():
        if supplier_name.get() or pan_no.get() or contact_no.get() != "":
            clear_table()
            for rows in backend.search(supplier_name.get(), pan_no.get(), contact_no.get()):
                supplier_dbTable.insert("", END, values=rows)
            counting = len(supplier_dbTable.get_children())

            # if counting is more than 1 then it will display plural entry and if counting is equal to 1, it will display singular entry
            entry = ""
            plural = "Entries"
            singular = "Entry"
            if counting > 1:
                entry, plural = plural, entry
            elif counting <= 1:
                entry, singular = singular, entry

            # displays a information status of adding the entry
            searchedLabel = Label(edit_frame, text=f"{counting} {entry} found", bg='#EAEEF4', fg="#202020")
            searchedLabel.place(x=5, y=240)
            searchedLabel.after(4000, lambda: searchedLabel.destroy())  # timer for information
        else:
            nothingToSarchLabel = Label(edit_frame, text="Nothing to search", bg='#EAEEF4', fg="#202020")
            nothingToSarchLabel.place(x=5, y=240)
            nothingToSarchLabel.after(4000, lambda: nothingToSarchLabel.destroy())  # timer for information

    # function to update the information
    def update_command():
        global supplier_dbTable
        global id
        try:
            backend.update(id, supplier_name.get().capitalize(), pan_no.get(), contact_no.get())
            recentActivity_backend.insert(date_sting, time_string, supplier_name.get(), "Supplier Data Updated")
            clear_table()
            supplier_dbTable.insert("", END, values=(id, supplier_name.get(), pan_no.get(), contact_no.get()))
            display_supp_data()
            # displays a information status of updating entry
            updatedLabel = Label(edit_frame, text="Entry Updated Successfully", bg='#EAEEF4', fg="#202020")
            updatedLabel.place(x=5, y=240)
            updatedLabel.after(3000, lambda: updatedLabel.destroy())  # timer for information
            clear_command()
        except:
            # displays a information status of updating entry
            notupdatedLabel = Label(edit_frame, text="Nothing to update", bg='#EAEEF4', fg="#202020")
            notupdatedLabel.place(x=5, y=240)
            notupdatedLabel.after(3000, lambda: notupdatedLabel.destroy())  # timer for information

    # frame to display database of suppliers
    def supp_db_frame():
        global manage_supplier_frame
        global supplier_category_content_frame

        supplier_category_content_frame = Frame(dashboard_root, width=1366, height=728, bg="#EAEEF4")
        supplier_category_content_frame.place(x=200, y=50)

        manage_supplier_frame = Frame(supplier_category_content_frame, width=1120, height=780, bg='#EAEEF4')
        manage_supplier_frame.place(x=5, y=15)

        supp_list = Label(manage_supplier_frame, text='Supplier List', font=('Lato', 20, 'bold'),
                          fg="#25333C", bg="#EAEEF4")
        supp_list.place(x=20, y=0)

    # function to create a frame and do the editing of suppliers
    def edit_supplier_db():
        global edit_frame
        edit_frame = Frame(manage_supplier_frame, width=1200, height=260, bg='#EAEEF4')
        edit_frame.place(x=20, y=35)

        dbTable_frame = Frame(manage_supplier_frame, width=1200, height=380, bg='#EAEEF4')
        dbTable_frame.place(x=10, y=305)

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
        name_supp = Entry(edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                          textvariable=supplier_name,
                          font=('Roboto', 9, 'normal'))
        name_supp.place(x=200, y=30, width="290", height="35")

        pan_label = Label(edit_frame, text="PAN no.", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        pan_label.place(x=5, y=80)
        pan_supp = Entry(edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1, textvariable=pan_no,
                         font=('Roboto', 9, 'normal'))
        pan_supp.place(x=200, y=80, width="290", height="35")

        contact_label = Label(edit_frame, text="Contact", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        contact_label.place(x=5, y=130)
        contact_supp = Entry(edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                             textvariable=contact_no,
                             font=('Roboto', 9, 'normal'))
        contact_supp.place(x=200, y=130, width="290", height="35")

        add_btn = Button(edit_frame, text="Add Supplier", bd=0, bg='#266868', fg='#EAEEF4', font=('Roboto', 9, 'bold'),
                         command=add_command, cursor="hand2")
        add_btn.place(x=5, y=190, width="110", height="40")

        update_btn = Button(edit_frame, text="Update", bd=0, bg="#266868", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=update_command, cursor="hand2")
        update_btn.place(x=140, y=190, width="110", height="40")

        clear_btn = Button(edit_frame, text="Clear", bd=0, bg="#266868", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                           command=clear_command, cursor="hand2")
        clear_btn.place(x=275, y=190, width="110", height="40")

        search_btn = Button(edit_frame, text="Search", bd=0, bg="#266868", fg="#EAEEF4", font=('Roboto', 9, 'bold'),
                            command=search_command, cursor="hand2")
        search_btn.place(x=410, y=190, width="110", height="40")

        show_btn = Button(edit_frame, text="Show Data", bd=0, bg="#266868", fg="#ffffff",
                          font=('Roboto', 9, 'bold'), command=display_supp_data, cursor="hand2")
        show_btn.place(x=545, y=190, width="110", height="40")

        delete_btn = Button(edit_frame, text="Delete", bd=0, bg="#BB272B", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command, cursor="hand2")
        delete_btn.place(x=680, y=190, width="110", height="40")
        # delete_btn.bind("<Delete>", delete_command)

        global supplier_dbTable
        supplier_dbTable = ttk.Treeview(dbTable_frame, column=('column1', 'column2', 'column3', 'column4'),
                                        show='headings', height=17)

        supplier_dbTable.heading('#1', text="Id")
        supplier_dbTable.column('#1', width="30", anchor="center")

        supplier_dbTable.heading('#2', text="Supplier Name")
        supplier_dbTable.column('#2', width="500", anchor="center")

        supplier_dbTable.heading('#3', text="PAN", anchor="center")
        supplier_dbTable.column('#3', width="250", anchor="center")

        supplier_dbTable.heading('#4', text="Contact")
        supplier_dbTable.column('#4', width="250", anchor="center")

        supplier_dbTable.place(x=10, y=0)
        supplier_dbTable.bind('<Double-1>', get_selected_row)

    supp_db_frame()
    edit_supplier_db()
    display_supp_data()


def product_frame():
    time_string = time.strftime('%H:%M:%S')
    date_sting = f"{datetime.datetime.now(): %a, %b %d %Y}"

    # function to add the user data into the database
    def add_command():
        global product_dbTable
        if prodDate.get() or prodName.get() or prodPrice.get() or prodQuan.get() or prodSupp.get() or prodTotal.get() != "":
            try:
                product_backend.insert(prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),
                                       prodTotal.get())
                product_dbTable.insert("", END, value=(
                    "", prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),
                    prodTotal.get()))
                recentActivity_backend.insert(date_sting, time_string, prodName.get(), "Purchase Added")
                # displays a information status of adding the entry
                addedLabel = Label(product_edit_frame, text="Purchase Added Successfully", bg='#EAEEF4', fg="#202020")
                addedLabel.place(x=5, y=240)
                addedLabel.after(3000, lambda: addedLabel.destroy())  # timer for information
            except:
                NotaddedLabel = Label(product_edit_frame, text="Purchase Not Added", bg='#EAEEF4', fg="#202020")
                NotaddedLabel.place(x=5, y=240)
                NotaddedLabel.after(3000, lambda: NotaddedLabel.destroy())  # timer for information
        else:
            emptyaddedLabel = Label(product_edit_frame, text="Entry Empty", bg='#EAEEF4', fg="#202020")
            emptyaddedLabel.place(x=5, y=240)
            emptyaddedLabel.after(3000, lambda: emptyaddedLabel.destroy())  # timer for information

        display_prod_data()

    def clear_table():
        global product_dbTable
        for records in product_dbTable.get_children():
            product_dbTable.delete(records)

    # function to show Firm table data scroll list
    def display_prod_data():
        clear_table()
        for rows in product_backend.view():
            product_dbTable.insert("", END, values=rows)

    def get_selected_row(event):
        global selectRow
        selectRow = product_dbTable.selection()
        try:
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

                defaultForSuppDropdown()
                prodSupp.set(supplierofProduct)

                total_prod.delete(0, 'end')
                total_prod.insert(END, totalamtofProduct)
        except Exception as e:
            print(e)

    # function to clear the entry field
    def clear_command():
        date_prod.delete(0, END)
        name_prod.delete(0, END)
        price_prod.delete(0, END)
        quantity_prod.delete(0, END)
        defaultForSuppDropdown()
        total_prod.delete(0, END)

    # function to delete the data from database
    def delete_command():
        global product_dbTable
        for idGet in product_dbTable.selection():
            product_dbTable.delete(idGet)
        idList = product_backend.prod_id_list()
        if id in idList:
            # print("deleted")
            product_backend.delete(id)
            recentActivity_backend.insert(date_sting, time_string, prodName.get(), "Purchase Data Deleted")
            # displays a information status of deleting entry
            deletedLabel = Label(product_edit_frame, text="Data Deleted Successfully", bg='#EAEEF4', fg="#202020")
            deletedLabel.place(x=5, y=240)
            deletedLabel.after(3000, lambda: deletedLabel.destroy())  # timer for information

        elif id not in idList:
            # print("nothing to delete")
            nothingTodeleteLabel = Label(product_edit_frame, text="No Data Selected To Delete", bg='#EAEEF4',
                                         fg="#202020")
            nothingTodeleteLabel.place(x=5, y=240)
            nothingTodeleteLabel.after(3000, lambda: nothingTodeleteLabel.destroy())  # timer for information

        clear_command()

    # function to search the info from database
    def search_command():
        if prodDate.get() or prodName.get() or prodPrice.get() or prodQuan.get() or prodSupp.get() or prodTotal.get() != "":
            clear_table()
            for rows in product_backend.search(prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(),
                                               prodSupp.get(), prodTotal.get()):
                product_dbTable.insert("", END, values=rows)

            # Stores the number of entries shown in table
            counting = len(product_dbTable.get_children())
            # if counting is more than 1 then it will display plural entry and if counting is equal to 1, it will display singular entry
            entry = ""
            plural = "Entries"
            singular = "Entry"
            if counting > 1:
                entry, plural = plural, entry
            elif counting <= 1:
                entry, singular = singular, entry

            # displays a information status of adding the entry
            searchedLabel = Label(product_edit_frame, text=f"{counting} {entry} found", bg='#EAEEF4', fg="#202020")
            searchedLabel.place(x=5, y=240)
            searchedLabel.after(4000, lambda: searchedLabel.destroy())  # timer for information
        else:
            # displays a information status of adding the entry
            searchedLabel = Label(product_edit_frame, text="Nothing To Search", bg='#EAEEF4', fg="#202020")
            searchedLabel.place(x=5, y=240)
            searchedLabel.after(4000, lambda: searchedLabel.destroy())  # timer for information

    # function to update the information
    def update_command():
        global id
        try:
            product_backend.update(id, prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(),
                                   prodTotal.get())
            clear_table()
            product_dbTable.insert("", END, values=(
            id, prodDate.get(), prodName.get(), prodPrice.get(), prodQuan.get(), prodSupp.get(), prodTotal.get()))
            # displays a information status of updating entry
            updatedLabel = Label(product_edit_frame, text="Entry Updated Successfully", bg='#EAEEF4', fg="#202020")
            updatedLabel.place(x=5, y=240)
            updatedLabel.after(3000, lambda: updatedLabel.destroy())  # timer for information
            recentActivity_backend.insert(date_sting, time_string, prodName.get(),
                                          "Purchase Data Updated")  # sends activity report to recent activity
        except:
            # displays a information status of updating entry
            notupdatedLabel = Label(product_edit_frame, text="Nothing to update", bg='#EAEEF4', fg="#202020")
            notupdatedLabel.place(x=5, y=240)
            notupdatedLabel.after(3000, lambda: notupdatedLabel.destroy())  # timer for information

        display_prod_data()

    # function to insert the calculated value to total amount entry box on click
    def totalAmtonclick_focusin(event):
        price_val = int(price_prod.get())
        quan_val = int(quantity_prod.get())
        tot = price_val * quan_val
        if total_prod.get() == "":
            total_prod.insert(0, tot)
            total_prod.config(fg='black')

    def clearTotalAmount_onclickPrice(event):
        if price_prod.get() != '':
            total_prod.delete(0, END)
            total_prod.config(fg='black')

    def clearTotalAmount_onclickQuantity(event):
        if quantity_prod.get() != '':
            total_prod.delete(0, END)
            total_prod.config(fg='black')

    def defaultForSuppDropdown():
        prodSupp.set("")

    # function to create a frame and do the editing of suppliers
    def edit_product_db():

        global manage_product_frame
        global product_category_content_frame
        product_category_content_frame = Frame(dashboard_root, width=1366, height=728, bg="#EAEEF4")
        product_category_content_frame.place(x=200, y=60)

        manage_product_frame = Frame(product_category_content_frame, width=1120, height=780, bg='#EAEEF4')
        manage_product_frame.place(x=5, y=5)

        prod_list = Label(manage_product_frame, text='Stock Inventory', font=('Lato', 20, 'bold'),
                          fg="#25333C", bg="#EAEEF4")
        prod_list.place(x=20, y=0)

        global product_edit_frame
        product_edit_frame = Frame(manage_product_frame, width=1200, height=260, bg='#EAEEF4')
        product_edit_frame.place(x=20, y=35)

        dbTable_frame = Frame(manage_product_frame, width=1200, height=410, bg='#EAEEF4')
        dbTable_frame.place(x=10, y=305)

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
        prodTotal = StringVar()

        date_label = Label(product_edit_frame, text="Date", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        date_label.place(x=5, y=30)

        date_prod = Entry(product_edit_frame, textvariable=prodDate, font=('Roboto', 9, 'normal'), bd=0,
                          highlightbackground="#CDCDCD", highlightthickness=1)
        prodDate.set("")
        date_prod.place(x=200, y=30, width="290", height="35")

        name_label = Label(product_edit_frame, text="Product Name", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                           fg="#202020")
        name_label.place(x=5, y=80)
        name_prod = Entry(product_edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                          textvariable=prodName,
                          font=('Roboto', 9, 'normal'))
        name_prod.place(x=200, y=80, width="290", height="35")

        price_label = Label(product_edit_frame, text="Price", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        price_label.place(x=5, y=130)
        price_prod = Entry(product_edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                           textvariable=prodPrice,
                           font=('Roboto', 9, 'normal'))
        price_prod.place(x=200, y=130, width="290", height="35")
        price_prod.bind("<FocusIn>", clearTotalAmount_onclickPrice)

        quantity_label = Label(product_edit_frame, text="Quantity", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                               fg="#202020")
        quantity_label.place(x=600, y=30)
        quantity_prod = Entry(product_edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                              textvariable=prodQuan,
                              font=('Roboto', 9, 'normal'))
        quantity_prod.place(x=795, y=30, width="290", height="35")
        quantity_prod.bind("<FocusIn>", clearTotalAmount_onclickQuantity)

        supp_label = Label(product_edit_frame, text="Supplier", font=("Roboto", 10, 'bold'), bg='#EAEEF4', fg="#202020")
        supp_label.place(x=600, y=80)

        # Dropdown for Supplier Entry
        prodSupp = StringVar()
        defaultForSuppDropdown()  # Sets option menu default to blank
        list_supplier = backend.list_supplier()  # Gets a list of supplier from list_supplier function in backend.py
        supp_dropdown = OptionMenu(product_edit_frame, prodSupp, *sorted(list_supplier))
        # Set the background color of Displayed Options to white
        supp_dropdown["menu"].configure(bg="white")
        # Se the background color of Options Menu to white
        supp_dropdown.configure(bg="white", bd=0, highlightbackground="#CDCDCD", highlightthickness=1, cursor="hand2")
        supp_dropdown.place(x=795, y=80, width=290, height=35)

        total_amt_label = Label(product_edit_frame, text="Total Amount", font=("Roboto", 10, 'bold'), bg='#EAEEF4',
                                fg="#202020")
        total_amt_label.place(x=600, y=130)
        total_prod = Entry(product_edit_frame, bd=0, highlightbackground="#CDCDCD", highlightthickness=1,
                           textvariable=prodTotal, font=('Roboto', 9, 'normal'))
        total_prod.place(x=795, y=130, width="290", height="35")
        total_prod.insert(0, '')
        total_prod.bind("<FocusIn>", totalAmtonclick_focusin)
        # total_prod.bind("<FocusOut>", onclick_focusout)

        # Buttons Section
        add_btn = Button(product_edit_frame, text="Add Product", bd=0, bg='#266868', fg='#ffffff',
                         font=('Roboto', 9, 'bold'), command=add_command, cursor="hand2")
        add_btn.place(x=5, y=190, width="110", height="40")

        update_btn = Button(product_edit_frame, text="Update", bd=0, bg="#266868", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=update_command, cursor="hand2")
        update_btn.place(x=140, y=190, width="110", height="40")

        clear_btn = Button(product_edit_frame, text="Clear", bd=0, bg="#266868", fg="#ffffff",
                           font=('Roboto', 9, 'bold'),
                           command=clear_command, cursor="hand2")
        clear_btn.place(x=275, y=190, width="110", height="40")

        search_btn = Button(product_edit_frame, text="Search", bd=0, bg="#266868", fg="#ffffff",
                            font=('Roboto', 9, 'bold'),
                            command=search_command, cursor="hand2")
        search_btn.place(x=410, y=190, width="110", height="40")

        show_btn = Button(product_edit_frame, text="Show Data", bd=0, bg="#266868", fg="#ffffff",
                          font=('Roboto', 9, 'bold'), command=display_prod_data, cursor="hand2")
        show_btn.place(x=545, y=190, width="110", height="40")

        delete_btn = Button(product_edit_frame, text="Delete", bd=0, bg="#BB272B", fg="#ffffff",
                            font=('Roboto', 9, 'bold'), command=delete_command, cursor="hand2")
        delete_btn.place(x=680, y=190, width="110", height="40")
        delete_btn.bind("<Delete>", delete_command)

        global product_dbTable
        product_dbTable = ttk.Treeview(dbTable_frame, column=(
            'column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7'), show='headings', height=14)

        product_dbTable.heading('#1', text="Id")
        product_dbTable.column("#1", width=30, anchor="center")

        product_dbTable.heading('#2', text="Date")
        product_dbTable.column("#2", width=120, anchor="center")

        product_dbTable.heading('#3', text="Product Name")
        product_dbTable.column("#3", width=300, anchor="center")

        product_dbTable.heading('#4', text="Price")
        product_dbTable.column("#4", width=100, anchor="center")

        product_dbTable.heading('#5', text="Quantity")
        product_dbTable.column("#5", width=100, anchor="center")

        product_dbTable.heading('#6', text="Supplier")
        product_dbTable.column("#6", width=300, anchor="center")

        product_dbTable.heading('#7', text="Total Amount")
        product_dbTable.column("#7", width=130, anchor="center")

        product_dbTable.place(x=10, y=0)
        product_dbTable.bind('<Double-1>', get_selected_row)

    edit_product_db()
    display_prod_data()


def main_win():
    global dashboard_root
    global recentActivityData
    dashboard_root = Tk()
    dashboard_root.resizable(False, False)
    dashboard_root.title('EasyInv - Dashboard')
    dashboard_root.geometry("1366x768")
    dashboard_root.iconbitmap('D:\sem project\icon_pack\ico\Database-Upload.ico')

    category_main_frame()
    dashboard()

    dashboard_root.mainloop()
