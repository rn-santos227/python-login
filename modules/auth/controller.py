from students.controller import get_student_by_email

def login(email, password) -> bool:
  student = get_student_by_email(email)
  return False