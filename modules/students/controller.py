from modules.students.model import Student

import config.database as DB

def get_student_by_id(id):
  pass

def get_student_by_email(email):
  sql_query = DB.query_builder('students', 'email = ?', 'select')
  pass

def get_students():
  pass

def create_student(student: Student):
  pass

def update_student(student: Student):
  pass

def delete_student(id):
  pass