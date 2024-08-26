from dotenv import load_dotenv
import os

load_dotenv()

app_name = os.getenv("APP_NAME")

dpfj_url = "C:/Program Files/DigitalPersona/U.are.U SDK/Windows/Lib/x64/dpfj.dll"
dpfpdd_url = "C:/Program Files/DigitalPersona/U.are.U SDK/Windows/Lib/x64/dpfpdd.dll"

connection_params = {
  "user": os.getenv("DB_USER"),
  "password": os.getenv("DB_PASSWORD"),
  "host": os.getenv("DB_HOST"),
  "raise_on_warnings": os.getenv("DB_RAISE_ON_WARNINGS") == "True",
}

database_name = os.getenv("DB_NAME")

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")

sms_api = os.getenv("SMS_API")
sms_key = os.getenv("SMS_KEY")