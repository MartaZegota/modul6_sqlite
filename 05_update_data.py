# 05_update_data.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by the db_file
   :param db_file: dbase file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
   except Error as e:
       print(e)

   return conn

def update(conn, table, id, **kwargs):
   """
   update name of the product, price and weight of a produkt
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

if __name__ == "__main__":
   conn = create_connection("dbase.db")
   update(conn, "todo", 9, product="listek laurowy")
   conn.close()