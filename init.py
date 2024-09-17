import config.database as DB

from database.migration import table_migration
from database.seeder import create_default_user

def init():
  print("initializing app config.")
  if(DB.check_db_connection()):
    print("database has already been created.")

  else:
    initialize_db()

def initialize_db():
  print("creating database...")
  DB.create_db()

  print("creating tables...")
  table_migration()

  print("creating default user...")
  create_default_user()

def reset_db():
  print("resetting database...")
  DB.drop_db()

if __name__ == "__main__":
  init()