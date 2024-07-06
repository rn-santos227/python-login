from typing import List

from modules.admin.model import Admin
from modules.admin.controller import get_admins

admins: List[Admin] = get_admins("status = 'active", "select")