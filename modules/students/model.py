from modules.users.model import User

class Student(User):
  def __init__(self, id, full_name, student_number, email, contact_number, section, level, password):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.student_number = student_number
    self.contact_number = contact_number
    self.section = section
    self.level = level