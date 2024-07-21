import sys
import math

from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget

class Clock(QWidget):
  def __init__(self):
    super().__init__()