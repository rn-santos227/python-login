import re
from datetime import datetime

import modules.admin.controller as admins_controller
import modules.guards.controller as guards_controller
import modules.parents.controller as parents_controller
import modules.students.controller as students_controller

class ValidationHandler:
  @staticmethod
  def is_not_empty(input_str):
    input_str = str(input_str)
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
  def is_unique_admin_email(input_email):
    return admins_controller.get_admin_by_email(email=input_email) == None
  
  @staticmethod
  def is_unique_student_email(input_email):
    return students_controller.get_student_by_email(email=input_email) == None
  
  @staticmethod
  def is_unique_guard_email(input_email):
    return guards_controller.get_guard_by_email(email=input_email) == None

  @staticmethod
  def is_unique_parents_email(input_email):
    return parents_controller.get_parent_by_email(email=input_email) == None

  @staticmethod
  def is_unique_student_number(input_student_number):
    return students_controller.get_student_by_student_number(student_number=input_student_number) == None

  @staticmethod
  def validate_fields(self, fields):
    for validation_method, field_value, error_message in fields:
      if not validation_method(field_value):
        self.message_dialog.show_message("Validation Error", error_message, "error")
        return False
    return True