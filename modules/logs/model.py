from modules.students.model import Student
from modules.students.controller import get_student_by_id

class Log:
  def __init__(self,
    id=None,
    student_id=None,
    login_time=None,
    logout_time=None,
    date=None,
  ):
    self.id = id
    self.student_id = student_id
    self.login_time = login_time
    self.logout_time = logout_time
    self.date = date

  @property
  def student(self) -> Student:
    return get_student_by_id(self.student_id)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE logs (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT NOT NULL,
      login_time DATETIME,
      logout_time DATETIME,
      date DATE,
      CONSTRAINT log_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''
  
class StudentLog:
  def __init__(self, log_id, student_id, login_time, logout_time, date, email, full_name, contact_number, section, course, face_url):
    self.log_id = log_id
    self.student_id = student_id
    self.login_time = login_time
    self.logout_time = logout_time
    self.date = date
    self.email = email
    self.full_name = full_name
    self.contact_number = contact_number
    self.section = section
    self.course = course
    self.face_url = face_url