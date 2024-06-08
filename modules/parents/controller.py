import config.database as DB

from typing import Union
from database.query import builder
from modules.parents.model import Parent

table = "parents"

def get_parent_by_id(id) -> Union[Parent, str]:
  sql_query = builder(table, 'id = ?', 'select')
  cursor = DB.connect_db().cursor()
  
  try:
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      parent = Parent(*row)
      return parent
    else:
      return "No parent found."
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_parents(query, action) -> Union[list[Parent], str]:
  sql_query = builder(table, query, action)
  cursor = DB.connect_db().cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    parents = []
    for row in rows:
      parent = Parent(*row)
      parents.append(parent)
    return parents if parents else "No parent records available."
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def create_parent(parent: Parent) -> Parent:
  columns = "(student_id, full_name, contact)" 
  sql_query = builder(table, f"{columns} VALUES (?, ?, ?)", 'insert')
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
  sql_query = builder(table, f"{set_clause} WHERE {where_clause}", 'update')
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
  sql_query = builder(table, f"WHERE {where_clause}", 'delete')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False
  
  finally:
    cursor.close()
    DB.connect_db.close()