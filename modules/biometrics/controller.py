import config.database as DB

from typing import Union
from database.query import builder
from modules.biometrics.model import Biometric

__table = "biometrics"

def get_biometrics(query, action):
  sql_query = builder(__table, query, action)

def match_biometrics():
  pass

def add_biometric():
  pass

def delete_biometric():
  pass