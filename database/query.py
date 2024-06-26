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