from config.database import query_builder
from modules.students.model import Student

def get_student_by_id(id):
  pass

def get_student_by_email(email):
  query = 'SELECT * FROM students WHERE email = ?;'
  pass

def get_students():
  pass

def create_student(student: Student):
  pass

def update_student(student: Student):
  pass

def delete_student(id):
  pass