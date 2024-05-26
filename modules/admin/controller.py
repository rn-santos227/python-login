
import config.database as DB

from typing import Union
from modules.admin.model import Admin

table = "admins"

def get_admin_by_id(id) -> Union[Admin, str]:
  sql_query = DB.query_builder(table, 'id = ?', 'select')
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
  sql_query = DB.query_builder(table, query, action)
  try:
    cursor = DB.connect_db.cursor()
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
    DB.connect_db.close()

def create_admin(admin: Admin) -> Admin:
  columns = "(full_name, email, password, status)"
  values = f"'{admin.full_name}', '{admin.email}', {admin.password}, '{admin.status}'"
  sql_query = DB.query_builder(table, f"{columns} VALUES ({values})", 'insert')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return admin

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def update_admin(admin: Admin):
  set_clause = (
    f"email = '{admin.email}', "
    f"password = '{admin.encrypt_password(admin.password)}', "
    f"full_name = '{admin.full_name}', "
    f"status = '{admin.status}', "
  )
  where_clause = f"id = {admin.id}"
  sql_query = DB.query_builder(table, f"{set_clause} WHERE {where_clause}", 'update')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return admin

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def delete_admin(id):
  where_clause = f"id = {id}"