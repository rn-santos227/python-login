import re

def builder(table, query, action):
  if action.lower() == "select":
    if query.lower() == "all":
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


def join_builder(table1, table2, join_condition, join_type="inner", columns="*", query=None):
  if join_type and join_type.lower() not in ["inner", "left", "right", "full"]:
    raise ValueError("Invalid join type. Supported join types are: 'inner', 'left', 'right', 'full'.")
  
  join_type = join_type.upper()
  
  sql_query = f"SELECT {columns} FROM {table1} {join_type} JOIN {table2} ON {join_condition}"
  
  if not query:
    query = "all"

  if query and query.lower() == "all":
    sql_query += ";"

  elif query and re.search(r'limit:(\d+),(asc|desc)', query, re.IGNORECASE):
    match = re.search(r'limit:(\d+),(asc|desc)', query, re.IGNORECASE)
    limit_value = match.group(1)
    order = match.group(2).upper()
    sql_query += f" ORDER BY login_time {order} LIMIT {limit_value};"

  elif query:
    sql_query += f" WHERE {query};"
  
  return sql_query