import requests

from config.config import app_name, sms_api

def send_sms(student, contact_number):
  data = {
    "apikey": sms_api,
    "sendername": app_name,
  }