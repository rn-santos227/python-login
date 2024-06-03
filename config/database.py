import os
import pyodbc
import pypyodbc

from config.config import database_name

def create_db():
  if not os.path.exists(database_name):
    pypyodbc.win_create_mdb(database_name)
    print(f"Database '{database_name}' created successfully.")
    
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=" + database_name
    )
    conn = pypyodbc.connect(conn_str)
    print(f"Connected to the database '{database_name}' successfully.")
    
    conn.close()
    print(f"Connection to the database '{database_name}' closed.")
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

def check_db_connection() -> bool:
  if os.path.exists(database_name):
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        r"DBQ=" + database_name
    )
    
    try:
      conn = pypyodbc.connect(conn_str)
      print(f"Connected to the database '{database_name}' successfully.")
      conn.close()
      print(f"Connection to the database '{database_name}' closed.")
      return True
    
    except pypyodbc.Error as e:
      print(f"Failed to connect to the database '{database_name}': {e}")
      return False
      
  else:
    print(f"Database '{database_name}' does not exist. Please create it first.")
    return False

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

def create_table(query):
  conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=" + database_name
  )

