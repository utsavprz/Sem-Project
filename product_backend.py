import sqlite3


# backend connection for database of product

# Creating a database

def supp_dbect():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS ProductItem(id INTEGER PRIMARY KEY,name text,price integer,quantity integer,supplier text)")
    supp_db.commit()
    supp_db.close()


# Inserting Datas
def insert(name, price, quantity, supplier):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("INSERT INTO ProductItem VALUES(NULL,?,?,?,?)", (name, price, quantity, supplier))
    supp_db.commit()
    supp_db.close()


def view():
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM ProductItem")
    rows = cur.fetchall()
    supp_db.close()
    return rows


def search(name="", price="", quantity="", supplier=""):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM ProductItem WHERE name=? OR price=? OR quantity=? OR supplier=?",
                (name, price, quantity, supplier))
    rows = cur.fetchall()
    supp_db.close()
    return rows


def delete(id):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("DELETE FROM ProductItem WHERE id=?", (id,))
    supp_db.commit()
    supp_db.close()


def update(id, name, price, quantity, supplier):
    supp_db = sqlite3.connect("products.db")
    cur = supp_db.cursor()
    cur.execute("UPDATE ProductItem SET name=?,price=?,quantity=?,supplier=? WHERE id=?",
                (name, price, quantity, supplier, id))
    supp_db.commit()
    supp_db.close()


supp_dbect()
