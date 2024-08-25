class Biometric():
  def __init__(self, id=None, student_id=None, fingerprint_data=None):
    self.id = id
    self.student_id = student_id
    self.fingerprint_data = fingerprint_data

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE biometrics (
      id INT AUTO_INCREMENT PRIMARY KEY,
      student_id INT
      fingerprint_data BLOB NOT NULL,
      CONSTRAINT parent_student FOREIGN KEY (student_id) REFERENCES students(id)
    );
    '''  