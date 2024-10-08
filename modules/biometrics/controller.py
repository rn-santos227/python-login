import config.database as DB

from typing import Union
from database.query import builder, join_builder

from modules.biometrics.model import Biometric, StudentBiometrics

__table = "biometrics"

def get_biometrics_by_student_id(student_id)  -> Union[Biometric, None]:
  sql_query = builder(__table, 'student_id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id,))
    row = cursor.fetchone()

    if row:
      biometric: Biometric = Biometric(*row)
      return biometric

  except Exception as e:
    print(f"Error: {e}")

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
    return biometrics

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_biometrics_with_students(query) -> list[StudentBiometrics]:
  condition = f"{__table}.student_id = students.id"
  columns = f"{__table}.id as biometrics_id, {__table}.student_id, students.email, students.full_name, students.course"
  sql_query = join_builder(table1=__table, table2="students", join_condition=condition, columns=columns, query=query)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    student_biometrics: list[StudentBiometrics] = []
    for row in rows:
      biometric: StudentBiometrics = StudentBiometrics(*row)
      student_biometrics.append(biometric)
    return student_biometrics

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def create_biometric(biometric: Biometric):
  columns = "(student_id, fingerprint_data)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s)", "insert")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    fingerprint_blob = biometric.fingerprint_data if isinstance(biometric.fingerprint_data, bytes) else bytes(biometric.fingerprint_data)

    values = (biometric.student_id, fingerprint_blob)
    cursor.execute(sql_query, values)
    connection.commit()
    return biometric

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def remove_biometric(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, where_clause, "delete")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 