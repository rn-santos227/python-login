from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Log:
  def __init__(self,
    id=None,
    student_id=None,
    login_time=None,
    logout_time=None,
    date=None,
    student_name=None,
    student_number=None,
  ):
    self.id = id
    self.student_id = student_id
    self.login_time = login_time
    self.logout_time = logout_time
    self.date = date
    self.student_name = student_name,
    self.student_number = student_number,

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE logs (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT,
      login_time DATETIME,
      logout_time DATETIME,
      date DATE,
      CONSTRAINT log_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''