from modules.users.model import User

class Admin(User):
  def __init__(self, id, name, email, password, status):
    super().__init__(id, email, password)
    self.name = name
    self.status = status

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE administrators (
      id AUTOINCREMENT PRIMARY KEY,
      name TEXT,
      email TEXT,
      password TEXT,
    );
    '''