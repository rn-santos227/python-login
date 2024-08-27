import config.database as DB

from typing import Union
from database.query import builder
from modules.biometrics.model import Biometric

__table = "biometrics"

def get_biometrics(query, action) -> list[Biometric]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)

  except Exception as e:
    print(f"Error: {e}")

def match_biometrics():
  pass

def add_biometric():
  pass

def delete_biometric():
  pass