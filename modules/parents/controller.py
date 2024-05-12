from typing import Union
from modules.parents.model import Parent

import config.database as DB

def get_parent_by_id(id):
  pass

def get_parents(query, action) -> Union[list[Parent], str]:
  sql_query = DB.query_builder('students', query, action)
  cursor = DB.connect_db.cursor()

def create_parent(parent: Parent):
  pass

def update_parent(parent: Parent):
  pass

def delete_parent(id):
  pass