import requests

from config.config import app_name, sms_api

def send_sms(contact_number, message):
  data = {
    "apikey": sms_api,
    "sendername": app_name,
    "number": contact_number,
    "message": message,
  }