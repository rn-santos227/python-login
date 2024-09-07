from modules.users.model import User

class Student(User):
  def __init__(self, id=None, email=None, password=None, full_name=None, student_number=None, contact_number=None, section=None, course=None, face_encode=None, face_url=None, status=None):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.student_number = student_number
    self.contact_number = contact_number
    self.section = section
    self.course = course
    self.face_encode = face_encode
    self.face_url = face_url
    self.status = status

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE students (
      id INT AUTO_INCREMENT PRIMARY KEY,
      email VARCHAR(255) UNIQUE NOT NULL,
      password VARCHAR(255) NOT NULL,
      full_name VARCHAR(255) NOT NULL,
      student_number VARCHAR(255) UNIQUE NOT NULL,
      contact_number VARCHAR(25) NOT NULL,
      section VARCHAR(10) NOT NULL,
      course VARCHAR(15) NOT NULL,
      face_encode TEXT,
      face_url TEXT,
      status VARCHAR(10)
    );
    '''