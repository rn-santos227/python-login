from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Parent:
  def __init__(self, id=None, student_id=None, email=None, full_name=None, contact=None):
    self.id = id
    self.student_id = student_id
    self.email = email
    self.full_name = full_name
    self.contact = contact

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE parents (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT,
      full_name VARCHAR(255),
      contact VARCHAR(25),
      CONSTRAINT parent_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''