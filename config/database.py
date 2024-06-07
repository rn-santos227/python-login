import os
import pyodbc
import pypyodbc

from config.config import database_path
from config.config import data_folder
from config.config import connection_string

def create_db():
  if not os.path.exists(database_path):
    pypyodbc.win_create_mdb(database_path)
    print(f"Database '{database_path}' created successfully.")
    conn = pypyodbc.connect(connection_string)
    print(f"Connected to the database '{database_path}' successfully.")
    
    conn.close()
    print(f"Connection to the database '{database_path}' closed.")
  else:
    print(f"Database '{database_path}' already exists.")
    
def connect_db():
  conn = pyodbc.connect(connection_string)
  return conn

def check_db_connection() -> bool:
  if not os.path.exists(data_folder):
    os.makedirs(data_folder)

  if os.path.exists(database_path):
    try:
      conn = pypyodbc.connect(connection_string)
      print(f"Connected to the database '{database_path}' successfully.")
      conn.close()
      print(f"Connection to the database '{database_path}' closed.")
      return True
    
    except pypyodbc.Error as e:
      print(f"Failed to connect to the database '{database_path}': {e}")
      return False
      
  else:
    print(f"Database '{database_path}' does not exist. Please create it first.")
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
      print(f"Connection to the database '{database_path}' closed.")

