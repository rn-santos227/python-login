import config.database as DB

from typing import Union
from database.query import builder
from modules.parents.model import Parent

__table = "parents"

def get_parent_by_id(id) -> Union[Parent, None]:
  sql_query = builder(__table, 'id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query, (id,))
    row = cursor.fetchone()

    if row:
      parent = Parent(*row)
      return parent
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_parent_by_student_id(student_id) -> Union[Parent, None]:
  sql_query = builder(__table, 'student_id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id,))
    row = cursor.fetchone()

    if row:
      parent = Parent(*row)
      return parent
    else:
      return None

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_parents(query, action) -> list[Parent]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    parents = []
    for row in rows:
      parent = Parent(*row)
      parents.append(parent)
    return parents
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def create_parent(parent: Parent) -> Parent:
  columns = "(student_id, full_name, contact)" 
  sql_query = builder(__table, f"{columns} VALUES (%s, %s, %s)", "insert")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    values = (parent.student_id, parent.full_name, parent.contact)
    cursor.execute(sql_query, values)
    connection.commit()
    return parent

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_parent(parent: Parent) -> Parent:
  set_clause = (
    f"full_name = '{parent.full_name}', "
    f"contact_number = '{parent.contact_number}', "
  )
  where_clause = f"id = {parent.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return parent

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def delete_parent(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, f"WHERE {where_clause}", "delete")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False
  
  finally:
    cursor.close()