#psycopg2


import psycopg2

def create_table():
    conn = psycopg2.connect("Databases in python/lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("Databases in python/lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("Databases in python/lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("Databases in python/lite.db")
    cur=conn.cursor()
    cur.execute("Delete FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("Databases in python/lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item = ?", (quantity,price,item))
    conn.commit()
    conn.close()
    
update(11,6,"Coffee Cup")
#delete("Water Glass")
print(view())
#insert("Coffee Cup", 10, 5)