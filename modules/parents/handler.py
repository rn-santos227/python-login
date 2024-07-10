from typing import List

from modules.parents.model import Parent
from modules.parents.controller import get_parents

parents: List[Parent] = get_parents("all", "select")

def update_parents():
  global parents
  parents = get_parents("all", "select")