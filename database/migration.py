import config.database as db

from modules.admin.model import Admin
from modules.students.model import Student
from modules.logs.model import Log
from modules.parents.model import Parent

def table_migration():
  db.create_table(Admin.create_table(), "admins")
  db.create_table(Student.create_table(), "students")
  db.create_table(Log.create_table(), "logs")
  db.create_table(Parent.create_table(), "parents")
