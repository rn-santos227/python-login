from students.model import Student

class Log:
  def __init__(self,
    id,
    student_id,
    timestamp
  ):
    self.id = id
    self.student_id = student_id
    self.timestamp = timestamp

  def get_student(self):
    pass