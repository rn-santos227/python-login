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
    pass
  elif action.lower() == 'insert':
    pass
  pass