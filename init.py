import config.database as DB
import modules.admin.controller as ctr_admin

from database.migration import table_migration
from modules.admin.model import Admin


def init():
  print("initializing app config.")
  if(DB.check_db_connection):
    print("database has already been created.")

  else:
    initialize_db()


def initialize_db():
  print("creating database...")
  DB.create_db()

  print("creating tables...")
  table_migration()

  print("creating default user...")
  admin = Admin(full_name="Administrator", email="test@test.com", password="test@123", status="active")
  ctr_admin.create_admin(admin)

if __name__ == "__main__":
  init()