import config.database as DB

from typing import Union
from database.query import builder
from modules.guards.model import Guard

__table = "guards"

def get_guard_by_id(id) -> Union[Guard, None]:
  sql_query = builder(__table, "id = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      guard: Guard = Guard(*row)
      return guard

    else:
      return None

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback()

  finally:
    cursor.close()
    connection.close() 

def get_admin_by_email(email: str) -> Union[Guard, None]:
  sql_query = builder(__table, "email = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (email))
    row = cursor.fetchone()

    if row:
      guard: Guard = Guard(*row)
      return guard
    else:
      return None

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close()

def get_guards(query, action) -> list[Guard]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    guards: list[Guard] = []
    for row in rows:
      guard: Guard = Guard(*row)
      guards.append(guard)
    return guards

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def create_guard(guard: Guard) -> Guard:
  columns = "(full_name, email, password, status)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s, %s, %s)", "insert")

  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    values = (guard.full_name, guard.email, guard.password, guard.status)
    cursor.execute(sql_query, values)
    connection.commit()
    return guard

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback()

  finally:
    cursor.close()
    connection.close()

def update_admin(guard: Guard):
  set_clause = (
    
  )