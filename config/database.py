import mysql.connector
from mysql.connector import errorcode

from config.config import database_name, connection_params

def create_db():
  print(connection_params)
  conn = mysql.connector.connect(**connection_params)
  cursor = conn.cursor()  
  
  try:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database '{database_name}' created successfully.")

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    
    else:
      print(err)

  finally:
    cursor.close()
    print(f"Connection to the MySQL server closed.")

def connect_db():
  connection_params_with_db = connection_params.copy()
  connection_params_with_db['database'] = database_name
  return mysql.connector.connect(**connection_params_with_db)

def check_db_connection() -> bool:
  connection_params_with_db = connection_params.copy()
  connection_params_with_db['database'] = database_name
  
  try:
    conn = mysql.connector.connect(**connection_params_with_db)
    print(f"Connected to the database '{database_name}' successfully.")
    conn.close()
    print(f"Connection to the database '{database_name}' closed.")
    return True
  
  except mysql.connector.Error as err:
    print(f"Failed to connect to the database '{database_name}': {err}")
    return False

def create_table(query, table):
  conn = connect_db()
  cursor = conn.cursor()

  try:
    cursor.execute(query)
    conn.commit()
    print(f"Table '{table}' created successfully.")

  except mysql.connector.Error as err:
    print(f"Failed to create table '{table}': {err}")

  finally:
    cursor.close()
    print(f"Connection to the database '{database_name}' closed.")
