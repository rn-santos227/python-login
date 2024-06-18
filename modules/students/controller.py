
import config.database as DB

from typing import Union
from database.query import builder
from modules.students.model import Student

table = "students"

def get_student_by_id(id)-> Union[Student, None]:
  sql_query = builder(table, 'id = ?', "select")
  cursor = DB.connect_db().cursor()
  try:
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      student = Student(*row)
      return student
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_student_by_email(email) -> Union[Student, None]:
  sql_query = builder(table, 'email = ?', "select")
  cursor = DB.connect_db().cursor()
  try:
    cursor.execute(sql_query, (email))
    row = cursor.fetchone()

    if row:
      student = Student(*row)
      return student
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def get_student_by_student_number(student_number) -> Union[Student, None]:
  sql_query = builder(table, 'student_number = ?', "select")

def get_students(query, action) -> list[Student]:
  sql_query = builder(table, query, action)
  cursor = DB.connect_db().cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    students = []
    for row in rows:
      student = Student(*row)
      students.append(student)
    return students
  
  except Exception as e:
    print(f"Error: {e}")
  
  finally:
    cursor.close()

def create_student(student: Student) -> Student:
  columns = "(email, password, full_name, student_number, contact_number, section, grade, status)"
  sql_query = builder(table, f"{columns} VALUES (?, ?, ?, ?, ?, ?, ?, ?)", "insert")
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    values = (student.email, student.password, student.full_name, student.student_number, student.contact_number, student.section, student.grade, student.status)
    cursor.execute(sql_query, values)
    connection.commit()
    return student
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_student(student: Student) -> Student:
  set_clause = (
    f"email = '{student.email}', "
    f"password = '{student.encrypt_password(student.password)}', "
    f"full_name = '{student.full_name}', "
    f"student_number = '{student.student_number}', "
    f"contact_number = '{student.contact_number}', "
    f"section = '{student.section}', "
    f"grade = '{student.grade}', "
    f"status = '{student.status}'"
  )
  where_clause = f"id = {student.id}"
  sql_query = builder(table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return student

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def delete_student(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(table, f"WHERE {where_clause}", "delete")
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