import requests

from config.config import app_name, sms_api, sms_key

from modules.students.model import Student

def send_sms(contact_number, message):
  data = {
    "apikey": sms_key,
    "sendername": app_name,
    "number": contact_number,
    "message": message,
  }

  response = requests.post(sms_api, data=data)

  if response.status_code == 200:
    print("Message sent successfully!")
    print("Response:", response.json())

  else:
    print("Failed to send message.")
    print("Response:", response.text)


def compose_message(student: Student, type: str) -> str:
  message = ""
  return message