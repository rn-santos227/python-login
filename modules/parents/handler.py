from typing import List

from modules.parents.model import Parent
from modules.parents.controller import get_parents

parents: List[Parent] = get_parents("all", "select")