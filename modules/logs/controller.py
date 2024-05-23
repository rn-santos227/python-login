
import config.database as DB

from typing import Union
from modules.logs.model import Log

table = "logs"

def get_log_by_id(id) -> Union[Log, str]:
  sql_query = DB.query_builder(table, 'id = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      log = Log(*row)
      return log
    else:
      return "No logs found."
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def get_logs(query, action) -> Union[list[Log], str]:
  sql_query = DB.query_builder(table, query, action)
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    logs = []
    for row in rows:
      log = Log(*row)
      logs.append(log)

    return logs if logs else "No logs available."
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def get_logs_by_student(student_id) -> Union[list[Log], str]:
  sql_query = DB.query_builder(table, 'student_id = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query, (student_id))
    rows = cursor.fetchall()

    logs = []
    for row in rows:
      log = Log(*row)
      logs.append(log)

    return logs if logs else "No logs available."
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def create_log(log: Log) -> Log:
  columns = "(student_id, ip_address)"
  values =  f"'{log.student_id}', '{log.ip_address}'"
  sql_query = DB.query_builder(table, f"{columns} VALUES ({values})", 'insert')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def add_login_time(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = DB.query_builder(table, f"{set_clause} WHERE {where_clause}", 'update')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def add_logout_time(log: Log) -> Log:
  set_clause = (
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = DB.query_builder(table, f"{set_clause} WHERE {where_clause}", 'update')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def update_log(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = DB.query_builder(table, f"{set_clause} WHERE {where_clause}", 'update')
  try:
    cursor = DB.connect_db.cursor()

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def delete_log(id):
  pass