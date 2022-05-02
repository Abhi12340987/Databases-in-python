import psycopg2
#psycopg2 - postgreSQL

def create_table():
    conn = psycopg2.connect("dbname='database_1' user='postgres' password='7894' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

create_table()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database_1' user='postgres' password='7894' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

insert("orange", 1, 2.5)

def view():
    conn = psycopg2.connect("dbname='database_1' user='postgres' password='7894' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

def delete(item):
    conn = psycopg2.connect("dbname='database_1' user='postgres' password='7894' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("Delete FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

#delete("orange")

def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database_1' user='postgres' password='7894' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item =%s",(quantity,price,item))
    conn.commit()
    conn.close()
update(5, 10, "orange")

#update(11, 6, "Coffee Cup")
#delete("Water Glass")
#print(view())
#insert("Coffee Cup", 10, 5)
