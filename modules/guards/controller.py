import config.database as DB

from typing import Union
from database.query import builder
from modules.guards.model import Guard

__table = "guards"

def get_guards_by_id(id) -> Union[Guard, None]:
  pass