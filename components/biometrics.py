import modules.biometrics.controller as biometrics_controller

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from components.combo_box import ComboBox
from components.message_box import MessageBox

from handlers.biometrics_handler import BiometricsHandler

class Biometrics(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.biometrics_handler: BiometricsHandler = BiometricsHandler()
    self.message_box: MessageBox = MessageBox(self)
    self.devices = []
    self.init_ui()

  def init_ui(self):
    self.layout: QVBoxLayout = QVBoxLayout(self)
    
    self.label = QLabel(self)
    self.layout.addWidget(self.label)

    self.cap = None
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_frame)

  def start_scanner(self):
    try:
      self.timer.start(20)

    except Exception as e:
      self.message_box.show_message("Error", f"Error during fingerprint capture: {str(e)}", "error")

  def stop_scanner(self):
    pass
    
  def update_frame(self):
    try:
      fingerprint_image = self.biometrics_handler.capture_fingerprint()

      if fingerprint_image:
        self.display_image(fingerprint_image)

      else:
        print("Waiting for fingerprint...")

    except Exception as e:
      self.message_box.show_message("Error", f"Error during fingerprint capture: {str(e)}", "error")

  def display_image(self, img_data):
    img = QImage.fromData(img_data)
    pixmap = QPixmap.fromImage(img)

    self.label.setPixmap(pixmap.scaled(256, 360, aspectRatioMode=Qt.KeepAspectRatio))