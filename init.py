import config.database as db

from modules.admin.model import Admin
from modules.students.model import Student
from modules.logs.model import Log
from modules.parents.model import Parent

def init():
  print("initializing app config.")
  if(db.check_db_connection):
    print("database has already been created.")


def initialize_db():
  print("creating database...")
  db.create_db()

  print("creating tables...")
  db.create_table(Admin.create_table(), "admins")
  db.create_table(Student.create_table(), "students")
  db.create_table(Log.create_table(), "logs")
  db.create_table(Parent.create_table(), "parents")

  admin = Admin(full_name="Administrator", email="test@test.com", password="test@123", status="active")

if __name__ == "__main__":
  init()