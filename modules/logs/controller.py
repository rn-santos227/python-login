
import config.database as DB

from typing import Union
from database.query import builder, join_builder
from modules.logs.model import Log

__table = "logs"

def get_log_by_id(id) -> Union[Log, None]:
  sql_query = builder(__table, 'id = ?', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query, (id,))
    row = cursor.fetchone()

    if row:
      log = Log(*row)
      return log
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_log_by_student_and_date(student_id, date) -> Union[Log, None]:
  sql_query = builder(__table, f"student_id = %s AND date = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id, date))
    row = cursor.fetchone()

    if row:
      log = Log(*row)
      return log
    else:
      return None
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_logs(query, action) -> list[Log]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    logs = []
    for row in rows:
      log = Log(*row)
      logs.append(log)

    return logs
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_logs_by_student(student_id) -> list[Log]:
  sql_query = builder(__table, 'student_id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id,))
    rows = cursor.fetchall()

    logs = []
    for row in rows:
      log = Log(*row)
      logs.append(log)

    return logs
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def create_log(log: Log) -> Log:
  columns = "(student_id, date)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s)", "insert")

  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    values = (log.student_id, log.ip_address)
    cursor.execute(sql_query, values)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_logs_with_students() -> list[Log]:
  pass

def add_login_time(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
    
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def add_logout_time(log: Log) -> Log:
  set_clause = (
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")

  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_log(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")

  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def delete_log(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, f"WHERE {where_clause}", "delete")

  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    connection.commit()
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False
  
  finally:
    cursor.close()