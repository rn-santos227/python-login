import math

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Clock(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()
    self.timer = QtCore.QTimer(self)
    self.timer.start(1000)

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    self.label = QLabel(self)
    self.layout.addWidget(self.label)

  def update_time(self):
    current_time = QtCore.QTime.currentTime()
    self.display_clock(current_time)

  def display_clock(self, time):
    side = 255