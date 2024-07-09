import os
import mysql.connector
from mysql.connector import errorcode

from config.config import database_name, connection_params

def create_db():
  try:
    conn = mysql.connector.connect(**connection_params)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")

def connect_db():
  pass

def check_db_connection() -> bool:
  pass

def create_table(query, table):
  pass
