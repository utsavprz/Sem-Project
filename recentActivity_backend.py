import sqlite3

def recAct_dbect():
    recAct_db = sqlite3.connect("recent_activity.db")
    cur = recAct_db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS RecentActivity(date integer, time integer,supplierORproduct text,action text)")
    recAct_db.commit()
    recAct_db.close()

# Inserting Datas
def insert(date, time, supplierORproduct, action):
    recAct_db = sqlite3.connect("recent_activity.db")
    cur = recAct_db.cursor()
    cur.execute("INSERT INTO RecentActivity VALUES(?,?,?,?)", (date, time, supplierORproduct, action))
    recAct_db.commit()
    recAct_db.close()

# display data
def view():
    recAct_db = sqlite3.connect("recent_activity.db")
    cur = recAct_db.cursor()
    cur.execute("SELECT * FROM RecentActivity")
    rows = cur.fetchall()
    recAct_db.close()
    return rows

def delete():
    recAct_db = sqlite3.connect("recent_activity.db")
    cur = recAct_db.cursor()
    cur.execute("DELETE FROM RecentActivity")
    recAct_db.commit()
    recAct_db.close()

recAct_dbect()