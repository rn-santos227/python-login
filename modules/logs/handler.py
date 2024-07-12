from typing import List
from datetime import datetime

from modules.logs.model import Log
from modules.logs.controller import get_logs

logs: List[Log] = get_logs("all", "select")

def update_logs(start_date, end_date):
  global logs
  current_date = datetime.now().strftime("%Y-%m-%d")
  
  logs = get_logs("all", "select")