import os
import mysql.connector
from mysql.connector import errorcode

from config.config import database_name, connection_params

def create_db():
  try:
    conn = mysql.connector.connect(**connection_params)
    cursor = conn.cursor()

  except mysql.connector.Error as err:
    pass

def connect_db():
  pass

def check_db_connection() -> bool:
  pass

def create_table(query, table):
  pass
