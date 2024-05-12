from typing import Union
from modules.parents.model import Parent

import config.database as DB

def get_parent_by_id(id):
  pass

def get_parents(query, action) -> Union[list[Parent], str]:
  pass

def create_parent(parent: Parent):
  pass

def update_parent(parent: Parent):
  pass

def delete_parent(id):
  pass