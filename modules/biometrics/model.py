class Biometric():
  def __init__(self, id=None, student_id=None, fingerprint_data=None):
    self.id = id
    self.student_id = student_id
    self.fingerprint_data = fingerprint_data

  @staticmethod
  def create_table() -> str:
    return '''
    
    '''  