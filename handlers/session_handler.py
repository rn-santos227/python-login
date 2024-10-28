from modules.admin.model import Admin
from modules.guards.model import Guard
from modules.students.model import Student
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
    if isinstance(self.user, Student):
      return "student"
    
    elif isinstance(self.user, Admin):
      return "admin"
    
    else:
      return ""
    
  def destroy_session(self):
    self.user = None