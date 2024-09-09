from modules.users.model import User

class Admin(User):
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
    CREATE TABLE admins (
      id INT AUTO_INCREMENT PRIMARY KEY,
      full_name VARCHAR(255) NOT NULL,
      email VARCHAR(255) UNIQUE,
      password VARCHAR(255) NOT NULL,
      status VARCHAR(10)
    );
  '''