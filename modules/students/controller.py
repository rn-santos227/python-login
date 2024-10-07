
import config.database as DB

from typing import Union
from database.query import builder
from modules.students.model import Student

__table = "students"

def get_student_by_id(id)-> Union[Student, None]:
  sql_query = builder(__table, 'id = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (id,))
    row = cursor.fetchone()

    if row:
      student: Student = Student(*row)
      return student
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_student_by_email(email: str) -> Union[Student, None]:
  sql_query = builder(__table, 'email = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (email,))
    row = cursor.fetchone()

    if row:
      student: Student = Student(*row)
      return student
    else:
      return None
    
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_student_by_student_number(student_number) -> Union[Student, None]:
  sql_query = builder(__table, 'student_number = %s', "select")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query, (student_number,))
    row = cursor.fetchone()

    if row:
      student: Student = Student(*row)
      return student
    else:
      return None

  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def get_students(query, action) -> list[Student]:
  sql_query = builder(__table, query, action)
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()

    students: list[Student] = []
    for row in rows:
      student: Student = Student(*row)
      students.append(student)
    return students
  
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 
  
  finally:
    cursor.close()
    connection.close() 

def create_student(student: Student) -> Student:
  columns = "(email, password, full_name, student_number, contact_number, section, course, status)"
  sql_query = builder(__table, f"{columns} VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", "insert")
  connection = DB.connect_db()
  cursor = connection.cursor()
  
  try:
    values = (student.email, student.password, student.full_name, student.student_number, student.contact_number, student.section, student.course, student.status)
    cursor.execute(sql_query, values)
    connection.commit()
    return student
  
  except Exception as e:
    print(f"Error: {e}")
    connection.rollback() 

  finally:
    cursor.close()
    connection.close() 

def add_face_encode(student: Student) -> Student:
  set_clause = (
    f"face_encode = '{student.face_encode}'"
  )
  where_clause = f"id = {student.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return student

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def add_face_url(student: Student) -> Student:
  set_clause = (
    f"face_url = '{student.face_url}'"
  )
  where_clause = f"id = {student.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return student

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def update_student(student: Student) -> Student:
  set_clause = (
    f"email = '{student.email}', "
    f"password = '{student.encrypt_password(student.password)}', "
    f"full_name = '{student.full_name}', "
    f"student_number = '{student.student_number}', "
    f"contact_number = '{student.contact_number}', "
    f"section = '{student.section}', "
    f"course = '{student.course}', "
    f"status = 'active'"
  )
  where_clause = f"id = {student.id}"
  sql_query = builder(__table, f"{set_clause} WHERE {where_clause}", "update")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return student

  except Exception as e:
    print(f"Error: {e}")

  finally:
    cursor.close()

def delete_student(id) -> bool:
  where_clause = f"id = {id}"
  sql_query = builder(__table, where_clause, "delete")
  connection = DB.connect_db()
  cursor = connection.cursor()

  try:
    cursor.execute(sql_query)
    connection.commit()
    return True

  except Exception as e:
    print(f"Error: {e}")
    return False
  
  finally:
    cursor.close()