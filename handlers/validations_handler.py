import re

import modules.students.controller as student_controller

class ValidationHandler:
  @staticmethod
  def is_not_empty(input_str):
    return bool(input_str.strip())

  @staticmethod
  def is_valid_integer(input_str):
    try:
      int(input_str)
      return True
    except ValueError:
      return False

  @staticmethod
  def is_valid_email(input_str):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, input_str) is not None

  @staticmethod
  def is_valid_phone(input_str):
    phone_regex = r'^\+?1?\d{9,15}$'
    return re.match(phone_regex, input_str) is not None
  
  @staticmethod
  def is_unique_email(input_email):
    return student_controller.get_student_by_email(email=input_email) == None

  @staticmethod
  def is_unique_student_number(input_student_number):
    pass

  @staticmethod
  def validate_fields(self, fields):
    for validation_method, field_value, error_message in fields:
      if not validation_method(field_value):
        self.message_box.show_message("Validation Error", error_message, "error")
        return False
    return True