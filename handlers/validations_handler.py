import re

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