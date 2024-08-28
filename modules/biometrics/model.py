from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Biometric():
  def __init__(self, id=None, student_id=None, fingerprint_data=None):
    self.id = id
    self.student_id = student_id
    self.fingerprint_data = fingerprint_data

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE biometrics (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT,
      fingerprint_data BLOB NOT NULL,
      CONSTRAINT student_biometric FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''  