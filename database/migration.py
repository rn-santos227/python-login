import pyodbc

def create_access_database(database_name):
  conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + database_name + ';'
  )
  conn = pyodbc.connect(conn_str)
  conn.close()