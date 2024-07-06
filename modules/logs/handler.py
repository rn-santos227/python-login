from typing import List

from modules.logs.model import Log
from modules.logs.controller import get_logs

logs: List[Log] = get_logs("status = 'active'", "select")