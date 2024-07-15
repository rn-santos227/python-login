import requests

from config.config import app_name, sms_api, sms_key

def send_sms(contact_number, message):
  data = {
    "apikey": sms_key,
    "sendername": app_name,
    "number": contact_number,
    "message": message,
  }

  response = requests.post(sms_api, data=data)

  