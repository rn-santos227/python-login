
import config.database as DB

from typing import Union
from database.query import builder
from modules.admin.model import Admin

table = "admins"

def get_admin_by_id(id) -> Union[Admin, str]:
  sql_query = builder(table, 'id = ?', 'select')
  cursor = DB.connect_db().cursor()
  try:
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

def get_admins(query, action) -> Union[list[Admin], str]:
  sql_query = builder(table, query, action)
  cursor = DB.connect_db().cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    admins = []
    for row in rows:
      admin = Admin(*row)
      admins.append(admin)
    return admins if admins else "No admin records available."
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def create_admin(admin: Admin) -> Admin:
  columns = "(full_name, email, password, status)"
  sql_query = builder(table, f"{columns} VALUES (?, ?, ?, ?);", 'insert')
  cursor = DB.connect_db().cursor()
  
  try:
    values = (admin.full_name, admin.email, admin.password, admin.status)
    cursor.execute(sql_query, values)
    return admin

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_admin(admin: Admin):
  set_clause = (
    f"email = '{admin.email}', "
    f"password = '{admin.encrypt_password(admin.password)}', "
    f"full_name = '{admin.full_name}', "
    f"status = '{admin.status}', "
  )
  where_clause = f"id = {admin.id}"
  sql_query = builder(table, f"{set_clause} WHERE {where_clause}", 'update')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return admin

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def delete_admin(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(table, f"WHERE {where_clause}", 'delete')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False