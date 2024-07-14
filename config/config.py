from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME")

connection_params = {
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "host": os.getenv("DB_HOST"),
  "raise_on_warnings": os.getenv("DB_RAISE_ON_WARNINGS") == "True",
}

database_name = os.getenv("DB_NAME")

sms_api = os.getenv("SMS_API")