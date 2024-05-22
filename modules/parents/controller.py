import config.database as DB

from typing import Union
from modules.parents.model import Parent

table = "parents"

def get_parent_by_id(id) -> Union[Parent, str]:
  sql_query = DB.query_builder(table, 'id = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
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
    DB.connect_db.close()

def get_parents(query, action) -> Union[list[Parent], str]:
  sql_query = DB.query_builder(table, query, action)
  try:
    cursor = DB.connect_db.cursor()
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
    DB.connect_db.close()

def create_parent(parent: Parent) -> Parent:
  columns = "(student_id, full_name, contact)" 
  values = f"'{parent.student_id}', '{parent.full_name}', {parent.contact}"
  sql_query = DB.query_builder(table, f"{columns} VALUES ({values})", 'insert')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return parent

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def update_parent(parent: Parent) -> Parent:
  set_clause = (

  )

def delete_parent(id):
  pass