from dotenv import load_dotenv
import os

load_dotenv()

connection_params = {
  "user": "root",
  "password": "",
  "host": "localhost",
  "raise_on_warnings": True,
}

database_name = "db_logbook"