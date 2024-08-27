import config.database as DB

from database.query import builder

from handlers.biometrics_handler import BiometricsHandler

from modules.biometrics.model import Biometric

__table = "biometrics"

def get_biometrics(query, action) -> list[Biometric]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    biometrics: list[Biometric] = []
    for row in rows:
      biometric: Biometric = Biometric(*row)
      biometrics.append(biometric)

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def match_biometrics():
  pass

def add_biometric():
  pass

def delete_biometric():
  pass