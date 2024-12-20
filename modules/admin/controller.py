
import config.database as DB

from typing import Union
from database.query import builder
from modules.admin.model import Admin

__table = "admins"

def get_admin_by_id(id) -> Union[Admin, None]:
  sql_query = builder(__table, "id = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      admin: Admin = Admin(*row)
      return admin
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_admin_by_email(email: str) -> Union[Admin, None]:
  sql_query = builder(__table, "email = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (email,))
    row = cursor.fetchone()

    if row:
      admin: Admin = Admin(*row)
      return admin
    else:
      return None
  
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_admins(query, action) -> list[Admin]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    admins: list[Admin] = []
    for row in rows:
      admin: Admin = Admin(*row)
      admins.append(admin)
    return admins
  
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def create_admin(admin: Admin) -> Admin:
  columns = "(full_name, email, password, status)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s, %s, %s)", "insert")

  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    values = (admin.full_name, admin.email, admin.password, admin.status)
    cursor.execute(sql_query, values)
    connection.commit()
    return admin

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def update_admin(admin: Admin):
  set_clause = (
    f"email = '{admin.email}', "
    f"password = '{admin.encrypt_password(admin.password)}', "
    f"full_name = '{admin.full_name}', "
    f"status = '{admin.status}', "
  )
  where_clause = f"id = {admin.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return admin

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def delete_admin(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, where_clause, "delete")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return True

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 
    return False
  
  finally:
    cursor.close()
    connection.close() 