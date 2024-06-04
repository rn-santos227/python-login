def builder(table, query, action):
  if action.lower() == 'select':
    pass

  else:
    raise ValueError("Invalid action. Supported actions are: 'select', 'insert', 'update', 'delete'.")
  