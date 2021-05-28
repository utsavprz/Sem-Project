import sqlite3


# backend connection for database of product

# Creating a database

def supp_dbect():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ProductItem(id INTEGER PRIMARY KEY,name text,price integer,quantity integer,supplier text)")
    #cur.execute("ALTER TABLE ProductItem ADD totalAmount integer")
    supp_db.commit()
    supp_db.close()


# Inserting Datas
def insert(date, name, price, quantity, supplier,totalAmount):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("INSERT INTO ProductItem VALUES(NULL,?,?,?,?,?,?)", (date,name, price, quantity, supplier, totalAmount))
    supp_db.commit()
    supp_db.close()


def view():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM ProductItem")
    rows = cur.fetchall()
    supp_db.close()
    return rows


def search(date ="", name="", price="", quantity="", supplier="",totalAmount=""):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM ProductItem WHERE date=? OR name=? OR price=? OR quantity=? OR supplier=? OR totalAmount=?",(date,name, price, quantity, supplier,totalAmount))
    rows = cur.fetchall()
    supp_db.close()
    return rows


def delete(id):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("DELETE FROM ProductItem WHERE id=?", (id,))
    supp_db.commit()
    supp_db.close()


def update(id, date, name, price, quantity, supplier,totalAmount):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("UPDATE ProductItem SET date=?,name=?,price=?,quantity=?,supplier=?,totalAmount=? WHERE id=?",
                (date, name, price, quantity, supplier, totalAmount, id))
    supp_db.commit()
    supp_db.close()

def count_products():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    count_prod =cur.execute("SELECT COUNT(DISTINCT name) FROM ProductItem")
    count_num = count_prod.fetchall()
    for num in count_num:
        print(num[0])
    supp_db.commit()
    supp_db.close()

def purchase_amount():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    sum = cur.execute("SELECT name, sum(totalAmount) FROM ProductItem")
    total = sum.fetchall()
    for x in total:
        print(x)
    supp_db.commit()
    supp_db.close()

supp_dbect()

