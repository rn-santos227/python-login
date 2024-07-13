def builder(table, query, action):
  if action.lower() == "select":
    if query.lower() == 'all':
      sql_query = f"SELECT * FROM {table};"
    else:
      sql_query = f"SELECT * FROM {table} WHERE {query};"

  elif action.lower() == "insert":
    sql_query = f"INSERT INTO {table}{query};"

  elif action.lower() == "update":
    sql_query = f"UPDATE {table} SET {query};"

  elif action.lower() == "delete":
    sql_query = f"DELETE FROM {table} WHERE {query};"

  else:
    raise ValueError("Invalid action. Supported actions are: 'select', 'insert', 'update', 'delete'.")

  return sql_query 


def join_builder(table1, table2, join_condition=None, join_type=None, query=None):
  if join_type and join_type.lower() not in ["inner", "left", "right", "full"]:
    raise ValueError("Invalid join type. Supported join types are: 'inner', 'left', 'right', 'full'.")
  
  if join_type:
    join_type = join_type.upper()
  
  if not query:
    query = "all"

  if query.lower() == 'all':
    if table2 and join_condition:
      sql_query = f"SELECT * FROM {table1} {join_type} JOIN {table2} ON {join_condition};"