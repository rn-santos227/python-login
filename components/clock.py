from PyQt5 import QtCore, QtGui
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from handlers.asset_handler import AssetHandler

class Clock(QWidget):
  def __init__(self):
    super().__init__()
    self.init_ui()
    self.timer: QtCore.QTimer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.update_time)

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    self.label: QLabel = QLabel(self)
    self.layout.addWidget(self.label)
    self.update_time()

  def update_time(self):
    current_time: QtCore.QTime = QtCore.QTime.currentTime()
    self.display_clock(current_time)

  def display_clock(self, time):
    asset_handler: AssetHandler = AssetHandler()
    side = 500
    image: QtGui.QImage = QtGui.QImage(side, side, QtGui.QImage.Format_ARGB32)
    image.fill(QtCore.Qt.transparent)

    painter: QtGui.QPainter = QtGui.QPainter(image)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)

    painter.translate(side / 2, side / 2)
    painter.scale(side / 200.0, side / 200.0)
    painter.rotate(-90)

    painter.save()
    painter.setPen(QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine))
    painter.drawEllipse(QtCore.QPointF(0, 0), 95, 95)
    painter.restore()

    painter.setBrush(QtGui.QColor(255, 255, 255)) 
    painter.setPen(QtCore.Qt.NoPen)
    painter.drawEllipse(QtCore.QPointF(0, 0), 94, 94) 

    for i in range(1, 13):
      painter.save()
      angle = 30.0 * (i)
      painter.rotate(angle)
      painter.translate(80, -5)  
      painter.rotate(-angle + 90) 
      svg_renderer: QSvgRenderer = asset_handler.get_svg(svg_folder="numbers", svg_name=f"{i}.svg")
      painter.scale(0.04, 0.04)
      svg_renderer.render(painter)
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
    painter.drawLine(0, 0, 70, 0)
    painter.restore()

    painter.end()
    self.label.setPixmap(QtGui.QPixmap.fromImage(image))

  def stop_clock(self):
    self.timer.stop()

  def start_clock(self):
    self.timer.start(1000)