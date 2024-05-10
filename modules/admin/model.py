from modules.users.model import User

class Admin(User):
  def __init__(self, id, name, email, password):
    super().__init__(id, email, password)
    self.name = name

  @User.password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)

  @staticmethod
  def create_table() -> str:
    return '''
    CREATE TABLE administrators (
      id AUTOINCREMENT PRIMARY KEY,
      full_name TEXT,
      email TEXT,
      password TEXT,
    );
    '''