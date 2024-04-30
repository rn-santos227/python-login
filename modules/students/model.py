class Student:
  def __init__(self,
    id, email, first_name, middle_name, last_name, section, level
  ):
    self.id = id
    self.email = email
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.section = section
    self.level = level

  def get_full_name(self) -> str:
    if (self.middle_name):
      return f"{self.first_name} {self.middle_name[0]}. {self.last_name}"
    else:
      return f"{self.first_name} {self.last_name}"