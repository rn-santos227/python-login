import config.database as db

def init():
  print("initializing app config.")
  if(db.check_db_connection):
    print("database has already been created.")

if __name__ == "__main__":
  init()