from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Parent:
  def __init__(self, id=None, student_id=None, full_name=None, contact=None):
    self.id = id
    self.student_id = student_id
    self.full_name = full_name
    self.contact = contact

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE parents (
      id AUTOINCREMENT PRIMARY KEY,
      student_id INT,
      full_name TEXT,
      contact TEXT,
      CONSTRAINT parent_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''