from modules.users.model import User

class SessionHandler:
  def __init__(self):
    self.user: User = None

  def create_session(self, user: User):
    pass