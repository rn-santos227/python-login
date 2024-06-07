import modules.admin.controller as admin_controller
import modules.students.controller as student_controller

from modules.admin.model import Admin
from modules.students.model import Student

def login(email, password) -> bool:
  student = student_controller.get_student_by_email(email)
  admin = admin_controller.get_admin_by_email(email)
  
  if(student.verify_password(password) | admin.verify_password(password)):
    print(f"User has been logged in.")
    return True
  else:
    print(f"User could not login.")
    return False