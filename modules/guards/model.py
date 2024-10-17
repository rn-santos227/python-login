from modules.users.model import User

class Guard(User):
  def __init__(self, id=None, full_name=None, email=None, password=None, status=None):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.status = status

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE guards (
      id INT AUTO_INCREMENT PRIMARY KEY,
      full_name VARCHAR(255) NOT NULL,
      email VARCHAR(255) UNIQUE,
    );
    '''
