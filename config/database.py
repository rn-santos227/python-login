import os
import mysql.connector
from mysql.connector import errorcode

from config.config import database_name, connection_params

def create_db():
  try:
    conn = mysql.connector.connect(**connection_params)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database '{database_name}' created successfully.")

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    
    else:
      print(err)

  finally:
    cursor.close()
    conn.close()
    print(f"Connection to the MySQL server closed.")

def connect_db():
  connection_params['database'] = database_name
  conn = mysql.connector.connect(**connection_params)
  return conn

def check_db_connection() -> bool:
  try:
    conn = connect_db()
    print(f"Connected to the database '{database_name}' successfully.")
    conn.close()
    print(f"Connection to the database '{database_name}' closed.")
    return True

  except mysql.connector.Error as err:
    print(f"Failed to connect to the database '{database_name}': {err}")
    return False

def create_table(query, table):
  try:
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print(f"Table '{table}' created successfully.")

  except mysql.connector.Error as err:
    print(f"Failed to create table '{table}': {err}")

  finally:
    cursor.close()
    conn.close()
    print(f"Connection to the database '{database_name}' closed.")
