
import config.database as DB

from typing import Union
from modules.students.model import Student

table = "students"

def get_student_by_id(id)-> Union[Student, str]:
  sql_query = DB.query_builder(table, 'id = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query, (id))
    row = cursor.fetchone()

    if row:
      student = Student(*row)
      return student
    else:
      return "No students found."
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def get_student_by_email(email) -> Union[Student, str]:
  sql_query = DB.query_builder(table, 'email = ?', 'select')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query, (email))
    row = cursor.fetchone()

    if row:
      student = Student(*row)
      return student
    else:
      return "No student found with the provided email."
    
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def get_students(query, action) -> Union[list[Student], str]:
  sql_query = DB.query_builder(table, query, action)
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    students = []
    for row in rows:
      student = Student(*row)
      students.append(student)
    return students if students else "No student records available."
  
  except Exception as e:
    print(f"Error: {e}")
  
  finally:
    cursor.close()
    DB.connect_db.close()

def create_student(student: Student) -> Student:
  columns = "(email, password, full_name, student_number, contact_number, section, level, status)"
  values = f"'{student.email}', '{student.password}', '{student.full_name}', '{student.student_number}', '{student.contact_number}', '{student.section}', '{student.level}', '{student.status}'"
  sql_query = DB.query_builder(table, f"{columns} VALUES ({values})", 'insert')
  try:
    cursor = DB.connect_db.cursor()
    cursor.execute(sql_query)
    return student
  
  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()
    DB.connect_db.close()

def update_student(student: Student) -> Student:
  set_clause = (f"email = '{student.email}', "
    f"password = '{student.password}', "
    f"full_name = '{student.full_name}', "
    f"student_number = '{student.student_number}', "
    f"contact_number = '{student.contact_number}', "
    f"section = '{student.section}', "
    f"level = '{student.level}', "
    f"status = '{student.status}'")
  where_clause = f"id = {student.id}"

def delete_student(id):
  pass