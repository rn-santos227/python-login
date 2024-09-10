import config.database as DB

from database.query import builder, join_builder

from handlers.biometrics_handler import BiometricsHandler

from modules.biometrics.model import Biometric, StudentBiometrics

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

def match_biometrics(biometric_handler: BiometricsHandler, fingerprint_1, fingerprint_2) -> bool:
  return biometric_handler.verify_fingerprints(fingerprint_1=fingerprint_1, fingerprint_2=fingerprint_2)

def add_biometric(biometric_handler: BiometricsHandler):
  pass

def remove_biometric(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, where_clause, "delete")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()