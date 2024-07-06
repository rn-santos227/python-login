import sys
import init
import config.database as db

from components.screen_window import ScreenWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

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
