import os
import pyodbc
import win32com.client

from config.config import database_name

def create_db():
  if not os.path.exists(database_name):
    access_app = win32com.client.Dispatch("Access.Application")
    access_app.NewCurrentDatabase(database_name)
    access_app.Quit()
    print(f"Database '{database_name}' created successfully.")
  else:
    print(f"Database '{database_name}' already exists.")
    
def connect_db():
  conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=" + database_name + ";"
  )
  conn = pyodbc.connect(conn_str)
  conn.close()
  return conn

def query_builder(table, query, action):
  if action.lower() == 'select':
    if query.lower() == 'all':
      sql_query = f"SELECT * FROM {table};"
    else:
      sql_query = f"SELECT * FROM {table} WHERE {query};"
  
  elif action.lower() == 'insert':
    sql_query = f"INSERT INTO {table} VALUES ({query});"
  
  elif action.lower() == 'update':
    sql_query = f"UPDATE {table} SET {query};"

  elif action.lower() == 'delete':
    sql_query = f"DELETE FROM {table} WHERE {query};"

  else:
    raise ValueError("Invalid action. Supported actions are: 'select', 'insert', 'update', 'delete'.")

  return sql_query