import modules.admin.controller as admin_controller
import modules.guards.controller as guard_controller
import modules.students.controller as student_controller

from modules.admin.model import Admin
from modules.guards.model import Guard
from modules.students.model import Student

def login(email, password) -> str:
  student = student_controller.get_student_by_email(email)
  guard = guard_controller.get_admin_by_email(email)
  admin = admin_controller.get_admin_by_email(email)
  
  admin_valid = isinstance(admin, Admin) and admin.verify_password(password)
  guard_valid = isinstance(guard, Guard) and guard.verify_password(password)
  student_valid = isinstance(student, Student) and student.verify_password(password)
  
  if admin_valid:
    return "admin"

  elif student_valid:
    return "student"

  elif guard_valid:
    return "guard"

  else:
    return ""
  
def get_user(email):
  student = student_controller.get_student_by_email(email)
  if isinstance(student, Student):
    return student
  
  admin = admin_controller.get_admin_by_email(email)
  if isinstance(admin, Admin):
    return admin
  
  guard = guard_controller.get_admin_by_email(email)

  return None