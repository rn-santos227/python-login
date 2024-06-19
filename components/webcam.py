from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class WebcamComponent(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)

  def init_ui(self):
    self.layout = QVBoxLayout(self)

    self.label = QLabel(self)
    self.layout.addWidget(self.label)