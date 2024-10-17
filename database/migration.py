import config.database as db

from modules.admin.model import Admin
from modules.guards.model import Guard
from modules.students.model import Student
from modules.logs.model import Log
from modules.parents.model import Parent
from modules.biometrics.model import Biometric

def table_migration():
  db.create_table(Admin.create_table(), "admins")
  db.create_table(Guard.create_table(), "guards")
  db.create_table(Student.create_table(), "students")
  db.create_table(Log.create_table(), "logs")
  db.create_table(Parent.create_table(), "parents")
  db.create_table(Biometric.create_table(), "biometrics")
