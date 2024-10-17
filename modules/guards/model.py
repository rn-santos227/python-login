from modules.users.model import User

class Guard(User):
  def __init__(self, id=None, full_name=None, email=None, password=None, status=None):
    super().__init__(id, email, password)
    self.full_name = full_name
    self.status = status