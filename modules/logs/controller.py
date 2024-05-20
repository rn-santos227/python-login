
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
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()

  logs = []
  for row in rows:
    log = Log(*row)
    logs.append(log)

  cursor.close()
  DB.connect_db.close()
  return logs if logs else "No logs available."

def get_logs_by_student(student_id) -> Union[list[Log], str]:
  sql_query = DB.query_builder('logs', 'student_id = ?', 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query, (student_id))
  rows = cursor.fetchall()

  logs = []
  for row in rows:
    log = Log(*row)
    logs.append(log)

  cursor.close()
  DB.connect_db.close()
  return logs if logs else "No logs available."

def create_log(log: Log) -> Log:
  pass

def update_log(log: Log) -> Log:
  pass

def delete_log(id):
  pass