
import config.database as DB

from typing import Union
from database.query import builder, join_builder

from modules.logs.model import Log, StudentLog

__table = "logs"

def get_log_by_id(id) -> Union[Log, None]:
  sql_query = builder(__table, 'id = ?', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query, (id,))
    row = cursor.fetchone()

    if row:
      log: Log = Log(*row)
      return log
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_log_by_student_and_date(student_id, date) -> Union[Log, None]:
  sql_query = builder(__table, f"student_id = %s AND date = %s", "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id, date))
    row = cursor.fetchone()

    if row:
      log: Log = Log(*row)
      return log
    else:
      return None
  
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_logs(query, action) -> list[Log]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    logs: list[Log] = []
    for row in rows:
      log: Log = Log(*row)
      logs.append(log)

    return logs
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_logs_by_student(student_id) -> list[Log]:
  sql_query = builder(__table, 'student_id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_id,))
    rows = cursor.fetchall()

    logs: list[Log] = []
    for row in rows:
      log: Log = Log(*row)
      logs.append(log)

    return logs
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_logs_with_students(query) -> list[StudentLog]:
  condition = f"{__table}.student_id = students.id"
  columns = f"{__table}.id as log_id, {__table}.student_id, {__table}.login_time, {__table}.logout_time, {__table}.date, students.email, students.full_name, students.student_number, students.section, students.course, students.face_url"
  sql_query = join_builder(table1=__table, table2="students", join_condition=condition, columns=columns, query=query)
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    student_logs: list[StudentLog] = []
    for row in rows:
      student_log: StudentLog = StudentLog(*row)
      student_logs.append(student_log)

    return student_logs

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def create_log(log: Log) -> Log:
  columns = "(student_id, date)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s)", "insert")
  sql_select = builder(__table, "id = LAST_INSERT_ID()", "select")

  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    values = (log.student_id, log.date)
    cursor.execute(sql_query, values)
    connection.commit()

    cursor.execute(sql_select)
    result = cursor.fetchone()
    
    if result:
      log: Log = Log(*result)
      return log
    else:
      return None

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def add_login_time(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
    
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def add_logout_time(log: Log) -> Log:
  set_clause = (
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")

  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_log(log: Log) -> Log:
  set_clause = (
    f"login_time = '{log.login_time}'"
    f"logout_time = '{log.logout_time}'"
  )
  where_clause = f"id = {log.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")

  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    connection.commit()
    return log

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def delete_log(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, where_clause, "delete")

  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    connection.commit()
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False
  
  finally:
    cursor.close()