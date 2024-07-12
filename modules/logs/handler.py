from typing import List, Optional
from datetime import datetime

from modules.logs.model import Log
from modules.logs.controller import get_logs

logs: List[Log] = get_logs("all", "select")

def update_logs(start_date: Optional[str] = None, end_date: Optional[str] = None):
  global logs
  current_date = datetime.now().strftime("%Y-%m-%d")

  logs = get_logs("all", "select")