from typing import List

from modules.logs.model import Log
from modules.logs.controller import get_logs

logs: List[Log] = get_logs("all", "select")

def update_logs():
  global logs
  logs = get_logs("all", "select")