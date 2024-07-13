from modules.users.model import User

class Student(User):
  def __init__(self, id=None, email=None, password=None, full_name=None, student_number=None, contact_number=None, section=None, grade=None, face_encode=None, status=None):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.student_number = student_number
    self.contact_number = contact_number
    self.section = section
    self.grade = grade
    self.face_encode = face_encode
    self.status = status

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE students (
      id INT AUTO_INCREMENT PRIMARY KEY,
      email VARCHAR(255) UNIQUE,
      password VARCHAR(255),
      full_name VARCHAR(255),
      student_number VARCHAR(255) UNIQUE,
      contact_number VARCHAR(25),
      section VARCHAR(10),
      grade VARCHAR(15),
      face_encode TEXT,
      status VARCHAR(10)
    );
    '''
  
class StudentLog:
  def __init__(self, log_id, student_id, login_time, logout_time, date, student_name, student_number, email, full_name, contact_number, section):
    self.log_id = log_id
    self.student_id = student_id
    self.login_time = login_time
    self.logout_time = logout_time
    self.date = date
    self.student_name = student_name
    self.student_number = student_number
    self.email = email
    self.full_name = full_name
    self.contact_number = contact_number
    self.section = section