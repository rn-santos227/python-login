
from typing import Union
import config.database as DB

from modules.admin.model import Admin

def get_admin_by_id(id):
  sql_query = DB.query_builder('admins', 'id = ?', 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query, (id))
  row = cursor.fetchone()

  cursor.close()

def get_admins(query, action) -> Union[list[Admin], str]:
  sql_query = DB.query_builder('admins', query, action)
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()

  admins = []
  for row in rows:
    admin = Admin(*row)
    admins.append(admin)

  cursor.close()
  DB.connect_db.close()
  return admins if admins else "No admin records available."

def create_admin(admin: Admin):
  pass

def update_admin(admin: Admin):
  pass

def delete_admin(id):
  pass