from modules.users.model import User

class Admin(User):
  def __init__(self, id, full_name, email, password):
    super().__init__(id, email, password)