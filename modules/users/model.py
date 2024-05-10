import hashlib
import re
class User:
  def __init__(self, id, email, password):
    self.id = id
    self.email = email
    self._password_hash = self.encrypt_password(password)

  @staticmethod
  def encrypt_password(password) -> str:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

  def verify_password(self, password):
    input_password_hash = self.encrypt_password(password)
    return input_password_hash == self._password_hash
  
  def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
      return email
    else:
      raise AttributeError("Invalid email address")

  @property
  def password(self):
    raise AttributeError("Password is not readable")
  
  @password.setter
  def password(self, new_password):
    self._password_hash = self.encrypt_password(new_password)