import pyodbc

# Create Access database
def connect_db(database_name):
  conn_str = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=" + database_name + ";"
  )
  conn = pyodbc.connect(conn_str)
  conn.close()
  return conn

def query_builder(table, query, action):
  if action.lower() == 'select':
    sql_query = f"SELECT * FROM {table} WHERE {query};"
  
  elif action.lower() == 'insert':
    sql_query = f"INSERT INTO {table} VALUES ({query});"
  
  elif action.lower() == 'update':
    pass

  elif action.lower() == 'delete':
    pass

  else:
    raise ValueError("Invalid action. Supported actions are: 'select', 'insert', 'update', 'delete'.")