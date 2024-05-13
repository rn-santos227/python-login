from typing import Union
from modules.parents.model import Parent

import config.database as DB

def get_parent_by_id(id):
  sql_query = DB.query_builder('parents', 'id = ?', 'select')
  cursor = DB.connect_db.cursor()

def get_parents(query, action) -> Union[list[Parent], str]:
  sql_query = DB.query_builder('parents', query, action)
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchall()

  parents = []
  for row in rows:
    parent = Parent(*row)
    parents.append(parent)

  cursor.close()
  DB.connect_db.close()
  return parents if parents else "No parent records available."

def create_parent(parent: Parent):
  pass

def update_parent(parent: Parent):
  pass

def delete_parent(id):
  pass