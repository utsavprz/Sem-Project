import sqlite3


# backend connection for database of product

# Creating a database

def prod_dbect():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ProductItem(id INTEGER PRIMARY KEY,name text,price integer,quantity integer,supplier text)")
    #cur.execute("ALTER TABLE ProductItem ADD totalAmount integer")
    prod_db.commit()
    prod_db.close()


# Inserting Datas
def insert(date, name, price, quantity, supplier,totalAmount):
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("INSERT INTO ProductItem VALUES(NULL,?,?,?,?,?,?)", (date,name, price, quantity, supplier, totalAmount))
    prod_db.commit()
    prod_db.close()


def view():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("SELECT * FROM ProductItem")
    rows = cur.fetchall()
    prod_db.close()
    return rows


def search(date ="", name="", price="", quantity="", supplier="",totalAmount=""):
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("SELECT * FROM ProductItem WHERE date=? OR name=? OR price=? OR quantity=? OR supplier=? OR totalAmount=?",(date,name, price, quantity, supplier,totalAmount))
    rows = cur.fetchall()
    prod_db.close()
    return rows



def delete(id):
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("DELETE FROM ProductItem WHERE id=?", (id,))
    prod_db.commit()
    prod_db.close()


def update(id, date, name, price, quantity, supplier,totalAmount):
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    cur.execute("UPDATE ProductItem SET date=?,name=?,price=?,quantity=?,supplier=?,totalAmount=? WHERE id=?",
                (date, name, price, quantity, supplier, totalAmount, id))
    prod_db.commit()
    prod_db.close()


def count_products():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    count_prod =cur.execute("SELECT COUNT(DISTINCT name) FROM ProductItem")
    count_num = count_prod.fetchall()
    for num in count_num:
        return num
    prod_db.commit()
    prod_db.close()

def count_invoices():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    count_date =cur.execute("SELECT COUNT(date) FROM ProductItem").fetchall()
    for num in count_date:
        return num
    prod_db.commit()
    prod_db.close()


def purchase_amount():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    sum = cur.execute("SELECT sum(totalAmount) FROM ProductItem")
    total = sum.fetchall()
    for x in total:
        return x[0]
    prod_db.commit()
    prod_db.close()

def prod_id_list():
    prod_db = sqlite3.connect("products.db")
    cur = prod_db.cursor()
    listId = cur.execute("SELECT id FROM ProductItem").fetchall()
    iList=[]
    for listing in listId:
        iList.append(listing[0])
    return iList
    prod_db.commit()
    prod_db.close()

prod_dbect()





