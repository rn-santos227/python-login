import sys
import math

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Clock(QWidget):
  def __init__(self):
    super().__init__()
    self.timer = QtCore.QTimer(self)