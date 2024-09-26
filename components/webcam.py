import cv2
import numpy as np

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class Webcam(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.init_ui()
    self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    self.display_black_screen()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)

    self.label: QLabel = QLabel(self)
    self.layout.addWidget(self.label)

    self.cap = None
    self.timer: QTimer = QTimer(self)
    self.timer.timeout.connect(self.update_frame)

  def start_webcam(self):
    self.cap = cv2.VideoCapture(0)
    self.timer.start(20)

  def update_frame(self):
    ret, frame = self.cap.read()
    
    if ret:
      frame = self.detect_faces(frame)
      self.display_image(frame)
    else:
      self.display_black_screen()
    
  def display_image(self, img):
    qformat: QImage = QImage.Format_RGB888
    img = QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
    img = img.rgbSwapped()
    self.label.setPixmap(QPixmap.fromImage(img))

  def detect_faces(self, img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return img

  def capture_image(self):
    ret, frame = self.cap.read()
    if ret:
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

      if len(faces) == 1:
        return ret, frame
    return False, None
  
  def display_black_screen(self):
    black_img = np.zeros((480, 640, 3), dtype=np.uint8)
    self.display_image(black_img)
  
  def stop_webcam(self):
    if self.cap is not None:
      self.cap.release()
    self.timer.stop()