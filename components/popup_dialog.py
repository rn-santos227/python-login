from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from modules.logs.model import StudentLog

class PopupDialog(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self, log: StudentLog):
    self.setWindowTitle("Information")
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)
    