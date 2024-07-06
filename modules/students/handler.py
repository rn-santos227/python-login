from typing import List

from modules.students.model import Student
from modules.students.controller import get_students

students: List[Student] = get_students("status = 'active'", "select")

def update_students():
  global students
  students = get_students("status = 'active'", "select")