from typing import List, Optional
from datetime import datetime

from modules.logs.model import StudentLog
from modules.logs.controller import get_logs_with_students

def get_current_date():
  return str(datetime.now().strftime("%Y-%m-%d"))

logs: List[StudentLog] = get_logs_with_students(f"date >= '{get_current_date()}' AND date <= '{get_current_date()}'")

def update_logs(start_date: Optional[str] = None, end_date: Optional[str] = None):
  global logs
  
  start_date = start_date or get_current_date()
  end_date = end_date or get_current_date()

  logs = get_logs_with_students(f"date >= '{start_date}' AND date <= '{end_date}'")