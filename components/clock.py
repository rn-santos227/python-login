import math

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Clock(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()
    self.timer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.update_time)
    self.timer.start(1000)

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    self.label = QLabel(self)
    self.layout.addWidget(self.label)
    self.update_time()

  def update_time(self):
    current_time = QtCore.QTime.currentTime()
    self.display_clock(current_time)

  def display_clock(self, time):
    side = 255
    image = QtGui.QImage(side, side, QtGui.QImage.Format_ARGB32)
    image.fill(QtCore.Qt.transparent)

    painter = QtGui.QPainter(image)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)

    painter.translate(side / 2, side / 2)
    painter.scale(side / 200.0, side / 200.0)

    painter.setPen(QtCore.Qt.NoPen)
    painter.setBrush(QtGui.QColor(0, 0, 0))

    for i in range(12):
      painter.save()
      painter.rotate(30.0 * i)
      painter.drawRect(85, -5, 10, 10)
      painter.restore()

    # Draw hour hand
    painter.save()
    painter.rotate(30.0 * (time.hour() + time.minute() / 60.0))
    painter.setPen(QtGui.QPen(QtCore.Qt.black, 6, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    painter.drawLine(0, 0, 50, 0)
    painter.restore()

    # Draw minute hand
    painter.save()
    painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
    painter.setPen(QtGui.QPen(QtCore.Qt.black, 4, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    painter.drawLine(0, 0, 70, 0)
    painter.restore()

    # Draw second hand
    painter.save()
    painter.rotate(6.0 * time.second())
    painter.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    painter.drawLine(0, 0, 90, 0)
    painter.restore()

    painter.end()
    self.label.setPixmap(QtGui.QPixmap.fromImage(image))

  def stop_clock(self):
    self.timer.stop()

  def start_clock(self):
    self.timer.start(1000)