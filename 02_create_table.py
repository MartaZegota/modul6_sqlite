# 02_create_table.py

import sqlite3
from sqlite3 import Error

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
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_todo_sql = """
   -- todo table
   CREATE TABLE IF NOT EXISTS todo (
      id integer PRIMARY KEY,
      product text NOT NULL,
      price_PLN float NOT NULL,
      weight_kg float NOT NULL
   );
   """

   db_file = "dbase.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_todo_sql)
       conn.close()