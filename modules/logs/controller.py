
import config.database as DB

from typing import Union
from modules.logs.model import Log

def get_log_by_id(id):
  sql_query = DB.query_builder('logs', 'id = ?', 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query, (id))
  row = cursor.fetchone()

  cursor.close()
  DB.connect_db.close()
  if row:
    log = Log(*row)
    return log

def get_logs():
  pass

def get_logs_by_student(student_id):
  pass

def create_log(log: Log):
  pass

def update_log(log: Log):
  pass

def delete_log(id):
  pass