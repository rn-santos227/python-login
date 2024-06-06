import os
import config.database as DB

from database.migration import table_migration
from database.seeder import create_default_user

def init():
  print("initializing app config.")
  if(DB.check_db_connection):
    print("database has already been created.")

  else:
    project_directory = os.path.dirname(os.path.abspath(__file__))
    initialize_db()


def initialize_db():
  print("creating database...")
  DB.create_db()

  print("creating tables...")
  table_migration()

  print("creating default user...")
  create_default_user()

if __name__ == "__main__":
  init()