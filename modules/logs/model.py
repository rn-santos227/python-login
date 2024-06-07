from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Log:
  def __init__(self,
    id,
    student_id,
    login_time,
    logout_time,
    ip_address,
  ):
    self.id = id
    self.student_id = student_id
    self.login_time = login_time
    self.logout_time = logout_time
    self.ip_address = ip_address

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE logs (
      id AUTOINCREMENT PRIMARY KEY,
      student_id INT,
      login_time DATETIME,
      logout_time DATETIME,
      ip_address TEXT,
      CONSTRAINT log_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''