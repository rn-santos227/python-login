def builder(table, query, action):
  sql_query = ""
  if action.lower() == 'select':
    pass

  else:
    raise ValueError("Invalid action. Supported actions are: 'select', 'insert', 'update', 'delete'.")

  return sql_query 