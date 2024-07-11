from dotenv import load_dotenv
import os

load_dotenv()

connection_params = {
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "host": os.getenv("DB_HOST"),
  "raise_on_warnings": True,
}

database_name = os.getenv("DB_NAME")