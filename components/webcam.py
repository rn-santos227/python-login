import cv2

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class WebcamComponent(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.init_ui()

  def init_ui(self):
    self.layout = QVBoxLayout(self)

    self.label = QLabel(self)
    self.layout.addWidget(self.label)

    self.cap = None
    self.timer = QtCore.QTimer(self)
    self.timer.timeout.connect(self.update_frame)

  def start_webcam(self):
    self.cap = cv2.VideoCapture(0)
    self.timer.start(20)

  def update_frame(self):
    ret, frame = self.cap.read()
    if ret:
      self.display_image(frame)
    
  def display_image(self, img):
    qformat = QtGui.QImage.Format_RGB888
    img = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
    img = img.rgbSwapped()
    self.label.setPixmap(QtGui.QPixmap.fromImage(img))