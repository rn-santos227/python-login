import hashlib
class User:
  def __init__(self, id, email, password):
    self.id = id
    self.email = email
    self.password = password

  @staticmethod
  def encrypt_password(password) -> str:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

  def verify_password(self, password):
    pass