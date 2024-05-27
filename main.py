import sys
import components.ScreenWindow as screen

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

def main():
  app = QApplication(sys.argv)
  window = screen()

if __name__ == "__main__":
  main()