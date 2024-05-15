
import config.database as DB

from typing import Union
from modules.logs.model import Log

def get_log_by_id(id):
  sql_query = DB.query_builder('logs', 'id = ?', 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query, (id))

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