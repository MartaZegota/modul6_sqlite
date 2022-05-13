# 03_add_data.py

import sqlite3

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: dbase file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def add_produkt(conn, produkt):
   """
   Create a new produkt into the todo table
   :param conn:
   :param produkt:
   :return: produkt id
   """
   sql = '''INSERT INTO todo(product, price_PLN, weight_kg)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, produkt)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   conn = create_connection("dbase.db")
 
   produkt = (
       " roquefort",
       12.50,
       2
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " stilton",
       11.24,
       1
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " brie",
       9.30,
       1
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " gouda",
       8.55,
       1
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " edam",
       11,
       1
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " parmezan",
       16.50,
       3.5
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " mozzarella",
       14,
       1.3
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " owczy",
       122.32,
       2.2
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   produkt = (
       " listek mięty",
       20,
       0.2
   )
   produkt_id = add_produkt(conn, produkt)
   print(produkt_id)

   conn.commit()