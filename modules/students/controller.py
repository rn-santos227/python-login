from typing import Union
from modules.students.model import Student

import config.database as DB

def get_student_by_id(id):
  pass

def get_student_by_email(email) -> Union[Student, str]:
  sql_query = DB.query_builder('students', 'email = ?', 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query, (email))
  row = cursor.fetchone()

  cursor.close()
  DB.connect_db.close()
  if row:
    student = Student(*row)
    return student
  else:
    return "No student found with the provided email."

def get_students(query):
  sql_query = DB.query_builder('students', query, 'select')
  cursor = DB.connect_db.cursor()
  cursor.execute(sql_query)
  rows = cursor.fetchAll()

  students = []
  for row in rows:
    student = Student(*row)
    students.append(student)

  cursor.close()
  DB.connect_db.close()
  return students if students else ["No student records available."]

def create_student(student: Student):
  pass

def update_student(student: Student):
  pass

def delete_student(id):
  pass