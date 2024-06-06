import modules.students.controller as student_controller

def login(email, password) -> bool:
  student = student_controller.get_student_by_email(email)
  
  if(student.verify_password(password)):
    print(f"User has been logged in.")
    return True
  else:
    print(f"User could not login.")
    return False