from modules.users.model import User

class Student(User):
  def __init__(self, id=None, email=None, password=None, full_name=None, student_number=None, contact_number=None, section=None, level=None, status="active"):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.student_number = student_number
    self.contact_number = contact_number
    self.section = section
    self.level = level
    self.status = status

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE students (
      id AUTOINCREMENT PRIMARY KEY,
      email TEXT,
      password TEXT,
      full_name TEXT,
      student_number TEXT,
      contact_number TEXT,
      section TEXT,
      level TEXT,
      status TEXT
    );
    '''