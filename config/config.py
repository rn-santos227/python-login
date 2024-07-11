from dotenv import load_dotenv
import os

load_dotenv()

connection_params = {
  "user": os.getenv("DB_USER"),
  "password": "",
  "host": "localhost",
  "raise_on_warnings": True,
}

database_name = os.getenv("DB_NAME")