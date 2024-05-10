from students.model import Student

class Log:
  def __init__(self,
    id,
    student_id,
    login_time
  ):
    self.id = id
    self.student_id = student_id
    self.login_time = login_time

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE logs (
      id AUTOINCREMENT PRIMARY KEY,
      student_id INT,
      timestamp DATETIME,
      FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''