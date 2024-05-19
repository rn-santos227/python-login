
import config.database as DB

from typing import Union
from modules.admin.model import Admin

def get_admin_by_id(id) -> Union[Admin, str]:
  sql_query = DB.query_builder('admins', 'id = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      admin = Admin(*row)
      return admin
    else:
      return "No admin found."
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def get_admins(query, action) -> Union[list[Admin], str]:
  sql_query = DB.query_builder('admins', query, action)
  try:
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
  
  except Exception as e:
    print(f"Error: {e}")

def create_admin(admin: Admin):
  pass

def update_admin(admin: Admin):
  pass

def delete_admin(id):
  pass