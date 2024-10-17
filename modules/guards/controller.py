import config.database as DB

from typing import Union
from database.query import builder
from modules.guards.model import Guard

__table = "guards"

def get_guards_by_id(id) -> Union[Guard, None]:
  sql_query = builder(__table, "id = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (id))

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 