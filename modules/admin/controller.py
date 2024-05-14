
from typing import Union
import config.database as DB

from modules.admin.model import Admin

def get_admin_by_id(id):
  pass

def get_admins(query, action):
  sql_query = DB.query_builder('admins', query, action)
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()

def create_admin(admin: Admin):
  pass

def update_admin(admin: Admin):
  pass

def delete_admin(id):
  pass