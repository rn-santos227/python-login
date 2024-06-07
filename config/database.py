import os
import pyodbc
import pypyodbc

from config.config import database_name
from config.config import data_folder
from config.config import connection_string

def create_db():
  if not os.path.exists(database_name):
    pypyodbc.win_create_mdb(database_name)
    print(f"Database '{database_name}' created successfully.")
    conn = pypyodbc.connect(connection_string)
    print(f"Connected to the database '{database_name}' successfully.")
    
    conn.close()
    print(f"Connection to the database '{database_name}' closed.")
  else:
    print(f"Database '{database_name}' already exists.")
    
def connect_db():
  conn = pyodbc.connect(connection_string)
  return conn

def check_db_connection() -> bool:
  if os.path.exists(database_name):
    try:
      conn = pypyodbc.connect(connection_string)
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

def create_table(query, table):
  conn = pypyodbc.connect(connection_string)  
  cursor = conn.cursor()

  try:
    cursor.execute(query)
    conn.commit()
    print(f"Table '{table}' created successfully.")

  except Exception as e:
      print(f"Failed to create table '{table}': {e}")

  finally:
      cursor.close()
      conn.close()
      print(f"Connection to the database '{database_name}' closed.")

