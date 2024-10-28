from modules.users.model import User

class SessionHandler:
  def __init__(self):
    self.user: User = None

  def create_session(self, user: User):
    self.user = user

  def verify_password(self, password) -> bool:
    if self.user:
      return self.user.verify_password(password)
    
    else:
      return False
    
  def get_user_type(self) -> str:
    pass
    
  def destroy_session(self):
    self.user = None