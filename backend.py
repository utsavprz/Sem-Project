import sqlite3

# backend connection for database of supplier


# Creating a database

def supp_dbect():
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Firm(id INTEGER PRIMARY KEY,name text,pan integer,contact integer)")
    supp_db.commit()
    supp_db.close()


# Inserting Datas
def insert(name, pan, contact):
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("INSERT INTO Firm VALUES(NULL,?,?,?)", (name, pan, contact))
    supp_db.commit()
    supp_db.close()


def view():
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM Firm")
    rows = cur.fetchall()
    supp_db.close()
    return rows


def search(name="", pan="", contact=""):
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("SELECT * FROM Firm WHERE name=? OR pan=? OR contact=?", (name, pan, contact))
    rows = cur.fetchall()
    supp_db.close()
    return rows


def delete(id):
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("DELETE FROM Firm WHERE id=?", (id,))
    supp_db.commit()
    supp_db.close()


def update(id, name, pan, contact):
    supp_db = sqlite3.connect("suppliers.db")
    cur = supp_db.cursor()
    cur.execute("UPDATE Firm SET name=?,pan=?,contact=? WHERE id=?", (name, pan, contact, id))
    supp_db.commit()
    supp_db.close()

def count_suppliers():
    supp_db = sqlite3.connect("suppliers.db")
    cur =supp_db.cursor()
    count_supp = cur.execute("SELECT COUNT(DISTINCT name) FROM Firm")
    count_num = count_supp.fetchall()
    for num in count_num:
        return num
    supp_db.commit()
    supp_db.close()


supp_dbect()