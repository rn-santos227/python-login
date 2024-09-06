from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from modules.students.model import Student

class PopupDialog(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self, student):
    self.setWindowTitle("Information")
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)