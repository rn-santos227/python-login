import sys
import init
import config.database as db

import jpype
import jpype.imports
from jpype.types import *

from config.config import jar_path

jpype.startJVM(
  classpath = [
    f"{jar_path}/dpuareu.jar",
    f"{jar_path}/xercesImpl-2.6.2.jar",
    f"{jar_path}/xmlParserAPIs.jar"
  ]
)

from components.screen_window import ScreenWindow
from PyQt5.QtWidgets import QApplication

def main():
  app = QApplication(sys.argv)
  window = ScreenWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  if not db.check_db_connection():
    print("running init...")
    init.init()

  main()
